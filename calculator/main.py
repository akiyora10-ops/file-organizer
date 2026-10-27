"""Safe arithmetic calculator."""

from __future__ import annotations

import argparse
import ast
import operator
from typing import Iterable

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_eval(expr: str) -> float:
    node = ast.parse(expr, mode="eval").body
    return _eval(node)


def _eval(node):
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.operand))
    raise ValueError("unsupported expression")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Calculator.")
    parser.add_argument("expr", nargs="+")
    args = parser.parse_args(list(argv) if argv is not None else None)
    expr = " ".join(args.expr)
    try:
        print(safe_eval(expr))
    except Exception as e:
        print(f"error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

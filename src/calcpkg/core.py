
"""
一个安全的 calculate(expression: str) 实现，只允许 + - * / 和括号。
使用 Python 的 ast 解析并手写一个极简求值器，避免 eval 风险。
"""
from __future__ import annotations
import ast
import operator as op

# 允许的运算
_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def calculate(expression: str) -> float:
    """计算形如 "1 + 2 * (3 - 1) / 4" 的表达式。
    只允许数字、空白、括号、以及 + - * /。
    若有非法字符或结构，抛出 ValueError。
    """
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("expression must be a non-empty string")

    # 解析 AST
    try:
        node = ast.parse(expression, mode='eval')
    except SyntaxError as e:
        raise ValueError(f"invalid expression: {e}") from None

    # 递归安全求值
    def _eval(n: ast.AST) -> float:
        if isinstance(n, ast.Expression):
            return _eval(n.body)
        elif isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)
        elif isinstance(n, ast.BinOp) and type(n.op) in _OPS:
            left = _eval(n.left)
            right = _eval(n.right)
            try:
                return float(_OPS[type(n.op)](left, right))
            except ZeroDivisionError:
                raise ValueError("division by zero")
        elif isinstance(n, ast.UnaryOp) and type(n.op) in _OPS:
            val = _eval(n.operand)
            return float(_OPS[type(n.op)](val))
        elif isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            # 禁止任何函数调用
            raise ValueError("function calls are not allowed")
        else:
            # 禁止 Name、Attribute、Subscript 等
            raise ValueError("unsupported expression")

    return _eval(node)

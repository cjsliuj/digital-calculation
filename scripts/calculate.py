#!/usr/bin/env python3
import ast
import operator
import sys

# Safe operators for calculation
ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def safe_eval(expression):
    """Evaluate a mathematical expression safely"""
    tree = ast.parse(expression, mode='eval')
    
    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        elif isinstance(node, ast.BinOp):
            op = type(node.op)
            if op not in ALLOWED_OPERATORS:
                raise ValueError(f"Unsupported operator: {op}")
            left = evaluate(node.left)
            right = evaluate(node.right)
            return ALLOWED_OPERATORS[op](left, right)
        elif isinstance(node, ast.UnaryOp):
            op = type(node.op)
            if op not in ALLOWED_OPERATORS:
                raise ValueError(f"Unsupported unary operator: {op}")
            operand = evaluate(node.operand)
            return ALLOWED_OPERATORS[op](operand)
        else:
            raise ValueError(f"Unsupported expression element: {type(node)}")
    
    return evaluate(tree.body)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculate.py '<mathematical expression>'")
        sys.exit(1)
    
    expression = sys.argv[1]
    try:
        result = safe_eval(expression)
        # Remove trailing .0 if result is integer
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

import sympy as sp
from sympy.parsing.latex import parse_latex
from sympy import *


from N1 import N1
from N2 import *
from tree_building import *

def print_tree(node, level=0, label='.'):
    indent = '   ' * level
    print(f"{indent}{label}: {node.value}")
    if node.left: print_tree(node.left, level + 1, 'L')
    if node.right: print_tree(node.right, level + 1, 'R')

def print_expression(node):
    if node is None:
        return ""
    if node.left is None and node.right is None:
        return node.value
    left_expr = print_expression(node.left)
    right_expr = print_expression(node.right)
    if node.value == 'sqrt':
        return f"sqrt({left_expr})"
    if node.value == 'pow':
        return f"pow({left_expr}, {right_expr})"
    return f"({left_expr} {node.value} {right_expr})"

def main():
    expression = "sqrt(4)"
    expression = add_one_star_before_standalone_letters(expression)
    tokens = expression.replace(' ', '')
    postfix = infix_to_postfix(tokens)
    print("Postfix:", postfix)
    tree = build_expression_tree(postfix)
    print_tree(tree)

    sorted_tree = order_summation(tree)
    print_tree(sorted_tree)
    resulting_expression = print_expression(sorted_tree)
    print("Resulting Expression:", resulting_expression)

    
 

if __name__ == "__main__":
    main()
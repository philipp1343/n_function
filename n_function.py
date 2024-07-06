import sympy as sp
from sympy.parsing.latex import parse_latex
from sympy import *


from N1 import N1
from N2 import *
from tree_building import *
from latex_to_string import latex_to_string

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
    return f"{left_expr} {node.value} {right_expr}"

def main():

    expression = r'a·b × c + ()() ab + bc + a * sqrt()'
    expression = latex_to_string(expression)
    print(expression)
    n1 = N1(expression)
    print(n1)
    '''
    tokens = expression.replace(' ', '')
    postfix = infix_to_postfix(tokens)
    print("Postfix:", postfix)
    tree = build_expression_tree(postfix)
    print_tree(tree)
    sorted_tree = order_summation(tree)
    print_tree(sorted_tree)
    resulting_expression = print_expression(tree)
    print("Resulting Expression:", resulting_expression)
    '''
   

    
 

if __name__ == "__main__":
    main()
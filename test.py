import re

def add_one_star_before_standalone_letters(input_string):
    # Pattern to match standalone letters (a-z or A-Z)
    pattern = r'(?<!\S)([a-zA-Z])(?!\S)'
    
    # Replace each match with '1*' followed by the letter
    result = re.sub(pattern, r'1*\1', input_string)
    
    return result

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def is_operand(char):
    return char.isnumeric() or char.isalpha()

def infix_to_postfix(expression):
    stack = []
    output = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if is_operand(char):
            operand = char
            while i + 1 < len(expression) and (expression[i + 1].isalnum() or expression[i + 1] == '.'):
                i += 1
                operand += expression[i]
            output.append(operand)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)
        i += 1
    while stack:
        output.append(stack.pop())
    return output

def build_expression_tree(postfix):
    stack = []
    for char in postfix:
        if is_operand(char):
            node = TreeNode(char)
            stack.append(node)
        else:
            node = TreeNode(char)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack[0]

def order_summation(tree):
    variables = []
    counter = [0] 
    
    def traverse(node):
        nonlocal variables
        if node is None:
            return 
        if node.value == '+':
            traverse(node.left)
            traverse(node.right)
        elif node.value == '*' and node.left.value.isalnum() and node.right.value.isalnum():
            variables.append((node.left.value, node.value, node.right.value))
        elif node.value == '/':
            traverse(node.left)
            variables = sorted(variables, key=lambda x: x[2])
            sort(node.left)
            variables = []
            counter[0] = 0
            traverse(node.right)
            variables = sorted(variables, key=lambda x: x[2])
            sort(node.right)
            variables = []
            counter[0] = 0


    def sort(node):
        if node is None:
            return 
        if node.value == '+':
            sort(node.left)
            sort(node.right)
        elif node.value == '*' and node.left.value.isalnum() and node.right.value.isalnum():
            node.value = '*'
            node.left.value = variables[counter[0]][0]
            node.right.value = variables[counter[0]][2]
            counter[0] += 1

    traverse(tree)
    variables = sorted(variables, key=lambda x: x[2])
    sort(tree)
    return tree

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
    return f"{left_expr} {node.value} {right_expr}"

expression = "3*b + 2*a "
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

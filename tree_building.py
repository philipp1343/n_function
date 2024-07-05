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
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op in ['sqrt', 'pow']:
        return 3
    return 0

def is_operand(char):
    return char.isnumeric() or char.isalpha()


def infix_to_postfix(expression):
    stack = []
    output = []
    sqrt_pow = False
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == 's' and expression[i:i+5] == 'sqrt(':
            stack.append('sqrt')
            i += 4
            sqrt_pow = True
        elif char == 'p' and expression[i:i+4] == 'pow(':
            stack.append('pow')
            i += 3
            sqrt_pow = True
        elif is_operand(char):
            operand = char
            while i + 1 < len(expression) and (expression[i + 1].isalnum() or expression[i + 1] == '.'):
                i += 1
                operand += expression[i]
            output.append(operand)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if sqrt_pow:
                output.append(stack.pop())
            else:
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
        if is_operand(char) and char != 'sqrt' and char != 'pow':
            node = TreeNode(char)
            stack.append(node)
        else:
            node = TreeNode(char)
            if char in ['+', '-', '*', '/']:
                node.right = stack.pop()
                node.left = stack.pop()
            elif char == 'sqrt':
                node.left = stack.pop()
            elif char == 'pow':
                node.right = stack.pop()
                node.left = stack.pop()
            stack.append(node)
    return stack[0]

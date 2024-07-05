
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
        elif node.value == 'sqrt':
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

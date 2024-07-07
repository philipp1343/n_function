
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
        elif node.value == '*' and check_prod(node):
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
        elif node.value == '*' and check_prod(node):
            node.value = '*'
            node.left.value = variables[counter[0]][0]
            node.right.value = variables[counter[0]][2]
            counter[0] += 1

    traverse(tree)
    variables = sorted(variables, key=lambda x: x[2])
    sort(tree)
    return tree

def order_product(tree):
    variables = []
    counter = [0] 
    
    def traverse(node):
        nonlocal variables
        if node is None:
            return 
        if node.value == '*' and check_prod(node):
            variables.append((node.left.value, node.value, node.right.value))
        elif node.value == '*':
            traverse(node.left)
            traverse(node.right)
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
        if node.value == '*' and check_prod(node):
            node.value = '*'
            node.left.value = variables[counter[0]][0]
            node.right.value = variables[counter[0]][2]
            counter[0] += 1
        elif node.value == '*':
            sort(node.left)
            sort(node.right)
        

    traverse(tree)
    
  
    
    variables = sorted(variables, key=lambda x: x[2])
    variables[1*b/2*x]
    # 1*b/2*x ------ 0.6 * x / 4
    
    sort(tree)
    return tree

def check_prod(node):
    if node.left.value.isdigit() and node.right.value.islower():
        return True
    if node.left.value.islower() and node.right.value.isdigit():
        return True 


  '''
    variables 

    if division then check if num and denom == digit * variable 
      variables.append(3,*,x,*p,/,1,*,y)

    op1 = variables.find(isdigit())
    op2 = variables.find(isdigit())
    expr1 = op1 +'/' + op2
    expr2 = .... 
    expr1 + expr2 = result 

    3 * x * p ....  / 1 * y ... 
    -> 6/1 * x*p/y
    '''
import re

def latex_to_string(latex_expr):
   
    replacements = {
        r'\\times': '×',
        r'\\div': '/',
        r'\\sqrt': 'sqrt',
        r'\\cdot': '·',

        
    }

    for latex, string in replacements.items():
        latex_expr = re.sub(latex, string, latex_expr)

    latex_expr = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'\1/\2', latex_expr)
    latex_expr = re.sub(r'\\sqrt\{([^}]*)\}', r'sqrt(\1)', latex_expr)
    latex_expr = re.sub(r'([^{}()]+)\^([^{}()]+)', r'pow(\1,\2)', latex_expr)
    latex_expr = latex_expr.replace('{', '(').replace('}', ')')

    return latex_expr



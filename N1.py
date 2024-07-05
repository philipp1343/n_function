import re

def N1(equation):
    
    eq_string = str(equation)
    eq_string = re.sub(r'sqrt\((.*?)\)\*a', r'a * sqrt(\1)', eq_string)
    eq_string = re.sub(r'(?<![a-zA-Z0-9])([a-zA-Z])(\()', r'\1 * \2', eq_string)
    eq_string = re.sub(r'\s+', '', eq_string)
    return eq_string
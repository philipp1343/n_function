import re

def N1(input_string):
   
   
    input_string = input_string.replace('·', '*')
    input_string = input_string.replace('×', '*')
    input_string = re.sub(r'(?<![sqrt])([a-zA-Z])(?![sqrt])([a-zA-Z])', r'\1*\2', input_string)
    input_string = re.sub(r'(?<![sqrt])([a-zA-Z])(\()', r'\1*\2', input_string)
    input_string = re.sub(r'(\))(\()', r'\1*\2', input_string)

    return input_string





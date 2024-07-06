import re

def N1(input_string):
    
    input_string = input_string.replace('·', '*')
    input_string = input_string.replace('×', '*')
    
    return input_string
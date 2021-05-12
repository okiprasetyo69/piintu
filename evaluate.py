import re

def evaluate(params):
    return sum(map(int, re.findall(r'[+-]?\d+', params)))


input_param = input('Please input [0-9, +, -] : ')
print('Your input : ' + str(input_param))
print('Output : ' + str(evaluate(input_param)))
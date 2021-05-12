from math import floor, ceil

def sum_recursive(value) :
    params = int(value)
    if params <= 1:
       return params
    else:
        return params + floor(sum_recursive(params/2)) + floor(sum_recursive(params**(1/2)))


input_params = input('Please input params ! : ')
print('Your params : ' + str(input_params))
print(sum_recursive(input_params))

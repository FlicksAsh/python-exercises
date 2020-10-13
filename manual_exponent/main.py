# def manual_exponent(base, exp):
#     total = 1 
#     index = 1

#     while index <= exp:
#         total *= base
#         index += 1 

#     return total 

import functools


def manual_exponent(base, exp):
    numbers = [base for y in range(exp)]

    return functools.reduce(lambda x, y: x * y, numbers)





print(manual_exponent(5, 5))


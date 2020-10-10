import functools 
import operator 

def dynamic_reduce(list_of_numbers, operation):
  if operation == "+":
    return functools.reduce(lambda x, y: operator.add(x, y), list_of_numbers)
  if operation == "/":
    return functools.reduce(lambda x, y: operator.truediv(x, y), list_of_numbers)
  if operation == "*":
    return functools.reduce(lambda x, y: operator.mul(x, y), list_of_numbers)
  if operation == "-":
    return functools.reduce(lambda x, y: operator.sub(x, y), list_of_numbers)


print(dynamic_reduce([1, 2, 3], "-"))
from functools import reduce 

def get_average(num_list):
  average = reduce(lambda x, y: x + y, num_list)
  return average / len(num_list)

num_list = list(range(6))

get_average(num_list)
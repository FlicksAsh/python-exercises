def median(numbers): 
  sorted_numbers = sorted(numbers)
  return sorted_numbers[len(sorted_numbers) // 2]

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]


print(median(sale_prices))
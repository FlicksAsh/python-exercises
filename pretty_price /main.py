def pretty_price(num, decimal):
  if "." in str(decimal):
    decimal = str(decimal).split(".")[1]
  num_string = str(num) + "." + str(decimal)
  print(num_string)


pretty_price(4, 0.98)
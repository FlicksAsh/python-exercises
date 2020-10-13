def manual_exponent(base, exp):
    total = 1 
    index = 1

    while index <= exp:
        total *= base
        index += 1 

    return total 


print(manual_exponent(5, 5))
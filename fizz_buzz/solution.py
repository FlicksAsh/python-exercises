def fizz_buzz(max_value):
    for num in range(1, max_value + 1):
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)


fizz_buzz(100)
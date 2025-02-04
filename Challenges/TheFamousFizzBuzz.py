"""
Write a program that displays (using print) the numbers from 1 to 100 (inclusive and with a line break between each output), replacing the following:
- Multiples of 3 with the word "fizz".
- Multiples of 5 with the word "buzz".
- Multiples of both 3 and 5 with the word "fizzbuzz".
"""
def fizzbuzz(number):
    for num in range(1, number + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)


fizzbuzz(100)
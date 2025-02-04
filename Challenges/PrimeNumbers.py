"""
IS IT A PRIME NUMBER?
Write a program that checks whether a number is prime or not.
Once done, print all prime numbers between 1 and 100.
"""

def is_prime(n:int):
    for number in range(2, n + 1):  # Iterate through numbers from 2 to n
        is_prime = True  # Assume number is prime

        for divisor in range(2, int(number ** 0.5) + 1):  # Check divisibility up to sqrt(number)
            if number % divisor == 0:
                is_prime = False  # Not a prime
                break

        if is_prime:  # If no divisors were found, it's prime
            print(number, end=' ')

is_prime(100)
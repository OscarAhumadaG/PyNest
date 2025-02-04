"""
Write a program that prints the first 50 numbers of the Fibonacci sequence, starting from 0.
The Fibonacci sequence consists of a series of numbers where the next number is always the sum of the two previous ones.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def FibonacciSequence(n):
    x, y = 0, 1

    for number in range(n):
        print(x)
        x, y = y, x + y

FibonacciSequence(50)


def FibonacciSequence2(n, x=0, y=1, count=0):
    if count == n:
        return
    print(x, end=" ")
    FibonacciSequence2(n, y, x + y, count + 1)

FibonacciSequence2(50)
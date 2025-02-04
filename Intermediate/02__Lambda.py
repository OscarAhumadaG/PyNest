### Lambda ###


# Lambda with a single statement
sum_to_values = lambda x, y: x + y
print(sum_to_values(7,6))

multiply_values = lambda x, y: x * y -3

print(multiply_values(2,4))

def sum_three_values(value):
    return lambda x, y: x + y + value

print(sum_three_values(5)(2,4))

# lambda with Condition Checking
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))

# Lambda with List Comprehension
li = [lambda arg = x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# Lambda with Multiple Statements
# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)
print(res)

# Using lambda with filter()
# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

# Using lambda with map()
# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

# Using lambda with reduce()
from functools import reduce

# Example: Find the product of all numbers in a list
a = [2, 3, 4, 5]
b = reduce(lambda x, y: x * y, a)
print(b)



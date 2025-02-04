### Higher Order Functions ###

from functools import reduce
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_numbers_adding_one(first_number, second_number, f_sum):
    return f_sum( first_number + second_number)


print(sum_two_numbers_adding_one(5, 6, sum_one))
print(sum_two_numbers_adding_one(5, 6, sum_five))


### Closures ###
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(5)
print(add_closure(3))
print(sum_ten(5)(3))


### Built-In Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map
print(list(map(add_closure, numbers))) # Using the last closure

print(list(map(lambda x: x * 2, numbers)))

# Filter
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda x: x > 10, numbers)))

# Reduce
def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(lambda x, y: x * y, numbers))
print(reduce(lambda x, y: x + y, numbers))
print(reduce(sum_two_values, numbers))
### List Comprehension ###

my_original_list = [35, 24, 62, 52, 30, 30, 17]

# Creating a list from an existing list
my_list = [i for i in my_original_list]
print(my_list)

# Creating a list from a range of numbers
l2 = [0, 1, 2, 3, 4, 5, 6, 7]
my_range_list = [i for i in range(0,8)]
print(my_range_list)

# Creating a list from a range of numbers, adding 1 to each element
my_range_list2 = [i + 1 for i in range(0,8)]
print(my_range_list2)

# Creating a list from a range of numbers, by using a function to add 5 to each element
def sum_five(number):
    return number + 5

my_range_list3 = [sum_five(i) for i in range(0,8)]
print(my_range_list3)

# Creating a list from a range of numbers with a condition
my_cond_list = [i for i in range(0,10) if i % 2 == 0]
print(my_cond_list)

# Nested list comprehension
#  Creating a Matrix
matrix = []
for i in range(5):
    # Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

matrix = [[j for j in range(5)] for i in range(6)]
print(matrix)

# Filtering a Nested List Using List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flatten odd numbers matrix
odd_numbers = [
    element for row in matrix for element in row if element % 2 != 0]
print(odd_numbers)

# nested odd numbers matrix
odd_numbers = [[element for element in row if element % 2 != 0] for row in matrix]
print(odd_numbers)

# Flattening Nested Sub-Lists
# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flatten_matrix = [element for sublist in matrix for element in sublist]

print(flatten_matrix)

# Manipulate String Using List Comprehension
matrix = [["apple", "banana", "cherry"],
          ["date", "fig", "grape"],
          ["kiwi", "lemon", "mango"]]

modified_matrix = [[fruit.capitalize() for fruit in row] for row in matrix]

print(modified_matrix)
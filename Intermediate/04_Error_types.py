### Error Types ###

# SyntaxError
"""
Error:
print "Hi community!"
explanation: There is something wrong in the way you write the code
"""
print("Hi community!")


# NameError
"""
print(language)
explanation: You didn't define a variable before you use it in your code'
"""
language = "Python"
print(language)


# IndexError
"""
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[5])
explanation: When you try to use an index that's out of the range of you iterable
"""

my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[4])

# ModuleNotFoundError
"""
import maths
explanation: When you try to import a module that doesn't exist
"""
import math

# AttributeError
"""
print(math.PI)
explanation: When you try to use an attribute within a module that maybe it doesn't exist
"""
print(math.pi)

# KeyError
"""
my_dict = {"Nombre": "Oscar", "Apellido": "Gomez", "Edad": 35, 1: "Python"}
print(my_dict["Status"])
explanation: When you try to use a key within a dictionary that it doesn't exist
"""

my_dict = {"Nombre": "Oscar", "Apellido": "Gomez", "Edad": 35, 1: "Python"}
print(my_dict["Nombre"])


# TypeError
"""
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list["Nombre"])
explanation: When you try to use a parameter type that don't correspond of what python is expecting
"""
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[:])


# ImportError
"""
from math import PI
"""
from math import pi
print(pi)
"""Create a program that reverses the order of a string
 without using built-in functions that do it automatically.
 If we pass "Hello world", it should return "dlrow olleH".
 """

st1 = "Hello world"

def reverse(st1):
    rev = ''
    for i in range(len(st1),0,-1):
        rev += st1[i-1]
    return rev


print(reverse(st1))
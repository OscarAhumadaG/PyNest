### Regular Expressions ###

import re

# Match

my_string = "This is the lesson number 07: Regular Expressions"
my_other_string = "This is not the lesson number 06: files Handling "

match = re.match("This is the lesson", my_string, re.I) # Look for that expression since the beginning of the phrase
print(match)
print(match.span()) # Prints a tuple with the start and end indices of the matched substring.
start, end = match.span()
print(my_string[start:end]) # Using that tuple to access the expression we looked for
print(match.group()) # Using group method to access the expression we looked for

match = re.match("This is not the lesson", my_other_string)
# if not(match == None):
# if match is not None:
if match != None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end]) # Using that tuple to access the expression we looked for
    print(match.group())


#print(re.match("Regular Expressions", my_string))
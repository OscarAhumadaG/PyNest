### Regular Expressions ###

import re

#  re.match()
"""
🔸 Checks only the beginning of the string for a match.
🔸 If the pattern is found at the start, it returns a Match object; otherwise, it returns None.
"""

my_string = "This is the lesson number 07:\nLesson called Regular Expressions"
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
    print(match.group(), "\n\n")


#print(re.match("Regular Expressions", my_string))

# re.search()
"""
🔸 Searches the entire string for the first occurrence of the pattern.
🔸 Returns a Match object if found, otherwise None.
"""
search = re.search("lesson", my_string, re.I) # re.I stands for ignore case
print(search)
start, end = search.span()
print(my_string[start:end])
print(search.group(), "\n\n")

# re.findall()
"""
🔸 Finds all occurrences of the pattern in the string and returns a list of matches.
🔸 If no matches are found, it returns an empty list [].
"""
findall = re.findall("lesson", my_string, re.I)
print(findall, "\n\n")

"""
🔥 Key Differences:
Function	Searches Whole String?	Returns First Match?	Returns All Matches?
match()	        ❌ (only start)	             ✅ Yes	              ❌ No
search()	    ✅ Yes	                     ✅ Yes	              ❌ No
findall()	    ✅ Yes	                     ❌ No	              ✅ Yes
"""

# re.split()
"""
The re.split() function splits a string at each match of the given pattern and returns a list of substrings.
It works similarly to Python’s built-in str.split(), but allows splitting using complex patterns."""

print(re.split("\n", my_string))
print(re.split(":", my_string))

txt = "apple, orange; banana. mango"
pattern = r"[,;.\s]+"  # Split on commas, semicolons, periods, or spaces

result = re.split(pattern, txt)
print(result) # ['apple', 'orange', 'banana', 'mango']

txt = "apple, orange; banana. mango"
pattern = r"([,;.\s]+)"  # Capturing the separators

result = re.split(pattern, txt)
print(result) # ['apple', ', ', 'orange', '; ', 'banana', '. ', 'mango']

txt = "one1two22three333four"
pattern = r"\d+"  # Split at one or more digits

result = re.split(pattern, txt)
print(result) # ['one', 'two', 'three', 'four']

txt = "one1two22three333four"
pattern = r"\d+"

result = re.split(pattern, txt, maxsplit=2)  # Only split twice
print(result, "\n\n") # ['one', 'two', 'three333four']




# Sub
print(re.sub("lesson", "LESSONS", my_string))
print(re.sub("lesson|Lesson", "LESSONS", my_string)) # to change more than one word for the expression wanted
print(re.sub("[lL]esson", "LESSONS", my_string))
print(re.sub("Regular Expressions", "RegEx", my_string))

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

text_with_sub = re.sub('%', '', txt)
print(text_with_sub, "\n\n")

# Writing RegEx Patterns
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# If you want to match full words containing "a", you could use:
regex_pattern = r'\b\w*a\w*\b'
txt_test = " The plane could keep the same weight and altitude across the entire route way"
matches = re.findall(regex_pattern, txt_test)
print(matches, "\n\n")


# Square Bracket
# Let us use square bracket to include lower and upper case
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# If we want to look for the banana, we write the pattern as follows:
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches, "\n\n")  # ['Apple', 'banana', 'apple', 'banana']

# Escape character(\) in RegEx
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches, "\n\n")  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want

# One or more times(+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches, "\n\n")  # ['6', '2019', '8', '2021'] - now, this is better!

# Period(.)
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

txt1 = "Apple and banana are fruits"
txt2 = "Apple a"

pattern1 = r'[a].*'  # Zero or more
pattern2 = r'[a].+'  # One or more

print("Pattern r'[a].*':", re.findall(pattern1, txt1))  # ['and banana are fruits']
print("Pattern r'[a].+':", re.findall(pattern2, txt1))  # ['and banana are fruits']

print("Pattern r'[a].*':", re.findall(pattern1, txt2))  # ['a']
print("Pattern r'[a].+':", re.findall(pattern2, txt2), "\n\n")  # []


# Zero or more times(*)
# Zero or many times. The pattern could may not occur or it can occur many times.
regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']


# Zero or one time(?)
# Zero or one time. The pattern may not occur or it may occur once.
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifier in RegEx
# We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']

txt = 'This regular expression example was made on December 6, 2019 and revised on July 8, 2021'
regex_pattern = r'\b\w{1,4}\b'  # Encuentra palabras con 1 a 4 letras o números
matches = re.findall(regex_pattern, txt)
print(matches) # ['This', 'was', 'made', 'on', '6', '2019', 'and', 'on', '8', '2021']

regex_pattern = r'\b[a-zA-Z]{1,4}\b'
matches = re.findall(regex_pattern, txt)
print(matches) # ['This', 'was', 'made', 'on', 'and', 'on']


# Cart ^
# Starts with
txt = 'This regular expression example was made on December 6, 2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Negation
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']

# email validation regular expression (regex)
email = "odahumada26@gmail.com"
regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9-.]+$'
regex_pattern2 = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
print(re.match(regex_pattern, email))
print(re.search(regex_pattern, email))
print(re.findall(regex_pattern, email))

print(re.match(regex_pattern2, email))
print(re.search(regex_pattern2, email))
print(re.findall(regex_pattern2, email))

email2 = "odahumada26@gmail.com.co"
print(re.findall(regex_pattern2, email2))

# To learn and validate regular expressions: https://regex101.com

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.

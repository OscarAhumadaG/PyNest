### File Handling ###

"""
.txt file handling
Content:
My name is Oscar
My lastname is Ahumada
I'm 35 years old
Hello world
Intermediate Course
123 456
I also like JavaScript
"""

import os

# Reading a File in Read Mode (r)
txt_file = open("my_file.txt", "r+")
content = txt_file.read()
print(content)

txt_file.write("\nI also like JavaScript")
txt_file.close()




# To open a file we can use open() function, which close the file automatically after we finnish the whole block
with open("my_file.txt", "r") as txt_file:
    content = txt_file.read()
    print(content)


# Reading by selecting a certain amount of characters
with open("my_file.txt", "r") as txt_file:
    content2 = txt_file.read(10)
    print(content2)


# Reading by reading line per line
with open("my_file.txt", "r") as txt_file:
    print(txt_file.readline())
    print(txt_file.readline())


# Read the file by converting it in a list that we can iterate
with open("my_file.txt", "r") as txt_file:
    print(txt_file.readlines())


with open("my_file.txt", "r") as txt_file:
    lines = [line.strip() for line in txt_file.readlines()] # Removing  the newline character
    print(lines)

with open("my_file.txt", "r") as txt_file:
    print(txt_file.read(10))
    print(txt_file.readline())
    print(txt_file.readline())
    for line in txt_file.readlines():
        print(line.strip())


# Overwrite the file
with open("my_file.txt", "w+") as my_other_file:
    my_other_file.write("Hello world\nGeeksforGeeks\n123 456")

# Writing to a File in Append Mode (a)
file = open('my_file.txt', 'a')
file.write("\nThis will add this line\n")
file.close()

# Handling Exceptions When Closing a File
try:
    file = open("my_file.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()

# os.remove("my_file.txt")

# .json File

import json

python_dict_text = {
    "Name":"Oscar",
    "Lastname":"Ahumada",
    "Age":35,
    "Languages": ["Python", "Swift", "Kotlin"],
    "Website":"https://oahumada.aero"}

#  Convert the Python object to a JSON string
json_string = json.dumps(python_dict_text, indent=4)
print("JSON String:\n", json_string)

# deserializes into dict and returns dict.
y = json.loads(json_string)

print("python dict = ", y , ",", type(y))


json_file = open("my_file.json", "w+")

# Convert from Python to JSON:
json.dump(python_dict_text, json_file, indent=4) # If you use this command a second time it will insert the text again
json_file.close()

# Open and read the JSON file
with open('my_file.json', 'r') as json_file:
    data = json.load(json_file) #Adding the content to a dict python file
# Print the data
print("\n", data,",", type(data))
print(list(data.keys()))

with open('my_file.json', 'r') as json_file:
    for line in json_file.readlines():  # Reading line b line from the json object file
        print(line)

# .csv file
import csv

csv_file = open("my_file.csv", "w+")

csv_writer = csv.writer(csv_file)

csv_writer.writerow(["Name", "Lastname", "Age", "Language", "Website"])
csv_writer.writerow(["Oscar", "Ahumada", 35, "Python", "https://oahumada.aero.com"])
csv_writer.writerow(["Mateo", "", 7, "Cobol", ""])

csv_file.close()

with open('my_file.csv', 'r') as csv_file:
    for line in csv_file.readlines():
        print(line)


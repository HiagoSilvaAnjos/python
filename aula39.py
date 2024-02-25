"""
    TODO: INTERANDO COM WHILE
"""

name = input("Enter your name: ")
count = 0
new_name = ""

while count < len(name):
    character = f"{name[count]}*" 
    new_name += character
    count += 1

print(new_name.upper())
import re

password = input("Enter Password: ")

if len(password) < 8:
    print("Weak Password")
elif re.search("[A-Z]", password) and re.search("[0-9]", password):
    print("Medium Password")
elif re.search("[@#$%^&*!]", password):
    print("Strong Password")
else:
    print("Weak Password")

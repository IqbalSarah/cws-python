# Gives boolean output

a = "this is a aeroplane"
b = a.islower()  # checks if all characters are in lower case or not
print(b)

a = "THIS IS A AEROPLANE"
b = a.isupper()  # checks if all characters are in upper case or not
print(b)

a = "This is a 24aeroplane"
b = a.isalpha()  # checks if all characters are alphabet or not
print(b)

a = "This is a 23#$@@aeroplane"  # checks if all characters are alphabet or numbers or both
b = a.isalnum()
print(b)

a = "This is a 23sdhu"  # checks if all characters are digits or not
b = a.isdigit()
print(b)

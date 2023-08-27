"""
Ask a string from user. 
Ask a character from user.
Ask new character from user.

Replace character with new character from
the string entered by user.

hello
o
z

hellz
"""

a = input("Enter a string : ")
b = input("Enter a character : ")
c = input("Enter a new character : ")

c = a.replace(b, c)
print(c)

# OR
a = input("Enter a string : ")
b = input("Enter a character : ")
c = input("Enter a new character : ")

print(a.replace(b, c))

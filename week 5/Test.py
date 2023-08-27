# Q1. Reverse the order of words in a sentence. For example, change "Hello World" to "World Hello".

my_string = input("Enter a string : ").title()
words = my_string.split()
reversed_words = list(reversed(words))
reversed_string = " ".join(reversed_words)
print(reversed_string)


# Q2. Given a list of strings, concatenate them into a single string separated by spaces. For example, given the input ["Hello", "World", "Python"], the output should be "Hello World Python".

my_string = input("Enter a string : ").title()
b = my_string.split()
concatenated_string = ""

for i in b:
    concatenated_string += i + " "

print(b)
print(concatenated_string)


# Q3. Write a program to rotate the characters in a string by a given number of positions. For example, given the input "abcdef" and rotation of 2, the output should be "efabcd".
# Ask string and rotation from the user.

my_string = list(input("Enter a string : "))
rotation = int(input("Enter rotation : "))
rotated_string = ""

for i in range(rotation):
    my_string.insert(0, my_string[-1])
    my_string.pop()

for i in my_string:
    rotated_string += i

print(rotated_string)


# Q4. Given two strings s1 and s2. The task is to find out the minimum number of string rotations for the given string s1 to obtain the actual string s2.

a = input("Enter a string : ")
s = input("Enter a string : ")
b = ""
rotation = 0

for i in a:
    b += i

for i in a:
    rotation += 1
    if b == s:
        break
print(rotation)


# Q5. Write a Python program to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

my_string = input("Enter a string : ")
count = 0
for i in my_string[:4]:
    if i.isupper():
        count += 1

if count >= 2:
    print(my_string.upper())
else:
    print(my_string)

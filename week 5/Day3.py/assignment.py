# Q1. Write a Python program to get the 4th element from the last element of a tuple.

a = (12, 30, 54, 61, 27.85, 10, 55, 62, 30)
print(a[-4])


# Q2. Write a Python program to find repeated items in a tuple.

tuple_1 = (1, 5, 7, 11, 4, 32, 5, 3, 1, 24, 16, 11, 7)
a = []
for i in tuple_1:
    if tuple_1.count(i) > 1 and i not in a:
        a.append(i)
a = tuple(a)
print(a)


# Q3. Write a Python program to check whether an element exists within a tuple.

a = (54, 11, 61, 27, 85, 10, 55, 62, 12, 42, 25, 71, 91, 30)
n = int(input("Enter a number = "))
if n in a:
    print(n, "exists in the tuple.")
else:
    print(n, "does not exist in the tuple.")


# Q4. Write a Python program to remove an item from a tuple.

a = (54, 11, 61, 27, 85, 10, 55, 62, 12, 42, 25, 71, 91, 30)
a = list(a)
n = int(input("Enter a number to remove = "))
if n in a:
    a.remove(n)
    a = tuple(a)
    print(a)
elif n not in a:
    print("Invalid input")


# Q5. Write a Python program to reverse a tuple.

a = (54, 11, 61, 27, 85, 10, 55, 62)
a = list(a)
a.reverse()
a = tuple(a)
print(a)


# Q6. Write a Python program to check if a string has at least one letter and one number.
# If it has at least one letter and one number then print YES else print NO."""

a = "This is a very 234 pleasant day"
# a = "This is a very pleasant day"
is_alphabet = False
is_digit = False

for i in a:
    if i.isalpha():
        is_alphabet = True
    elif i.isdigit():
        is_digit = True

if is_alphabet and is_digit == True:
    print("YES")
else:
    print("NO")


# Q7. Write a python program to ask a string from the user. Then count the number of vowels and number of consonants in that string.

string = input("Enter a string : ")
string = string.lower()
vowels = 0
consonants = 0

for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


# Q8. Ask a string from the user. Print the string with the first 2 letters and the last 2 letters.

word = input("Enter a string : ")
first_letters = word[0:2]
last_letters = word[-2:]
final_word = first_letters + last_letters

print(final_word)


# Q9. Write a python program to only print the second half of the string. Ask string from user.

word = input("Enter a string : ")

print(word[len(word) // 2 :])

OR
word = input("Enter a string : ")
length = len(word) // 2
second_half = word[length:]
print(second_half)

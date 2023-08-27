# # # Q1. Write a Python program to check if a string is empty or not.

my_string = input("Enter a string : ")
if len(my_string) == 0:
    print("The string is empty")
else:
    print("The string is not empty")


# # # Q2. Write a Python program to find the length of the longest word in a string.

my_string = input("Enter a string : ")
b = my_string.split()
longest_word = 0
for i in b:
    if len(i) > longest_word:
        longest_word = len(i)

print(f"The length of the longest word in the string is: {longest_word}")


# # # Q3. Write a Python program to find the most common character in a string.
# # # (Print the letter which repeats most of the time).

a = input("Enter a string : ")
b = []
for i in a:
    if a.count(i) > 1 and i not in b:
        b.append(i)
print("Most common character in the string is :", max(b))

# # Better way

user_string = input("Enter a string = ")
string_list = list(user_string)


most_common_character = ""
max_count = 0


for char in string_list:
    if string_list.count(char) > max_count:
        max_count = string_list.count(char)
        most_common_character = char


print(f"Most common character = {most_common_character}")


# # # Q4. Write a Python program to remove duplicate characters from a string and return the modified string.

a = input("Enter a string : ")
b = []
for i in a:
    if i not in b:
        b.append(i)
modified_string = "".join(i for i in b)
print("Modified string is : ", modified_string)


# # # Q5. Write a Python program to check if a string is an isogram (no repeating characters).

a = input("Enter a string : ").lower()
b = list(a)
for i in b:
    if b.count(i) > 1:
        print("No, the string is not an isogram")
        break
else:
    print("Yes, the string is an isogram")

# Better way

user_string = input("Enter a string: ")
isogram = True

for i in user_string:
    if user_string.count(i) > 1:
        isogram = False
if isogram:
    print("String is isogram")
else:
    print("String is not isogram")


# # # Q6. Write a Python program to find the most frequent word in a string.

a = input("Enter a string : ").lower()
b = a.split()
for i in b:
    if b.count(i) > 1:
        break
print("Most frequent word in the string is : ", i)

# Better way

user_string = input("Enter a string = ").lower()
words = user_string.split()


most_common_word = ""
max_count = 0


for word in words:
    if words.count(word) > max_count:
        max_count = words.count(word)
        most_common_word = word


print(f"Most common word = {most_common_word}")

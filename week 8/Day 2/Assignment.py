# 1. Write a list comprehension to square each element in a given list.

# input_list = [1, 2, 3, 4]
# squared_list = [i**2 for i in input_list]
# print(squared_list)

# OR

# def squared_list(input_list):
#     return [x**2 for x in input_list]

# input_list = [1, 2, 3, 4]
# r = squared_list(input_list)
# print(r)


# 2. Create a list comprehension to filter out odd numbers from a given list.

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = [i for i in my_list if i % 2 == 0]
# print(even_list)

# OR

# def evenList(input_list):
#     return [x for x in my_list if x % 2 == 0]


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# r = evenList(my_list)
# print(r)


# 3. Generate a list comprehension to extract all vowels from a given string.
# Output: ['e', 'o', 'o']

# my_string = "hello world"

# vowels = ["a", "e", "i", "o", "u"]
# vowel_list = [i for i in my_string if i in vowels]
# print(vowel_list)

# OR


# def vowelList(my_string):
#     vowels = ["a", "e", "i", "o", "u"]
#     return [i for i in (my_string).lower() if i in vowels]

# my_string = "hello world"
# r = vowelList(my_string)
# print(r)


# 4. Calculate the length of each word in a sentence using list comprehension.

# my_string = "This is a sample sentence"

# output = [len(i) for i in my_string.split()]
# print(output)

# OR


# def wordLength(my_string):
#     return [len(i) for i in my_string.split()]

# my_string = "This is a sample sentence"
# r = wordLength(my_string)
# print(r)


# 5. Reverse each word in a list of strings using list comprehension.

# input = ["hello", "world", "python"]

# output = [i[::-1] for i in input]
# print(output)

# OR


# def stringList(input_string):
#     return [i[::-1] for i in input_string]

# input_string = ["hello", "world", "python"]
# r = stringList(input_string)
# print(r)


# 6. Count the frequency of each character in a string using list comprehension.
# Output: [('h', 1), ('e', 1), ('l', 2), ('o', 1)]

# input = "hello"

# output = [(i, input.count(i)) for i in input if i not in [x[0]] for x in output]
# print(output)


input_string = "hello"
char_count = {char: input_string.count(char) for char in input_string}
char_count_list = list(char_count.items())
print(char_count_list)


# 7. Write a list comprehension to remove duplicates from a given list.

# input_list = [1, 2, 2, 3, 4, 4, 5]
# output_list = []
# [output_list.append(i) for i in input_list if i not in output_list]
# print(output_list)

# OR

# def removeDuplicate(input_list):
#     output_list = []
#     [output_list.append(i) for i in input_list if i not in output_list]
#     return output_list


# input_list = [1, 2, 2, 3, 4, 4, 5]
# r = removeDuplicate(input_list)
# print(r)


# 8. Create a list of individual characters from a given string.
# Output = ['h', 'e', 'l', 'l', 'o']

# my_string = "hello"
# my_list = [i for i in list(my_string)]
# print(my_list)

# OR


# def string_list(my_string):
#     return [i for i in list(my_string)]


# my_string = "hello"
# r = string_list(my_string)
# print(r)


# 9. Generate a list of squares of numbers at odd indices from a given list.
# Output: [4, 16, 36]

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [list1[i] ** 2 for i in range(0, len(list1)) if i % 2 != 0]
# print(list2)

# OR

# input_list = [1, 2, 3, 4, 5, 6]
# output_list = [input_list[i] ** 2 for i in range(1, len(input_list), 2)]
# print(output_list)

# OR


# def squared_list(list1):
#     return [list1[i] ** 2 for i in range(0, len(list1)) if i % 2 != 0]

# list1 = [1, 2, 3, 4, 5, 6]
# r = squared_list(list1)
# print(r)


# 10. Find the intersection of two lists using list comprehension.

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# intersection = [x for x in list1 if x in list2]
# print(intersection)


# OR


# def intersectionList(list1, list2):
#     return [x for x in list1 if x in list2]

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# r = intersectionList(list1, list2)
# print(r)


# 11. Create a dictionary mapping each character in a string to 'vowel' if it's a vowel, and 'consonant' if it's a consonant.
# Output: {'h': 'consonant', 'e': 'vowel', 'l': 'consonant', 'o': 'vowel'}

# my_string = "hello"
# vowels = ["a", "e", "i", "o", "u"]
# my_dict = {i: "vowel" if i in vowels else "consonant" for i in my_string.lower()}
# print(my_dict)

# OR


# def classify_characters(my_string):
#     vowels = ["a", "e", "i", "o", "u"]
#     return {i: "vowel" if i in vowels else "consonant" for i in my_string.lower()}

# my_string = "hello"
# r = classify_characters(my_string)
# print(r)

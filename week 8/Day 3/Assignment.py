# # 1. Write a lambda function to filter out even numbers from a list of integers.

filterEvenNumbers = lambda my_list: [i for i in my_list if i % 2 == 0]
print(filterEvenNumbers([1, 2, 3, 4, 5, 6]))
print(filterEvenNumbers([10, 15, 20, 25]))
print(filterEvenNumbers([7, 9, 11, 13]))


# # 2. Create a lambda function that squares a given number.

numberSquare = lambda x: x**2
print(numberSquare(5))
print(numberSquare(-3))
print(numberSquare(0))


# # 3. Sort a list of tuples based on the second element of each tuple using a lambda function.

my_list = [(1, 5), (3, 2), (2, 8)]

sorted_list = sorted(my_list, key=lambda i: i[1])
print(sorted_list)


# # 4. Use a lambda function to calculate the sum of squares of a list of numbers.

my_list = [1, 2, 3, 4, 5]

sum_of_squares = sum((lambda i: i**2)(i) for i in my_list)
print(sum_of_squares)


# # 5. Use a lambda function to remove duplicates from a list while preserving the original order.

my_list = [1, 2, 2, 3, 4, 4, 5]

remove_duplicate = lambda my_list: [
    my_list[i] for i in range(len(my_list)) if my_list[i] not in my_list[:i]
]
unique_list = remove_duplicate(my_list)
print(unique_list)

# # OR

my_list = [1, 2, 2, 3, 4, 4, 5]
r = lambda my_list: list(dict.fromkeys(my_list))
print(r(my_list))


# # 6. Write a lambda function to reverse a string.

reverse_string = lambda s: s[::-1]
print(reverse_string("hello"))
print(reverse_string("python"))
print(reverse_string('""'))


# # 7. Use a lambda function to check if a given string is a palindrome.
# # Input: "racecar"
# # Output: True
# # Input: "python"
# # Output: False
# # Input: "madam"
# # Output: True

is_palindrome = lambda s: s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("python"))
print(is_palindrome("madam"))


# # 8. Sort a list of strings based on their lengths using a lambda function.

my_list = ["apple", "banana", "cherry", "date"]

sorted_list = sorted(my_list, key=lambda x: len(x))
print(sorted_list)


# # 9. Create a lambda function to filter out words from a list of strings that have a length greater than a given value.

my_list = ["apple", "banana", "cherry", "date"]
length = 5

filtered_list = [x for x in my_list if len(x) >= length]
print(filtered_list)

# # Using lambda

my_list = ["apple", "banana", "cherry", "date"]

filterWords = lambda lst, length: [i for i in lst if len(i) >= length]

print(filterWords(my_list, 5))


# # 10. Sort a dictionary by its values in ascending order using a lambda function.

x = {"apple": 3, "banana": 1, "cherry": 2}

r = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(r)


# # 11. Use a lambda function to check if all elements in a list of Boolean values are True.
# # Input: [True, True, True, True]
# # Output: True

my_list = [True, True, True, True]

checkBools = lambda lst: len(lst) == lst.count(True)

print(checkBools(my_list))

# Using all function

my_list = [True, True, True, True]

all_true = lambda lst: all(lst)

print(all_true(my_list))


# # 12. Use a lambda function to count the number of vowels (a, e, i, o, u) in a given string.

my_string = "hello"

count_vowels = len([x for x in my_string if x in "aeiouAEIOU"])
print(count_vowels)

# Using lambda

my_string = "hello"

count_vowels = lambda my_string: len([x for x in my_string if x in "aeiouAEIOU"])
print(count_vowels(my_string))


# 13. Write a lambda function to remove leading zeros from a string representing a number.

remove_zero = lambda s: str(int(s))
my_string = "007"
r = remove_zero(my_string)
print(r)

# Using lstrip
remove_zero = lambda x: x.lstrip("0")
print(remove_zero(my_string))

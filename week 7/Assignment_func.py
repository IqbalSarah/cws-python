"""Q1. Write a Python function is_palindrome(s) that takes a string s as input and returns Tru
if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
"""


def is_palindrome():
    s = input("Enter a string: ").lower()
    return s == s[::-1]


r = is_palindrome()
print(r)

"""Q2. Write a Python function factorial(n) 
that calculates and returns the factorial of a non-negative integer n."""


def factorial():
    num = int(input("Enter a number : "))
    result = 1
    if num < 0:
        return "Factorial of negative numbers doesn't exist"

    for i in range(1, num + 1):
        result *= i
    return result


result = factorial()
print(result)


"""
Q3. Write a Python function word_count(sentence) that takes a sentence as input
and returns a dictionary where keys are words and values are the counts of those 
words in the sentence."""


def word_count():
    sentence = input("Enter the sentence : ").lower().split()
    my_dict = {}

    for word in sentence:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    return my_dict


r = word_count()
print(r)


"""
Q4. Write a Python function flatten_list(nested_list) that takes a nested list as input 
and returns a flattened version of the list.
"""
# nested_list_1 = [1, [2, 3, [4, 5]], 6, [7, 8]]
# Outputs: [1, 2, 3, 4, 5, 6, 7, 8]

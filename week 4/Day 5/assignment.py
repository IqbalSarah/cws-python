# 1. Make your own list of numbers. Ask a start and end position from User. Print the list from start position to end position using Slicing.

a = [57, 22, 41, 93, 112, 145, 534, 32, 11, 21, 77, 62, 45]
n1 = int(input("Enter start position : "))
n2 = int(input("Enter end position : "))
a = a[n1 : n2 + 1]
print(a)


# 2. Make your own list of numbers. Ask a start and end position from User. Make another different list which will contain numbers from start to end position. Use slicing logic.

a = [10, -5, 8, 3, -1, -9, 7, 2]
b = []
n1 = int(input("Enter start position : "))
n2 = int(input("Enter end position : "))
b = a[n1 : n2 + 1]
print(b)


# 3. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list. Using slicing logic.

a = [10, -5, 8, 3, -1, -9, 7, 2]
b = []
n = int(input("Enter a number : "))
b = a[len(a) - n :]
print(b)


# 4. Make your own list. Write a Python program that takes an integer as an input, and make a new list containing the last n elements of the original list but in reverse order. Using slicing logic.

a = [10, -5, 8, 3, -1, -9, 7, 2]
b = []
n = int(input("Enter a number : "))
b = a[-1 : n - 1 : -1]
print(b)


# 5. Write a python program to interchange first and last elements in a list.

a = [10, -5, 8, 3, -1]
a[0], a[-1] = a[-1], a[0]
print(a)


# 6. Write a Python code to split a list into two halves using list slicing. (Keep the length of list even)

a = [1, 2, 3, 4, 5, 6, 7, 8]
mid_point = len(a) // 2
b = a[:mid_point]
c = a[mid_point:]
print(f"First half of the list is : {b}")
print(f"Second half of the list is : {c}")

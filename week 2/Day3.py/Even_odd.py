"""
Ask number from user, print is it odd or even or equal to zero
"""

num = int(input("Enter the number : "))
if num % 2 == 0 and num != 0:
    print(f"{num} is even")
elif num % 2 != 0:
    print(f"{num} is odd")
else:
    print("Equal to zero")

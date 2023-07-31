"""
Ask a number from user.

Print 1 to number, which are divisible by 5
"""
num = int(input("Enter a number = "))
i = 1
while i <= num:
    if i % 5 == 0:
        print(i, end=" ")
    i = i + 1

"""
Ask two numbers a and b from user
If a is divisible by b
print yes otherwise no
"""

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
if a % b == 0:
    print("Yes")
else:
    print("No")

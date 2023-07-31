"""
Ask a number from user
if number is divisible by 2 and 3
print yes

Else -> No

Less than 1 -> Invalid"""

num = int(input("Enter the number : "))
if num < 1:
    print("Invalid")
elif num % 2 == 0 and num % 3 == 0:
    print("YES")
else:
    print("NO")

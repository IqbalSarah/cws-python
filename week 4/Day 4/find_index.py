"""
Ask a number from user = 455

Number does not exists

45 is at position = 5
45 is at position = 6
45 is at position = 7
45 is at position = 10
"""

a = [54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
num = int(input("Enter a number = "))

if a.count(num) > 0:
    for i in range(0, len(a)):
        if a[i] == num:
            print(f"{num} is at position = {i}")
else:
    print("Number does not exists")

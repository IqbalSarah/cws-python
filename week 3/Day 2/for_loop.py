"""
Enter start number = 1
Enter end number = 100

Count - 5 and 6

3
"""

num1 = int(input("Enter start number = "))
num2 = int(input("Enter end number = "))
count = 0
for i in range(num1, num2 + 1):
    if i % 5 == 0 and i % 6 == 0:
        count = count + 1
print(f"total numbers divisible by 5 and 6 are {count}")

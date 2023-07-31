# Print all the numbers from start to end.

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
i = start
while i <= end:
    print(i, end=" ")
    i = i + 1

# Print all the numbers divisible by 5 or divisible by 7.

num = int(input("Enter a number = "))
if num < 5:
    print("No factors")
i = 1
while i <= num:
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
    i = i + 1


# Print the sum of all the numbers divisible by 4.

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
i = start
total = 0
while i <= end:
    if i % 4 == 0:
        total = total + i
    i = i + 1
print(total)


# Product/multiplication of numbers from 1 to 10

i = 1
total = 1
while i <= 10:
    total = total * i
    i = i + 1
print(total)


# Multiplication table of the number entered by user

num = int(input("Enter the number = "))
i = 1
table = 1
while i <= 10:
    table = num * i
    print(f"{num} * {i} = {table}")
    i = i + 1


# Count the total numbers divisible by 4 from 20 to 70

i = 20
count = 0
while i <= 70:
    if i % 4 == 0:
        count = count + 1
    i = i + 1
print(count)


# Check if the number entered by user is prime or not

num = int(input("Enter the number = "))
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count = count + 1
    i = i + 1
if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")

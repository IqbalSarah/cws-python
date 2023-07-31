# Q1. Print the following series using any loop:
# a. 10 20 30 40 … 200

i = 10
while i <= 200:
    print(i, end=" ")
    i = i + 10

# b. 1 10 100 1000 10000 … 100000000

i = 0
while i <= 8:
    number = 10**i
    print(number, end=" ")
    i += 1

# c. 1 11 111 1111 11111 … 1111111111

i = 1
while i <= 10:
    num = int("1" * i)
    print(num, end=" ")
    i = i + 1

# d. 1 3 6 8 11 13 16 … 28

i = 1
while i <= 28:
    print(i, end=" ")
    if i % 2 == 0:
        i += 3
    else:
        i += 2


number = 1
counter = 2
for i in range(1, 20):
    print(number, end=" ")
    number = number + counter
    if counter == 2:
        counter = 3
    else:
        counter = 2


# e. 1 2 4 8 16 32 64…2048

i = 1
while i <= 2048:
    print(i, end=" ")
    i = i * 2


# Q2. Ask a number from the user and store it n.
# Write a program to find the sum of the series 1 + 1/2 + 1/4 + 1/8 + ... + 1/2^n.

n = int(input("Enter a number: "))
sum = 0
power = 0

while power <= n:
    sum = sum + 1 / (2**power)
    power = power + 1
print(sum)


# Q3. Write a program that calculates sum of the squares of the first 10 natural numbers (1 to 10).

i = 1
sum = 0
while i <= 10:
    sum = sum + (i) ** 2
    i = i + 1
print(sum)


# Q4. Write a program to print all the numbers which are divisible by 2 and 3 but not 8, from 1 to 100.

i = 1
while i <= 100:
    if (i % 2 == 0 and i % 3 == 0) and i % 8 != 0:
        print(i, end=" ")
    i = i + 1

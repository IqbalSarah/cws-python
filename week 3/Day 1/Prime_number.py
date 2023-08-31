# print factors of a number

# num = int(input("Enter the number = "))
# factor = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")


# Total number of factors of a number

num = int(input("Enter the number = "))
factor = 0
for i in range(1, num + 1):
    if num % i == 0:
        factor = factor + 1
print(factor)


# Prime or not

num = int(input("Enter the number = "))
factor = 0
for i in range(1, num + 1):
    if num % i == 0:
        factor = factor + 1
print(factor)
if factor == 2:
    print("prime")
else:
    print("not prime")

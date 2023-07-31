"""
1 to 10
print sum of 1 to 10
"""
i = 1
total = 0
while i <= 10:
    total = total + i
    i = i + 1
print(total)

# Ask a number from user(n)....print 1 to n

num = int(input("Enter the number = "))
i = 1
total = 0
while i <= num:
    total = total + i
    i = i + 1
print(total)


# Ask start and end number from user and print sum
start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
i = start
total = 0
while i <= end:
    total = total + i
    i = i + 1
print(total)

"""
print 1 to 10
"""

i = 1
while i <= 10:
    print(i)
    i = i + 1

# or
i = 1
while i <= 10:
    print(i, end=" ")
    i = i + 1

# Ask a number from user (n), print 1 to n

n = int(input("Enter a number = "))
i = 1
while i <= n:
    print(i, end=" ")
    i = i + 1

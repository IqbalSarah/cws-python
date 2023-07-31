"""
Ask start and end numbers from user
print start to end
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start
while i <= end:
    print(i, end=" ")
    i = i + 1

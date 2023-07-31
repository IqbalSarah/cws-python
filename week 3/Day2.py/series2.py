"""
1 2 4 7 11 16 22....upto 20 numbers
"""

number = 1
counter = 1
for i in range(1, 21):
    print(number, end=" ")
    number = number + counter
    counter = counter + 1

# OR

number = 1
for i in range(1, 21):
    print(number, end=" ")
    number = number + i

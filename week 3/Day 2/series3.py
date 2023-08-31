"""
1 11 101 1001 10001.....upto 10 numbers
"""

num = 1
for i in range(1, 11):
    print(num, end=" ")
    num = (10**i) + 1

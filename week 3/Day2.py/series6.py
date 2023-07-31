"""
6 66 666 6666 66666....upto 15 numbers"""

num = 6
for i in range(1, 16):
    print(num, end=" ")
    num = (10**i) * num + num

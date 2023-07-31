"""9 99 999 9999 99999...upto 10 numbers"""

num = 1
for i in range(1, 11):
    num = 10**i - 1
    print(num, end=" ")

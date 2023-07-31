"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""

for i in range(6, 1, -1):
    for j in range(i - 1, 6):
        print(j, end=" ")
    print()

# OR
for i in range(5, 0, -1):
    for j in range(i, 6):
        print(j, end=" ")
    print()


"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

"""
1
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
"""

num = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()


"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end=" ")
    print()


"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""
for i in range(0, 6):
    for j in range(i + 1, 6):
        print(j, end=" ")
    print()


"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for i in range(6, 1, -1):
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


"""
Enter n = 8
8
7 8
6 7 8
5 6 7 8
4 5 6 7 8
...
1 2 3 4 5 6 7 8"""

n = int(input("Enter the number = "))

for i in range(n + 1, 1, -1):
    for j in range(i - 1, n + 1):
        print(j, end=" ")
    print()

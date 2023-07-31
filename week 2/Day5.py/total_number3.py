"""
Start number=4
End number=20
Enter any number=3

4 to 20 -> Divisible 3
6 9 12 15 18


Start number=45
End number=80
Enter any number=10

50 60 70 80
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
num = int(input("Enter any number = "))
i = start
total = 0
while i <= end:
    if i % num == 0:
        print(i, end=" ")
    i = i + 1

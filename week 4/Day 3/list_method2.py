a = [22, 54, 65, 76, 564, 43, 11]

"""
Ask number from user.
Enter position = 

User number=78
Position = 33
"""
num = int(input("Enter number to add = "))
position = int(input("Enter position to add = "))

if position > len(a):
    print("Cannot add")
else:
    a.insert(position, num)
    print(a)

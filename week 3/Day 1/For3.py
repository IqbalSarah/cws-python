"""
# 10 to 1
# """
# for i in range(10, 0, -1):
#     print(i, end=" ")


a = int(input("Enter start number = "))
b = int(input("Enter end number = "))
if a > b:
    for i in range(a, b - 1, -1):
        print(i, end=" ")

else:
    for i in range(a, b + 1):
        print(i, end=" ")

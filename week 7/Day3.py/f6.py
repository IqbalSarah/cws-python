"""
Write a function prodDigits() that inputs a number and
prints the product of digits of that number.
"""


def prodDigits():
    num = int(input("Enter number = "))
    product = 1
    for i in str(num):
        product *= int(i)
    print(product)


prodDigits()

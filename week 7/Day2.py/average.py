def average():
    num1 = int(input("Enter number 1 = "))
    num2 = int(input("Enter number 1 = "))
    num3 = int(input("Enter number 1 = "))
    num4 = int(input("Enter number 1 = "))
    num5 = int(input("Enter number 1 = "))
    average = (num1 + num2 + num3 + num4 + num5) / 5
    print(average)


average()


# OR


def average(a: int, b: int, c: int, d: int, e: int):
    average = (a + b + c + d + e) / 5
    print(average)


average(2, 4, 3, 5, 6)

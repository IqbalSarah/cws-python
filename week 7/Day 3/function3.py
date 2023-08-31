def add(a: int, b: int):
    total = a + b
    return total


def check(n: int):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


r = add(2, 3)
check(r)

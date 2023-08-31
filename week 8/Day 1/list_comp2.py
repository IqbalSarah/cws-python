from timeit import timeit  # Shows in how much time the code takes to run


def generateList():
    a = []
    for i in range(1, 101):
        a.append(i)
    return a


def generateList2():
    return [i for i in range(1, 101)]


t1 = timeit(stmt=generateList)
t2 = timeit(stmt=generateList2)

print(t1)
print(t2)

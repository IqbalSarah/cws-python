# 2
a = [54, 2, 1, 43, 676, 45, 54, 45, 45, 21, 787, 2, 45]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)


# 6

a = [54, 2, 1, 43, 676, 45, 54, 45, 45, 21, 787, 2, 45]
b = []

for i in a:
    if i not in b:
        b.append(i)

for i in b:
    print(f"{i} comes in list {a.count(i)} times")

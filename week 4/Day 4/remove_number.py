a = [54, 2, 1, 43, 676, 45, 45, 45, 21, 787, 45]
num = 45

while True:
    c = a.count(num)
    if c == 0:
        break
    a.remove(num)

print(a)

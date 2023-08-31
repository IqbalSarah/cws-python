a = [54, 1, 43, 234, 7, 7, 87]
b = [100, 211, 113, 4, 76, 73, 13]
c = []

for i in range(len(a)):
    c.append(a[i] + b[i])
print(c)

# OR

for i in range(len(a)):
    total = a[i] + b[i]
    c.append(total)
print(c)

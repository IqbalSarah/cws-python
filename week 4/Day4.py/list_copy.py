"""
print(id()) - shows memory of the list"""


a = [100, 211, 113, 4, 76, 73, 13]
b = a.copy()

print(id(a))
print(id(b))

print(a)
print(b)

a.append(100)
print(a)
print(b)

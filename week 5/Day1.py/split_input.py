# a = input("Enter numbers separated by spaces = ")

# print(a)
# print(type(a))

# x, y, z = a.split()
# print(x, type(x))
# print(y, type(y))
# print(z, type(z))

x, y, z = list(map(int, input("Enter numbers = ").split()))

print(x, type(x))
print(y, type(y))
print(z, type(z))

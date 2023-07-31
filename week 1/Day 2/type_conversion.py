"""Conversion from one data type to another"""

a = "1234"
b = "100"
c = int(a)
d = int(b)
print(c + d)

a = "1234"
b = "100"
print(int(a) + int(b))


a = int("1234")
b = int("100")
print(a + b)

# Truthy falsy values
a = "0"
b = bool(a)
print(b)

a = True
b = int(a)
print(b)

a = False
b = int(a)
print(b)

a = True
b = float(a)
print(b)


a = False
b = str(a)
print(b)

a = True
b = str(a)
print(b + "pqr", type(b))


# type coercion
print(1 + True)
print("1" + True)  # (it will show error)
print(1.2 + True)

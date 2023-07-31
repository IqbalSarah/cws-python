"""Different ways to print a variable
int(%d), float(%f), str(%s), bool
"""

name = "Sarah"
age = 18

# #Method 1
print("My name is", name)
print("My age is", age)

# #Method 2 - (F-strings)
print(f"My name is, {name} and my age is {age}")
print(f"{name}-{age}")

# Method 3
print("My name is %s" % (name))
print("My name is %s and my age is %d" % (name, age))

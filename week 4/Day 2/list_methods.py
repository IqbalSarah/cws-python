"""
List methods in python - removing or adding an elements in list
"""

a = [43, 21, 45, 65, 675]
a.append(100)
print(a)

a.insert(len(a), 25)
print(a)

a.insert(len(a) - 1, 10)
print(a)

a.insert(30, 400)
print(a)

a.insert(-1, 56)
print(a)

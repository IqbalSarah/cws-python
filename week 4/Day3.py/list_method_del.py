"""
delete fn - del a[o] : delte number at oth index in list
del a : delete whole variable

a.pop(): remvoes last value from list
a.pop(i): removes ith index element from list

a.remove(value): takes one arugment by default , also removes the value's first ocurence in list
"""


a = [22, 54, 65, 56, 11, 55, 45, 231, 801, 76, 564, 43, 11]
print(a)

del a[2]
print(a)


# It takes position and delete it
a.pop(3)
print(a)


# It takes element and delete it
a.remove(231)
print(a)

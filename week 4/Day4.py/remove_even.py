"""
Remove all even numbers from a list
"""

a = [100, 211, 113, 4, 76, 73, 13]
b = []

for i in a:
    if i % 2 != 0:
        b.append(i)

print(b)

"""
Addition of all even numbers
"""

a = [23, 54, 65, 32, 23, 54, 65, 7]
total = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        total += a[i]
print(f"Total={total}")

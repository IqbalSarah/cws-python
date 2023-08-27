"""
print in reverse order
Length=5
position=0 to 4
reverse=4to 0
"""

a = [43, 21, 45, 65, 675]
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")

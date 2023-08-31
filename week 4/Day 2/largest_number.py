a = [-54, -65, 34, 42, -98, -61, 75]
largest = a[0]
for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]

print(largest)

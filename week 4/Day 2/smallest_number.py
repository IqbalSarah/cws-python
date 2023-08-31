a = [-54, -65, 34, 42, -98, -61, 75]
smallest = a[0]
for i in range(len(a)):
    if a[i] < smallest:
        smallest = a[i]

print(smallest)

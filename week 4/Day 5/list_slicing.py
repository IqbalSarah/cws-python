a = [54, 2, 1, 43, 676, 45, 54, 45, 45, 21, 787, 2, 45]
b = []

# start to index 5
b = a[0:5]
print(b)

# start to end
b = a[0 : len(a)]
print(b)

# index 3 to index 5
b = a[3:5]
print(b)

# start to index 8 with interval of 2
b = a[0:8:2]
print(b)

# index 4 to end
b = a[4:]
print(b)

# start to index 6
b = a[:6]
print(b)

# start to end with interval of 2
b = a[::2]
print(b)

# index 7 to index 1 with negative interval of 1
b = a[7:1:-1]
print(b)

# index 7 to start with negative interval of -1
b = a[7::-1]
print(b)

# start to end with negative interval of -1
b = a[::-1]
print(b)

# end to index 0 with negative interval of -1
b = a[-1:0:-1]
print(b)

# end to start with negative interval of -1
b = a[-1::-1]
print(b)

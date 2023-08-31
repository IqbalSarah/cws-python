x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


# Sorting by values
r = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
print(r)


# Sorted by values but in reverse order
r = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
print(r)


# Sorting by keys
r = {k: v for k, v in sorted(x.items(), key=lambda item: item[0])}
print(r)

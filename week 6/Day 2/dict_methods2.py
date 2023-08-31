a = {
    "name": "Anirudh Khurana",
    "age": 33,
    "gender": "Male",
    "m1": 55,
    "m2": 99,
    "m3": 88,
}


# a.keys() - it gives key as output

for k in a.keys():
    print(k)
    print(f"{k} - {a[k]}")


# a.values() - it gives values as output
for v in a.values():
    print(v)


# # a.items() - it separates key-value in tuple
for item in a.items():
    print(f"{item[0]} -> {item[1]}")


# Another way of iterating
for k, v in a.items():
    print(k, v)

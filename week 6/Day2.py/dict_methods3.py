a = {"m1": 67, "m2": 98, "m3": 78, "m4": 31, "m5": 67, "m6": 62, "m7": 67}

# print(a["m3"])
# print(a["m33"])
# print(a.get("m3"))
# print(a.get("m33"))

key = input("Enter your key = ")

result = a.get(key)
if result == None:
    print("Key not found")
else:
    print(result)

# Another way

if key not in list(a.keys()):
    print("Key not found")
else:
    print(a[key])

# Another way

if key not in a:
    print("Key not found")
else:
    print(a[key])

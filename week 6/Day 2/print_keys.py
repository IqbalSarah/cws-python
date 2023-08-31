my_dict = {"m1": 67, "m2": 98, "m3": 78, "m4": 31, "m5": 67, "m6": 62, "m7": 67}

value = int(input("Enter value = "))

for k, v in my_dict.items():
    if v == value:
        print(k)

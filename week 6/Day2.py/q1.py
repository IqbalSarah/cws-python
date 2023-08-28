my_dict = {"m1": 67, "m2": 11, "m3": 78, "m4": 31, "m5": 17, "m6": 62, "m7": 7}
pass_marks = 33

for k, v in my_dict.items():
    if v < pass_marks:
        print(k)

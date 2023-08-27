def calculateMarks(maths, science, eng, hindi, history) -> int:
    # shortcut to print
    print(f"{maths = }")
    print(f"{science = }")
    print(f"{eng = }")
    print(f"{hindi = }")
    print(f"{history = }")
    return maths + science + eng + hindi + history


# Named Parameters
# print(calculateMarks(hindi=58, history=99, eng=11, science=77, maths=44))
# print(calculateMarks(44, hindi=58, history=99, eng=11, science=77))
print(calculateMarks(66, 11, 78, history=77, hindi=99))

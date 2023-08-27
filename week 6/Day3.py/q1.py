a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 67],
    "Karan": [77, 84, 21, 22, 20],
}

"""
Anirudh has highest marks = 88

With MAX()
Without MAX()
"""

# With MAX()

for k, v in a.items():
    print(f"{k}'s highest mark = {max(v)}")


# Without MAX()

for k, v in a.items():
    v.sort()
    print(f"{k}'s highest mark = {v[-1]}")

# Without sort

for k, v in a.items():
    highest = v[0]
    for m in v:
        if m > highest:
            highest = m
    print(f"{k}'s highest mark = {highest}")

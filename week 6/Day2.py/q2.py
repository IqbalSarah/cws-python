a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 67],
    "Karan": [77, 84, 21, 22, 20],
}

"""
Anirudh has scored total marks
Sanjay has scored total marks
Akul has scored total marks
Nihar has scored total marks
Karan has scored total marks

MEthod 1 - With using SUM()
MEthod 2 - Without using SUM()
"""

# MEthod 1 - With using SUM()

a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 67],
    "Karan": [77, 84, 21, 22, 20],
}

for k, v in a.items():
    total_marks = sum(v)
    print(f"{k} has scored total marks {total_marks}")


# MEthod 2 - Without using SUM()

a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 67],
    "Karan": [77, 84, 21, 22, 20],
}

for k, v in a.items():
    total = 0
    for i in v:
        total += i
    print(f"{k} has scored {total} marks")

a = {
    "Anirudh": [34, 15, 74, 88, 11],
    "Sanjay": [75, 12, 11, 89, 77],
    "Akul": [73, 99, 90, 91, 11],
    "Nihar": [55, 43, 19, 83, 67],
    "Karan": [77, 84, 21, 22, 20],
}

highest_total = 0
highest_student = ""

for k, v in a.items():
    total_marks = sum(v)
    if total_marks > highest_total:
        highest_total = total_marks
        highest_student = k

print(f"{highest_student} has the highest marks with a total of {highest_total}")

# Without sum

highest_total = 0
highest_student = ""

for k, v in a.items():
    total_marks = 0
    for m in v:
        total_marks = total_marks + m

    if total_marks > highest_total:
        highest_total = total_marks
        highest_student = k

print(f"{highest_student} has the highest marks with a total of {highest_total}")

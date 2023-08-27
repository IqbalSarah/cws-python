students = [
    {
        "name": "Anirudh",
        "marks": -89,
    },
    {
        "name": "Sagar",
        "marks": -11,
    },
    {
        "name": "Sanjay",
        "marks": -6,
    },
    {
        "name": "Vandana",
        "marks": -56,
    },
]

max = float("-inf")
for student in students:
    if student["marks"] > max:
        max = student["marks"]
print(max)

details = {
    "Anirudh": {
        "age": 55,
        "city": "Surat",
        "phone": 5678567,
        "marks": [11, 22, 33, 44, 55],
    },
    "Sagar": {
        "city": "Delhi",
        "phone": 985474587,
        "marks": [65, 12, 76, 88, 33],
    },
    "Muskan": {
        "age": 16,
        "city": "Agra",
        "phone": 8585747474,
        "marks": [98, 21, 54, 73, 88],
    },
}

# # With sum()
for k, v in details.items():
    print(f"{k} has scored {sum(v['marks'])}")


# Without sum()

for k, v in details.items():
    total = 0
    for m in v["marks"]:
        total += m
    print(f"{k} has scored {total} marks")

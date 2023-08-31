details = {
    "Anirudh": {
        "age": 55,
        "city": "Surat",
        "phone": 5678567,
    },
    "Sagar": {
        "age": 11,
        "city": "Delhi",
        "phone": 985474587,
    },
    "Muskan": {
        "age": 16,
        "city": "Agra",
        "phone": 8585747474,
    },
}


for k, v in details.items():
    age = v["age"]
    print(f"{k} has age of {age}")


# Print name, age, city, phone in proper format

for k, v in details.items():
    print(f"Name = {k}")
    print(f"Age = {v['age']}")
    print(f"City = {v['city']}")
    print(f"Phone = {v['phone']}\n")


# If age of any key does not exist

for k, v in details.items():
    print(f"Name = {k}")
    print(f"City = {v['city']}")
    print(f"Phone = {v['phone']}")
    age = v.get("age")  # 16 / None
    if age:
        print(age)
    else:
        print("Age does not exists")

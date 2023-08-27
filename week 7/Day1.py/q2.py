details = {
    "Anirudh": {
        "age": 55,
        "city": "Surat",
        "phone": 5678567,
        "marks": [11, 22, 33, 44, 55],
    },
    "Sagar": {
        "age": 11,
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


name = input("Enter name = ")
city = input("Enter city = ")
phone = int(input("Enter phone = "))
age = int(input("Enter age = "))
marks = list(map(int, input("Enter marks seprated by space = ").split()))

details[name] = {"city": city, "phone": phone, "age": age, "marks": marks}
print(details)

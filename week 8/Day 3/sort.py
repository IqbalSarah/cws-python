# my_list = [(1, 5), (3, 2), (2, 8)]
my_list = [
    {
        "name": "Anirudh1",
        "age": 88,
    },
    {
        "name": "Anirudh2",
        "age": 98,
    },
    {
        "name": "Anirudh3",
        "age": 18,
    },
]

r = sorted(my_list, key=lambda x: x["age"])

print(my_list)
print(r)

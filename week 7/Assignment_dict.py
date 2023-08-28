"""
Q1. Make a dictionary on your own, with mixed key values.
(Key can be any data type and value can be any data type).
Then ask a value (K) from the user. Remove all the keys from the dictionary having values greater than K.
test_dict = {"Anirudh":"Male","xyz":8,"Sagar":"1111","Pqr":2,"ABBC":9}
K = 6
Output = {'Anirudh': 'Male', 'Sagar': '1111', 'Pqr': 2}
"""

test_dict = {"Anirudh": "Male", "xyz": 8, "Sagar": "1111", "Pqr": 2, "ABBC": 9}
K = int(input("Enter a value K: "))
filtered_dict = {}

for key, value in test_dict.items():
    if isinstance(value, (int, float)):
        if value <= K:
            filtered_dict[key] = value
    else:
        filtered_dict[key] = value

print("Output:", filtered_dict)


"""Q2. Write a Python program to convert more than one list to a nested dictionary."""

# student_id = ["S001", "S002", "S003", "S004"]
# student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]
# student_grade = [85, 98, 89, 92]

# output = []

# for i in range(len(student_id)):
#     dict1 = {student_id[i]: {student_name[i]: student_grade[i]}}
#     output.append(dict1)

# print(output)


"""Q3. Write a Python program to filter the height and weight of students, 
which are stored in a dictionary. Ask height and weight from the user. Make your own dictionary."""

# students = {
#     "Alice Smith": (6.3, 72),
#     "Bob Johnson": (5.9, 68),
#     "Eva Brown": (6.1, 74),
#     "Jake Davis": (6.0, 70),
# }
# height = float(input("Enter height = "))
# weight = float(input("Enter weight = "))

# new_dict = {}

# for k, (h, w) in students.items():
#     if h >= height and w >= weight:
#         new_dict[k] = (h, w)

# print(new_dict)


"""Q4. Write a Python program to create a dictionary grouping a sequence of key-value pairs 
into a dictionary of lists. Make a list on your own."""

# colors = [("green", 1), ("purple", 2), ("orange", 3), ("green", 4), ("blue", 1)]
# new_dict = {}
# for i, j in colors:
#     if i in new_dict:
#         new_dict[i].append(j)
#     else:
#         new_dict[i] = [j]

# print(new_dict)


"""Q5. Make your own dictionary, sort the dictionary by values."""

data = {"apple": 5, "banana": 2, "orange": 8, "grape": 1}
sorted_data = {}
for key in sorted(data, key=data.get):
    sorted_data[key] = data[key]

print(sorted_data)

"""Q6. Write a Python program to convert a dictionary into a list of lists."""

# data = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
# output = []
# for k, v in data.items():
#     output.append([k, v])
# print(output)

"""Q7. Write a Python program to filter even numbers from a dictionary of values."""

# data = {"V": [1, 4, 6, 10], "VI": [1, 4, 12], "VII": [1, 3, 8]}

# for k, v in data.items():
#     for i in v:
#         if i % 2 != 0:
#             v.remove(i)
# print(data)


# for k, v in data.items():
#     even_values = []
#     for i in v:
#         if i % 2 == 0:
#             even_values.append(i)
#     data[k] = even_values

# print(data)


"""Q8. Write a Python program to find the shortest list of values for the keys in a given dictionary."""

# data = {
#     "A": [5, 10, 15],
#     "B": [20, 25],
#     "C": [30, 35, 40],
#     "D": [45],
#     "E": [50, 55, 60],
#     "F": [65, 70],
#     "G": [75, 80, 85],
#     "H": [90],
#     "I": [95, 100],
# }
# a = []
# for k, v in data.items():
#     if len(v) == 1:
#         a.append(k)
# print(a)


"""Q9. Write a Python program to count the frequency of a dictionary."""

# dict = {
#     "V": 10,
#     "VI": 10,
#     "VII": 40,
#     "VIII": 20,
#     "IX": 70,
#     "X": 80,
#     "XI": 40,
#     "XII": 20,
# }
# my_dict = {}

# for i in dict.values():
#     if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1

# print(my_dict)

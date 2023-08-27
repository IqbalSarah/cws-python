# Q1. Create a dictionary that counts the frequency of words in a given string. Ask string from user.

a = input("Enter the string : ")
my_dict = {}

my_str = a.split()
for i in my_str:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1

print(my_dict)


# Q2. Combine two dictionaries into a single dictionary, adding values for common keys.

d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 25}
d3 = {}

for key in d1:
    if key in d2:
        d3[key] = d1[key] + d2[key]
    else:
        d3[key] = d1[key]

for key in d2:
    if key not in d3:
        d3[key] = d2[key]
print(d3)


# Q3. Write a Python program to map two lists into a dictionary. Everything in both lists should be unique.

# list1 = ["red", "green", "blue"]
# list2 = ["#FF0000", "#008000", "#0000FF"]
list1 = ["Anirudh", "Sanjay", "Sagar"]
list2 = [33, 66, 88]

my_dict = {}

for i in range(len(list1)):
    key = list1[i]
    value = list2[i]
    my_dict[key] = value
print(my_dict)


# Q4. Write a Python program to convert string values of a given dictionary into integer/float data types.

list1 = [{"x": "10", "y": "20", "z": "30"}, {"p": "40", "q": "50", "r": "60"}]

list2 = []

for i in list1:
    my_dict = {}

    for key, value in i.items():
        if value.isdigit():
            converted_value = int(value)
        else:
            converted_value = value

        my_dict[key] = converted_value

    list2.append(my_dict)
print(list2)


# Q5. Write a Python program to convert a dictionary into a list of lists. (HARD).

my_dict = {1: "red", 2: "green", 3: "black", 4: "white", 5: "black"}
my_list = []

for key, value in my_dict.items():
    my_list.append([key, value])
print(my_list)

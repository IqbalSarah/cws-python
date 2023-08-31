# Q1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Ask n from the user.

n = int(input("Enter a number = "))
my_dict = {}
for x in range(1, n + 1):
    my_dict[x] = x * x
print(my_dict)


# Q2. Write a Python program to check if a dictionary is empty or not.

a = {"m1": 67, "m2": 98, "m3": 78, "m4": 31, "m5": 67, "m6": 62, "m7": 67}

if len(a) == 0:
    print("The dictionary is empty")

else:
    print("The dictionary is not empty")


# Q3. Write a Python program to combine two dictionaries by adding values for common keys.

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
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


# Q4. Python program to find the size of a Dictionary. Basically print how many total key-value pairs are there.

a = {"m1": 67, "m2": 98, "m3": 78, "m4": 31, "m5": 67, "m6": 62, "m7": 67}

key_value = len(a)
print(f"Total key-value pairs are {key_value}")


# Q5. Write a Python program to remove duplicates from Dictionary.


a = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
b = {}

for k, v in a.items():
    if v not in b.values():
        b[k] = v

print(b)

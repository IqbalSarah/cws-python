# List and its length

a = [9, 13, 14, 56, 32, 47, 89, 113, 543, 2098]
print(len(a))


# Make a list. Tell if the length of that list is Even or Odd.

# For even

a = [92, 680, 144, 56, 32, 47, 89, 113, 543, 2098]
if len(a) % 2 == 0:
    print(f"The length of the list is even")
else:
    print(f"The length of the list is odd")

# # For odd

a = [92, 680, 144, 56, 32, 47, 89, 113, 543, 2098, 1000]
if len(a) % 2 == 0:
    print(f"The length of the list is even")
else:
    print(f"The length of the list is odd")


# Make a list. Find the sum of all the elements in list which are divisible by 3.

a = [12, 24, 30, 45, 78, 98, 11, 42, 424, 376, 210, 420, 510, 4096, 309]
sum = 0
for i in range(len(a)):
    if a[i] % 3 == 0:
        print(a[i], end=" ")
        sum += a[i]
print()
print(f"Sum of all the elements in list which are divisible by 3 is {sum}")


# Make a list. Find how many positive and negative numbers are there.

a = [
    2,
    4,
    5,
    7,
    9,
    23,
    43,
    56,
    -87,
    -32,
    -55,
    -105,
    -642,
]
positive_count = 0
negative_count = 0
for i in a:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1
print(f"total count of Positive numbers = {positive_count}")
print(f"total count of negative numbers = {negative_count}")


# Make a list. Print all the elements in a list in reverse order.

a = [31, 72, 12, 54, 85]
index = len(a) - 1
while index >= 0:
    print(a[index], end=" ")
    index -= 1


# Make a list. Now print all the elements based on even index/position.

my_list = [45, 12, 59, 60, 47, 3412, 3111]
for i in range(len(my_list)):
    if i % 2 == 0:
        print(my_list[i], end=" ")

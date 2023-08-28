# Write a Python program to check if a list is empty or not.

a = []
if len(a) == 0:
    print("The list is empty")
else:
    print("The list is not empty")

a = [5, 15, 23, 42, 13]
if len(a) == 0:
    print("The list is empty")
else:
    print("The list is not empty")


#  Write a Python program to find the second smallest number in a list.

a = [43, 54, 65, 76, 123, 34, 45, 76, 75, 876, 88]
a.sort(reverse=True)
second_smallest = a[-2]
print(a)
print(f"Second smallest number in the given list is {second_smallest}")

# Write a Python program to find the second largest number in a List.

a = [43, 54, 65, 76, 123, 34, 45, 76, 75, 876, 88]
a.sort()
second_largest = a[-2]
print(a)
print(f"Second largest number in the given list is {second_largest}")


# Take 10 integer inputs from the user and store them in a list. Now, copy all the elements in another list but in reverse order.

a = []

for i in range(1, 11):
    n = int(input("Enter a number = "))
    a.append(n)
print(f"Original list is {a}")
b = a
b.reverse()
print(f"Reversed list is {b}")


# Write a program to find the average of all the numbers present in the list.

a = [54, 12, 43, 24, 72, 35, 87]
total = 0
for i in a:
    total += i
average = total / len(a)
print(f"Average of all the numbers presented in the given list = {average}")


# Make 2 different lists. First merge both lists into a third variable. And sort the merge list in descending order.

a = [41, 22, 31, 56, 43, 54, 22]
b = [65, 17, 87, 53, 95, 44]

c = []
for i in a:
    c.append(i)
for i in b:
    c.append(i)
c.sort(reverse=True)
print(c)

# Make a list. Write a simple program for addition of the 2nd element from start and 2nd element from the end.


a = [55, 201, 43, 74, 36, 82, 13, 20]

sum = a[1] + a[-2]
print(f"Sum = {sum}")

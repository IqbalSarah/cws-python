# Q1. Make your own list, find the largest element from that list without using the sort() method.

my_list = [27, 42, 21, 83, 117, 156, 320, 72, 11, 21, 77, 62, 45]
largest = 0
for i in my_list:
    if i > largest:
        largest = i
print(f"Largest element in the list is {largest}")


# Q2. Make your own list. Ask a frequency from the user. Print only those numbers in that list which have counts greater than or equal to the frequency entered by the user.

my_list = [54, 2, 2, 31, 223, 54, 54, 76, 2, 21, 43, 54, 5, 12]
b = []
frequency = int(input("Enter frequency = "))

for i in my_list:
    if i not in b:
        b.append(i)

for i in b:
    count = my_list.count(i)
    if count >= frequency:
        print(i, end=" ")


# Q3. Make your own list, calculate the product of all the numbers excluding the duplicates.

a = [1, 4, 6, 7, 7]
a = [3, 5, 1, 3, 6, 1]
product = 1
for i in a:
    count = a.count(i)
    if count > 1:
        del i
    else:
        product *= i

print(product)


# Q4. Find the missing number from the list, the numbers missing from the list should only be printed. Make sure the list you take is always sorted.

mylist = [1, 4, 5, 8, 10]
start_number = mylist[0]
end_number = mylist[-1]
missing_numbers = []
for i in range(start_number, end_number + 1):
    if i not in mylist:
        missing_numbers.append(i)
print(f"Missing numbers = {missing_numbers}")

# OR
# missing = []
# for i in range(mylist[0], mylist[len(mylist) - 1]):
#     if i not in mylist:
#         missing.append(i)
# print(missing)


# Q5. Make your own list. Ask a rotation number from the user. Rotate the list by the amount of the number entered by the user.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
n = int(input("Enter rotation = "))
b = a[-n:] + a[:-n]
print(b)

# OR

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotation = int(input("Enter rotation = "))
for i in range(rotation):
    # Add last element to start of the list
    mylist.insert(0, mylist[-1])
    # Delete the last element
    mylist.pop()
print(mylist)

"""1. Write code that takes a list of numbers as input and calculates the sum of all 
the elements in the list. Remember to first take input, and then calculate the sum 
without using the sum() function."""

a = []
total = 0
for i in range(1, 6):
    n = int(input("Enter a number = "))
    a.append(n)
    total += n
print(a)
print(f"Sum of all the elements in the list = {total}")


# 2. Write code that takes a list as input, removes all duplicate elements from it.

a = []
b = []

for i in range(1, 10):
    n = int(input("Enter a number = "))
    a.append(n)
for i in a:
    if i not in b:
        b.append(i)

print(b)

# 3. Write code that takes two lists and prints the elements that are common to both lists.

a = [51, 22, 61, 43, 76, 35, 41, 98, 70, 87, 17]
b = [17, 20, 55, 67, 25, 43, 41, 83, 87, 61, 40]
c = []

for i in a and b:
    if i in a and b:
        c.append(i)
print(c)

# 4. Write code that takes a list of numbers as input and prints a new list with the squares of each element.

a = []
b = []
for i in range(1, 6):
    n = int(input("Enter a number = "))
    a.append(n)
    n = n**2
    b.append(n)
print(f"Old list is {a}")
print(f"New list with squared elements is {b}")


# 5.Write code that checks if a given list is a palindrome, i.e., it reads the same backward as forward. Print "Palindrome" if it is, otherwise print "Not a Palindrome".

a = []
for i in range(1, 6):
    n = int(input("Enter a number = "))
    a.append(n)
if a[n] == a[len(a) - 1]:
    print("p")
    i -= 1
else:
    print("Np")


# 6. Write code that takes a list of elements as input and prints the count of each unique element along with the element itself.

a = [54, 2, 1, 43, 676, 45, 54, 45, 45, 21, 787, 2, 45]
b = []

for i in a:
    if i not in b:
        b.append(i)

for i in b:
    print(f"{i} comes in list {a.count(i)} times")

# 7. Write code that takes a list of numbers and an integer 'n' as input. Print the index of the first occurrence of 'n' in the list, or print "Not found" if 'n' is not present.

a = []
for i in range(1, 6):
    num = int(input("Enter a number for the list = "))
    a.append(num)
n = int(input("Enter a number to find the index = "))
if n in a:
    print(f"The index of first occurence of {n} in the list is {a.index(n)}")
else:
    print("Not found")


# 8. Write code that takes a list of numbers as input and calculates the sum of elements at even indices and the sum of elements at odd indices separately. Print both sums.

a = []
b = []
c = []
sum_b = 0
sum_c = 0

for i in range(1, 11):
    n = int(input("Enter a number = "))
    a.append(n)
for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

# for i in b:
#     sum_b += i
# for i in c:
#     sum_c += i
# print(f"The sum of elements at even indices = {sum_b}")
# print(f"The sum of elements at odd indices = {sum_c}")

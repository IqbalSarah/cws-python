"""
1st

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
# """
for i in range(1, 6):
    for j in range(1, 6 - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("* ", end="")

    print()

"""
2nd

        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
"""

for i in range(1, 6):
    for j in range(5 - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("* ", end="")

    print()

for i in range(4, 0, -1):
    for j in range(5 - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("* ", end="")

    print()


"""
3rd
* * * * *
*       *
*       *
*       *
* * * * *
"""

num_rows = 5
for i in range(num_rows):
    if i == 0 or i == num_rows - 1:
        print("* " * num_rows)
    else:
        print("*", " " * (2 * num_rows - 3), "*", sep="")

"""
4rd

Ask a start number = 
Ask a end number = 

Print all prime numbers between them.
"""
num1 = int(input("Enter start number = "))
num2 = int(input("Enter end number = "))

for i in range(num1, num2 + 1):
    factors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            factors += 1
    if factors == 2:
        print(i, end=" ")

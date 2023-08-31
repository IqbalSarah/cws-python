"""
        *
      * *
    * * *
  * * * *
* * * * *
"""

for i in range(0, 5):
    for j in range(i, 5):
        print(end=" ")
    for k in range(i + 1):
        print("*", end="")
    print()


# OR

for i in range(1, 6):
    for j in range(5, i, -1):
        print("", end=" ")

    for k in range(1, i + 1):
        print("*", end="")
    print()

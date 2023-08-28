""" 
Make a function which accepts one list as a parameter, return sum
Then make a function to check the sum of that list as a prime or not
"""


def returnListsum(a):
    return sum(a)


def checkPrime(n):
    factors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factors + 1
    if factors == 2:
        print("Prime Number!")
    else:
        print("Not a Prime Number!")


my_list = [1, 2, 3, 4]
result = returnListsum(my_list)
print(result)
checkPrime(result)

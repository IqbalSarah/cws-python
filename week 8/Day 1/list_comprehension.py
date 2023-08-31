# New method to create list

a = [i for i in range(1, 31)]
print(a)

# Gives even numbers

a = [i for i in range(1, 31) if i % 2 == 0]
print(a)


# Check prime


def checkPrime(num) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


# a = [i for i in range(1, 31) if checkPrime(i) == True]
# or
a = [i for i in range(1, 31) if checkPrime(i)]

print(a)

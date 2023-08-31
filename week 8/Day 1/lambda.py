# Lambda/Anonymous function
# Lambda function used when there is single line logic.
# It won't work if there is multi line logic code.


def add(num1, num2):
    return num1 + num2


print(add(10, 20))


# Same code with lambda function
add = lambda x, y: x + y
print(add(10, 20))


# To generate even list
generateEvenList = lambda start, end: [i for i in range(start, end + 1) if i % 2 == 0]

print(generateEvenList(4, 20))

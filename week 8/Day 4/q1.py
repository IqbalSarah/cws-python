user_string = input("Enter a string: ")

if user_string.isdigit():
    answer = int(user_string) * 2
    print(answer)
else:
    print("It is not a number")

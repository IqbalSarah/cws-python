"""
1. Ask a string from user. Tell if string is palindrom or not. (slicing)
mom -> It is palindrom
noon -> It is palindrom
abc -> It is not a palindrom"""

user_string = input("Enter a string: ")

reversed_input = user_string[::-1]

if user_string == reversed_input:
    print("The input string is a palindrome.")
else:
    print("The input string is not a palindrome.")


"""2. Ask a string from user. Count the number of "o" in it. (for loop)
good -> 2
goOd -> 2"""

user_input = input("Enter a string: ")
count = 0

for i in user_input:
    if i.lower() == "o":
        count += 1

print(count)


"""3. Ask a string from user. If the string added by user is a number. 
Then double the number and print it.
If it is not a number then print "Not a number"
"""

user_string = input("Enter a string: ")

if user_string.isdigit():
    answer = int(user_string) * 2
    print(answer)
else:
    print("It is not a number")

# # Q1. Make a text file. Enter random numbers in that file. Each line must contain only one number. Write a python program to calculate the sum of all the numbers.

f = open("number.txt", "r")
lines = f.readlines()
total = 0
for line in lines:
    line = line.strip()
    print(line)
    num = int(line)
    total += num
print(f"The sum of all the number in the file = {total}")

f.close()


# # Q2. Ask a word from the user. Print Yes or No if the word entered by user exists in a file or not.

with open("paragraph.txt", "r") as file:
    word = input("Enter a word to search : ").lower()
    word_found = False

    for line in file:
        if word in line:
            word_found = True
            break
if word_found:
    print("Yes, the word exists in the file.")
else:
    print("No, the word does not exist in the file.")


# # Q3. Ask a word from the user. Count the frequency of how many times that number comes in a file.

word = input("Enter a word to search : ").lower()

f = open("paragraph.txt", "r")
lines = f.readlines()
total = 0
for line in lines:
    line = line.strip()
    if word in line:
        total += 1
    # else:
    #     total = 0
print(f"The total occurrence of the word entered : {total}")

f.close()


# """Q4. Read a file using a python program. Print all the words in a reverse order.
# Example:
# abc.txt
# Hello Good morning
# I am the best

# Output
# olleH dog gninorm
# I ma eht tseb"""

with open("abc.txt", "r") as file:
    for line in file:
        words = line.split()
        reversed_words = [word[::-1] for word in words]

        reversed_line = " ".join(reversed_words)
        print(reversed_line)


# # Q5. Write a python program. Only print those lines which contain ‘a’ in it.

with open("para.txt", "r") as file:
    for line in file:
        if "a" in line:
            print(line, end="")

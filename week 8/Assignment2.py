# Q1. Write a Python program to read a text file and create a new file with the same content but with all the words in uppercase.

with open("abc.txt", "r") as f:
    data = f.read()

with open("abc2.txt", "w") as f:
    f.write(data.upper())


# Q2. Write a Python program to read a text file and create a new file that contains the original lines in reverse order (i.e., the last line of the original file should be the first line in the new file).


def reverseLines(old_file, new_file):
    input_file = open(old_file, "r")
    output_file = open(new_file, "w")

    lines = input_file.readlines()

    lines.reverse()

    for line in lines:
        output_file.write(line)

    input_file.close()
    output_file.close()


old_file = input("Enter old file name = ")
new_file = input("Enter new file name = ")
reverseLines(old_file, new_file)


# Q3. Write a Python program to read a text file and create a new file with the same content, but with all vowels (a, e, i, o, and u) replaced by an asterisk (*).


def replaceVowels(old_file, new_file):
    input_file = open(old_file, "r")
    output_file = open(new_file, "w")

    lines = input_file.readlines()
    vowels = "aeiouAEIOU"

    for line in lines:
        for i in vowels:
            line = line.replace(i, "*")
        output_file.write(line)

    input_file.close()
    output_file.close()


old_file = input("Enter old file name = ")
new_file = input("Enter new file name = ")
replaceVowels(old_file, new_file)


# Q4. Write a Python program to read two text files and create a new file that contains the
# lines of the first file followed by the lines of the second file (i.e., concatenate the two files).


def concatenate_files(old_file1, old_file2, output_file):
    with open(old_file1, "r") as f1:
        line1 = f1.readlines()

    with open(old_file2, "r") as f2:
        remaining_lines = f2.readlines()

    with open(output_file, "w") as output:
        output.writelines(line1)

        output.writelines(remaining_lines)


old_file1 = input("Enter the first file name: ")
old_file2 = input("Enter the second file name: ")
new_file = input("Enter the output file name: ")

concatenate_files(old_file1, old_file2, new_file)


# Q5. Write a Python program to read a text file and create a new file with the same content,
# but with each word's first letter capitalized.


def capitalizeWords(input_file, output_file):
    with open(input_file, "r") as f:
        lines = f.read()
        capitalized_line = " ".join(word.capitalize() for word in lines.split())

    with open(output_file, "w") as f:
        f.write(capitalized_line)


input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

capitalizeWords(input_file, output_file)


# Q6. Write a Python program to read a text file containing a list of numbers
# (one per line) and create a new file with the same numbers sorted in ascending order.


def sortedNumbers(input_file, output_file):
    with open(input_file, "r") as f:
        lines = [line.strip() for line in f]

    numbers = [int(line) for line in lines]
    sorted_numbers = sorted(numbers)

    with open(output_file, "w") as f:
        for number in sorted_numbers:
            f.write(f"{number}\n")


input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

sortedNumbers(input_file, output_file)

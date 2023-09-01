"""
Write a Python program to read last n lines of a file.

function readLastNLines(filename,n)

file -> 5 line
n -> 8
print("NOt enought lines")


file -> 5 line
n -> 3
print("NOt enought lines")
"""


# def readLastNLines(filename):
#     with open(filename, "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             line = line.strip()
#             print(line)


# print(readLastNLines("sentence.txt"))


def readLastNLines(filename: str, n: int) -> None:
    with open(filename, "r", encoding="UTF8") as f:
        lines = f.readlines()
        if n > len(lines):
            print("Not enough lines")
        else:
            # print("".join(line for line in lines[len(lines) - 3 :]))
            for line in lines[len(lines) - 3 :]:
                print(line.strip())


readLastNLines("sentence.txt", 3)

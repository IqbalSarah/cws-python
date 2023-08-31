"""
Function copyData():

copy old-file data to new-file
"""


def copyData(old, new):
    with open(f"{old}.txt", "r") as f:
        data = f.read()

    with open(f"{new}.txt", "w") as f:
        f.write(data)


old_file = input("Enter old file name = ")
new_file = input("Enter new file name = ")
copyData(old_file, new_file)

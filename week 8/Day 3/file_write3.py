data = input("Enter data = ")
filename = input("Enter file name = ")

with open(f"{filename}.txt", "w") as f:
    f.write(data)

f.write(data)
print("Done")

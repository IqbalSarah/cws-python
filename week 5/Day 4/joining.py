a = [4, 5, 6, 7, 8, 44, "anirudh", True]

b = " ".join(str(i) for i in a)
print(b)

a = ["OK", "This", "Done", "Bye"]
b = " ".join(i for i in a)
print(b)

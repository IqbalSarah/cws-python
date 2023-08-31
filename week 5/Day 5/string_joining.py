a = ["anirudh", "khurana", "zzz", "xyzxyz"]

r = " ".join(i for i in a)
print(r)

r = " ".join(i + "x" for i in a)
print(r)

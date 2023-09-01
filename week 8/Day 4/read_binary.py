"""
Mode
for text - r, w, a or rt, wt, at
for binary - rb, wb, ab
"""

with open("1.pdf", "rb") as f:
    data = f.read()
    print(data)

with open("1.pdf", "ab") as f:
    f.write(data)


# with open("2.pdf", "wb") as f:
#     f.write(data)

"""
Hello good morning
This is codingwise
Ok bye

morning good Hello  
codingwise is This
bye Ok 
"""

f = open("hello.txt", "r")
lines = f.readlines()
print(lines)
for line in lines:
    line = line.strip()
    words = line.split()
    words = words[::-1]
    # print(" ".join(w for w in words)) #or
    for w in words:
        print(w, end=" ")
    print()
f.close()

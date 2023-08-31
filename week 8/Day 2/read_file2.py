"""
Ok bye
This is codingwise
Hello good morning
 """


f = open("hello.txt", "r")
lines = f.readlines()
print(lines)
for line in lines[::-1]:
    print(line.strip())
f.close()

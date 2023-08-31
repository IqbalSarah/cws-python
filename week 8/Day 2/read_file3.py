f = open("hello.txt", "r")
r = f.read(5)
print(r)

r = f.readlines()
print(r)

r = f.read()
print(r)
print("---")

f.close()

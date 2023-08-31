"""
Read mode
"""

# To count number of 'o' in hello.txt file

f = open("hello.txt", "r")
data = f.read().lower()
print(data.count("o"))
f.close()

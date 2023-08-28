a = []
count = 0
for i in range(1, 6):
    n = int(input("Enter a number = "))
    a.append(n)

for i in range(0, len(a)):
    if a[i] % 2 == 0:
        count += 1
print(count)

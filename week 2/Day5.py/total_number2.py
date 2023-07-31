"""1 to 100, print total numbers divisible by 6"""


i = 1
total = 0
while i <= 100:
    if i % 6 == 0:
        total = total + i
    i = i + 1
print(total)

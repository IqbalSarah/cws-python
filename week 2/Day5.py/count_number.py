"""
1 to 20 
count all the numbers divisible by 3
"""

i = 1
count = 0
while i <= 20:
    if i % 3 == 0:
        count = count + 1
    i = i + 1
print(count)

"""
Factorial

Enter a number = 


5 -> 5*4*3*2*1 -> 120
10 -> 10*9*8*7*6*5*4*3*2*1
"""

num = int(input("Enter the number = "))
ans = 1
for i in range(1, num + 1):
    ans = ans * i
print(ans)

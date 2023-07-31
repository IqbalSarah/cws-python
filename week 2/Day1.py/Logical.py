"""
Logical Operators(Always in BOOLEAN)
AND, OR, NOT
"""

Maths = 89
Physics = 25
print(Maths > 33 and Physics > 33)
print(not (Maths) > 33 and Physics > 33)
print(Maths > 33 and not (Physics) > 33)
print(not (Maths > 33 and Physics > 33))
print(Maths > 33 or Physics > 33)
print(not (Maths) > 33 or Physics > 33)
print(Maths > 33 or not (Physics) > 33)
print(not (Maths > 33 or Physics > 33))

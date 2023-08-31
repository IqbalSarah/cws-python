"""
Distannce Rate Calculator

Ask distance from user (km)
Base price upto 5km -> 100Rs
5-10km -> 50Rs/km
10-15km -> 40Rs/km
15-20km -> 30Rs/km
Above 20km -> 15Rs/km
"""

dis = int(input("Enter the distance in kms = "))
if dis <= 5 and dis > 0:
    total = 100
elif dis >= 6 and dis <= 10:
    total = 100 + ((dis - 5) * 50)
elif dis >= 11 and dis <= 15:
    total = 100 + (5 * 50) + ((dis - 10) * 40)
elif dis >= 16 and dis <= 20:
    total = 100 + (5 * 50) + (5 * 40) + ((dis - 15) * 30)
else:
    total = 100 + (5 * 50) + (5 * 40) + (5 * 30) + ((dis - 20) * 15)

print(f"Total={total}")

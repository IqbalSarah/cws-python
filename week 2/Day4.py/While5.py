"""
Ask start number from user (start) #5
Ask end number from user (end) # 23

end to start
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = end
while i >= start:
    print(i, end=" ")
    i = i - 1

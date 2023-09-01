# a = ["EVEN" if i % 2 == 0 else "ODD" for i in range(1, 31)]


# a = ["EVEN" for i in range(1, 31) if i % 2 == 0 else "ODD"] # it will give error because else con not be in end


a = [
    {i: "EVEN"} if i % 2 == 0 else {i: "ODD"} for i in range(1, 31)
]  # Else can be in start after if function
print(a)

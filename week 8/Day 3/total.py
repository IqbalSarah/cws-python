def calculateTotal(filename):
    total = 0
    with open(f"{filename}.txt", "r") as f:
        lines = f.readlines()
        print(lines)
        for l in lines:
            num = int(l.strip())
            total = total + num
        print(total)


calculateTotal("total")

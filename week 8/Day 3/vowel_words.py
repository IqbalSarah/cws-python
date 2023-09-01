def countVowels(word: str) -> int:
    vowels = "aeiou"
    count = 0
    for ch in vowels:
        count = count + word.lower().count(ch)
    return count


def printVowels(filename: str, newfilename: str) -> None:
    with open(filename, "r") as f:
        data = f.readlines()
    with open(newfilename, "w") as f:
        for line in data:
            line = line.strip()
            words = line.split()
            for word in words:
                if countVowels(word) >= 3:
                    f.write(word + " ")
            f.write("\n")


printVowels("sentence.txt", "sentence1.txt")

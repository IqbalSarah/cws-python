def vowelWords(filename):
    sentence1 = []
    with open(f"{filename}.txt", "r") as f:
        lines = f.readlines()

    for line in lines.strip():
        for word in line:
            if vowelWords(word) >= 3:
                sentence1.append(word)

    with open("sentence1.txt", "w") as output_file:
        for word in sentence1:
            output_file.write(word + "\n")


vowelWords("sentence")

def longestWord(filename: str) -> None:
    with open(filename, "r") as f:
        data = f.readlines()
    longest_word = ""
    longest_word_length = 0
    for line in data:
        line = line.strip()
        words = line.split()
        for word in words:
            if len(word) > longest_word_length:
                longest_word_length = len(word)
                longest_word = word
    print(longest_word, longest_word_length)


longestWord("sentence.txt")

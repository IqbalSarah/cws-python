# travel of mode best the is Aeroplane

a = "Aeroplane is the best mode of travel"
words = a.split()  # Split the string into words
reversed_words = list(reversed(words))  # Reverse the order of the words
reversed_string = " ".join(
    reversed_words
)  # Join the reversed words with a space separator
print(reversed_string)

# enalporeA si eht tseb edom fo levart

a = "Aeroplane is the best mode of travel"
words = a.split()  # Split the string into words

reversed_words = [i[::-1] for i in words]  # Reverse each word
reversed_string = " ".join(
    reversed_words
)  # Join the reversed words with a space separator

print(reversed_string)


# levart fo edom tseb eht si enalporeA

a = "Aeroplane is the best mode of travel"
words = a.split()  # Split the string into words

reversed_words = " ".join(
    [i[::-1] for i in words[::-1]]
)  # Reverse both words and characters
print(reversed_words)

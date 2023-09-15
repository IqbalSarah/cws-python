# List of words to choose from
words = ["python", "hangman", "programming", "challenge", "word"]

# Choose a word from the list
word = words[0]  # You can manually set the word index to choose a specific word

# Initialize variables
guessed_letters = []
max_attempts = 6

# Create an initial display with underscores
displayed_word = "_" * len(word)

print("Welcome to Hangman!")

while True:
    print(displayed_word)
    guess = input("Please enter a letter guess: ").lower()

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        # Update the displayed word with correct guesses
        new_display = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_display += guess
            else:
                new_display += displayed_word[i]
        displayed_word = new_display
        print("Correct guess!")
    else:
        max_attempts -= 1
        print(f"Incorrect guess! You have {max_attempts} attempts left.")
        print(f"  ________      \n  |       |     \n  |       {'' if max_attempts < 6 else '|'}     \n  |      {'' if max_attempts < 3 else '/'}{'' if max_attempts < 5 else '|'}{'' if max_attempts < 4 else '\\'}    \n  |        |    \n  |       {'' if max_attempts < 1 else '/'},{'\\' if max_attempts < 2 else ''}       \n _|_           ")

    if max_attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was '{word}'.")
        break

    if "_" not in displayed_word:
        print(f"Congratulations! You guessed the word: '{word}'.")
        break

play_again = input("Would you like to play again? (yes/no): ").lower()
if play_again == "yes":
    # Choose a new word and reset variables
    word = words[1]  # You can manually set the word index to choose a different word
    guessed_letters = []
    max_attempts = 6
    displayed_word = "_" * len(word)
else:
    print("Thank you for playing Hangman!")

import random

# 5 predefined words
words = ["python", "computer", "engineer", "program", "mobile"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

print("================================")
print("        HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print()

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word!")
        print("The word was:", secret_word)
        break

    # Get player's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        print()
        continue

    # Check for repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        print()
        continue

    # Store the guessed letter
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

    print()

else:
    print("\nGame Over!")
    print("You ran out of guesses.")
    print("The correct word was:", secret_word)

import random

# 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Random word select
word = random.choice(words)

# Guessed letters
guessed_letters = []

# Incorrect guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("🎉 Congratulations! You won!")
        print("The word was:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Correct / incorrect
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
import random
word_list = ["apple", "grape", "plant"]
chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)
guessed_letters = []
lives = 6

print("Welcome to Hangman! Guess the 5-letter word.")

while lives > 0 and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display[i] = guess
        print("Correct!")
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")

if "_" not in display:
    print(f" Congratulations! You guessed the word: {chosen_word}")
else:
    print(f" Game Over! The word was: {chosen_word}")
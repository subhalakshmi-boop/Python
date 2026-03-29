import random
words = ["python", "computer", "science", "programming", "hangman"]
word = random.choice(words)
guessed_letters = []
attempts = 3
print("===== HANGMAN GAME =====")
while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    if "_" not in display_word:
        print(" Congratulations! You guessed the word:", word)
        break
    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single valid letter!")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess not in word:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)
    else:
        print("Good guess!")
if attempts == 0:
    print("Game Over! The word was:", word)

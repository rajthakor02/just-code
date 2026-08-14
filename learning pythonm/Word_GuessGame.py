import random

words = [
    "python",
    "computer",
    "keyboard",
    "program",
    "function",
    "variable",
    "string",
    "random",
    "loop",
    "guess",
]

print("Hi! Welcome to the Word Guessing Game.")
print("Guess the hidden word one letter at a time.")
print("You can make 7 wrong guesses before you lose.\n")

secret = random.choice(words)
secret = secret.lower()
length = len(secret)

# show blanks: _ _ _ ...
display = ""
for i in range(length):
    display = display + "_ "

guessed_letters = ""
wrong = 0
max_wrong = 7

while wrong < max_wrong:
    print("Word:", display)
    if guessed_letters == "":
        print("Letters tried: (none)")
    else:
        print("Letters tried:", guessed_letters)
    print("Wrong guesses left:", max_wrong - wrong)
    print()

    guess = input("Enter one letter: ")
    guess = guess.lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please type only one letter (a-z).\n")
        continue

    if guess in guessed_letters:
        print("You already tried that letter.\n")
        continue

    guessed_letters = guessed_letters + guess + " "

    if guess in secret:
        display = ""
        for i in range(length):
            if secret[i] in guessed_letters:
                display = display + secret[i] + " "
            else:
                display = display + "_ "
        print("Correct!\n")

        if "_" not in display:
            print("You guessed the whole word:", secret)
            print("You win!")
            break
    else:
        wrong = wrong + 1
        print("That letter is not in the word.\n")
else:
    if "_" in display:
        print("Sorry! You used all wrong guesses.")
        print("The word was:", secret)

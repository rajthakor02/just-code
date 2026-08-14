import random
print ("Hii! Welcome to number guessing game.\nYou have seven chances to guess this number. Let's start the game!")

low = int(input("Enter the lower bound : "))
upp = int(input("Enter the upper bound : "))

print(f"You have 7 chances to guess this numbers between {low} to {upp}. Let's start! ")

num = random.randint(low, upp) 
ch = 7
gc = 0

while gc <= ch:
    gc += 1
    guess = int(input("guess the number : "))
    if guess == num:
        print("You have guessed right number.")
        break
    elif gc >= ch:
        print(f"Sorry! The number was {num}. Better luck next time.")
    elif guess > num:
        print("Try lower number.")
    elif guess < num:
        print("Try higher number.")
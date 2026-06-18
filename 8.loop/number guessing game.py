"""
create a simple number guessing game 
the user get 10 chances to guess a number 
if the user guesse the number before 10 chances, atop asking the number form the user,
say congrats and end the game
if the user never guesses the number , ask them 10 times and then end the game !!
"""
import random

num = 1
 
print("Welcome to the number guessing game")
print("You have 10 chances to guess the number between 1 and 10")
secret_number = random.randint(a:=1, b:=10)
attempts = 10
is_guessed = False

while num <= 10:
    print(f"Attempt {attempts}:")
    user_number = int(input("Enter your guess: "))
    if user_number == secret_number:
        print("Congrats! You guessed the number correctly.")
        is_guessed = True   
        break
    else:
        if user_number < secret_number:
            higher_or_lower = "higher"
        else:
            higher_or_lower = "lower"
        print(f"Wrong guess! The secret number is {higher_or_lower} than your guess.")

    num += 1
    attempts -= 1

if not is_guessed:
    print(f"Sorry, you didn't guess the number. The secret number was {secret_number}.")
print("Game over!")

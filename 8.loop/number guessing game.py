"""
Roll a dice
write a program that simulates rolling a dice. 
The program should generate a random number between 1 and 6 (inclusive)
and print the result to the user.
"""
import random

print("welcome to the dice roller!")

while True:
    choice = input("Do you want to roll the dice? (yes/no): ")
    if choice=="no":
        print("Thanks for playing! Goodbye!")
        break
    elif choice=="yes":
        number = random.randint(1, 6)    
        print(f"You rolled a {number}!")
    else:
        print("Invalid input.")
        
"""
Roll a dice
write a program that simulates rolling a dice. 
The program should generate a random number between 1 and 6 (inclusive)
and print the result to the user.
"""
import random

print("welcome to the dice roller!")

while True:
    choice = input("Do you want to roll the dice? (yes/no): ")
    if choice=="no":
        print("Thanks for playing! Goodbye!")
        break
    elif choice=="yes":
        number = random.randint(1, 6)    
        print(f"You rolled a {number}!")
    else:
        print("Invalid input.")
        
""" 
Number Guessing Game
write a program that simulates a number guessing game.

The program should generate a random number between 1 and 100 (inclusive)
and ask the user to guess the number.
The program should give feedback to the user whether their guess is too low, too high, or correct.
The game should continue until the user guesses the correct number.
"""
import random
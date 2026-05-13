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
        
c
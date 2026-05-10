# Infinite While Loop
"""
Infinite Loop: This is the most critical error with while loops. It happens when the 
condition never becomes False, causing the loop to run endlessly. Your program will 
appear to freeze, or it might continuously print output. 
Python does not have a built-in mechanism to stop an infinite loop, so you will need to manually interrupt it 
(e.g., by pressing Ctrl+C in the terminal) to regain control of your program.
"""
"""
counter = 0 
while counter < 5: 
    print("Stuck!") #! This will print "Stuck!" forever 
#* Missing: counter += 1 
"""

correct_password ="secret"

while True : #infinte loop
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("Access granted!")
        break # Exit the loop when the correct password is entered
    else:
        print("Incorrect password, try again.")

num = 20

while num >=10:
    print(num)
    num = num-2
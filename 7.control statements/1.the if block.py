#|| The if Statement ||

"""
 The if statement is the simplest decision-making statement. It executes a block of code only
if a specified condition evaluates to True.
*indentation but the spaces to create block
*block is a multiple lines of code 
"""

"""
*syntax
*if condition:
 Code to execute if the condition is True
 (This code block MUST be indented)
"""


age = float(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")

print("welcome")

age2= float(input("Enter your age: "))
if age2 <= 18:
   print("You are an child")
print("welcome")



# Nothing is printed because the condition (16 >= 18) is False


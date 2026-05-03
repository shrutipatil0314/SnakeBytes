#|| 1.4 The if-else Statement  ||

"""
The if-else statement allows your program to execute one block of code if the condition is
True, and a different block of code if the condition is False. It provides an alternative path.
"""

"""
*syntax
if condition:
 Code to execute if the condition is True
*else:
 Code to execute if the condition is False
 (This code block MUST also be indented)
"""

age = float(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
   print("You are an child")
print("welcome")


uesrname = input("Enter your username: ")
password = input("Enter your password: ")

if uesrname == "shruti" and password == "12345":
    print("welcome to your login" )

else:
    print("your uesrname or password is incorrect")

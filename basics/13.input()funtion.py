#|| input () function
# input () function is used to take input from the user.  

#Syntax:
# input(prompt)


#Example 1: Basic Usage
name = input("Enter your name: ")
print("Hello, " + name + "!")

#Example 2: Taking numerical input

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("The sum of", num1, "and", num2, "is", result)

#Example 3: Taking multiple inputs

num1, num2 = map(int, input("Enter two numbers separated by space: ").split())
result = num1 + num2
print("The sum of", num1, "and", num2, "is", result)

#Example 4: Taking input without prompt

age = input("Enter your age: ")
print("Your age is:", age)

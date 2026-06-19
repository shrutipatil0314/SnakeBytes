# || Introduction to Functions in Python  ||

#^ Functions are a fundamental building block in Python programming. 
#^ They allow you to encapsulate code into reusable blocks, making your code more organized and easier to maintain.
#^    In this introduction, we will cover the basics of defining and using functions in Python.

#* Defining a Function:

#^ In Python, you define a function using the 'def' keyword, followed by the function
#^ name and parentheses. You can also specify parameters within the parentheses if your function needs to accept input values.

# Example:
def greet():
    print("Hello! Welcome to the world of functions.")

# Calling the function
greet()

# with parameters:
def greet(name):
    print(f"Hello, {name}! Welcome to the world of functions.")

# Calling the function with an argument
greet("Alice")

#* Return Values:
#^ Functions can also return values using the 'return' statement.
#^ This allows you to capture the output of a function and use it elsewhere in your code.

def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
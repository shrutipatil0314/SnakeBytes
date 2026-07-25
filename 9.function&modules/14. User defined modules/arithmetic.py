"""
a simple arithmetic module that provides basic mathematical operations such as
addition, subtraction, multiplication, and division.
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2



if __name__ == "__main__":
    # Example usage of the arithmetic module
    a = 55
    b = 5

    print(f"Addition of {a} and {b} is: {add(a, b)}")
    print(f"Subtraction of {a} and {b} is: {subtract(a, b)}")
    print(f"Multiplication of {a} and {b} is: {multiply(a, b)}")
    print(f"Division of {a} and {b} is: {divide(a, b)}")
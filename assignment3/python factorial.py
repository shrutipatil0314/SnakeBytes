"""
Task 1: Calculate Factorial Using a Function 
"""

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


number = int(input("Enter a number: "))
print(f"Factorial of {number} is: {factorial(number)}")
## // Types of arguments //

#* 1. Positional arguments
def add(num1, num2):
    return num1 + num2

print(add(5, 3))

#* 2. Keyword arguments
def subtract(num1, num2):
    return num1 - num2
    
print(subtract(num2=3, num1=5))

#* 3. Default arguments
def multiply(num1, num2=2):
    return num1 * num2

print(multiply(5))
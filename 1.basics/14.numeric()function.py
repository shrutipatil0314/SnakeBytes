#**|| NUMERIC FUNCTIONS ||**#

#!!The numeric functions in Python are used to perform various mathematical operations on numbers.
#Here are some commonly used numeric functions:

#1. abs(): This function returns the absolute value of a number.
num = -5
print(abs(num))  # Output: 5

#2. round(): This function rounds a number to a specified number of decimal places.
num = 3.14159
print(round(num, 2))  # Output: 3.14

#3. pow(): This function returns the value of a number raised to the power of another number.
base = 2
exponent = 3
print(pow(base, exponent))  # Output: 8

#4. max(): This function returns the largest of the given numbers.
print(max(1, 5, 3))  # Output: 5

#5. min(): This function returns the smallest of the given numbers.
print(min(1, 5, 3))  # Output: 1

#6. sum(): This function returns the sum of all the numbers in an iterable (like a list).
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15

#7. divmod(): This function takes two numbers and returns a tuple containing 
#the quotient and the remainder.
numerator = 10
denominator = 3
result = divmod(numerator, denominator)
print(result)  # Output: (3, 1)

#8. int(): This function converts a number or a string to an integer.
num_str = "42"
print(int(num_str))  # Output: 42

#9. float(): This function converts a number or a string to a floating-point number.
num_str = "3.14"
print(float(num_str))  # Output: 3.14

#10. complex(): This function creates a complex number from real and imaginary parts.
real_part = 2
imaginary_part = 3
complex_num = complex(real_part, imaginary_part)
print(complex_num)  # Output: (2+3j)

#!!These are just a few examples of the numeric functions available in Python.
#!!You can explore more functions in the Python documentation for further mathematical operations.

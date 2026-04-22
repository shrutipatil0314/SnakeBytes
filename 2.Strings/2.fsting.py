#||** F-Strings in Python **||#

#** F-strings, also known as formatted string literals, are a way to embed expressions 
#**inside string literals, using a minimal syntax. They were introduced in Python 3.6.**

name = "Alice"
age = 30
#^^ Using f-strings to format a string with variables.

greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  #& Output: Hello, my name is Alice and I am 30 years old.

#^^ We can also use expressions inside f-strings.

x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}"
print(result)  #& Output: The sum of 10 and 5 is 15

#** F-strings can also include format specifiers to control the formatting of the output.**

pi = 3.14159
formatted_pi = f"Pi is approximately {pi:.2f}"
print(formatted_pi)  #& Output: Pi is approximately 3.14
#^^ The format specifier :.2f formats the value of pi to 2 decimal places


#summary = """
#** F-strings, also known as formatted string literals, 
#**are a way to embed expressions inside string literals, using a minimal syntax. 
#**They were introduced in Python 3.6.**
#** F-strings can include variables and expressions inside curly braces {}.**
#** F-strings can also include format specifiers to control the formatting of the output.**
#"""
#literals

#integer- whole number 

a=10 #positive integer
b=-5 #negative integer
print(a)
print(type(a)) #output: <class 'int'>
print(b)
 
#float-decimal number

c=3.14
d=-0.001
print(type(c)) #output: <class 'float'>
print(d)
 
#string- sequence of characters

d="Hello, World!"
print(type(d)) #output: <class 'str'>
print(d)

#boolean- true or false

active=True
closed=False
print(type(active)) #output: <class 'bool'>
print(type(closed)) #output: <class 'bool'>
print(True+1) #output: 2
print(False+1) #output: 1

#they subclass int, so they can be used in arithmetic operations where True is treated as 1 and False is treated as 0.

#   None- represents the absence of a value
result=None
if result is None:
    print("No result found.") #run this code and it will print "No result found."


#string literals can be defined using single quotes, double quotes, or triple quotes
g='Hello'
h="World"
i="""This is a string literal that can span multiple lines."""
print(g)
print(h)
print(i)

"""
#summary:
 The code demonstrates the use of different types of literals in Python, including integers, floats,

strings, booleans, and None. It shows how to define and use these literals, as well as their types

 and some basic operations.
"""
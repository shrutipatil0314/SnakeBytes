#Variable 

"""
Variable is a container for storing data values. A Variable is created by assigning a value to it using the assignment operator (=). 
 The value can be of any data type, such as a number, string, or list.
"""
#example of Variable assignment and usage

#1
a=10 #assigning an integer value to Variable a
b=20
c=a+b #assigning the sum of a and b to Variable c
print(c) #output: 30


del c #deleting Variable c
# print(c) #this will raise an error because Variable c has been deleted    
print(c) #this will raise an error because Variable c has been deleted


x=5
y=10
z=x+y
print(z) #output: 15


a="Hello"
b="World"
c=a+b
print(c) #output: HelloWorld


_a=100 #Variable name can start with an underscore
print(_a) #output: 100  


5=10 #this will raise a syntax error because Variable name cannot start with a number   

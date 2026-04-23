# || Operations on String ||

#**String Concatenation**

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  #& Output: John Doe

#**String Length**

greeting = "Hello, World!"
print(len(greeting))  #& Output: 13

#**String Indexing**

message = "Hello, World!"
print(message[0])  #& Output: H
print(message[7])  #& Output: W 
print(message[-1]) #& Output: ! 

#**String Membership**

#^^We can check if a substring is present in a string using the in keyword.
print("Hello" in message)  #& Output: True
print("Python" in message)  #& Output: False

#**String Repetition**

#^^We can repeat a string multiple times using the * operator.
print("Hello " * 3)  #& Output: Hello Hello Hello

#**String strip**

#^^We can remove whitespace from the beginning and end of a string using the strip() method.
text = "   Hello, World!   "
print(text.strip())  #& Output: Hello, World!
print(text.lstrip()) #& Output: Hello, World!   
print(text.rstrip()) #& Output:    Hello, World!


#**String replace**
#^^We can replace a substring with another substring using the replace() method.
text = "Hello, World!"
print(text.replace("World", "Python"))  #& Output: Hello, Python!
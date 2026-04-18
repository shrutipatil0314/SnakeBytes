#**STRING ** 


#Escaping characters


#/n
print("Hello\nWorld")

#/t
print("Hello\tWorld")

# \\
#  to print a backslash
print("This is a backslash: \\")    

# \"
# to include a double quote in a string
print("She said, \"Hello!\"")

# \'
#  to include a single quote in a string
print('It\'s a nice day!')  


#**operations on strings**


#String Concatenation
first_name = "John"
last_name = "Doe"   
full_name = first_name + " " + last_name
print(full_name)


#string length
greeting = "Hello, World!"
print(len(greeting))


#String indexing
message = "Hello, World!"
print(message[0])  # ! frst character 
print(message[7])  # W
print(message[-1]) # ! (last character)


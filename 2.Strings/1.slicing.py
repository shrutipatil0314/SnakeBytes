#||**slicing in strings**||
"""
 slicing in strings is similar to slicing in lists.
 We can use the same syntax to slice a string.
"""
s1 = "Hello, World!"
#^^ slicing from index 0 to 4 (not including 5)

print(s1[0:5])  #& Output: Hello

s1_slice = s1[0:5]  #^^ slicing from index 0 to 4 (not including 5)
print(s1_slice)  #& Output: Hello

#!! We can also omit the start index to slice from the beginning of the string.

print(type(s1_slice))  #& Output: <class 'str'>
s2 = "Python Programming"

#^^ slicing from index 7 to the end of the string

print(s2[7:])  #& Output: Programming
#!! We can also omit the end index to slice until the end of the string.

print(s2[:6])  #& Output: Python

#!! We can also use negative indices to slice from the end of the string.

print(s2[-11:])  #& Output: Programming

#* We can also use negative indices to slice from the end of the string. *

print(s2[:-12])  #& Output: Python

"""
#summary = 
 Slicing in strings is similar to slicing in lists.**    
 We can use the same syntax to slice a string.**
 We can omit the start index to slice from the beginning of the string.**
 We can omit the end index to slice until the end of the string.**
 We can use negative indices to slice from the end of the string.
"""

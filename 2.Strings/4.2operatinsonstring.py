#|| operations on string ||

#*counting occurrences of a substring*
#^^The count() method returns the number of occurrences of a substring in a string.

text = "hello world, hello python"
print(text.count("hello"))  #& Output: 2

#*finding the index of a substring*
#^^The find() method returns the index of the first
#^^occurrence of a substring in a string. If the substring is not found, 
#^^it returns -1.

print(text.find("world"))  #& Output: 6\   
print(text.find("python"))  #& Output: 19

#*checking if a string starts with a substring*
#^^The startswith() method returns True if the string starts 
#^^with the specified substring, otherwise False.

print(text.startswith("hello"))  #& Output: True
print(text.startswith("world"))  #& Output: False

#*checking if a string ends with a substring*
#^^The endswith() method returns True if the string ends with the specified substring, 
#^^otherwise False.

print(text.endswith("python"))  #& Output: True
print(text.endswith("world"))  #& Output: False

#!!case sensitivity in string operations!!
#^^String operations are case-sensitive. 
#**For example, the count() method will treat "Hello" and "hello" as 
#*different strings.

print(text.count("Hello"))  #& Output: 0
print(text.count("hello"))  #& Output: 2


#summary:
#*String operations include concatenation, length, indexing, membership, repetition, 
#**stripping, replacing, counting occurrences, finding index, checking start 
#**and end of string.
#*String operations are case-sensitive.


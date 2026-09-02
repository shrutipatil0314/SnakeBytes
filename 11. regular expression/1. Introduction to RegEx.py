# regular expression (RegEx) is a sequence of characters that define a search pattern. 
# It is mainly used for string pattern matching and manipulation. In Python, 
# the `re` module provides support for working with regular expressions.

message = "Hello , welcome to the world of regular expressions!" 

#^ To use regular expressions in Python, you need to import the `re` module.

print("Original message" in message)  #* Check if the substring "Original message" is in the message
print("Hello" in message)  #* Check if the substring "Hello" is in the message (case-sensitive  )
print("Original message:", message)
print("Length of the message:", len(message))

print(message.find("welcome"))  #* Find the index of the substring "welcome" in the message
print(message.find("Python"))  #* Find the index of the substring "Python" in the message (not found, returns -1)

"""
# re.search(regex_pattern, string) is a function in the `re` module that searches for a specified pattern (regex_pattern) in a given string.
# If the pattern is found, it returns a match object; otherwise, it returns None.
"""

import re  #^ Import the `re` module for regular expressions

message = "Hello , welcome to the world of regular expressions!" 

match_obj = re.search(r"welcome", message)  #* Search for the substring "welcome" in the message using a regular expression
print(match_obj)  #* Print the match object if found, otherwise None


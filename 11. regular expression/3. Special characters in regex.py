import re 

s1 = "Hello , welcome to the world of regular expressions!"

# [A-Z] matches any uppercase letter from A to Z

pat = r"[A-Z][a-z][a-z]"  #* Define a regex pattern to match any uppercase letter followed by zero or more lowercase letters
match_obj = re.search(pat, s1)  #* Search for the pattern in the string s1
print(match_obj)  #* Print the match object (None if no match is found)


#\d and \D are used to match digits and non-digits respectively.
#\d matches any digit (0-9), while \D matches any character that is not a digit.

# \D matches any non-digit character (anything that is not 0-9)
pat = r"[a-z] [a-z] [a-z]\D"  #* Define a regex pattern to match any non-digit character
match_obj = re.search(pat, s1)  #* Search for the pattern in the string s1
print(match_obj)  #* Print the match object (None if no match is found)
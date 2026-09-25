import re 

s1 = "Hello , welcome to the world of regular expressions!"

# [A-Z] matches any uppercase letter from A to Z

pat = r"[A-Z][a-z][a-z]"  #* Define a regex pattern to match any uppercase letter followed by zero or more lowercase letters
match_obj = re.search(pat, s1)  #* Search for the pattern in the string s1
print(match_obj)  #* Print the match object (None if no match is found)
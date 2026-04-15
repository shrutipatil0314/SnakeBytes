#//logical operators\\#

#Logical operators are used to combine conditional statements. They include:
# and - returns True if both statements are true
# or - returns True if at least one statement is true
# not - reverse the result, returns False if the result is true

a = 10
b = 20

print(a > 5 and b > 15) #True
#?? checks if both conditions are true

print(a > 5 or b < 15) #True
#?? checks if at least one condition is true

print(not(a > 5)) #False
#?? negates the condition, checks if a is not greater than 5

#logical operators with non-boolean values#

x = 0
y = 5

print(x and y) #0
#?? returns the first falsy value or the last value if all are truthy

print(x or y) #5
#?? returns the first truthy value or the last value if all are falsy

print(not x) #True
#?? negates the value of x, returns True if x is falsy, otherwise returns False

#logical operators with boolean values#
p = True
q = False
print(p and q) #False
#?? returns True if both p and q are True, otherwise returns False

print(p or q) #True
#?? returns True if at least one of p or q is True, otherwise returns False

print(not p) #False
#?? negates the value of p, returns False if p is True, otherwise returns True

#logical operators with mixed values#

print(p and x) #0
#?? returns the first falsy value or the last value if all are truthy

print(p or x) #True
#?? returns the first truthy value or the last value if all are falsy

print(not q) #True
#?? negates the value of q, returns True if q is False, otherwise returns False

#logical operators can be used in complex expressions#

print((a > 5 and b > 15) or (x < 1 and y > 3)) #True
#?? evaluates the expression inside the parentheses first, then combines the results with the logical operators





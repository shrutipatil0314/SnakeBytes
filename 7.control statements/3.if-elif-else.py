#|| The elif Statement (Else If)  ||
#^ When you have more than two possible outcomes (more than just True or False), you use
#^ the elif (short for "else if") statement. This allows you to check multiple conditions
#^ sequentially.


#*Syntax:

#*if condition1:
# Code if condition1 is True
#*elif condition2:
# Code if condition1 is False AND condition2 is True
#*elif condition3:
# Code if condition1 is False AND condition2 is False AND condition3 is
#True
#*else:
# Code if all above conditions are False

marks = float(input("Enter your marks: "))
if marks >=90:
    print("excellent")
elif marks >=80 and marks <90:
    print ("garde A")
elif marks >=70 and marks <90:
    print ("garde B")

elif marks >=60 and marks <90:
    print ("garde C")

elif marks >=50 and marks <90:
    print ("garde D")

else:
    print("fail")


#|| nested if statement ||
#^A nested if-else statement in Python is simply an if or else block that contains 
#^another if or else block inside it. This is useful when you need to check 
#^multiple conditions that depend on one another.

#*if outer_condition:
    # Executes if outer_condition is True
  #*  if inner_condition:
        # Executes only if both outer and inner conditions are True
    #*    print("Both conditions are met.")
    #*else:
        # Executes if outer is True but inner is False
      #*  print("Outer met, but inner failed.")
#*else:
    # Executes if outer_condition is False
  #*  print("Outer condition failed.")

marks = float(input("Enter your marks: "))
if marks >=35:
    print("pass")
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

    elif marks >=40 and marks <90:
           print ("garde E")
    elif marks >=35 and marks <90:
           print ("just pass")
else:
      print ("fall")

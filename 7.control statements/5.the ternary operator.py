#|| trenary operator ||

#^ the trenary operator is a concies way or concise syntax for writing
#^ simple if else statements in a single line 
#^ evaluates the value based on a condition

num = int(input("Enter a number: "))
if num %2 == 0:
  print("even")
else:
  print("odd")

#* true-expression if conditionelse false-expression
#^one liner
print("even") if num %2 ==0 else print("odd")

#|| 1.4 The if-else Statement  ||

"""
The if-else statement allows your program to execute one block of code if the condition is
True, and a different block of code if the condition is False. It provides an alternative path.
"""

"""
*syntax
if condition:
 Code to execute if the condition is True
*else:
 Code to execute if the condition is False
 (This code block MUST also be indented)
"""

age = float(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
   print("You are an child")
print("welcome")


uesrname = input("Enter your username: ")
password = input("Enter your password: ")

if uesrname == "shruti" and password == "12345":
    print("welcome to your login" )

else:
    print("your uesrname or password is incorrect")


# Nothing is printed because the condition (16 >= 18) is False

# The range () funtion
#"""range () - bulit - in funtion used to generate sequence of integers in a given int
#range (start , stop , step ) stop is not included

#^ for i in range (start, stop, step):
      #statements
#
for i in range(1,11,3): # 1 , 2, 3, .... 8,9
    print(i)

#^ generate even numbers between 1 and 10 (10 exclued)
for i in range(2,10,2):
    print(i)
#^ reverse order -> 2- , 0 , 10 (excluding 10)
 #^    only even
for i in range(10,0,-2):
    print(i)
for i in range(10,0,-1):
    print(i)
print("happy new year")
#^ range(start,stop)-> step = 1 by default
for i in range (1,5): #step =1
    print(i)
groceries =['salt','sugar','rice']
for index in range (len(groceries)):
    print(index,groceries[index])
    print(groceries[index])
    q=index+1
    
    print (q,groceries[index])




# // modules in python //
#^ built-in modules are the modules that come with python installation. 
#^ we can use them directly without any installation.
#^ math , random , datetime , os , sys , json , re , urllib , 
#^ etc are some of the built-in modules in python.

#* how to import a module in python 
# & syntax : import module_name
# & syntax for importing only few funtions / variables : from module_name import f1 , f2 , f3


import math
import random

#^ calculate the square root of a number using math module

num = 100
output = math.sqrt(num) #* module_name.function_name(arg1, arg2, arg3,......)

print(f"the square root of {num} is : {output}")    

#^ calculate the factorial of a number using math module

num = 5
output = math.factorial(num)
print(f"the factorial of {num} is : {output}")


#^ throw a die
from random import randint


value = randint(1, 6) #* randint(a, b) returns a random integer N such that a <= N <= b
print(f"the value of the die is : {value}")


import datetime as dt

t = dt.datetime.now() #* returns the current local date and time
print(f"the current date and time is : {t}")

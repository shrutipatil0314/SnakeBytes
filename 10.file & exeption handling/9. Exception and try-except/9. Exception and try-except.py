#9. Exception and try-except
#* Exception handling is a mechanism to handle runtime errors, 
#* allowing the program to continue its execution instead of crashing. 
#* In Python, this is done using the try-except block.

#^ compile time error => syntax error, indentation error, etc.

#a = 10
#print(a+b)

#^ exception => runtime error, logical error, etc.

#* how to handle errors
try: 
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid integers!")    

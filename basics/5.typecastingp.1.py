# ! TYPE CASTING !
#Converting one data type to another data type is called type casting.
#In Python, we can convert data types using built-in functions like int(), float(), str(), etc.
#Example of type casting


#Converting a string to an integer

num_1= "123"
num_int = int(num_1)
print(num_int) #Output: 123
print(type(num_int)) #Output: <class 'int'>


#Converting a float to an integer
num_2 = 3.14
num_int_2 = int(num_2)
print(num_int_2) #Output: 3
print(type(num_int_2)) #Output: <class 'int'>


#Converting an integer to a float
num_3 = 10
num_float = float(num_3)
print(num_float) #Output: 10.0
print(type(num_float)) #Output: <class 'float'>


#Converting an integer to a string
num_4 = 456
num_str = str(num_4)
print(num_str) #Output: 456
print(type(num_str)) #Output: <class 'str'>

#Converting a float to a string
num_5 = 3.14
num_str_2 = str(num_5)
print(num_str_2) #Output: 3.14
print(type(num_str_2)) #Output: <class 'str'>

#Converting a string to a float
num_6 = "3.14"
num_float_2 = float(num_6)
print(num_float_2) #Output: 3.14
print(type(num_float_2)) #Output: <class 'float'>

#Note: When converting a string to an integer or float, the string must be a valid representation of a number, otherwise it will raise a ValueError.    

#ehwn we cahnge the data type of a variable, we can use the same variable name to store the new value. This is called variable reassignment. For example:
num = 10
print(num) #Output: 10  

num = "Hello"
print(num) #Output: Hello   

#when we perform type casting, the original variable remains unchanged unless we reassign it to the new value. For example:
num = 10    
num_str = str(num) #Type casting num to a string and storing it in num_str
print(num) #Output: 10 (original variable remains unchanged)
print(num_str) #Output: 10 (new variable num_str holds the string representation of num)

#In summary, type casting is a powerful feature in Python that allows us to convert data types as needed. It is important to be mindful of the data types we are working with and to use type casting appropriately to avoid errors and ensure our code runs smoothly.




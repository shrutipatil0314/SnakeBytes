# ! TYPE CASTING BOOLEAN VALUES
#In Python, we can also convert other data types to boolean values using the bool() function.
#The following values are considered False in Python:

VALLUES_CONSIDERED_FALSE = [0, 0.0, 0j, '', [], {}, set(), None, False]
#All other values are considered True in Python.

#Example of type casting to boolean values

#Converting a string to a boolean
str_3 = "Hello"
bool_str_3 = bool(str_3)
print(bool_str_3) #Output: True


#Converting an integer to a boolean

num_7 = 0
bool_num_7 = bool(num_7)
print(bool_num_7) #Output: False


#Converting a non-zero integer to a boolean

num_8 = 5
bool_num_8 = bool(num_8)
print(bool_num_8) #Output: True


#Converting an empty string to a boolean


str_1 = ""
bool_str_1 = bool(str_1)

print(bool_str_1) #Output: False


#Converting a non-empty string to a boolean


str_2 = "Hello"
bool_str_2 = bool(str_2)
print(bool_str_2) #Output: True


#Converting an empty list to a boolean


list_1 = []
bool_list_1 = bool(list_1)
print(bool_list_1) #Output: False


#Converting a non-empty list to a boolean


list_2 = [1, 2, 3]
bool_list_2 = bool(list_2)
print(bool_list_2) #Output: True


#Converting None to a boolean


none_value = None
bool_none_value = bool(none_value)
print(bool_none_value) #Output: False


#Converting False to a boolean


false_value = False
bool_false_value = bool(false_value)
print(bool_false_value) #Output: False


#Converting True to a boolean


true_value = True
bool_true_value = bool(true_value)
print(bool_true_value) #Output: True



#In summary, when we use the bool() function to convert a value to a boolean, it will return False for values that are considered "falsy" and True for all other values. This can be useful in conditional statements and when evaluating the truthiness of values in Python.

#|| tuples ||
"""
 tuples are immutable sequences, typically used to store collections of heterogeneous data.
 they are defined by enclosing the elements in parentheses () 
 and separating them with commas.
"""

#*Creating a tuple
my_tuple = (1, 2, 3, 'hello', [4, 5], (6, 7))
print(my_tuple)  #& Output: (1, 2, 3, 'hello', [4, 5], (6, 7))

"""
*Accessing elements in a tuple
print(my_tuple[0])  #& Output: 1
print(my_tuple[3])  #& Output: 'hello'
print(my_tuple[4])  #& Output: [4, 5]
print(my_tuple[5])  #& Output: (6, 7)
print(my_tuple[4][0])  #& Output: 4
print(my_tuple[5][0])  #& Output: 6
"""

"""
#*Tuples are immutable
# my_tuple[0] = 10  #^ This will raise a TypeError because tuples 
                         #^cannot be modified
# print(my_tuple)
"""

#*However, if a tuple contains mutable objects like lists,
# we can modify those mutable objects.
my_tuple[4][0] = 10
print(my_tuple)
#& Output: (1, 2, 3, 'hello', [10, 5], (6, 7))

"""
#summary:# - Tuples are immutable sequences defined by parentheses ().
 - They can contain heterogeneous data types
 - You can access elements in a tuple using indexing, 
 but you cannot modify the tuple itself.
 - However, if a tuple contains mutable objects like lists,
 you can modify those mutable objects
- Tuples are often used to group related data together,
 such as coordinates, database records, or function return values.
"""
#||     operations on tuples     ||
"""
 since tuples are immutable, we cannot modify them directly.
 However, we can perform various operations on tuples to create new tuples or 
 to access their elements.
"""
#*Concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
result = tuple1 + tuple2
print(result)
#& Output: (1, 2, 3, 'a', 'b', 'c')

#*Repetition
tuple3 = (1, 2)
result = tuple3 * 3
print(result)
#& Output: (1, 2, 1, 2, 1, 2)

#*Membership testing
my_tuple = (1, 2, 3, 'hello')
print(2 in my_tuple)  #& Output: True
print('world' in my_tuple)  #& Output: False

#*Length
print(len(my_tuple))  #& Output: 4

#*Slicing
print(my_tuple[1:3])  #& Output: (2, 'hello')
print(my_tuple[:2])  #& Output: (1, 2)
print(my_tuple[2:])  #& Output: (3, 'hello')    

#*Unpacking
a, b, c, d = my_tuple
print(a)  #& Output: 1
print(b)  #& Output: 2

#*min
print(min(my_tuple))  #& Output: 1

#*max
print(max(my_tuple))  #& Output: 'hello'

#*index
print(my_tuple.index('hello'))  #& Output: 3
#*count
print(my_tuple.count(2))  #& Output: 1

#*sorted
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)
#& Output: [1, 2, 3, 'hello']

#*reversed
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)
#& Output: ('hello', 3, 2, 1)

#*sum - only works with numeric tuples
numeric_tuple = (1, 2, 3, 4)
print(sum(numeric_tuple))  #& Output: 10

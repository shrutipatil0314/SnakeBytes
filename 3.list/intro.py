#||     introduction to list     ||
#^^   list is a collection of items in a particular order
#^^     list is mutable (can be changed)
#^^     list is defined by square brackets []
#^^     list can contain different types of data

#*creating a list*
my_list = [1, 2, 3, "hello", True]
print(my_list)  #& Output: [1, 2, 3, 'hello', True]
print(type(my_list))  #& Output: <class 'list'>
py 
#length of a list
print(len(my_list))  #& Output: 5
print(len([]))  #& Output: 0    

print(list("hello"))  #& Output: ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))  #& Output: [1, 2, 3]
print(list({1: "one", 2: "two"}))  #& Output: [1, 2]



#||     introduction to list     ||
""" 
   list is a collection of items in a particular order
     list is mutable (can be changed)
     list is defined by square brackets []
     list can contain different types of data
""" 

#*creating a list*
my_list = [1, 2, 3, "hello", True]
print(my_list)  #& Output: [1, 2, 3, 'hello', True]
print(type(my_list))  #& Output: <class 'list'>

#**length of a list
print(len(my_list))  #& Output: 5
print(len([]))  #& Output: 0    

print(list("hello"))  #& Output: ['h', 'e', 'l', 'l', 'o']
print(list((1, 2, 3)))  #& Output: [1, 2, 3]
print(list({1: "one", 2: "two"}))  #& Output: [1, 2]

#**accessing list items**
print(my_list[0])  #& Output: 1
print(my_list[3])  #& Output: 'hello'
print(my_list[-1])  #& Output: True
print(my_list[1:4])  #& Output: [2, 3, 'hello']
print(my_list[:3])  #& Output: [1, 2, 3]
print(my_list[2:])  #& Output: [3, 'hello', True]

#**modifying list items**
my_list[0] = 10
print(my_list)  #& Output: [10, 2, 3, 'hello', True]

my_list[1:3] = [20, 30]
print(my_list)  #& Output: [10, 20, 30, 'hello', True]

my_list.append("world")
print(my_list)  #& Output: [10, 20, 30, 'hello', True, 'world']

my_list.insert(2, 25)
print(my_list)
#& Output: [10, 20, 25, 30, 'hello', True, 'world']

my_list.remove("hello")
print(my_list)  #& Output: [10, 20, 25, 30, True, 'world']

my_list.pop(3)
print(my_list)  #& Output: [10, 20, 25, True, 'world']

my_list.clear()
print(my_list)  #& Output: []

my_list.extend([1, 2, 3])
print(my_list)
#& Output: [1, 2, 3]

my_list.extend((4, 5, 6))
print(my_list)
#& Output: [1, 2, 3, 4, 5, 6]

my_list.extend({7: "seven", 8: "eight"})
print(my_list)
#& Output: [1, 2, 3, 4, 5, 6, 7, 8]

my_list.sort()
print(my_list)
#& Output: [1, 2, 3, 4, 5, 6, 7, 8]

my_list.reverse()
print(my_list)
#& Output: [8, 7, 6, 5, 4, 3, 2, 1]

my_list.sort(reverse=True)
print(my_list)
#& Output: [8, 7, 6, 5, 4, 3, 2, 1]




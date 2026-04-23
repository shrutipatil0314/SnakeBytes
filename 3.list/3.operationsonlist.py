#||    list operations     ||

#*removing from a list
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  #& Removes the first occurrence of 3
print(my_list)  #& Output: [1, 2, 4, 5]



#*popping from a list
popped_element = my_list.pop()  #&  Pops the last element
print(popped_element)  #& Output: 5
print(my_list)  #& Output: [1, 2, 4]


#*extending a list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  #& Output: [1, 2, 3, 4, 5, 6]

#*clearing a list
my_list.clear()
print(my_list)  #& Output: []

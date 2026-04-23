#|| operations on list     ||

#*slicing a list
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])  #& Output: [2, 3, 4]
print(my_list[:3])   #& Output: [1, 2, 3]
print(my_list[2:5])  #& Output: [3, 4, 5]
print(my_list[2:])   #& Output: [3, 4, 5]
print(my_list[:])    #& Output: [1, 2, 3, 4, 5]

#*concatenation of lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  #& Output: [1, 2, 3, 4, 5, 6]

#*repetition of lists
repeated_list = list1 * 3
print(repeated_list)  #& Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

#*appending to a list
my_list.append(6)
print(my_list)  #& Output: [1, 2, 3, 4, 5, 6]

#*inserting into a list
my_list.insert(2, "inserted")
print(my_list)  #& Output: [1, 2, 'inserted', 3, 4, 5, 6]


# || nested lists ||

#*lists inside lists 
my_list = [1, 2, 3, [4, 5, 6], 7, 8]
print(my_list)  #& Output: [1, 2, 3, [4, 5, 6], 7, 8]

#*Accessing elements in a nested list
print(my_list[3])  #& Output: [4, 5, 6]
print(my_list[3][0])  #& Output: 4

#*Modifying elements in a nested list

my_list[3][1] = 10
print(my_list)  #& Output: [1, 2, 3, [4, 10, 6], 7, 8]

"""
explanation: my_list[3] accesses the nested list [4, 5, 6], and 
my_list[3][1] accesses the second element of that nested list, which is 5. 
We then change it to 10.
"""

#*Adding a new nested list
my_list.append([9, 10])
print(my_list)  #& Output: [1, 2, 3, [4, 10, 6], 7, 8, [9, 10]]


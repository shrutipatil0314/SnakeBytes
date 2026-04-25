#||    list operations     ||

#*reversing a list
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  #& Output: [5, 4, 3, 2, 1]

#*sorting a list
my_list.sort()
print(my_list)
#& Output: [1, 2, 3, 4, 5]
my_list.sort(reverse=True)
print(my_list)  #& Output: [5, 4, 3, 2, 1]

#*counting occurrences in a list
my_list = [1, 2, 3, 2, 4, 2, 5]
count = my_list.count(2)
print(count)  #& Output: 3

#*membership testing in a list
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  #& Output: True
print(6 in my_list)  #& Output: False



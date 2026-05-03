#||   introdusction to sets in python  ||
"""
 sets are unordered collection of unique items
 sets are mutable, meaning you can add or remove items from a set after it has
 been created
 sets are defined using curly braces {} or the set() function    
 sets dont have duplicate elemants 
"""
#* creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

#** creating a set using the set() function
my_set2 = set([1, 2, 3, 4, 8, 5])
print(my_set2) 


#* cannot have indexing with sets 

#print(my_set[0])  #will give error   

#* length of the set 

print(len(my_set))

#^ sets dont allow duplicate elements
my_set3 = {1,2.5,3,4,5,5,5,5,5}
print(my_set3)

#&output = {1,2.5,3,4,5}

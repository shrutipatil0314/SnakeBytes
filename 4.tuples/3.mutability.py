#|| list are mutable, tuples are immutable ||
# This means that once a tuple is created, its elements cannot be changed, added, or removed.
# In contrast, lists can be modified after they are created.

#example of mutability with lists
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  #& Output: [10, 2, 3]

#example of immutability with tuples
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  #^ This will raise a TypeError because tuples cannot be modified
# print(my_tuple)

#summary:
# - Lists are mutable, meaning you can change their contents after creation.
# - Tuples are immutable, meaning once they are created, their contents cannot be changed.

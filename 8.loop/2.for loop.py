#|| loops ||
"""
 it is an iterator based loop which steps through the items of a collection 
(lists , tuples , sets, dict, str) , and  executes a block od code repeatedly 
for a number of time equal to the number of items in the collection
"""

"""
#*for var in sequence:
#     statement 1
#     statement2
#     .........
#     statement n
"""

percents = [66.5 , 83.2 , 86.4 , 97.3]
print(percents[0])
print(percents[1])
print(percents[2])
print(percents[3])
#                      ^   2 diff method 
for x in percents:
    print(x)
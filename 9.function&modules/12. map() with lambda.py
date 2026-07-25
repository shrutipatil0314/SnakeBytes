# // map (function, iterable) -> map object
#  map() function is used to apply a given function to each item of an iterable 
# (list, tuple etc.) and returns a map object.

sequence = [1, 2, 3, 4, 5]
mapped_result = map(lambda x: x * 2, sequence)
print(mapped_result)
print(f"double of each number in the list are : {list(mapped_result)}")         
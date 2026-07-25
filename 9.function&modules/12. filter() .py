# // filter (funtion, sequence) -> filter object
#  filter() function is used to filter the given sequence with the help of a function that tests 
# each element in the sequence to be true or not. 

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_result = filter(lambda x:  True if x % 2 != 0 else False, sequence)
print(filtered_result)
print(f"odd number in the list are : {list(filtered_result)}")
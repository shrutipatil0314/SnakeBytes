#||  numerical operation  ||


number = [1, 2, 3, 4, 5]
#* 1. sum()
print(sum(number))  #& Output: 15
#* 2. max()
print(max(number))  #& Output: 5
#*3. min()
print(min(number))  #& Output: 1
#* 4. len()
print(len(number))  #& Output: 5
#* 5. sorted()
print(sorted(number))  #& Output: [1, 2, 3, 4, 5]
#* 6. reversed()
print(list(reversed(number)))  #& Output: [5, 4, 3, 2, 1]
#* 7. enumerate()
for index, value in enumerate(number):
    print(f"Index: {index}, Value: {value}")
#& Output:
# Index: 0, Value: 1
# Index: 1, Value: 2
# Index: 2, Value: 3
# Index: 3, Value: 4
# Index: 4, Value: 5
# 8. map()
squared = list(map(lambda x: x**2, number))
print(squared)  #& Output: [1, 4, 9, 16, 25]
#* 9. filter()
even_numbers = list(filter(lambda x: x % 2 == 0, number))
print(even_numbers)  #& Output: [2, 4]
#* 10. reduce()
from functools import reduce
product = reduce(lambda x, y: x*y, number)
print(product)
#& Output: 120

"""
*summary:
 The code demonstrates various numerical operations on a list of numbers. 
It uses built-in functions like sum(), max(), min(), len(), sorted(), reversed(), and enumerate() 
to perform different operations on the list. Additionally, it utilizes map() to create a new list of squared values, 
filter() to extract even numbers, and reduce() from the functools module to calculate the product of all numbers in the list. 
"""






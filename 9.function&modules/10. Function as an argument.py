# in python , we can pass a function as an argument to another function.
# This is a powerful feature that allows for higher-order functions and 
# functional programming techniques.

def add_1(number):
    return number + 1


def square(number):
    return number **2

num = int(input("Enter a number: "))
res = square(add_1(num))

print(f"output is :     {res}")

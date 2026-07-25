import arithmetic
a = 100
b = 200

reult = arithmetic.add(a, b)
print(f"the sum of {a} and {b} is : {reult}")

result = arithmetic.subtract(a, b)
print(f"the difference of {a} and {b} is : {result}")

result = arithmetic.multiply(a, b)
print(f"the product of {a} and {b} is : {result}")

result = arithmetic.divide(a, b)
print(f"the quotient of {a} and {b} is : {result}")



# for code.py => __name__ of the module is : __main__
# for arithmentic.py => __name__ of the module is : arithmetic
print(f"__name__ of the module is : {__name__}")
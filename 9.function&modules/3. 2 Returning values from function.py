def arithmetic(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div  # Return all results as a tuple




val_1 = int(input("Enter first number: "))
val_2 = int(input("Enter second number: "))

res1, res2, res3, res4 = arithmetic(val_1, val_2)
print(f"Addition: {val_1} and {val_2} is {res1}")
print(f"Subtraction: {val_1} and {val_2} is {res2}")
print(f"Multiplication: {val_1} and {val_2} is {res3}")
print(f"Division: {val_1} and {val_2} is {res4}")
# // Associativity of operators \\

#Associativity of operators determines the order in which operators of the same precedence are evaluated in an expression.
#??associativity determines the order in which operators of the same precedence are evaluated
#in Python, most operators are left-associative, meaning they are evaluated from left to right
#for example, the expression a - b - c is evaluated as (a - b) - c

a = 10
b = 5
c = 2
result = a - b - c
print(result) #3

#??in this case, the expression is evaluated as (10 - 5) - 2, which equals 3
#??some operators are right-associative, meaning they are evaluated from right to left
#for example, the exponentiation operator ** is right-associative, so the expression a ** b ** c
#is evaluated as a ** (b ** c)

result = a ** b ** c
print(result) #1000000000000

#??in this case, the expression is evaluated as 10 ** (5 ** 2), which equals 10 ** 25, resulting in 1000000000000
#??parentheses can be used to change the order of evaluation

result = (a - b) - c
print(result) #3
result = a - (b - c)
print(result) #7

#??in the first case, the expression is evaluated as (10 - 5) - 2, which equals 3
#??in the second case, the expression is evaluated as 10 - (5 - 2), which equals 10 - 3, resulting in 7

name = "Alice"
age = 30

name == "Alice" or "Bob" == name and age > 25

#??in this case, the expression is evaluated as (name == "Alice") or (( "Bob" == name) and (age > 25))
#??which simplifies to True or (False and True), resulting in True

print(name == "Alice" or "Bob" == name and age > 25) #True

#??if we want to change the order of evaluation, we can use parentheses

print((name == "Alice" or "Bob" == name) and age > 25) #True

#??in this case, the expression is evaluated as ((name == "Alice") or ("Bob" == name)) and (age > 25), 
#??which simplifies to (True or False) and True, resulting in True 

#understanding the associativity of operators is important for correctly interpreting 
#and writing expressions in Python.

#it helps to ensure that the intended order of operations is maintained, 
#especially when multiple operators of the same precedence are involved.

#by using parentheses, you can explicitly specify the order of evaluation 
#and avoid any ambiguity in your expressions.

#in summary, associativity of operators determines the order in which operators of the same precedence
#are evaluated,
#and it is important to understand this concept to write correct and unambiguous code in Python.


#||**//precdence of operators\\**||
#precedence of operators determines the order in which operators are evaluated in an expression
#in Python, operators have a specific precedence level, which determines the order of evaluation
#for example, the expression a + b * c is evaluated as a + (b * c) because the multiplication 
#operator has higher precedence than the addition operator

a = 10
b = 5
c = 2
result = a + b * c
print(result) #20

#??in this case, the expression is evaluated as 10 + (5 * 2), which equals 10 + 10, resulting in 20
#??if we want to change the order of evaluation, we can use parentheses

result = (a + b) * c
print(result) #30

#??in this case, the expression is evaluated as (10 + 5) * 2, which equals 15 * 2, resulting in 30
#??understanding the precedence of operators is important for correctly interpreting
#??and writing expressions in Python

#it helps to ensure that the intended order of operations is maintained,
#especially when multiple operators are involved

#by using parentheses, you can explicitly specify the order of evaluation
#and avoid any ambiguity in your expressions

#in summary, precedence of operators determines the order in which operators are evaluated 
#in an expression

#in Python, operators have a specific precedence level, 
#and understanding this precedence is crucial for writing
#correct and unambiguous code.

#associativity of operators determines the order in which operators of the same 
#precedence level are evaluated
#in Python,most operators are left-associative,
#which means that they are evaluated from left to right
#for example, the expression a - b - c is evaluated as (a - b) - c 
#because the subtraction operator is left-associative 

a = 10
b = 5
c = 2   
result = a - b - c
print(result) #3

#??in this case, the expression is evaluated as (10 - 5) - 2, which equals 5 - 2, resulting in 3
#??if we want to change the order of evaluation, we can use parentheses

result = a - (b - c)
print(result) #7

#??in this case, the expression is evaluated as 10 - (5 - 2), which equals 10 - 3, resulting in 7
#??understanding the associativity of operators is important for correctly interpreting
#??and writing expressions in Python, especially when multiple operators of the same precedence level are involved
#??by using parentheses, you can explicitly specify the order of evaluation
#??and avoid any ambiguity in your expressions

#||**//precedence of unary, binary, and ternary operators\\**||

#||unary||

#unary operators, such as the negation operator (-) and the logical NOT operator (not),
#have a higher precedence than binary operators, such as addition and multiplication
#for example, the expression -a + b is evaluated as (-a) + b 
#because the negation operator has higher precedence than the addition operator

a = 10
b = 5
result = -a + b
print(result) #-5
#??in this case, the expression is evaluated as (-10) + 5, which equals -10 + 5, resulting in -5
#??if we want to change the order of evaluation, we can use parentheses

result = -(a + b)   
print(result) #-15

#??in this case, the expression is evaluated as -(10 + 5), which equals -(15), resulting in -15
#??understanding the precedence of unary operators is important for correctly interpreting
#??and writing expressions in Python, especially when unary operators are involved
#??by using parentheses, you can explicitly specify the order of evaluation
#??and avoid any ambiguity in your expressions

#||binary||

#binary operators, such as addition and multiplication, have a lower precedence than unary operators
#for example, the expression a + -b is evaluated as a + (-b)

a = 10
b = 5
result = a + -b
print(result) #5

#??in this case, the expression is evaluated as 10 + (-5), which equals
#??10 - 5, resulting in 5
#??if we want to change the order of evaluation, we can use parentheses

result = (a + -b)
print(result) #5

#??in this case, the expression is evaluated as (10 + (-5)), which equals 10 - 5, resulting in 5
#??understanding the precedence of binary operators is important for correctly interpreting
#??and writing expressions in Python, especially when binary operators are involved
#??by using parentheses, you can explicitly specify the order of evaluation
#??and avoid any ambiguity in your expressions


#||ternary|| 

#also known as the conditional expression, has a lower precedence than most other operators    
#for example, the expression a if condition else b is evaluated as a if condition else b

a = 10
b = 5
condition = True
result = a if condition else b
print(result) #10

#??in this case, the expression is evaluated as 10 if True else 5, which equals 10, resulting in 10
#??if we want to change the order of evaluation, we can use parentheses

result = (a if condition else b)
print(result) #10

#??in this case, the expression is evaluated as (10 if True else 5), 
#which equals 10, resulting in 10
#??understanding the precedence of the ternary operator is important for correctly interpreting
#??and writing expressions in Python, especially when the ternary operator is involved
#by using parentheses, you can explicitly specify the order of evaluation
#??and avoid any ambiguity in your expressions

#||//in summary, understanding the precedence and associativity of operators is crucial for writing
#correct and unambiguous code in Python
#by using parentheses, you can explicitly specify the order of evaluation
#and ensure that your expressions are evaluated in the intended order.\\||

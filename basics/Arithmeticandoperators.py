#Arithmetic Operators

print(5 + 3)  # Addition
print(5 - 3)  # Subtraction
print(5 * 3)  # Multiplication
print(5 / 3)  # Division

#give float value

print(5 // 3) # Floor Division
print(5 % 3)  # Modulus
#gives the remainder of the division
print(5 ** 3) # Exponentiation 
#5*5*5

#Operator Precedence

print(5 + 3 * 2) # Multiplication is done before addition
print((5 + 3) * 2) # Parentheses change the order of operations


#Comparison Operators

print(5 > 3)  # Greater than
print(5 < 3)  # Less than
print(5 >= 3) # Greater than or equal to
print(5 <= 3) # Less than or equal to
print(5 == 3) # Equal to
print(5 != 3) # Not equal to



#Logical Operators

print(True and False)  # Logical AND
print(True or False)   # Logical OR
print(not True)       # Logical NOT



#Bitwise Operators

print(5 & 3)  # Bitwise AND
print(5 | 3)  # Bitwise OR
print(5 ^ 3)  # Bitwise XOR
print(~5)     # Bitwise NOT
print(5 << 1) # Left Shift
print(5 >> 1) # Right Shift


#Identity Operators

a = [1, 2, 3]
b = a  # b references the same list as a
c = [1, 2, 3]  # c is a different list with the same content
print(a is b)  # True, because a and b reference the same object
print(a is c)  # False, because a and c reference different objects
print(a == c)  # True, because a and c have the same content

#Membership Operators

my_list = [1, 2, 3, 4, 5]    

print(3 in my_list)  # True, because 3 is in the list
print(6 in my_list)  # False, because 6 is not in the list
print(3 not in my_list)  # False, because 3 is in the list
print(6 not in my_list)  # True, because 6 is not in the list

#Ternary Operator   

age = 18
status = "Adult" if age >= 18 else "Minor"

print(status)  # Output: Adult




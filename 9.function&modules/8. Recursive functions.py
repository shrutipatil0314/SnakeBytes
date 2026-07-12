# // recursive function to calculate the factorial of a number //
"""
factorial of n => n * (n-1)*(n-2)*...2*1
n!
4! = 4 * 3 * 2 * 1 = 24

n! => n * (n-1)*(n-2)*...2*1
   => n * (n-1)!
   => n * (n-1) * (n-2)!

therefore, we can define the factorial function recursively as follows:
"""

def rec_factorial(n):
    if n == 1:
        return 1
    else:
        factorial = n * rec_factorial(n-1)
    return factorial

print(rec_factorial(4))  # Output: 24
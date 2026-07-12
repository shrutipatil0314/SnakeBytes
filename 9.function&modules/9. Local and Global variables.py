# // local and global variables //

n = 10  # global variable

def func():
    n = 5  # local variable
    print("Local variable n:", n)
    
func()
print("Global variable n:", n)
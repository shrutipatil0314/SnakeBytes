#|| the while loop ||
"""
The while loop is used to execute a block of code repeatedly as long as a certain condition is true.
The syntax of a while loop is as follows:
while condition:
    # code to be executed
"""

#|| example of while loop ||
i=1
while i<=5:
    print(i)
    i=i+1


#|# example of while loop with else ||
i=1
while i<=5:
    print(i)
    i=i+1
else:
    print("i is greater than 5")
    print("end of loop")


#
#|| example of while loop with break ||
i=1
while i<=5:
    if i==3:
        break
    print(i)
    i=i+1
else:
    print("i is greater than 5")
    print("end of loop")
    
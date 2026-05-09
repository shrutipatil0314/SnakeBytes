#|| continue and break ||

"""
continue and break are used to control the flow of a loop.
continue skips the current iteration and moves to the next one.
break exits the loop entirely.
"""

#|| continue ||
for i in range(1, 11):
    if i%2==0:
        continue
    print(i)

#|| break ||
for i in range(1, 11):
    if i==5:
        break
    print(i)

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
    
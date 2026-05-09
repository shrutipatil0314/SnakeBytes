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


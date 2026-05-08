#|| TOTAL , HIGEST AND LOWEST ||

#|| total ||
num1=[10,20,30,40,50]

total=0
for i in num1:
    total=total+i
print(total)    

total= sum(num1)
print(total)

#|| HIGEST ||
higest=num1[0]

for i in num1:
    if i>higest:
        higest=i
print(higest)

higest=max(num1)
print(higest)


#|| LOWEST ||
lowest=num1[0]

for i in num1:
    if i<lowest:
        lowest=i
print(lowest)
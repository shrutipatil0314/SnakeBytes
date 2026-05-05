#|| the range () funtion 

"""
range () - bulit - in funtion used to generate sequence of integers in a given int 
range (start , stop , step ) stop is not included

^ for i in range (start, stop, step):
      #statements
"""

for i in range(1,11,3): # 1 , 2, 3, .... 8,9
    print(i)

#^ generate even numbers between 1 and 10 (10 exclued)

for i in range(2,10,2):
    print(i)


#^ reverse order -> 2- , 0 , 10 (excluding 10)
 #^    only even

for i in range(10,0,-2):
    print(i)

for i in range(10,0,-1):
    print(i)
print("happy new year")

#^ range(start,stop)-> step = 1 by default 

for i in range (1,5): #step =1
    print(i)

groceries =['salt','sugar','rice']
for index in range (len(groceries)):
    print(index,groceries[index])
    print(groceries[index])
    q=index+1
    
    print (q,groceries[index])
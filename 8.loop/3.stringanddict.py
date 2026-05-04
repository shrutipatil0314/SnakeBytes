s1= "hello world"

for x in s1:
    print(x)
print("end of loop")


employee ={'empid': 1001,'name':"john","department":"hr"}

for i in employee:
    print(i) #^ print key only
print("end of loop")

for i in employee:
    print(employee[i]) #^ print value only
print("end of loop")


for i in employee:
    print(i,employee[i]) #^ print key and value
print("end of loop")

#*item funtion 

print(employee.items())

for i in employee.items():
    print(i)
print("end of loop")

for i,j in employee.items():
    print(i,j)
print("end of loop")

for i in employee.items():
    print(i[1])
print("end of loop")



for i in employee.items():
    print(i[0],i[1])
print("end of loop")

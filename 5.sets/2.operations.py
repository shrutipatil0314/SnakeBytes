#|| operations on set ||

#* membership operator - in or not in 
#^ in this operator checks and give us true if any element o
#^ is present in a list a tuple and sets

mem = {1,2,3,4,-5}
print(0 in mem) #& false 
print(1 not in mem) #& false

#*concatenations 
#con={1,2,3,4,5}
#con2={6,7,8,9,10}
#print(con + con2)
#!! will give typeerror


#*repeating

#print(mem * 2)
#!! will give typeerror

#*typecasing 
weekday= {"monday","tuesday","wednesday","thursday","friday","saturday","sunday"}
weekday=set(weekday)
print(weekday)
print(type(weekday))


#* sets are mutable 
 
set1={1,2,3,4,5}
print(set1)
#*add
set1.add(6)
print(set1)
#*remove
set1.remove(5)
print(set1)
#*discard
set1.discard(4)
print(set1)
#*pop
set1.pop()
print(set1)
#*clear
set1.clear()
print(set1)


#|| working with keys & dictionaries  ||

# d1 = {[1,2,3]:9,[4,5,6]:4}
# print(d1)
#!! will give typeerror 

#* key
#^ key dont allowed list ,set , dict bc they are mutable datatype
#^ key only allowed str , int , float , bool bc they are immutable datatype 
#^ keys of a dictionay can only be mutable datatype 


#^ values can be any datatype

employee = {'id':1010, 'name':'j' , 'salary':[50000, 30000, 20000, 2.22]}
print(employee)
print(employee['salary'])
print(employee['salary'][1])

#^ we can store that into a key-vale pair as a dictionaries 
#^we cannt fetch the value 
employee2 = {'id':1010, 'name':'j' , 'salary':{'basic':50000, 'hra':30000, 'bonus':2.22} }
print(employee2)
print(employee2['salary'])
print(employee2['salary']['hra'])

#* fetch the keys 

#* keys()
print(employee2.keys())

#*value 
print(employee2.values())

#*items
print(employee2.items())
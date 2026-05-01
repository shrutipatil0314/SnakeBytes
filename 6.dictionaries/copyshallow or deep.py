#|| copy shallow or deep ||
#^copy module is an internal module to python 
#^ copy function of the copy module is use to create shallow copy 
#^ we have to import the module using the import syntax "import copy "


import copy

elm = [1,2.5,[10,20,44],'python']

#*shallow copy 
elm2 = copy.copy(elm)
print(elm2)

#^ elm2 will be created in a different memory location or the same value will be stored
#^ in a different memory location with same structure list 
#^ both elm and elm2 have differentt memory addresses 

#* id funtion 
print(id(elm))
print(id(elm2))

#^ change first value of elm 
#^ the memory addresse of elm and elm2 are diff
elm[0]= 100

print(f"eml->{elm}", id(elm)) #&[100,2.5,[10,20,44],'python']
print(f"elm2->{elm2}", id(elm2)) #&[1,2.5,[10,20,44],'python']

#^but if we change internally it will get change 
#^ when we have elm and memory adress we have created , then we create a copy 
#^ elm2 shallow copy gets created in new memory location 
#^inner value have thery own memory addresses these adresses are not copied 
#^or they are not diff same 

elm [2][0]=50

print(f"eml->{elm}", id(elm)) #&[100,2.5,[50,20,44],'python']
print(f"elm2->{elm2}", id(elm2)) #&[1,2.5,[50,20,44],'python'] 

#*deep copy
#^ in deep copy inner element also gets copyed at different time 
ls1 = [1,2.5,[10,20,44],'python']

ls2 = copy.deepcopy(ls1)
print(ls2)

ls1[0]= 100
ls1 [2][0]=50

print(f"lsl->{ls1}", id(ls1)) #&[100,2.5,[50,20,44],'python']
print(f"ls2->{ls2}", id(ls2)) #&[1,2.5,[10,20,44],'python'] 



#|| dictionaries ||

#^ comma separated key-value pairs enclosed within {}
#& {sub1:value , key2:value,........}

subject = {'dbms':60, 'dsa':30 , 'sql':90}
print(subject)
print(type(subject))
print(len(subject   ))

print(subject['dbms'])
print(subject['dsa'])
print(subject['sql'])

#*dist aremutable
#^ add new key-value pair to the dictionary 
subject['dbms']=65 
print(subject)

#    * add
#^ update the value of the key 
subject['c++'] = 40
print(subject)


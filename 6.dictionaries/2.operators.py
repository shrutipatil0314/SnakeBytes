#|| operators on dictionaries

content1 = {'youtube':10 , 'facebook':20 ,'instagarm': 40 }
print(content1)

#*fech the  content platform 

print(content1['youtube'])
print(content1['facebook'])
print(content1['instagarm'])

"""
* get
^ get fech the key , so the key is not present get will give 
^ you the output as none
"""

print(content1.get('youtube'))
print(content1.get('whatsapp'))
print(content1.get('netfilx',30.5))


emp1 = {'id': 1001, 'name' : 'shruti', 'salary ': 50000}
print(emp1.get ('phone', 912345577222 ))

"""
*membership operator => in
print (1001 in emp1)
& output : false
^ membership operator does not look at value but it looks for the key 

print ('id' in emp1)
& output true

"""
#*update function 
sem1= {'dsa':78.5, 'dbms' :72.7, 'c++':86.9}
sem2={'cn':44.3 , 'entc':90.44}
sem3={'c++':90.2}
sem1.update(sem2)
print(sem1)

sem1.update(sem3)
print(sem1) 
#^update dsa marks

#*pop 
sem1.pop('dsa')
print(sem1)

#^keys cannot be duplicated on a dict 
name = {'shruti':40, 'swaroop':0.3, 'kiki': 232,'shruti': 324}
print(name)

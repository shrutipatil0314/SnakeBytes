import json

students = {'student1': { 'roll': 1, 'name': 'John', 'age': 20, 'major': 'Computer Science', 'sports': True},
            'student2': {'roll': 2, 'name': 'Alice', 'age': 22, 'major': 'Mathematics', 'sports': True},
            'student3': {'roll': 3, 'name': 'Bob', 'age': 21, 'major': 'Physics', 'sports': False}}

print(students)
print(type(students))

#load

with open("students.json", "r") as fh:
    loaded_students = json.load(fh)
    
print(loaded_students)
print(type(loaded_students))
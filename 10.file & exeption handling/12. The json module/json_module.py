import json

students = {'student1': { 'roll': 1, 'name': 'John', 'age': 20, 'major': 'Computer Science', 'sports': True},
            'student2': {'roll': 2, 'name': 'Alice', 'age': 22, 'major': 'Mathematics', 'sports': True},
            'student3': {'roll': 3, 'name': 'Bob', 'age': 21, 'major': 'Physics', 'sports': False}}

print(students)
print(type(students))

#dump 

with open("students.json", "w") as fh:
    json.dump(students, fh, indent=4)

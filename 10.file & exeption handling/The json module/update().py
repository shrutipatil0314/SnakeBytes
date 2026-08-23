import json

students = {'student1': { 'roll': 1, 'name': 'John', 'age': 29, 'major': 'Computer Science', 'sports': True},
            'student2': {'roll': 2, 'name': 'Alice', 'age': 27, 'major': 'Mathematics', 'sports': False},
            'student3': {'roll': 3, 'name': 'Bob', 'age': 21, 'major': 'Physics', 'sports': True}}
print(students)
print(type(students))


try:
     #read the old data from the json file
    with open("students.json", "r") as fh:
        data = json.load(fh)
except FileNotFoundError:
    with open("students.json", "w") as fh:
        json.dump(students, fh, indent=4)
else:
    #update operation
    data.update(students)
    #dump - write the updated data back to the json file
    with open("students.json", "w") as fh:
     json.dump(data, fh, indent=4)
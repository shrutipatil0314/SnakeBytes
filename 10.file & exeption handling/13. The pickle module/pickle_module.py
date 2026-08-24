import pickle

students = {'student1': { 'roll': 1, 'name': 'John', 'age': 29, 'major': 'Computer Science', 'sports': True},
            'student2': {'roll': 2, 'name': 'Alice', 'age': 27, 'major': 'Mathematics', 'sports': False},
            'student3': {'roll': 3, 'name': 'Bob', 'age': 21, 'major': 'Physics', 'sports': True}}
print(students)
print(type(students))

#* Serializing the dictionary using pickle
with open('students.pkl', 'bx') as fh:
    for student in students:
        pickle.dump(students[student], fh)
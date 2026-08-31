import pickle 

students ={'student1': { 'roll': 1, 'name': 'John', 'percentage': 85.5 },
           'student2': { 'roll': 2, 'name': 'Alice', 'percentage': 90.0 },
           'student3': { 'roll': 3, 'name': 'Bob', 'percentage': 78.0}} 

print(students)
print(type(students))

#serializing the dictionary using pickle
with open('students.bin', 'bw') as fh:
    for student in students:
        pickle.dump(students[student], fh)

student_list_90 = []
with open('students.bin', 'rb') as fh:
    while True:
        try:
            data = pickle.load(fh)
            if data['percentage'] > 90:
                student_list_90.append(data['name'])
        except EOFError:
            print("done!")
            break

print(f"Students with percentage greater than 90: {student_list_90}")
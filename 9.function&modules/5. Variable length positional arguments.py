# 5. Variable length positional arguments

#*args 
#^ is used to pass a variable number of positional arguments to a function. 
#^#It allows you to handle more arguments than you specified when defining the function.

def student_details(name, sid, *marks):
    if len(marks) == 0:
        print(f"Name: {name} with id {sid} was absent in all the exams !")
    else:
        percent = sum(marks) / len(marks)
    
        print(f"Name: {name} with id {sid} has scored {percent}% in the exams !")

student_details("John", 101, 80, 95, 90, 78)
student_details(name="Alice", sid=456)
student_details("Bob", 789, 92, 88, 95, 80)
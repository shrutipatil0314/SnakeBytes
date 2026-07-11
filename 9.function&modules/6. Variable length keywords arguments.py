# **kwargs
## **kwargs allows you to pass a variable number of keyword arguments to a function.
##* It allows you to handle named arguments that you have not defined in advance.

def student_details(name, sid, **marks):
    if len(marks) == 0:
        print(f"Name: {name} with id {sid} was absent in all the exams !")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"Name: {name} with id {sid} has scored {percent}% in the exams !")

student_details("John", 101, math=80, science=95, english=90, history=78)
student_details(name="Alice", sid=456)
student_details("Bob", 789, math=92, science=88, english=95, history=80)
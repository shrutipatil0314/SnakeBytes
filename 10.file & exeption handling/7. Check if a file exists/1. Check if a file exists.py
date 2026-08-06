import os 

file_name ="1.for loop.py"

if os.path.exists(file_name):
    print(f"The file '{file_name}' exists.")
else:
    print(f"The file '{file_name}' does not exist.")
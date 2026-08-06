
from pathlib import Path
import os

file_name ="new.txt"

if os.path.exists(file_name):
    print(f"The file '{file_name}' exists.")
else:
    print(f"The file '{file_name}' does not exist.")
    fh = open(file_name, "xt")
    fh.write("This file has been created using 'x' mode. \n")
    fh.write("If the file does not exist, it will be created. \n")
    fh.close()
    print(f"The file '{file_name}' has been created.")
# Task 1: Read a File and Handle Errors
# Assignment 4 - Module 5: Files, Exceptions, and Errors in Python

try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        for line_number, line in enumerate(file, start=1):
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

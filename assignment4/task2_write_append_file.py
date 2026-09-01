# Task 2: Write and Append Data to a File
# Assignment 4 - Module 5: Files, Exceptions, and Errors in Python

# Step 1: Take user input and WRITE to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.")

# Step 2: Take additional input and APPEND to file
extra_text = input("\nEnter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(extra_text + "\n")

print("Data successfully appended.")

# Step 3: Read and display the final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

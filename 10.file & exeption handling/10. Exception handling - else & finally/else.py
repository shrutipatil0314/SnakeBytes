try :
    with open ("file.txt", "r") as file:
        data = file.read()

except FileNotFoundError as file_error:
    print("The file was not found. Please check the file path and try again.")
    print(file_error)
    
else:
    print(data)
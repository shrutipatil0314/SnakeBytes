import io


try :
    fh = open ("file.txt", "wt")
    fh.write("heloo world")
    fh.close()
except FileNotFoundError as file_error:
    print("The file was not found. Please check the file path and try again.")
    print(file_error)
except io.UnsupportedOperation as io_error:
    print("The operation is not supported for the file.")
    print(io_error)
else:
    print("else block")
finally:
    print("finally block")
    fh.close()
# 'a' mode => Append mode
# if the file does not exist , 'a' mode creates a new file and opens it in append mode.
# If the file already exists, it opens the file in append mode and the new data will be written
# at the end of the file without overwriting the existing content.

fh = open("file1.txt", "at")  # Open the file in append mode
fh.write ("this file has been created using 'a' mode. \n")
fh.write("If the file does not exist, it will be created. \n")
fh.write("If the file already exists, it opens the file in append mode and the new data will be written at the end of the file without overwriting the existing content. \n")
fh.close()  # Close the file    
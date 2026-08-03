# 'a' mode  => Append mode 

fh = open("test.txt", "at")  # Open the file in append mode
fh.write("\n Hello, World!")  # Write data to the file
fh.write("this content has been written using  'a' mode. \n")
fh.write("'a' mode is used to add new content at the end od the file without overwriting the existing content. \n")
fh.write("If the file does not exist, it will be created. \n")
fh.close()  # Close the file
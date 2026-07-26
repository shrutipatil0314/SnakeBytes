# x mode => create a file 

fh = open("file1.txt", "xt")

#Writing into a file 
# write (content)

fh.write("this file is created using this 'x' mode in python. \n")
fh.write("next line.")

#close the file
fh.close()

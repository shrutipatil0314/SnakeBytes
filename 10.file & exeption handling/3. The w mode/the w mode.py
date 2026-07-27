# w mode - open the file for writing . overwrites the file 
# creates a new file if file does not exist 

fh = open ("file.txt", 'wt')
fh.write("this file is overwritten using 'w' mode\n")
fh.write("have a nice day!")
fh.close()
# %%    
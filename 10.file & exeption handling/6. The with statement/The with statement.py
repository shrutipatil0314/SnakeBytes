with open ("file1.txt", "xt") as fh:
    fh.write ("this file has been created using 'x' mode. \n")
    fh.write("If the file does not exist, it will be created. \n")

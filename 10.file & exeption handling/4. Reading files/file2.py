file_handler = open("practice.txt",'rt')

content = file_handler.readline()  

file_handler.close()


print(content)
print(type(content))
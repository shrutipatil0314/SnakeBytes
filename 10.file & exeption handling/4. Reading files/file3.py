file_handler = open("practice.txt",'rt')

line1 = file_handler.readline()
line2 = file_handler.readline()
line3 = file_handler.readline()

file_handler.close()


print(line1)
print(line2)
print(line3)
print(type(line1))
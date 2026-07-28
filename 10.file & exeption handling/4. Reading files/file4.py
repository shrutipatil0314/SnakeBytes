file_handler = open("practice.txt",'rt')

lines = file_handler.readlines()   

file_handler.close()


print(f"lines : {lines}")
print(type(lines))

for line in lines:
    print(line.strip())
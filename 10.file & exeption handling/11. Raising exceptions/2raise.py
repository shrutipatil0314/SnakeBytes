age = float(input("Enter your age: "))

if age < 0:
    raise Exception("Age cannot be negative.")
else:
    if age >=18:
        print("You are voter.")
    else:
        print("You are not voter.")
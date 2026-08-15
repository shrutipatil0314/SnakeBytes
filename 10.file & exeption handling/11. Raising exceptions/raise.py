# raise

salary = float(input("Enter your salary: "))

if salary < 0:
    raise ValueError("Salary cannot be negative.")
else:
    print("Salary is valid.")

    
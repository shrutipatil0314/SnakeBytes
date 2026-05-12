#|| nested loops

#^ A nested loop is a loop that is contained within another loop.
#  The inner loop will be executed for each iteration of the outer loop.    

# Example 1: Nested for loops
for i in range(3):
    for j in range(2):
        print(f"Outer loop iteration: {i}, Inner loop iteration: {j}")
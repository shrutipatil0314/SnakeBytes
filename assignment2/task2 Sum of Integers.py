# || Task 2: Sum of Integers from 1 to 50 Using a Loop ||
sum_number =(input("Enter a number:"))
n= int(sum_number)

total_sum=0

for current_num in range(1,n+1):
    total_sum+=current_num


print(f"\n sum of all number for 1 to {n} is {total_sum}")


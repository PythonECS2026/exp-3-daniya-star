# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:khan daniya rehman
# Date:03/03/2026

# Write your code here
salary = float(input("Enter Basic Salary: "))

da = (salary * 70) / 100  # DA = 70% of BS
ta = (salary * 30) / 100  # TA = 30% of BS
hra = (salary * 10) / 100 # HRA = 10% of BS

print("Salary Details:")
print("Basic Salary:   ", salary)
print("DA (70%):       ", da)
print("TA (30%):       ", ta)
print("Gross Salary:   ", gross)
print("HRA (10%):      ", hra)

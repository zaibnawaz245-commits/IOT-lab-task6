# Question 3 - 3 employees
employees = []
for i in range(3):
    print(f"\nEnter info for Employee {i+1}:")
    name = input("Name: ")
    age = input("Age: ")
    salary = input("Salary: ")
    employees.append((name, age, salary))

print("\nAll Employees List:", employees)
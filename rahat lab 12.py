employee_list = []

for i in range(1, 4):
    print(f"\nEnter details for Employee {i}:")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    emp_tuple = (name, age, salary)
    employee_list.append(emp_tuple)

print("\n--- All Employees List ---")
print(employee_list)
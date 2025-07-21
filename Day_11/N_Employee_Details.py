n = int(input("Enter number of employees: "))
employees = []

for i in range(0,n,1):
    print("\nEnter details for Employee ",i+1,": ")
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    employee = {
        "ID": emp_id,
        "Name": name,
        "Department": department,
        "Salary": salary
    }
    employees.append(employee)

print("\nEmployee Details")
i = 1
for emp in employees:
    print("\nEmployee", i, ":")
    print("ID        :", emp["ID"])
    print("Name      :", emp["Name"])
    print("Department:", emp["Department"])
    print("Salary    :", emp["Salary"])
    i = i + 1

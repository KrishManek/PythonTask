class employee:
    employees = []
    #employees={'name':'ename','employeeid':eid,'salary':salary,'role':'developer/manager','extra_info':'Dept/lang'}
    def display_all_employees():
        print(employee.employees)

    def filter_by_role(role):
        f = 0
        for i in employee.employees:
            if i['role'] == role:
                f = 1
                print(f"{i['name']}, {i['id']}, {i['salary']}, {i['role']}, {i['extra_info']}")
        if f == 0:
            print(f"No Employees found  for role of {role}")

    def filter_by_salary(min_salary,max_salary):
        f = 0
        for i in employee.employees:
            if i['salary'] >= min_salary and i['salary'] <= max_salary:
                f = 1
                print(f"{i['name']}, {i['id']}, {i['salary']}, {i['role']}, {i['extra_info']}")
        if f == 0:
            print(f"No Employees found for salary range between {min_salary} and {max_salary}")

    def create_emp():
        try:
            emp = {}
            employee_name = input("Enter Employee Name: ").capitalize()
            if not employee_name.isalpha():
                employee_name = input("Enter Employee Name in alphabets only: ").capitalize()
            employee_id =int(input("Enter Employee Id: "))
            if not employee_id.is_integer():
                  employee_id =int(input("Enter Employee Id in numeric: "))
            salary = int(input("Enter Employee Salary: "))
            if not salary.is_integer():
                  salary =int(input("Enter Employee Salary in numeric: "))
            employee_role = input("Enter Employee Role: ").capitalize()
            extra_info =input("Enter Department for Manager OR Pogramming Language for Deveploper: ").capitalize()
            if not extra_info.isalpha():
                extra_info =input("Enter Department for Manager OR Pogramming Language for Deveploper in alphabets only: ").capitalize()
            if employee_role == "Developer" or employee_role == "Manager":
                emp["name"] = employee_name
                emp["id"] = employee_id
                emp["salary"] = salary
                emp["role"] = employee_role
                emp["extra_info"] = extra_info
                print("Data added successfully")
                return emp
            else:
                print(f"Data not added! You have entered wrong role {employee_role}. Please add from developer or manager only")
                choice =int(input("Select 1 for manager & 2 for developer: "))
                if choice == 1:
                    employee_role = "Manager"
                    emp["name"] = employee_name
                    emp["id"] = employee_id
                    emp["salary"] = salary
                    emp["role"] = employee_role
                    emp["extra_info"] = extra_info
                    print("Data added successfully")
                    return emp
                else:
                    employee_role = "Developer"
                    emp["name"] = employee_name
                    emp["id"] = employee_id
                    emp["salary"] = salary
                    emp["role"] = employee_role
                    emp["extra_info"] = extra_info
                    print("Data added successfully")
                    return emp
        except Exception as e:
            print(e)
emp = employee

noofemp = int(input("Enter no of employees you want to create: "))
for i in range(noofemp):
    data = emp.create_emp()
    emp.employees.append(data)

emp.display_all_employees()
role = input("Enter role you want to search all employees for: ")
emp.filter_by_role(role.capitalize())

minsal = int(input("Enter Min salary range: "))
maxsal = int(input("Enter Max salary range: "))
emp.filter_by_salary(minsal,maxsal)
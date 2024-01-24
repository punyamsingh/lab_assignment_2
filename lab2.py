import pandas as pd

class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_employees(self, parameter):
        if parameter == 'Age':
            self.employees.sort(key=lambda x: x.age)
        elif parameter == 'Name':
            self.employees.sort(key=lambda x: x.name)
        elif parameter == 'Salary':
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter")

    def print_employees(self):
        for employee in self.employees:
            print(employee)

data = {
    'Employee ID': ['161E90', '171E22', '171G55', '152K46'],
    'Name': ['Ramu', 'Tejas', 'Abhi', 'Jaya'],
    'Age': [35, 30, 25, 32],
    'Salary (PM)': [59000, 82100, 100000, 85000]
}

db = EmployeeDatabase()

for i in range(len(data['Employee ID'])):
    employee = Employee(data['Employee ID'][i], data['Name'][i], data['Age'][i], data['Salary (PM)'][i])
    db.add_employee(employee)

sorting_parameter = input("Enter the sorting parameter (1. Age, 2. Name, 3. Salary) Press 1,2or3: ")

if sorting_parameter == '1':
    db.sort_employees('Age')
elif sorting_parameter == '2':
    db.sort_employees('Name')
elif sorting_parameter == '3':
    db.sort_employees('Salary')
else:
    print("Invalid sorting parameter")

db.print_employees()

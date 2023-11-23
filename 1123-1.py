class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            self.emp_salary += overtime_amount

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)
        print()

# Sample Employee Data
employees_data = [
    ("ADAMS", "E7876", 50000, "ACCOUNTING"),
    ("JONES", "E7499", 45000, "RESEARCH"),
    ("MARTIN", "E7900", 50000, "SALES"),
    ("SMITH", "E7698", 55000, "OPERATIONS")
]

# Create Employee Objects
employees = [Employee(*data) for data in employees_data]

# Example Usage
for employee in employees:
    employee.calculate_emp_salary(55)  # Example of calculating salary with overtime
    employee.assign_department("IT")  # Example of assigning a new department
    employee.print_employee_details()  # Example of printing employee details

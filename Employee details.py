
class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Dept: {self.department}, Salary: {self.salary}")

    def update_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)
employees = [
    Employee("Alice", 101, "HR", 50000),
    Employee("Bob", 102, "IT", 60000),
    Employee("Charlie", 103, "HR", 52000),
    Employee("David", 104, "Finance", 55000),
    Employee("Eva", 105, "IT", 58000)
]

dept = input("Enter department to update salary: ")
percent = float(input("Enter salary increment percentage: "))

print("\n--- Updated Employee Details ---")
for emp in employees:
    if emp.department.lower() == dept.lower():
        emp.update_salary(percent)
    \emp.display//

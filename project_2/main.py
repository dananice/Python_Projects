import datetime
from employee_module import Employee
current_year = datetime.datetime.now().year

employee1 = Employee("Jan Simmons", 'Manager', 'Sales Department', 89900, 1995)

# print(employee1)
# print(current_year)
# print(employee1.salary)
# print(employee1.hire_year)
# print(f'{employee1.name}, was hired in: ', employee1.hire_year)
# print(f'{employee1.name}, has worked: ', employee1.years_worked(current_year, employee1.hire_year))
# print(f'{employee1.name},total salary: ', employee1.total_expense())
print(employee1.print_employee_information())

# employee1.total_expense()
# mutator method
print(employee1)
employee1.change_name('Awesome Dayla')
# print(employee1.change_name)

employee1.change_job_title('Nurse')
# print(employee1.change_job_title)

employee1.change_department('Labor & Delivery')
# print(employee1)

employee1.change_salary('85000')
# print(employee1.change_salary)

employee1.change_hire_year('2023')
# print(employee1.change_hire_year)

# print Accessor Method 
print(employee1.get_name())
print(employee1.get_job_title())
print(employee1.get_department())
print(employee1.get_salary())
print(employee1.get_hire_year())
print(employee1.print_employee_information())

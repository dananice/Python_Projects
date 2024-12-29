import datetime
from datetime import datetime
import csv
import pandas as pd
import os # Set our cwd as (current working directory) same folder of our python file


os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Employee():
    
    # Initializer/Constructor. This is always the first method, it builds your object
    # creating employee file
    
    def __init__(self, name, job_title, department, salary, hire_year):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year
        
             
     # This method will run when you use the print built in function
    def __str__(self):
        return f'Employee name: {self.name}\nJob Title: {self.job_title}\nDepartment:  {self.department}\nSalary:  ${self.salary:.2f}\nYear hired: {self.hire_year}'
    
        
    # how many years has the employee worked with the company
    def years_worked(self):
        current_year = datetime.now().year
        return(current_year - self.hire_year)
        
    # what the total_expense of the employee
    def total_expense(self):
       print(int(self.years_worked() * (self.salary)))
       
    # prints the employee info to a csv file   
    def print_employee_information(self):
            
        # Redlines reads entire file to a list
        with open(f'{self.name}.csv', 'w') as employee_file:
            data = (f'{self.name}, {self.job_title}, {self.department}, {self.salary}, {self.hire_year}')
                               
            employee_file.write(data)
             
      
        
    #   # Mutator methods
    # # Functions within classes, become methods of the class
    def change_name(self, new_name):
        self.name = new_name
        
    def change_job_title(self, new_job_title):
        self.job_title = new_job_title     
        
    
    def change_department(self, new_department):
        self.department = new_department
        
    def change_salary(self, new_salary):
        self.salary = new_salary
         
                
    def change_hire_year(self, new_hire_year):
        self.hire_year = new_hire_year               
        
    
    # Accessor methods get the value of our attributes
    def get_name(self):
        return(self.name)
        
    def get_job_title(self):
        return(self.job_title)    
        
    def get_department(self):
        return(self.department)
        
    def get_salary(self):
        return(self.salary) 
                
    def get_hire_year(self):
        return(self.hire_year)    


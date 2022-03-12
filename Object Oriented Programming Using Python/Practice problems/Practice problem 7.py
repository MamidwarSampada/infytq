"""
Problem Statement
An IT company wants to automate the process of allocating projects to its employees.
Write a python program to implement the class diagram given below.

Class description

Employee:
Initialize static variable, employee_count to 1000
generate_employee_id(): Auto-generate attribute, employee_id starting from 'E1001' ('E1001','E1002','E1003'…etc)

Project:
update_number_of_employees(): Increment attribute, number_of_employees by 1

Department:
dep_project_list: Static list of Project objects which are in this department. Initialize it to an empty list.
employee_dict: Static dictionary which contains the employee id as key and corresponding project_id as value. Initialize it to an empty dictionary.
add_project(project_list): Accept a list of projects to be added to the department.
Append the projects in the project list to static list, dep_project_list, if the total number of projects is not more than 5 (existing projects + new projects waiting to be added)
Otherwise, return -1
add_employee(employee,project_id): Accept the object of the Employee who should be added to the given project_id.
If the given project is not available in the department, display appropriate message and return -1
A project can have maximum 10 employees. If the number of employees in the given project is already 10, then display an error message and return -2
Otherwise,
Generate employee id by invoking Employee.generate_employee_id() method
Add the employee to the given project by adding the employee_id as key and project_id as value in employee_dict
Increment the number of employees in the given project by invoking Project.update_number_of_employees() method
Perform case sensitive string comparison.
Create objects of Project class. Create a list of projects and add it to department by invoking add_project() method. Also add employees to the projects in the department by invoking add_employee() method and test your program.
"""
#lex_auth_012752551756767232304
#Start writing you code here
class Employee:
    __employee_count=1000
    def __init__(self):
        self.__employee_id=None
    
    def get_employee_id(self):
        return self.__employee_id
        
    def generate_employee_id(self):
        Employee.__employee_count+=1
        self.__employee_id="E"+str(Employee.__employee_count)
        

class Project:
    def __init__(self,project_id,number_of_employees):
        self.__project_id=project_id
        self.__number_of_employees=number_of_employees
        
    def get_project__id(self):
        return self.__project_id
        
    def update_number_of_employees(self):
        self.__number_of_employees+=1
        
    def get_number_of_employees(self):
        return self.__number_of_employees 


class Department:
    __dep_project_list=[]
    __employee_dict={}
    @staticmethod
    def add_project(project_list):
        if (len(Department.__dep_project_list)+len(project_list))<=5:
            for p in project_list:
                Department.__dep_project_list.append(p)
        else:
            return -1
    
    @staticmethod
    def add_employee(employee,project_id):
        ind=-1
        for i in range(len(Department.__dep_project_list)):
            if Department.__dep_project_list[i].get_project__id()==project_id:
                ind=i
                break
        
        if ind==-1:
            print("project is not available")
            return -1
            
        if Department.__dep_project_list[ind].get_number_of_employees()<10:
            employee.generate_employee_id()
            Department.__employee_dict[employee.get_employee_id()]=project_id
            Department.__dep_project_list[ind].update_number_of_employees()
        elif Department.__dep_project_list[ind].get_number_of_employees()==10:
            print("number of employees can not be added")
            return -2
            
            

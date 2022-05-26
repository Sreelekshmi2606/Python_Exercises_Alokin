from statistics import harmonic_mean


class Employee:
    def __init__(self, emp_no,emp_name,emp_desig,emp_addr,emp_phno):
        self.emp_no=emp_no
        self.emp_name=emp_name 
        self.emp_desig=emp_desig
        self.emp_addr=emp_addr
        self.emp_phno=emp_no
  
    # To get name
    def getData(self, emp_no,emp_name,emp_desig,emp_addr,emp_phno):
        print("\n")
        print("\tEmployee Details")
        print("******************************")
        print("Employee Number       :",emp_no)
        print("Employee Name         :",emp_name)
        print("Eployee Designation   :",emp_desig)
        print("Eployee Address       :",emp_addr)
        print("Employeee Phone Number:",emp_phno)
        
class Salary(Employee):
    def __init__(self,emp_basic):
        self.emp_basic=emp_basic

        hra,da,net=0,0,0
        gross,pf=0,0
        

    def getData1(self,emp_basic):
        super()
        hra=emp_basic * .15     
        da=emp_basic * 0.08     
        net=emp_basic + hra + da 
        pf=emp_basic*.11
        gross=emp_basic+hra+da-pf

        print("Net Pay  of employee is   :",net)
        print("Gross    pay of           :",gross)

employee_no=int(input("Enter Employee Number          : "))
employee_name=input("Enter Employee   Name            : ")

employee_designation=input("Enter Employee Designation: ")
employee_address=input("Enter Employee   Address          : ")
employee_phno=int(input("Enter Phone Number          : "))

#stud = student(stud_no,stud_name)  # An Object of Person
#print("Stuednt number: ",stud.getData(stud_no))

#emp=Employee(employee_no,employee_name,employee_designation,employee_address,employee_phno)
#emp.getData(employee_no,employee_name,employee_designation,employee_address,employee_phno)

employee_basic=int(input("Enter basic   pay     : "))
salary=Salary(employee_basic)
salary.getData(employee_no,employee_name,employee_designation,employee_address,employee_phno)
salary.getData1(employee_basic)
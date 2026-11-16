class EmployeeSalary:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender 
        

    def salary_taxes(self, init_salary1,children,hrs):
        self.init_salary1 = init_salary1
        self.children = children
        self.hrs = hrs
        if self.hrs <=40 :
            self.init_salary2 = self.init_salary1 * self.hrs
        if self.hrs > 40:
            self.init_salary2 = (self.init_salary1 * (1.5*(self.hrs-40)) + (self.init_salary1 * 40))
        
        self.taxes = 0.185 * float(self.init_salary2)
        if self.children == 0:
            self.final_pay = self.init_salary2 - self.taxes
        if self.children <= 3:
            self.final_pay = (self.init_salary2 - (self.children*10)) - (self.taxes) 
        if self.children > 3:
            self.ch_calc = ((self.children-3)*20) + 30
            self.final_pay = (self.init_salary2 - (self.ch_calc)) - (self.taxes)
        return self.final_pay    
        

print("Employee Net-Pay Estimator is ONLINE. ")

em_name = input("Please enter the employee's name : ")
em_gender = input("Please enter the employee's gender(Male/Female) : ")
m_m = int(input("Enter 1 if the employee is married, otherwise enter 0 : "))
hours_worked = float(input("Enter the number of hours worked : "))

if em_gender == "M" or "Male" or "male":
    init_salary = 500
if em_gender == "F" or "Female" or "female":
    init_salary = 550

if m_m == 1 :
    ch_no = int(input("Enter the number of children the employee has : "))
    emp = EmployeeSalary(name=em_name, gender=em_gender)
    net_pay = emp.salary_taxes(init_salary1=init_salary, children=ch_no,hrs=hours_worked)
    print(f"{emp.name} has a net pay of {net_pay}")
if m_m == 0 :
    ch_no = 0
    emp = EmployeeSalary(name=em_name, gender=em_gender)
    net_pay = emp.salary_taxes(init_salary1=init_salary, children=ch_no,hrs=hours_worked)
    print(f"{emp.name} has a net pay of {net_pay}")
    


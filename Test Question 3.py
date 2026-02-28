class Employee:
    def __init__(self,emp_id,name,department,basic_salary,experience_years):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.basic_salary = basic_salary
        self.experience_years = experience_years

    def calculate_annual_salary(self):
        return (self.basic_salary*12)
    
    def apply_increment(self,increment_percent):
        self.basic_salary = self.basic_salary+(self.basic_salary*increment_percent/100)

    def add_experience(self,years):
        self.experience_years = self.experience_years + years

    def change_department(self,new_department):
        self.department = new_department

    def get_employee_summary(self):
        print(f'{self.emp_id} - {self.name} - {self.department} - {self.experience_years} - {self.basic_salary}')


Emp1 =Employee('1098279','Jitender Sahani','Finance',45000,7)
Emp1.add_experience(2)
Emp1.apply_increment(6)
Emp1.change_department('Supply Chain')
print(f'Current Annual Salary: {Emp1.calculate_annual_salary()}')
Emp1.get_employee_summary()
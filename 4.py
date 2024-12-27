class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        
employee1 = Employee('Lev',50000)
employee2 = Employee('Mikhail', 172346641)
employees = [employee1, employee2]
for employee in employees:
    print(f'Имя:{employee.name},Зарплата:{employee.salary}')
total_salary = sum(employee.salary for employee in employees)
print(f'Сумма зарплат:{total_salary}')
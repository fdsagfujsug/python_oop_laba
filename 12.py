class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def increase_salary(self):
        self.salary *= 1.10

employee = Employee('Ivan', 50000)

print('Имя работника:', employee.get_name())
print('Зарплата работника:', employee.get_salary())

employee.increase_salary()

print('Новая зарплата работника:', employee.get_salary())

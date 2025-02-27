class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.__add_sign(self.salary)

    def __add_sign(self, num):
        return str(num) + '$'

employee = Employee('Ivam', 10000)

print(employee.get_salary())
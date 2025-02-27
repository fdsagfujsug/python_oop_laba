class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_age(self, age):
        self.__age = age

employee = Employee('nIKITA', 10000, 17)


employee.set_name('John')
employee.set_salary(60000)
employee.set_age(32)


print("Имя:", employee.get_name())
print("Зарплата:", employee.get_salary())
print("Возраст:", employee.get_age())
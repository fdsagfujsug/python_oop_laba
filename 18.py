class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def get_name(self):
        return self.__name

    def get_salary(self):
        return f"{self.__salary}$"

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            raise Exception('Name is incorrect')

    def set_salary(self, salary):
        self.__salary = salary

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            raise Exception("Age must be between 0 and 120")


employee = Employee('Ivan', 10000, 15)

employee.set_name('John')
employee.set_salary(60000)
employee.set_age(35)


print("Имя:", employee.get_name())
print("Зарплата:", employee.get_salary())
print("Возраст:", employee.get_age())


try:
    employee.set_age(150)
except Exception as e:
    print(e)
class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_employee_data(self):
        return f"Имя: {self.__name}, Зарплата: {self.__salary}, Возраст: {self.__age}"

employee = Employee('Ivam', 150000, 18)


print(employee.get_employee_data())
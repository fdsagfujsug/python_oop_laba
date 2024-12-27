class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
employee = Employee("Иван", 129874932147)
print(f"Информация о работнике")
print(f"Имя:{employee.name},Зарпоата:{employee.salary}")
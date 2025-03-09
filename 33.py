class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name

    def getSurn(self):
        return self.surname


class Employee(User):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname)
        self.age = age
        self.salary = salary

    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary



employee = Employee("Алексей", "Петров", 30, 60000)

print(f"Имя: {employee.getName()}")
print(f"Фамилия: {employee.getSurn()}")
print(f"Возраст: {employee.getAge()}")
print(f"Зарплата: {employee.getSalary()}")

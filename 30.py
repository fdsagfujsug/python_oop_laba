class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getSurname(self):
        return self.surname

    def setSurname(self, surname):
        self.surname = surname


class Employee(User):
    def __init__(self, name, surname, salary=0):
        super().__init__(name, surname)
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.salary = salary


employee = Employee("Иван", "Иванов")
employee.setName("Петр")
employee.setSurname("Петров")
employee.setSalary(50000)

name = employee.getName()
surname = employee.getSurname()
salary = employee.getSalary()

print(f"Имя: {name}, Фамилия: {surname}, Зарплата: {salary}")

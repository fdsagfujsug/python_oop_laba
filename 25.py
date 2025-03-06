class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary


class EmployeesCollection:
    def __init__(self):
        self.__employees = []

    def add(self, employee: Employee):
        self.__employees.append(employee)

    def show(self):
        for employee in self.__employees:
            print(f"Имя: {employee.getName()}, Зарплата: {employee.getSalary()}")

    def totalSalary(self) -> float:
        return sum(employee.getSalary() for employee in self.__employees)

    def averageSalary(self) -> float:
        if len(self.__employees) == 0:
            return 0
        return self.totalSalary() / len(self.__employees)


if __name__ == "__main__":
    ec = EmployeesCollection()
    ec.add(Employee('John', 50000))
    ec.add(Employee('Eric', 60000))
    ec.add(Employee('Kyle', 55000))

    ec.show()
    print(f"Суммарная зарплата всех работников: {ec.totalSalary()}")
    print(f"Средняя зарплата всех работников: {ec.averageSalary()}")

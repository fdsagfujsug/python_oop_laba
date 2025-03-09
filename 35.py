class User:
    __name = None
    __surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurn(self, surname):
        self.__surname = surname

    def getSurn(self):
        return self.__surname


class Employee(User):
    def getFull(self):
        return self.__name + ' ' + self.__surname 



employee = Employee()


employee.setName('john')
employee.setSurn('doe')


name = employee.getName()
surname = employee.getSurn()

print(f"Имя: {name}, Фамилия: {surname}")


try:
    full_name = employee.getFull()
    print(f"Полное имя: {full_name}")
except AttributeError as e:
    print(e)  

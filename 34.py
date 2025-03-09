class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.__capitalizeFirst(self.name)

    def __capitalizeFirst(self, string):
        return string.capitalize()


class Employee(User):
    def setSurn(self, surname):
        self.surname = surname

    def getSurn(self):

        return self.__capitalizeFirst(self.surname)  



employee = Employee()
employee.setName("алексей")
employee.setSurn("петров")

print(f"Имя: {employee.getName()}")  
try:
    print(f"Фамилия: {employee.getSurn()}")  
    print(e)
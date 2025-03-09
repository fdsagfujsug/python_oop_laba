class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Employee(User):
    def __init__(self, name=None, age=None):
        super().__init__()
        self.age = age

    def getAge(self):
        return self.age

    def setAge(self, age):
        if 18 <= age <= 65:
            self.age = age
        else:
            raise Exception("Возраст должен быть от 18 до 65 лет.")



employee = Employee()


employee.setAge(30) 

age = employee.getAge()
print(f"Возраст: {age}")


try:
    employee.setAge(17) 
except Exception as e:
    print(e)  

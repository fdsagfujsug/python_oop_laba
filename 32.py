class User:
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('need age more 0')


class Employee(User):
    def setAge(self, age):
        if age <= 120:
            super().setAge(age) 
        else:
            raise Exception('need age less 120')




employee = Employee()


try:
    employee.setAge(30) 
    print(f"Возраст установлен: {employee.age}")
except Exception as e:
    print(e)


try:
    employee.setAge(130)  
except Exception as e:
    print(e)  

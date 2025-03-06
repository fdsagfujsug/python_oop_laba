class Position:
    def __init__(self, title):
        self.title = title

class Department:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name, position: Position, department: Department):
        self.name = name
        self.position = position
        self.department = department


position = Position("Менеджер проекта")
department = Department("Разработка")


user = User("Лев Белавин", position, department)

# Выводим информацию о работнике
print(f"Имя: {user.name}")
print(f"Должность: {user.position.title}")
print(f"Отдел: {user.department.name}")

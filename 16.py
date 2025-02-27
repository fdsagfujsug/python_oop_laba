class User:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname


user = User('Dima', 'Ekimovskiy')

print(user.get_name())
print(user.get_surname())
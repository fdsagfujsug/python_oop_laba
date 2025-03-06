class Validator:
    @staticmethod
    def isEmail(email: str) -> bool:

        if "@" in email and "." in email.split("@")[-1]:
            return True
        return False

    @staticmethod
    def isDomain(domain: str) -> bool:

        if '.' in domain and all(part.isalnum() or part == '-' for part in domain.split('.')):
            return True
        return False

    @staticmethod
    def isNumber(number: str) -> bool:

        return number.isdigit()


validator = Validator()


print(validator.isEmail("example@test.com"))  
print(validator.isEmail("invalid-email"))    

print(validator.isDomain("example.com"))       
print(validator.isDomain("example-.com"))      


print(validator.isNumber("12345"))             
print(validator.isNumber("123a45"))          

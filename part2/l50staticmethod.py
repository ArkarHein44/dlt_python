class CalUilities:
    @staticmethod # decorator
    def addresult(x,y): # no need self
        return x + y
    
    @staticmethod
    def iseven(num):
        return num % 2 == 0
    
print(CalUilities.addresult(10,5)) # 5
print(CalUilities.iseven(20)) # True

# example exercise
class EmailValidator:
    @staticmethod
    def isemail(email):
        return "@" in email and "." in email
    
    @staticmethod
    def ispositiveint(num):
        return isinstance(num,int) and num > 0

print(EmailValidator.isemail("dataland@gmail.com")) # True
print(EmailValidator.ispositiveint(-1)) # False

# Method Type       Decorator       First Parameter
# Instance Method   None            self
# Abstract Method   @abstractmethod self
# Static Method     @staticmethod   None
# Class Method      @classmethod    cls


# 6SM

# Modifier     Syntax       Access inside class Access inside subclass Access outside class
# Public        self.name   Yes                 Yes                    Yes
# Private       self.__name Yes                 No                      No
# Protected     self._name  Yes                 Yes                     Possible(should not use)

class Car:  # defining the class
    def __init__(self,brand:str,wheels:int) -> None:  # the constructor __init__() type hint
        self.brand = brand  # public attribute
        self._wheels = wheels  # protected attrubute
        self.__enginestatus = False  # private attribute

    def engineon(self)-> None:
        self.__enginestatus = True
        print(f'Engine on : {self.brand}')

    def engineoff(self)-> None:
        self.__enginestatus = False
        print(f'Engine off : {self.brand}')

    def drive(self,km:float)-> None:
        if self.__enginestatus:
            print(f'Driving : {self.brand} for {km} km/h')
        else:
            print(f'Cannot Drive : {self.brand} engine is off!')

    def describe(self)->None:
        print(f'{self.brand} is a car with {self.wheels} wheels')

    def __checkcomputerbox(self)-> None: # instance private methods
        print(f"checking computer box of {self.brand}")

    def _serviceengine(self)->None: # instance protected methods
        print(f"servicing the engine of {self.brand}")
    
    def maintainance(self)->None:   # instance public methods (as getter)
        print(f"Maintence on {self.brand}")
        self.__checkcomputerbox()
        self._serviceengine()
    
def main()-> None:
    toyota: Car = Car('Toyota', 4)
    toyota.engineon()    
    toyota.drive(50)
    toyota.engineoff()
    toyota.describe()

    # print(f"This is protected attribute = {toyota._wheels}") # not recommended

    # print(f"This is private attribute = {toyota.__enginestatus}") # error

    # print(f"This is private attribute = {toyota._Car__enginestatus}") # not recommended

    # toyota._serviceengine() # not recommended
    # toyota.__checkcomputerbox() # error
    # toyota._Car__checkcomputerbox() # not recomanded

    toyota.maintainance()
# main()

if __name__ == "__main__":
    main()

class Staff:
    def __init__(self,name:str,age:int, hascar:bool) -> None:
        print(f'My name is {name}, I\'m {age} years old.')
    
        self.name = name
        self.age = age
        self.hascar = hascar

    def getinfo(self) -> None:
        print(f'Name is {self.name}, Age is {self.age}, car status {self.hascar}')

def main()->None:
    staffObj1: Staff = Staff("Nu Nu", 27, True)
    staffObj2 : Staff = Staff("Tun Tun", 30, False)

    staffObj1.getinfo()
    staffObj2.getinfo()

    print(staffObj1.name)
    print(staffObj1.age)
    print(staffObj1.hascar)

    print(staffObj2.name)
    print(staffObj2.age)
    print(staffObj2.hascar)

if __name__ == '__main__':
    main()
    
# 2AM
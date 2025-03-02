# Parent Class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand # instance variable
    
    def power(self):
        return "Petrol"

# Subclass (inherit from Vehicle)
class EV(Vehicle):
    def power(self): # Overriding parent method
        return "Battery"
    
carObj = EV("Tesla")
print(carObj.brand) # Tesla
print(carObj.power()) # Battery

# => Using super()

class Employee:
    def task(self):
        return "Frontend Developement"
    
class Employeer(Employee):
    def task(self):
        return super().task() + " and specialized frameworks."

jobObj = Employeer()
print(jobObj.task()) # Frontend Developement and specialized frameworks.

# => exe2

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def detailinfo(self):
        return f"Person Name = {self.name}, Age = {self.age}"
    
class Student(Person):
    def __init__(self,name,age,subject):
        super().__init__(name, age)
        self.subject = subject
    
    def detailinfo(self):
        originalinfo = super().detailinfo()
        return f"{originalinfo}, Subject = {self.subject}"
    
studentObj = Student("Myat Noe", 20,"Computer Science")
print(studentObj.detailinfo()) # Person Name = Myat Noe, Age = 20, Subject = Computer Science

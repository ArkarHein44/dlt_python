# => Override Decorator

class Animal:
    datas: list[str] = []  # Properties, Attributes

    def __init__(self,name:str)->None:
        self.name = name
    
    def task(self,todo:str)->None:
        self.datas.append(todo)

def main()->None:
    cat: Animal = Animal('Cat')
    dog: Animal = Animal('Dog')

    cat.task("sleep")
    cat.task("eat")
    print(cat.datas)

    dog.task("run")
    dog.task("watch")
    print(dog.datas)

if __name__ == "__main__":
    main()

# => Override Decorator
# exe without Override Decorator 

class Parent1:
    def greet(self) -> None:
        print("Hello form Parent 1!")

class Child1(Parent1):
    def greet(self)-> None:
        print("Hello from Child 1!")

Child1().greet() # Hello from Child 1!

# exe with Override Decorator (@override, python3 --0version (v 3.12.6))

from typing import override # optional

class Parent2:
    def greet(self) -> None:
        print("Hello form Parent 2!")

class Child2(Parent2):
    @override
    def greet(self)-> None:
        print("Hello from Child 2!")

Child2().greet() # Hello from Child 2!

# exe 
from typing import override

class Shape:
    def __init__(self, name:str, sides:int)-> None:
        self.name = name
        self.sides = sides 

    def describe(self) -> None:
        print(f"{self.name} have {self.sides} sides")
    
    def info(self)-> None:
        print(f"this is {self.name} info method.")
    
class Square(Shape):
    def __init__(self,size:float)->None:
        super().__init__("Square",4)
        self.size = size
    
    @override
    def info(self) -> None:
        print(f"this is {self.name} info method with a shape of {self.size}")

class Rectangle(Shape):
    def __init__(self,width:float, height:float)->None:
        super().__init__("Rectangle",4)
        self.width = width
        self.height = height
    
    @override
    def info(self) -> None:
        print(f"this is {self.name} info method with a area of ({self.width} x {self.height}).")

def main()->None:
    square: Square = Square(10)
    square.describe()
    square.info()

    rectangle: Rectangle = Rectangle(10,20)
    rectangle.describe()
    rectangle.info()

if __name__ == "__main__":
    main()
# => Dunder Methods 
from typing import Self

class Article:
    def __init__(self, title:str, rating:int) -> None: # Dunder Methods
        self.title = title
        self.rating = rating

    def __len__(self) -> int: # Dunder Methods
        return self.rating

    def __add__(self, other: Self) -> Self: # Dunder Methods
        combinedtitle:str = f"{self.title} & {other.title}"
        combinedrating: int = self.rating + other.rating
        return Article(combinedtitle,combinedrating)

def main() -> None:  # function, outside of the class
    sport: Article = Article("This is sport article", 3)
    news: Article = Article("This is news article", 5)

    print(sport.title)
    print(len(sport))
    
    print(news.title)
    print(len(news))
    # print(news.__len__()) # not recommanded

    mixarticles: Article = sport + news 
    print(mixarticles.title)
    print(mixarticles.rating)


if __name__ == "__main__":
    main()

# => __eq__

from typing import Self

class Mobile:
    def __init__(self, brand: str, price:int, color:str) -> None:
        self.brand = brand
        self.price = price
        self.color = color
    
    # def __eq__(self, other:Self)-> bool: # check only1 parameter
    #     return self.price == other.price

    def __eq__(self, other:Self)-> bool: # check all parameter
        print("Current = ",self.__dict__)
        print("Other = ",other.__dict__)
        return self.__dict__ == other.__dict__


def main() -> None: 
    mob1: Mobile = Mobile("Oppo", 300, "blue")
    mob2: Mobile = Mobile("Oppo", 300, "blue")

    print(mob1)
    print(mob2)
    print(mob1 == mob2) # False before eq, True after eq


if __name__ == "__main__":
    main()

class Person:
    def __init__(self,name:str,age:int)->None:
        self.name = name
        self.age = age

# => indexing 
# => __getitem__

class Worker:
    def __init__(self,names):
        self.names = names
    
    def __getitme__(self,index):
        return self.names[index]
    
def main()->None:
    workerobj: Worker = Worker(["Aung Aung", "Tun Tun", "Kyaw Kyaw"])
    print(workerobj[0])
    print(workerobj[1])
    print(workerobj[2])

class People:
    def __init__(self,name):
        self.name = name

    def __del__(self):
        print(f"{self.name} has been deleted.")
    
def main()->None:
    peopleObj: People = People("Linn Linn")
    del peopleObj
    
if __name__ == "__main__":
    main()




# 9DD
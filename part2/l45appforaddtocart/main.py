from models.book import Book
from models.user import User
# from models.utilities import gettitles, specialdiscount
from models.utilities import *

def main():
    bookObj1 =  Book("Python", "Daw Win Win", 20, 500)
    bookObj2 = Book("Django", "U Tun Tun", 40, 800)
    bookObj3 = Book("Open AI", "Daw Hnin Hnin", 50, 1000)

    specialdiscount(bookObj1)
    specialdiscount(bookObj2)

    user = User("Yamin")
    user.addtocart(bookObj1)
    user.addtocart(bookObj2)

    print("Book Titles : ", gettitles(user.carts))
    print(f"Total pages in book 1 = {len(bookObj1)}")
    print(f"Total pages in book 2 = {len(bookObj2)}")

    print(user)

    print(f"Total price: {user.totalprice():.2f}")

if __name__ == "__main__":
    main()

# 4BK
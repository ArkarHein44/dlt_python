def pricestatusdeco(func):
    def wrapper(book):
        print(f"Original Prie = {book.getprice():.2f}") # format specification, : start the format specification, .3 3 decimal places, f fixed point
        func(book)
        print(f"After Discount Prie = {book.getprice():.2f}")
    return wrapper

@pricestatusdeco

def specialdiscount(book):
    book.applydiscount(10)
    # book.applydiscount(0.1)

def gettitles(books):
    return list(map(lambda book: book.title, books))
# string slicing and indexing
# strings are character list in python
# so, we can iterate with index
smallLetters = "abcdefghijklmnopqrstuvwxyz"
print(smallLetters[0])  # a

# negative index start from last
print(smallLetters[-1])  # z

# str[start:stop:step]
# start = startion point
# stop = target point
# setp = next every step after start

print(smallLetters[0:10])  # abcdefghij
print(smallLetters[0:10:3])  # adgj

# [::-1] make reverse order
print(smallLetters[::-1])  # zyxwvutsrqponmlkjihgfedcba

# check length of string < len(str) >
print(len(smallLetters))  # 26

# upper() - make capital for all string
print(smallLetters.upper())  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# capitalize() - make first letter capital
print(smallLetters.capitalize())  # Abcdefghijklmnopqrstuvwxyz

# title() - make all starting word make capital
print('the shwedagon bagoda'.title())  # The Shwedagon Bagoda

# lower() and casefold()  - make all characters small
capletters = smallLetters.upper()
print(capletters.lower())  # abcdefghijklmnopqrstuvwxyz
print(capletters.casefold())  # abcdefghijklmnopqrstuvwxyz

# swapcasse() - swap lower and upper respectively
print(smallLetters.swapcase())  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(capletters.swapcase())  # abcdefghijklmnopqrstuvwxyz

# strip - trim spaces around words
spacechar = "     inner      "
print(spacechar.strip())  # inner

# lstrip - remove spaces before words
print(spacechar.lstrip())  # "inner      "

# rstrip - remove spaces after words
print(spacechar.rstrip())  # "     inner"

# replace() - replace letters
greet = "Hello Friend"
print(greet.replace("Friend", "Sir"))  # Hello Sir

# startswith() - check wether start with sub char in a string
print(smallLetters.startswith("a"))  # True
print(smallLetters.startswith("z"))  # False

# endswith() - check wether end with sub char in a string
print(smallLetters.endswith("a"))  # False
print(smallLetters.endswith("z"))  # True

num1 = "0123456789"
num2 = "0123456seven"

# isdigit - check wether (0-9)only in a string
print(num1.isdigit())  # True

# isalpha - check wether (a-z and A-Z)only in a string
print(smallLetters.isalpha())  # True
print(num2.isalpha())  # False

# isnumeric - check wether (0-9 and other numeric chars (roman num and super scrip and sub scrip)only in a string
print(num1.isnumeric())  # True

# isalnum - check wether (a-z and A-Z and 0-9)only in a string
print(num2.isalnum())  # True
print("aung aung".isalnum())  # False cuz space is special char

# isspace - check contains space only in string
print(" ".isspace())  # True
print("    ".isspace())  # True

# istitle() - check string is like title
print("Aung Aung".istitle())  # True

# split()  - split as substrin of string base on delimeter and return list
print("Hello Friend".split())  # ['Hello', 'Friend']
print("Hello Friend".split(" "))  # ['Hello', 'Friend']
print("red,green,blue,black,white".split(","))  # ['red', 'green', 'blue', 'black', 'white']

# \n = newline
# splitlines() - split as substrin of string base on \n and return list
newline = "line1\nline2\nline3"
print(newline)
# line1
# line2
# line3
print(newline.splitlines())  # ['line1', 'line2', 'line3']

# partition() - it's split 3 parts a string (before separator , separator and after separator)
print(newline.partition("\n"))  # ('line1', '\n', 'line2\nline3')

# ljust, rjust and center are text aligns methods, they add fill characters as padding
post = "new post"
print(post.ljust(10, "*"))  # new post**  ljust align left and fill
print(post.rjust(10, "*"))  # **new post  ljust align right and fill
print(post.center(10, "*"))  # *new post*  ljust align center and fill

# format() - format string and make dynamic
name = "Alice"
age = 30
introduce = "My name is {} and I'm {} years old."
print(introduce.format(name, age))  # My name is Alice and I'm 30 years old.

# format_map() - format key of objects like dict to a string
person = {"name": "Alice", "age": 30}
# print(introduce.format_map(person).format_map(person))

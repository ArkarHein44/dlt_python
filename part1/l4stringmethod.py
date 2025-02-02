# strings are character array also in python
# so, we can acess with index
# negative index make reverse  (-1 is the last character)

name = "aung kyaw"
print(name)
print(name[0])
print(name[3])
print(name[8])
print(name[-1])
print(name[-2])
print(name[-8])

# start:end(next count):step
print(name[0:1])
print(name[0:2])
print(name[0:3])
print(name[0:4])

print(name[1:4])
print(name[1:7])
print(name[0:9])  # aung kyaw

print(name[0:9:1])
print(name[0:9:2])
print(name[0:9:3])  # agy

# fullname = name
# fullname = name[:]
# fullname = name[0:4]
fullname = name[::-1]
print(fullname)  # wayk gnua

getLength = len(name)
print(getLength)  # 9

text = "hello friend"
print(text.upper())  # HELLO FRIEND

print(text.capitalize())  # Hello friend
print(text.title())  # Hello Friend

task = "HAVE TO GO"
print(task.lower())  # have to go
print(task.casefold())  # have to go

todo = "Have To Shop"
print(todo.swapcase())  # hAVE tO sHOP

hifi = "     hello friend   "
print(hifi)  # "     hello friend   "
print(hifi.strip())  # hello friend
print(hifi.lstrip())  # hello friend
print(hifi.rstrip())  # "     hello friend"

greet = "hello friend"
print(greet.replace("friend", "sir"))  # hello sir
print(greet.replace("Friend", "sir"))  # hello friend

print(greet.startswith("h"))  # True
print(greet.startswith("he"))  # True
print(greet.startswith("H"))  # False
print(greet.startswith("He"))  # False

print(greet.endswith("nd"))  # True
print(greet.endswith("friend"))  # True
print(greet.endswith("Friend"))  # False

num1 = 528
num2 = "1500"
num3 = "ten"
num4 = "number ten"
num5 = "hay!"

# print(num1.isdigit())  # error cuz of isdigit() can check only for string
print(str(num1).isdigit())  # True
print(num2.isdigit())  # True
print(num3.isdigit())  # False
print(num3.isalnum())  # True

print(num2.isalpha())  # False
print(num3.isalpha())  # True
print(num4.isalpha())  # False

print(num2.isnumeric())  # True
print(num3.isnumeric())  # False

print(num2.isalnum())  # True
print(num3.isalnum())  # True  (alpha and num <check escape char> also space is a special escape character)
print(num4.isalnum())  # False (cuz of space)
print(num5.isalnum())  # False (cuz of !)

middleName = " "
print(middleName.isspace())  # True

nickName = "Aung Moe"
print(nickName.isspace())  # False
print(nickName.istitle())  # True

sayhi = "Hi My Friend"
print(sayhi.split())  # ['Hi', 'My', 'Friend']

color = "red, green, blue, white, black"
print(color.rsplit())  # ['red,', 'green,', 'blue,', 'white,', 'black']
print(color.rsplit(","))  # ['red', ' green', ' blue', ' white', ' black']
print(color.rsplit(",", 1))  # ['red, green, blue, white', ' black']

# \n = new line
sayhello = "Hello\nFriend"
print(sayhello)
# Hello
# Friend
print(sayhello.splitlines())  # ['Hello', 'Friend']

sayhifi = "Hello Friend Mr.Maung"
print(sayhifi.partition(" "))  # ('Hello', ' ', 'Friend Mr.Maung')
print(sayhifi.partition("."))  # ('Hello Friend Mr', '.', 'Maung')
print(type(sayhifi.partition(".")))  # <class 'tuple'>


post = "Read"
print(post.ljust(10, '-'))  # Read------
print(post.rjust(10, '-'))  # ------Read
print(post.center(10, '-'))  # ---Read---
print(post.center(10, '*'))  # ***Read***

city = "Hello {}"
print(city.format("Mandalay"))  # Hello Mandalay

country = "Hello {} {}"
print(country.format("Mandalay", "Myanmar"))  # Hello Mandalay Myanmar

val1 = "sister"
val2 = "Su Su"
print("Hello my {}. are you {}!".format(val1, val2))  # Hello my sister. are you Su Su!

# dictionary
student = {"name": "su su"}
sayname = "Dear, {name}"
print(sayname.format_map(student))  # Dear, su su

message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy Text ever since the 1500s lorem"

countoflorem = message.count("Lorem")
print(countoflorem)  # 2

countoftext = message.count("text")
print(countoftext)  # 1
# 13SM
# Functions
# 1. Simple Function with no parameter
# 2. Function with parameter
# (i) single parameter function
# (ii) multi parameter function
# 3. Function with default parameter
# 4. Function with a Return Value
# 5. Function with multi return values
# 5. Lambda Function (anonymous function)

# 1. Simple Function with no parameter
def sayname():
    print("Hello Aung Aung")


sayname()
sayname()


# 2. Function with parameter
#     (i) single parameter


def saycity(city):
    print("Hello" + city)


saycity("Yangon")
saycity("Mandalay")


# 3. Function with default parameter


def country(countryname="Thailand"):
    print(f"Hello {countryname}")


country()
country("Myanmar")
country("Indonesia")


# 4. Function with a return value


def sayage():
    return "I am 25 years old."


print(sayage())


def saynickname():
    result = "Daw Pu"
    return result

print(saynickname())

def saynum(num1=20):
    return num1

print(saynum(100))
print(saynum())

def greeting(value="yamin"):
    return f"Hello {value}"

# Fstring used to call variables, comma separators, do padding with zeros and date format.

print(greeting("Su Su"))
print(greeting())

def funone(num1, num2):
    result = num1 + num2
    return result

print(funone(10, 20))

def funtwo(num1, num2=200):
    result = num1 + num2
    return f"Total value of {num1} + {num2} is = {result}"

print(funtwo(10))
print(funtwo(10, 20))

# 5. Function with multi return values
def saynameandage():
    name1 = "Honey"
    age1 = 26
    return name1, age1

print(saynameandage())

name, age = saynameandage()

print(name)
print(age)

# 5. Lambda function (Anonymous Function)
addresult = lambda num1, num2, num3: num1 + num2 + num3
print(addresult(200, 300, 400))

sumresult = lambda num1, num2 = 200, num3 = 500: num1 + num2 + num3
print(sumresult(200,300))
print(sumresult(100))

# inputval = input("Enter your name = ")
# msg = "Hello "+inputval
# msg = "Hello %s" % inputval # v2 do not use
# msg = f"Hello {inputval}"

# print(msg)

# firstname = input("Enter First name = ")
# lastname = input("Enter Last name = ")
# fullname = "Hello %s%s" % (firstname,lastname) #v2
# fullname = "Hello %s %s" % (firstname,lastname) #v2
# fullname = f"Hello {firstname} {lastname}"
# print(fullname)

# Generator Function
def genfun():
    yield 1
    yield 2
    yield 3

print(genfun())  # <generator object genfun at 0x0000027934104BF0>
print(list(genfun()))  # [1, 2, 3]

for value in genfun():
    print(value)  # 1 2 3

"""
print("hello world")
print("hello world")
"""
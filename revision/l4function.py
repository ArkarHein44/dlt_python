# equal
if 20 == 20:
    print("Yes, it's equal")
else:
    print("Not equal")

if 10 != 20:
    print("Yes, not equal")
else:
    print("No, it's equal")

if 10 > 20:
    pirnt("Yes, greater than")
else:
    print("No, less than")

if 20 < 10:
    print("Yes, less than")
else:
    print("No, greater than")

# identity operators
a = [10, 20, 30]
b = a

print("identity", a is b)
print("identity", a is not b)


# membership operators
arr = [10, 20, 30, 40]
print(20 in arr)
print(10 not in arr)


def funone():
    return "I am funone"


funone()

if isinstance("abc", int):
    print("Yes, 10 is int")
else:
    print("No")

print(type({"name": "nu nu"}))

"use f in front of string"
name = "Jame"
print("Hello, %s !" % name)

# multi lines f string (""")
print(f"""
fstring used in python v 3.6+
easy to use and read than modulo operator (%)
""")

# fstring float decimal (.2f for 2 decimal)
fnum = 10.35489
print(f"float in 2 decimal {fnum:.2f}")

# expression in fstring
num1 = 190
num2 = 130
print(f"{num1} + {num2} = {num1 + num2}")

# function call in fstring
print(f"{funone()}")

lambdafun = lambda num1, num2 : num1 + num2

print(lambdafun(100,2000))


def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(4)

print(mydoubler(11))



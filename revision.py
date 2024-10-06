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
a = [10,20,30]
b = a

print("identity", a is b)
print("identity", a is not b)


# membership operators
arr = [10, 20, 30, 40]
print(20 in arr)
print(10 not in arr)


def funone():
    print("I am funone")


funone()

if isinstance("abc", int):
    print("Yes, 10 is int")
else:
    print("No")

print(type({"name": "nu nu"}))

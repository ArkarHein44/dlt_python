# => Data Containers 

# list
mylist = [1,2,3,4,5]
print(type(mylist))  # <class 'list'>

# tupple
mytuple = (1,2,3,4,5)
print(type(mytuple))  # <class 'tuple'>

# dict
mydict = {"a":1, "b":2, "c":3}
print(type(mydict))  # <class 'dict'>

# set 
# In Python, a set is a built-in data type that stores multiple items in a single variable. Sets are unordered, unchangeable, and unindexed. They are useful for removing duplicate values from a list or tuple, and for performing math operations like unions and intersections

myset = {1,2,3,4,5}
print(myset)
print(type(myset))  # <class 'set'>

# we can't create empty set with {}
dict1 = {}
print(type(dict1))  # <class 'dict'>

set1 = {}
print(type(set1))  # <class 'dict'>

# create an empty set
set2 = set()
print(type(set2))  # <class 'set'>

colors = {"red", "green", "blue", "white", "black"}
print(colors)

for color in colors:
	print(color)

print("green" in colors)  # True
print("steelblue" in colors)  # False   

fruits = {"apple", "orange"}
print(fruits)

# Adding a Single Element 
fruits.add("cherry")
print(fruits)

# Adding Multiple Element []
fruits.update(["mango", "grape"])
print(fruits)

# Remove Elements 
fruits.remove("orange")  # if element doesn't exists display error
print(fruits)

# Remove Elements (using discard)
fruits.discard("red") # if no elements exist  no error display
print(fruits)

fruits.discard("apple")
print(fruits)

# clear elements 
fruits.clear()
print(fruits)  # set()

# frozenset (Immutable set)
fornumbers = frozenset([10,20,30,40])
# fornumbers.add(50) # error
# fornumbers.remove(40) # error 
print(fornumbers)  # frozenset({40, 10, 20, 30}) 
print(20 in fornumbers)  # True
print(50 in fornumbers)  # False

sayhi = "Hello Friend"
print(set(sayhi)) # 'F', 'o', ' ', 'H', 'e', 'r', 'n', 'd', 'l', 'i'}


set3 = {1,2,3,6,7}
set4 = {3,4,6,5}

# Union Combines 
print(set3 | set4) # {1, 2, 3, 4, 5, 6, 7}
print(set3.union(set4))

# Intersection ( & )
print(set3 & set4) # {3, 6}
print(set3.intersection(set4)) 

# Difference ( - )
print(set3 - set4) # {1, 2, 7}
print(set3.difference(set4)) # {1, 2, 7}

# Symmetric Difference ( ^ )
print(set3 ^ set4)  # {1, 2, 4, 5, 7}
print(set3.symmetric_difference(set4)) # {1, 2, 4, 5, 7}

print(set4 ^ set3) # {1, 2, 4, 5, 7}
print(set4.symmetric_difference(set3)) # {1, 2, 4, 5, 7}

# => set comprehension
# {expression for item in iterable if condition}

squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}
# how does it work
# 0 ** 2 = 0
# 1 ** 2 = 1
# 2 ** 2 = 4
# 3 ** 2 = 9
# 4 ** 2 = 16

evens = {x for x in range(10) if x%2 == 0}
print(evens)  # {0, 2, 4, 6, 8}

uniquechars = {char for char in "hello world"}
print(uniquechars)  # {'d', 'w', ' ', 'e', 'h', 'r', 'l', 'o'}

numbers = [1, 2, 2, 3, 4, 7, 5, 7]
uniquenumbers = {x for x in numbers}
print(uniquenumbers)  # {1, 2, 3, 4, 5, 7}

# => Nested Loops in set comprehension
couplenums = {(x,y) for x in range(3) for y in range(2)}
print(couplenums)  # {(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0)}

# x takes values 0 to 2
# y takes values 0 to 1
# x=0 y=0 (0,0)
# x=0 y=1 (0,1)
# x=1 y=0 (1,0)
# x=1 y=1 (1,1)
# x=2 y=0 (2,0)
# x=2 y=1 (2,1)
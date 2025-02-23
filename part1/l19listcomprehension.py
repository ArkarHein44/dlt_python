# => List Comprehension
# [expression for item in iterable ]

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
# how does it work
# 0 ** 2 = 0
# 1 ** 2 = 1
# 2 ** 2 = 4
# 3 ** 2 = 9
# 4 ** 2 = 16

evens = [x for x in range(10) if x%2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

uniquechars = [char for char in "hello world"]
print(uniquechars)  # ['d', 'w', ' ', 'e', 'h', 'r', 'l', 'o']

numbers = [1, 2, 2, 3, 4, 7, 5, 7]
uniquenumbers = [x for x in numbers]
print(uniquenumbers)  # [1, 2, 3, 4, 5, 7]

# => Nested Loops in set comprehension
couplenums = [(x,y) for x in range(3) for y in range(2)]
print(couplenums)  # [(0, 1), (2, 1), (0, 0), (1, 1), (2, 0), (1, 0)]

# x takes values 0 to 2
# y takes values 0 to 1
# x=0 y=0 (0,0)
# x=0 y=1 (0,1)
# x=1 y=0 (1,0)
# x=1 y=1 (1,1)
# x=2 y=0 (2,0)
# x=2 y=1 (2,1)

# => Nested list comprehension 

nestnumberarr = [[1,2,3],[40,50,60],[700,800,900]]

flatarrs = [y for x in nestnumberarr for y in x]
print(flatarrs) #

# for x in nestnumberarr
# first iteration x = [1,2,3]
# second iteration x = [40,50,60]
# third iteration x = [700,800,900]

# for y in x 
# first iteration x = [1,2,3] . process y = 1, y = 2, y = 3
# second iteration x = [40,50,60] . process y = 40, y = 50, y = 60
# third iteration x = [700,800,900] . process y = 700, y = 800, y = 900
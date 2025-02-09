# enumerate()

colors = ["red", "green", "blue"]

for color in colors:
    print(color) # red green blue

for index,color in enumerate(colors):
    print(index, color) # 0 red 1 green 2 blue

numbers = [10, 20, 30, 40]

for idx, value in enumerate(numbers):
    numbers[idx] = value * 2

print(numbers) # [20, 40, 60, 80]

colors = ["red", "green", "blue", "black", "white"]

for index,color in enumerate(colors):
    if color == "black":
        print(f"black color is exists.")

# = custom start index
for index,color in enumerate(colors, start=10):
    print(f"Index {index} : {color}") # start from index 10

message = "Hello World"

for index, msg in enumerate(message):
    print(index, msg)  

colours = ["Red", "Green", "Blue"]

colorlist = list(enumerate(colors, 100))
print(colorlist) # [(100, 'red'), (101, 'green'), (102, 'blue'), (103, 'black'), (104, 'white')]
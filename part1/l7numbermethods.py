# int() convert to integer
num1 = 256.99
print(int(num1))  # 256

num2 = "528"
print(int(num2))  # 528

num3 = "1500.56"
# print(int(num3))  # error 

# abs() make absolute value (no negative value)
num4 = 100
print(abs(num4))  # 100

num5 = -200
print(abs(num5))  # 200

# float() make a floating number
num6 = "3.67"
print(float(num6))  # 3.67

num7 = 5
print(float(num7))  # 5.0

# round() add 1 decimal point over 5 (0.56 to 0.6)
num8 = 4.56862
print(round(num8))  # 5
print(round(num8,1))  # 4.6
print(round(num8,2))  # 4.57
print(round(num8,3))  # 4.569

# pow(base,power) -> base^power
# 2^3 = 8
print(pow(2,3))  # 8
print(pow(2,5))  # 32

# 10//2 = 5, 10%2 = 0
# division and modules divmod()
print(divmod(10,2))  # (5,0)
print(divmod(9,2))  # (4,1)
print(divmod(100,3))  # (33,1)

# find max num
print(max(10,50,20,18,30))
# find min num
print(min(10,50,20,18,30))

# sum all nums
print(sum([1,2,3,4,5]))  # 15
print(sum((1,2,3,4,5)))  # 15

# Mathematical Functions (from math module)
# To use the math module ! you need to import

import math

# math.pow give value with decimals point 
print(math.pow(2,3))  # 8.0
print(math.pow(3,3))  # 27.0

# square root form math module ( output with decimals )
print(math.sqrt(16))  # 4.0
print(math.sqrt(64))  # 8.0
print(math.sqrt(36))  # 6.0
print(math.sqrt(35))  # 5.916079783099616

# math.ceil make no decimal add 1 for any decimal except 0 
print(math.ceil(3.2))  # 4
print(math.ceil(3.5))  # 4
print(math.ceil(3.0))  # 3

# substract decimal from number 
print(math.floor(3.2))  # 3
print(math.floor(3.7))  # 3

# e - Euler number is approximately 
# 1e = power of 10 
# 1e-16 = 10^-16
# 2e3 = 2x10^3 = 2000

print(math.e)  # 2.718281828459045

print(math.log(100,10))  # 2.0 (log base 10)
print(math.log(81,9))  # 2.0 (log base 9)

print(math.log(10,2))  # 3.3219280948873626
print(math.log(100,2))  # 6.643856189774725

# default is e
print(math.log(100))  # 4.605170185988092

print(math.log10(100))  # 2.0 (log base 10)
print(math.log10(1000))  # 3.0 (log base 10)

print(math.log2(8))  # 3.0

# math.exp(exponential) , base is e
print(pow(2.718281828459045,2))  # 7.3890560989306495
print(math.exp(2))  # 7.38905609893065

print(pow(2.718281828459045,3))  # 20.085536923187664
print(math.exp(3))  # 20.085536923187668 print(pow(float(math.e),3))

# module for random 
import random

print(random.random()) # 
print(random.random()) # 

# random integer 
print(random.randint(1,10)) # return an integer between x and y

print(random.uniform(1.5, 4.5)) # return a float between x and y

numlists = [10, 200, 300, 400, 5000]
print(random.choice(numlists))  # random  element from the list

numtuple1s = (10, 200, 300, 400, 5000)
print(random.choice(numtuple1s))  # random  element from the tuplet

numtuple2s = 10, 200, 300, 400, 5000
print(random.choice(numtuple2s))  # random  element from the tuplet

# 27TP
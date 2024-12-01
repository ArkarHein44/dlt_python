
# OOP 
class MyMath:
	def sum(self,x,y):
		return x+y
	def sub(self,x,y):
		return x-y
	def multi(self,x,y):
		return x*y
	def div(self,x,y):
		return x/y
	
class MyMathExtt(MyMath):
	def square(self,x):
		return x**2
	def three(self,x):
		return x**3
	
math = MyMath()

print(math.sum(100,200))
print(math.sub(400,60))
print(math.multi(30,5))
print(math.div(65,5))

pow = MyMathExtt()
print(pow.square(8))
print(pow.three(72))


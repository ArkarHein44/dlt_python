# => Unpacking Arguments

def sayhi(name,age):
	print(f"Hello friend! my name is {name}, I'm {age} years old.")

# Unpacking positional argument 
sayhi("Su Su",30)
args = ("Yu Yu",20)
sayhi(*args) # Hello friend! my name is Yu Yu, I'm 20 years old.

def addingnumbers(a,b,c):
	print(f"Sum Result = {a+b+c}")

addingnumbers(1,2,3)

tuplenumbers= (10,20,30)
addingnumbers(*tuplenumbers)

listnumbers = [100, 200, 300]
addingnumbers(*listnumbers)

#Unpack keyword argument
listinfo = {"name":"Hla Hla", "age":30}
sayhi(**listinfo)

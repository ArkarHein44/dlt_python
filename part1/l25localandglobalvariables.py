# => Same Name for local and global variable

globalvar = "i am Global"

def myfun3():
    golbalvar = "i am local"
    print("Insider function myfun3 = ",globalvar)

myfun3() # i am local
print("Outside function myfun3 = ", globalvar) # i am Global

# = Exercise

msg1 = "Hello Sir, this is global variable"

def funone():
    msg2 = "Hi Students, this is local variable"
    print("Inside function funone = ",msg1)
    print("Inside function funone = ",msg2)

def funtwo():
    msg1 = "Hello Teacher, this is global variable"    
    msg2 = "Hi Staffs, this is local variable"

    print("Inside function funtwo = ",msg1)
    print("Inside function funtwo = ",msg2)

def funthree():
    global msg1 # global keyword
    msg1 = "Hello Boss, this is global variable"    
    msg2 = "Hi Employee, this is local variable"

    print("Inside function funthree = ",msg1)
    print("Inside function funthree = ",msg2)

funone() # Sir, Students
funtwo() # Teacher, Staffs
# print("Outside function funtwo = ",msg2) # NameError:

funthree() # Boss, Employee

print("Outside function after funthree = ",msg1) # Boss...

# => Nested function and nonlocal keyword
def funfour():
    msg3 = "i am msg3 from outside funfive"

    def funfive():
        nonlocal msg3
        msg3 = "i am msg3 Modified by funfive"
    
    print("Before invoking funfive = ", msg3)
    funfive()
    print("After invoking funfive = ", msg3)

funfour()
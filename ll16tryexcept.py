# => Exception Handling 

# try:
#     exception
# except exceptiontype:
#     code to handle the exception 

# => exceptiontype 
    # (i) ValueError
    # (ii) ZeroDivisionError

# try:
#     number = int(input("Enter lucky number: "))
#     print(f"Your Lucky number is = {number}")
# except:
#     print("Something went wrong! please enter a valid number.")

# try: 
#     number = int(input("Enter number: "))
#     print(10/number)
# except ValueError:
#     print("Invalid input! please enter a valid number.")
# except ZeroDivisionError:
#     print("You can't divide by zero")

# else and finally 

# else block (optional) = execute only if no Exception occurs in the try block 
# finally block (optional) = excute whether or not an excepetion coours

# try: 
#     number = int(input("Enter number: "))
#     result = 10/number
# except ValueError:
#     print("Invalid input! please enter a valid number.")
# except ZeroDivisionError:
#     print("You can't divide by zero")
# else:
#     print(f"Result is = {result}")
# finally:
#     print("Program Completed")

# => Raising Exception 

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age can't be negative")
    else:
        print(f"Your age is = {age}")
except ValueError as err:
    print(f"Error : {err}")
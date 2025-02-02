# => Write a File 
# mode
# 'r' = Read (default)
# 'w' = write
# 'a' = Append

# syntax
# oepn('filename.txt', mode)

# => Write File 

# write()
# writelines()

# => Method 1, write() 
print("\n Method 1 write()")

file = open("files/file2.txt", "w")
file.write("Hello World!")
file.close() # Always need to close to save changes

# => Method 2, wirtelines()
print("\nMethod2, writelines()")

lines = ["Hello Sir! \n", "This is Python Batch 1 zoom class.\n", "How to read file in python programming  language."]

file = open("files/file3.txt", "w")
file.writelines(lines)
file.close()

# => Using with statement
print("\n Using with statement")

with open("files/file4.txt", "w") as file:
    file.write("Hello Sir!")
    file.write("This is Python Batch 1 zoom class.")
    file.write("How to read file in python programming  language.")

# => Append to a file
print("\n Append to a file")

with open("files/file5.txt", "a") as file:
    file.write("\n This line is appened to the file.")

print("\nWith Variable ")

name = "Yu Yu"
age = 27

with open("files/file6.txt", "w") as file:
    file.write(f"My name is {name} and I'm {age} years old. \n")

# => Error Handling 
print("\n Error Handling")

try:
    with open("files/file7.txt", "w") as file:
        file.write("This is python batch 1 zoom class. \n")
except Exception as err:  # IOError/Exception 
    print(f"an IO error: {err}")
finally:
    print("Program Completed")




# 19WF
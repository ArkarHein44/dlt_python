# => Open File 
# mode
# 'r' = Read (default)
# 'w' = write
# 'a' = Append

# syntax
# oepn('filename.txt', mode)

# => Read File 

# read()      = Read the entire file
# readline()  = Read on line at a time 
# readlines() = Read all lines into a list



# => Method 1, read() ( With statement ), Read all content at once, Not memory-efficient for large files

# default is read 
# with open('files/file1.txt', 'r') as file:
print('\n Method 1, read() ')
with open('files/file1.txt', 'r') as file:
    # print(file)
    # <_io.TextIOWrapper name='files/file1.txt' mode='r' encoding='cp1252'>

    getcontent = file.read()
    print(getcontent)
    # Hello World!
    # This is Python Batch 1 zoom class.
    # How to read file in python programming  language.  

# => File Encoding 
print('\n File Encoding')
with open('files/file1.txt', 'r', encoding='UTF-8') as file:
        getcontent = file.read()
        print(getcontent)
        # Hello World!
        # This is Python Batch 1 zoom class.
        # How to read file in python programming  language.

# => Read Specific Number of characters
print('\n Read Specific Number of characters')

with open('files/file1.txt', 'r', encoding='UTF-8') as file:
        getcontent = file.read(10)
        print(getcontent)
        # Hello Worl

# => Method 2, using strip(), Read line by line, (one line at a time, Eficient for large file)
print('\n using strip()')

with open('files/file1.txt', 'r') as file:
    for line in file:
        # print(line)
        print(line.strip()) # .strip() removes extra newline characteers

# => Method 3, readline(), Read line by line, (one line at a time, Eficient for large file)
print('\nMethod 3, readline()')

with open('files/file1.txt', 'r') as file:
    lines = file.readline()
    # print(lines)

    while lines:
        print(lines.strip())
        lines = file.readline()
        # Hello World!
        # This is Python Batch 1 zoom class.
        # How to read file in python programming  language.

# => Method 3, readlines(), Read lines by line, (one line at a time, Eficient for large files)
print('\nMethod 3, readlines()')

with open('files/file1.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    # ['Hello World!\n', 'This is Python Batch 1 zoom class.\n', 'How to read file in python programming  language.'] 

    for line in lines:
         print(line.strip()) # .strip() removes extra newline characters

# => Handling Exceptions
print('\nFile Handling Exceptions')
# => exceptiontype
    # (i) FileNotFoundError
    # (ii) PermissionError
    # (iii) IOError

try:
    with open("files/file1.txt", 'r') as file:
        getcontent = file.read()
        print(getcontent)
except FileNotFoundError:
    print("Your file does not exist.")
except PermissionError:
    print("You do not have the necessary permission.")
except IOError as err:
    print(f"An IO error :{err} ")
finally:
    print("Program Completed")
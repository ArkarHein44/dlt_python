# => Types of Argument in Python 
# Positional Arguments 
# Keyword Arguments
# Default Arguments 
# Variable-length Argumentss (*args) (Non-keyword Variable Arguments)
# Variable-length Argumentss (**kwargs) (keyword Variable Arguments)

# Positional arguments 
def greet(name,age):
    print(f"Hello frient! my name is {name}, I am {age} years old.")

greet("Su Su",23)  # Hello frient! my name is Su Su, I am 23 years old.
greet(25,"Nu Nu")  # Hello frient! my name is 25, I am Nu Nu years old.


# Keyword Arguments 
def hifi(name,age):
    print(f"Hello frient! my name is {name}, I am {age} years old.")

hifi(name="Min Min",age = 25)  # Hello frient! my name is Min Min, I am 25 years old.
hifi(age=30,name="Nyi Nyi")  # Hello frient! my name is Nyi Nyi, I am 30 years old.

# Default Arguments 
def hime(name,age=18):
    print(f"Hello frient! my name is {name}, I am {age} years old.")

hime("Yamin")  # Hello frient! my name is Yamin, I am 18 years old.
hime("Thuzar",20)  # Hello frient! my name is Thuzar, I am 20 years old.

# Variable-length Argumentss (*args) (Non-keyword Variable Arguments)
def boys(*args):
    print(args)

boys("aung aung")  # ('aung aung',)
boys("aung aung", "kyaw kyaw")  # ('aung aung', 'kyaw kyaw')
boys("aung aung", "kyaw kyaw", "zaw zaw", "tun tun")  # ('aung aung', 'kyaw kyaw', 'zaw zaw', 'tun tun')

def sumresults(*numbers):
    total = sum(numbers)
    print(f"Sum result is = {total}")

sumresults(1,2,3)  # Sum result is = 6
sumresults(10,20,30,40,50)  # Sum result is = 150

def myfunone(num, *nums):
    print(num)
    print(nums)

myfunone(1,2,3,4,5)

# ERROR 
# def myfuntwo(*nums,num):
#     print(num)
#     print(nums)

# myfunone(1,2,3,4,5)

# Variable-length Argumentss (**kwargs) (keyword Variable Arguments)
def personinfos(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} = {value}")

personinfos(name="Thuzar",age=25,city="Mandalay")
# name = Thuzar
# age = 25
# city = Mandalay

personinfos(name="Kaung Kaung",professional="Engineer",city="Yangon")
# name = Kaung Kaung
# professional = Engineer
# city = Yangon

# Exercise (Combining Different Type of Arguments)

def emailsender(address, *messages, **files):
    print(f"Address = {address}")
    if messages:
        for message in messages:
            print(f"Message = {message}")
    if files:
        for key,value in files.items():
            print(f"{key} = {value}")

emailsender("dataland@gmail.com", "Hello admin", "I want to request vdo records", lesson="Python B1", classdate="25/Nov/2025")
# Address = dataland@gmail.com
# Message = Hello admin
# Message = I want to request vdo records
# lesson = Python B1
# classdate = 25/Nov/2025

def studentinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"Age = {age}")
    if hobbies:
        for hobbie in hobbies:
            print(f"Hobbies = {hobbie}")
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")

studentinfos("Nandar")
studentinfos("Maung Maung", 25)
studentinfos("Aung Kyaw", 25, 'reading', 'travelling')
studentinfos("Aung Kyaw", 25, 'reading', 'travelling', city="Bago", profession="Enginner")


def staffinfos(name,age=18,*hobbies,**infos):
    print(f"Name = {name}")
    print(f"Age = {age}")
    if hobbies:
        for hobbie in hobbies:
            # print(f"Hobbies = {hobbies}") 
            print(f"Hobbies = {','.join(hobbie)}")
    if infos:
        for key,value in infos.items():
            print(f"{key} = {value}")
staffinfos("Ni Lar", 20, 'reading', 'travelling', city="Yangon", profession = "Engineer")


# 25OV
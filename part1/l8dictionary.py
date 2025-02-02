# Method 1

student = {
    "name":"su su",
    "age":20,
    "city":"yangon"
}

print(student)  # {'name': 'su su', 'age': 20, 'city': 'yangon'}
print(student["name"])  # su su
print(student.get("city"))  # yangon

# Method 2 dict()
staff = dict(name="Aung Aung",age=30,city="Mandalay")

print(staff)  # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay'}
print(staff["age"])  # 30
print(staff.get('city'))  # Mandalay

# bracket notation နဲ့ခေါ်ရင် မရှိရင် error တက်မယ် 
# print(student["country"])  # KeyError: 'country'
# print(staff["country"])  # KeyError: 'country'

# get() method နဲ့ခေါ်ရင် မရှိရင် None လို့ print out ထွက်မယ် 
print(student.get('country'))  # None
print(staff.get('country'))  # None

# value ၁ခုထက်ပိုထုတ်ကြည့်ပါက မရှိတာကို ချန်လှပ်၍ ရှိတဲ့ key name ကိုပဲ access လုပ်ကာ value ကိုထုတ်ပေးမယ်
print(student.get('country','Myanmar'))  # Myanmar
print(staff.get('country','Thailand'))  # Thailand

print(student.get('age', 40))  # 20
print(staff.get('age', 40))  # 30

employee = {
    "name" : "Aung Aung",
    "age" : 30,
    "city":"Mandalay"
}

print(employee)  # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay'}

# key value pair အသစ်တစ်ခုထပ်ထည့်မယ်
employee["email"] = "aungaung@gmail.com"
print(employee)  # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}

# modified or over write လုပ်မယ်
employee["age"] = 25
print(employee)  # {'name': 'Aung Aung', 'age': 25, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}

# key value pair ဖျက်မယ် 
del employee["city"]
print(employee)  # {'name': 'Aung Aung', 'age': 25, 'email': 'aungaung@gmail.com'}

worker = dict(name="Nilar",age=18,city="Bago")

print(worker)  # {'name': 'Nilar', 'age': 18, 'city': 'Bago'}

# key value pair အသစ်တစ်ခုထပ်ထည့်မယ်
worker["email"] = 'nilar@gmail.com'
print(worker)  # {'name': 'Nilar', 'age': 18, 'city': 'Bago', 'email': 'nilar@gmail.com'}

# modified or over write လုပ်မယ်
worker["age"] = 25
print(worker)  # {'name': 'Nilar', 'age': 25, 'city': 'Bago', 'email': 'nilar@gmail.com'}

# key value pair ဖျက်မယ် 
del worker["email"]
print(worker)  # {'name': 'Nilar', 'age': 25, 'city': 'Bago'}
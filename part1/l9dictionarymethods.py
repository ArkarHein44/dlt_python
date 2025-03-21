lady = {"name":"Yadanar","age":30}
print(lady)  # {'name': 'Yadanar', 'age': 30}
print(type(lady))  # <class 'dict'>

# dict.get() method သည် dictionary ထဲမှ value ကို ရယူရန် သုံးနိုင်သည်။ key ကိုထည့်ပေးရမည်။ key သည် dict အတွင်းမရှိပါက None ဟု return ပြန်ပေးသည်။

print(lady.get('name')) # <class 'dict'>
print(lady.get('gender')) # None
print(lady.get('gender', 'Not Defined')) # Not Defined

# dict.keys 
print(lady.keys())  # dict_keys(['name', 'age'])
print(type(lady.keys()))  # <class 'dict_keys'>

# list(dict.keys)
print(list(lady.keys())) # ['name', 'age']
print(list(lady.keys())[0]) # name
print(list(lady.keys())[1]) # age

# dict.values
print(lady.values()) # dict_values(['Yadanar', 30])

# list(dict.values)
print(list(lady.values())) # ['Yadanar', 30]
print(list(lady.values())[0]) # Yadanar
print(list(lady.values())[1]) # 30

# dict.items()
print(lady.items())  # dict_items([('name', 'Yadanar'), ('age', 30)])

# list(dict.items())
print(list(lady.items()))   # [('name', 'Yadanar'), ('age', 30)]
print(list(lady.items())[0])  # ('name', 'Yadanar')
print(list(lady.items())[1])  # ('age', 30)
print(list(lady.items())[0][0])  # name
print(list(lady.items())[0][1])  # Yadanar
print(list(lady.items())[1][0])  # age
print(list(lady.items())[1][1])  # 30

# dict.update() (insert new and modifie old)
lady.update({'age':20, 'gender':'female'})
print(lady)  # {'name': 'Yadanar', 'age': 20, 'gender': 'female'}

# dict.pop()
lady.pop('age')
print(lady)  # {'name': 'Yadanar', 'gender': 'female'}

# dict.clear()
lady.clear()
print(lady) # {}

# boy = {'name':'Zaw Zaw','city':"Yangon"}
# boy.pop()
# print(boy) #error

girl = {'name':'yadanar','age':30,'city':'Mawlamyine'}

# dict.popitem()
item = girl.popitem()
print(item) # ('city', 'Mawlamyine')
print(item[0]) # city
print(item[1]) # Mawlamyine

print(girl) # {'name': 'yadanar', 'age': 30}

# dict.copy()
woman = girl.copy()
print(woman) # {'name': 'yadanar', 'age': 30}

# 3DM
# => all(iterable)
# Note (true) : Non-zero numbers, non-empty, True
# Note (false) : 0, empty, False

# List 
boollists = [True, True, True]
print(all(boollists)) # True
print(any(boollists)) 

boollists = [True, False, True]
print(all(boollists)) # True
print(any(boollists))

numlists = [1,2,3,4,5]
print(all(numlists))
print(any(numlists))

numlists = [1,2,0,4,5]
print(all(numlists))
print(any(numlists))

emptylsit = []
print(all(emptylsit))
print(any(emptylsit))

# Tuple
booltuple = (True, True, True)
print(all(booltuple))
print(any(booltuple))

# Set 
numset = (1,2,3,4,0)
print(all(numset))
print(any(numset))

# Dictionary 
colordict = {1:"red", 2:"green", 23:"blue"}
print(all(colordict))
print(any(colordict))

# Dictionary 
colordict = {1:"red", 0:"green", 23:"blue"}
print(all(colordict))
print(any(colordict))

# using Cases
stringlists = ["red", "green", "blue"]
print(all(stringlists))
print(any(stringlists))

stringlists = ["red", "", "blue"]
print(all(stringlists))
print(any(stringlists))

# check all numbers positive
numlists = [10,20,30,40,50]

checkposit = all(num>0 for num in numlists)
print(checkposit)

numlists = [10,-20,30,40,50]
checkposit = all(num>0 for num in numlists)
print(checkposit)

# Validate a list of conditions 

requiredfields = ['username', 'email', 'password']

users ={
    "uername":"su su",
    "email":"susu@gmail.com",
    "password":"123456789"
}

getresult = all(field in users and users[field] for field in requiredfields) # all(True, True, True) = True
print(getresult)

# Explaination
# username in users = True
# users['username'] = su su (truthy) = True


users ={
    "uername":"su su",
    "email":"",
    "password":"123456789"
}

getresult = all(field in users and users[field] for field in requiredfields) # all(True, False, True) = False
print(getresult)

# 2AA
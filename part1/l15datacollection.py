# => Data Collection ( Module Containers )
from collections import Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import ChainMap

# => Counter (from collections module)
# from collections import Counter

getcounts = Counter("Hello World")
print(getcounts)  # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})

# => Queues ( from collections module)
# from collections import deque

qpersons = deque(["Su Su", "Nu Nu", "Yu Yu"])

qpersons.append("Tun Tun")  # last in
qpersons.appendleft("Sai Sai")  # first in
print(qpersons)  # deque(['Sai Sai', 'Su Su', 'Nu Nu', 'Yu Yu', 'Tun Tun'])

for person in qpersons:
    print(person)
# Sai Sai
# Su Su
# Nu Nu
# Yu Yu
# Tun Tun

# Removing elementes
lastout = qpersons.pop()  # last out
print(lastout)  # Tun Tun

firstout = qpersons.popleft()  # first out
print(firstout)  # Sai Sai

for person in qpersons:
    print(person)
# Su Su
# Nu Nu
# Yu Yu

# => defaultdict (from collections module)
# from collections import defaultdict

items = defaultdict(list)

items["fruits"].append('apple')
items["fruits"].append('mango')
items["fruits"].append('banana')
items["colors"].append('orange')
items["colors"].append('red')

print(items["fruits"])  # ['apple', 'mango', 'banana']
print(items["colors"])  # ['orange', 'red']
print(items["candy"])  # []

# use += insteads =
numitems = defaultdict(int)
numitems["val"] += 1

print(numitems)  # defaultdict(<class 'int'>, {'val': 1})
print(numitems["val"])  # 1

# Grouping Items 
groups = defaultdict(list)

foods = [("fruit", "apple"), ("fruit", "orange"), ("vegetable", "carrot"), ("fruit", "mango")]

for key, value in foods:
    groups[key].append(value)

print(groups)  # defaultdict(<class 'list'>, {'fruit': ['apple', 'orange', 'mango'], 'vegetable': ['carrot']})

numitems = defaultdict(int)
print(numitems["val"])  # 0
numitems["val"] = 1
print(numitems["val"])  # 1

# Counting Elements 
colorcounts = defaultdict(int)
candycolors = ["red", "green", "blue", "green", "red", "black", "green"]

for candycolor in candycolors:
    colorcounts[candycolor] += 1

print(colorcounts)  # defaultdict(<class 'int'>, {'red': 2, 'green': 3, 'blue': 1, 'black': 1})

# => OrderedDict (from collections module)
# from collections import OrderedDict

myorders = OrderedDict()
myorders["num1"] = 100
myorders["num2"] = 200
myorders["num3"] = 300
myorders["num4"] = 400
myorders["num5"] = 500

print(myorders)
print(myorders['num2'])  #  200

# Reordering Item 
myorders.move_to_end("num2")
print(myorders)  # OrderedDict({'num1': 100, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200}) 

# re-inserting 
myorders["num1"] = 10
print(myorders)  # OrderedDict({'num1': 10, 'num3': 300, 'num4': 400, 'num5': 500, 'num2': 200}) 

# Reordering item 
del myorders['num3']
print(myorders)  # OrderedDict({'num1': 10, 'num4': 400, 'num5': 500, 'num2': 200})

config = OrderedDict()
config['host'] = 'localhost'
config['post'] = 8080
config['debug'] = True

for key, value in config.items():
    print(f"{key} : {value}")

# host : localhost
# post : 8080
# debug : True   

# => namedtuple (from collections module)
LuckyNumbers = namedtuple("LuckyNumbers",["num1","num2","num3"])

getnums = LuckyNumbers(33,66,99)
print(getnums.num1)
print(getnums.num2)
print(getnums.num3)

# exercise with tuple, hard to remember what index number represent 
staff = ("Yu Yu", 20, "Developer")
print(staff[0])
print(staff[1])
print(staff[2])

# namedtuple
Student = namedtuple('Student',["name", "age", "profesion"])
# pupil = Student('Su Su', 30, "Engineer")
pupil = Student("Su Su", age=30, profesion="Engineer")
print(pupil.name)
print(pupil.profesion)
print(pupil.age)

# => ChainMap (from collections module)

dict1 = {"name":"Aye Aye"}
dict2 = {"city":"Yangon"}
getdata = ChainMap(dict1, dict2)
print(getdata)  # ChainMap({'name': 'Aye Aye'}, {'city': 'Yangon'})
print(getdata['name'])  # Aye Aye
print(getdata['city'])  # Yangon


# => array (from array module)
from array import array

myarrs = array('i', [10, 20, 30, 40])
print(myarrs)

getlength = len(myarrs)
print(getlength)

print(myarrs[0])
print(myarrs[2])

myarrs.append(50)
print(myarrs)

print(myarrs.index(50))

print(myarrs.count(20))

myarrs.insert(1, 100)
print(myarrs)

myarrs.remove(30)
print(myarrs)

for value in myarrs:
    print(value)

myarrs.reverse()
print(myarrs)

# => Queue (from queue module)
from queue import Queue

qone = Queue()  # Queue(0) mean infinite size
qone.put(400)
qone.put(100)
qone.put(300)

print(qone.get()) # 400 get after remove data
print(qone.get()) # 100
print(qone.get()) # 300

# 15CM


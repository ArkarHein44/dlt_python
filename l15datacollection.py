# => Data Collection ( Module Containers )
from collections import Counter
from collections import deque
from collections import defaultdict

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

# 11POV
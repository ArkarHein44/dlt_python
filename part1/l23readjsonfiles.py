import json
import os 

# => Reading JSON from a string

jsonstring = '{"name":"Hsu Myat Noe","age":18, "isstudent":true}'

datas = json.loads(jsonstring)
print(datas["name"])
print(datas["age"])

# => Reading a simple JSON file

def readjson(filename):
    with open(filename, 'r') as file:
        datas = json.load(file)
    return datas

getsimplejson = readjson('files/file8.json')

print(getsimplejson)

print(getsimplejson["name"])
print(getsimplejson["age"])
print(getsimplejson["hoobies"][0])
print(getsimplejson["hoobies"][1])

# => Reading a JSON Array file (load for json format)

getarrayjsons = readjson('files/file9.json')
print(getarrayjsons)

for getarrayjson in getarrayjsons:
    print(f"Name: {getarrayjson['name']} , Age: {getsimplejson['age']}")

# => Reading a complex JSON file (load for json format)

getcomplexjsons = readjson('./files/file10.json')

print(getcomplexjsons)
print(getcomplexjsons["company"])
getproduct = getcomplexjsons["product"]
print(getproduct)
print(getproduct[0]["name"])
print(getproduct[1]["price"])

# => Error Handling (check file exist or not)

try:
    with open('files/file10.txt', 'r') as file:
        datas = json.load(file)
except FileNotFoundError as e:
    print("Error: File not found.", str(e))
except json.JSONDecodeError as e:
    print("Error: Invalid JSON format!", str(e))
else:
    print(datas)

getfile = 'files/file100.json'

if not os.path.isfile(getfile):
    print (f"Error: File {getfile} does not exist.")
else:
    with open(getfile, 'r') as file:
        datas = json.load(file)
        print(datas)
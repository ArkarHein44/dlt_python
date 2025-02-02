import json 

# => Write a simple JSON file

datas = {
    "title":"Python FastAPI Batch 1",
    "price":25.99,
    "packages":["FastAPI", "Jinja2", "websocket", "Open Ai"]
}

with open("files/file1.json", "w") as file:
    # json.dump(datas,file)
    # json.dump(datas, file, indent=3) # indent is option for text indentation
    # json.dump(datas, file,indent=3, sort_keys=False) # sort_key is option for a to z
    json.dump(datas, file,indent=3, sort_keys=True)
    print("Successfully Created")

# => Error Handling

try:
    invaliddatas = {"numbers":{10,20,30}} # Set is not JSON-serializable
    with open('files/fileerror.json', 'w') as file:
        json.dump(invaliddatas, file)
except TypeError as e:
    print("Error:Type Error : ",str(e) )

# 26WJ
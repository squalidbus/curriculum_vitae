import json

filename = input("The filename is: ")


with open(filename, 'r') as f:
    json_loaded = json.load(f)

print(json_loaded)

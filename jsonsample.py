import json

with open('test.json', 'r') as fp:
    data = json.load(fp)

print(str(data))
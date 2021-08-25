import json

x = '{"name": "John", "age": 30, "city": "New York"}' #Dictionary

# y = json.dumps(x) #Convert dictionary to json
y = json.loads(x) #Convert json to dictionary
print(y)
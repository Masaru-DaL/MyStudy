import json

dictionary = {"a": 1, "b": 2}
dictionary_str = json.dumps(dictionary)
print(type(dictionary_str))

print(type(json.loads(dictionary_str)))

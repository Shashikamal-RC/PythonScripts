'''
Problem Statement : To convert json to dict and vice versa
Developer : Shashikamal R C
'''

import json

# json to dict
some_json = '{"name" : "Shashikamal R C", "job": "Developer"}'
# This wonk work
# print(dict["name"])
dict = json.loads(some_json)
print(dict["name"])

# dict to json
some_dict = {"name" : "Shashikamal R C", "job": "Developer"}
print(some_dict)
json_data = json.dumps(some_dict)
print(json_data)

'''
Problem Statement : To pretty print dictionaries
Developer : Shashikamal R C
'''

import json

dict = {"name" : "Shashikamal R C", "job": "Developer"}

print(json.dumps(dict,indent=4, sort_keys = True))

'''
Problem Statement : To merge two dictionaries
Developer : Shashikamal R C
'''

dict1 = {"one":"one_value", "two" : "two_value"}
dict2 = {"four":"four_value", "three" : "three_value", }

merge_dict = {**dict1, **dict2}

print(merge_dict)

'''
Note : If both dict have same key, then First dict data will be considered.
'''

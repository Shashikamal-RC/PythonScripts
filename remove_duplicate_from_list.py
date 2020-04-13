'''
Problem Statement : To remove duplicates from list
Developer : Shashikamal RC
'''

list_data = [1,3,5,7,9,3,5, "shashi"]
print("with duplicates : ", list_data)

def remove_duplicate(list_data):
    new_list = []
    [new_list.append(item) for item in list_data if item not in new_list]
    return new_list

distinct_list = remove_duplicate(list_data)
print("Without duplicates : ", distinct_list)

'''
Problem Statement : To make a Python dictionary to be accessible with dot (.) operator
Developer : Shashikamal  R C
'''

class MakeDotAccess(dict):
    ''' dot notation access to dictionary attributes'''
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delatte__ = dict.__delitem__

example_dict = { "name" : "shashkamal",
                 "job" : "developer"
               }
#this will work
print(example_dict['name'])

#this won't work
#print(example_dict.name)

#make dot notation accessible
doc_access_dict = MakeDotAccess(example_dict)

#now this will work
print(doc_access_dict.name)
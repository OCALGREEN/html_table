
users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

size = len(users)
list_keys = []



for m in users: # m == every dictionary in the list User
    for k in m: # k == every key in the each dictionary
        print(m['first_name']) # m[k] == every value for every key

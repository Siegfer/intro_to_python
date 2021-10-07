# Making an empty dictionary
Dict = {}
print(Dict)
# => {}

# Adding elements one at a time
Dict[0] = 'Hello'
Dict[2] = 'World'
Dict[3] = 1
print(Dict)
# => {0: 'Hello', 2: 'World', 3:1}

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print(Dict)
# => {0: 'Hello', 2: 'World', 3:1, 'Value_set': (2,3,4)}

# Adding Nested Key value to Dictionary
five = 5
Dict[five] = {'Nested': {'1': 'Goodbye', '2': 'Friends'}}
print(Dict)

for key in Dict:
    print(Dict[key])

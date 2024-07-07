# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'Canada':'Ottawa',
            'UK':'London',
            'China':'Beijing'}

print(capitals['USA'])
print(capitals.get('germany')) # we're using get() so that if the entered key is not present in the dictionary, it'll print none

print(capitals)
print(capitals.keys())
print(capitals.values())
capitals.pop('USA')
print(capitals.items())
capitals.update({'Pakistan':'Islamabad'})

for keys, values in capitals.items():
    print(keys, values)

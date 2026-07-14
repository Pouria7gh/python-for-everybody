cabinet = dict()
cabinet['summer'] = 2
cabinet['winter'] = 4
cabinet['fall'] = 3
print(cabinet)
print(cabinet['fall'])

keys = cabinet.keys()
for key in keys :
    print(key)

values = cabinet.values()
for value in values :
    print(value)

### dictionary constant ###

jjj = {'Chuck': 1, 'fred': 2, 'jan': 100}
print(jjj)
ooo = {}
print(ooo)

### counting with dictionaries ###

names = ['pouria', 'ali', 'pouria', 'sare', 'ali']
counts = dict()

# for name in names :
#     if name not in counts :
#         counts[name] = 1
#     else :
#         counts[name] = counts[name] + 1

for name in names :
    counts[name] = counts.get(name, 0) + 1

print(counts)

for key in counts : print(key, counts[key])

print(counts.items())

for key,value in counts.items() :
    print(key, value)
d=dict({'abc':12,'nepal':13})
print(d)

#dict([()()()])

d1=dict([('Steve',4987),('Harry',7895)])
print(d1)

d2={x:x**2 for x in (2,4,6)}
print(d2)

d3={x:y for x in ('Hari','Ram') for y in (1,2)}
print(d3)

for key,value in d.items():
    print(key,value)

for index,key in enumerate(d):
    print(index,key)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

value=d.get('nepal','Key is not in the dictionary d!')
print(value)

print(d)
#dictionary.pop(key,default)
val=d.pop('nepal',"Key not found!")
print(val)

print(d)

print(d2)
val1=d2.popitem()
print(d2)
#DELETING ENTIRE DICT
d2.clear()
print(d2)

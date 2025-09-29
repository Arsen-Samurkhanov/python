sammy = {'username': 'sammy-shark', 'online': True, 'follower': 987}
print(sammy)

print(type(sammy))

print(sammy['username'])

print(sammy.keys())

print(sammy.values())

for key, value in sammy.items():
    print(key, value)

sammy.update({'color': 'red'})
print(sammy) 

sammy.update({'color': 'green'})
print(sammy)

del sammy['color']
print(sammy)

sammy.clear()
print(sammy)

del sammy
#print(sammy)
sammy = {'username': 'sammy-shark', 'online': True, 'follower': 987}
print(sammy)

print(type(sammy))

print(sammy['username'])

print(sammy.keys())

print(sammy.values())

for key, value in sammy.items():
    print(key, value)
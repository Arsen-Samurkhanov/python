fish = ['barracuda', 'cod', 'devil ray', 'eel']
print(fish)

fish.append('flounder')
print(fish)

fish.insert(0, 'anchovy')
print(fish)

more_fish = ['goby', 'herring', 'ide', 'kissing gourami']
fish.extend(more_fish)
print(fish)

fish.remove('kissing gourami')
print(fish)
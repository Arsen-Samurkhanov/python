shark_letters = [letter for letter in 'shark']
print(shark_letters)


shark_letters = []
for letter in 'shark':
    shark_letters.append(letter)
print(shark_letters)    
print('\n')

fish_tupl = ('blowfish','clownfish', 'catfish', 'octopus')
fish_list = [fish for fish in fish_tupl if fish != 'octopus']
print(fish_list)
print('\n')

number_list = [x for x in range(10)]
print(number_list)

number_list = [x for x in range(10) if x % 2 ==0 ]
print(number_list)

number_list = [x**2 for x in range(10)]
print(number_list)

# List numbers devided by 2 and 5
number_list = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(number_list)




lstudents = [
    ['john', 23, 'tampa'],
    [['jane','doe'], 29, 'brooklyn'],
    ['david', 25, 'jersey city'],
    ['raj', 27, 'dallas']
]
print('information:', lstudents[1][0][0])
print('information:', lstudents [1][0][1])

student6 = {'name': 'raj', 'age': 27, 'location': 'dallas'}
print(student6)
print(f"name of the student:{student6 [ 'name'].title()}")
print(f"age of the student:{student6 [ 'age']}")
print(f"location of the student:{student6 [ 'location'].title()}")
student6['age'] = 30
student6['last_name'] = 'petel'
print(student6)
print(f"{student6 ['name'].title()} {student6 ['last_name'].title()} is {student6 ['age']} yaers old.")

print(f'\nDictionary examples from book')
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['point'])
print(f"You just earned {alien_0['point']} points!")
alien_0['position'] = 25
alien_0['day'] = 'tuesday'
print(alien_0)
print(f"His position is {alien_0['position']} and he plays every {alien_0['day'].title()}s.")
del alien_0['day']
print(f'After deleting day {alien_0}')

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment= 1
elif alien_0['speed'] == 'medium':
    x_increment =2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print( f"New position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'
alien_0['x_position'] = alien_0['x_position'] + x_increment
print( f"New position: {alien_0['x_position']}")
alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
del alien_0['point']
print(alien_0)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print(favorite_languages['sarah'])
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

alien_0 = {'color': 'green', 'point': 5}
speed_value = alien_0.get('speed', 'No speed value assigned.')
print(speed_value)
print(f'\nLOOPING DICTIONARIES')
# looping all key value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
print(user_0)
for key, value in user_0.items():
    print(f"\tkey: {key}")
    print(f"\tvalue: {value}")
for k, v in user_0.items():
    print(f"key: {k}")
    print(f"value: {v}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for k,v in favorite_languages.items():
    print(f'\tkey: {k}')
    print(f'\tvalue: {v}')

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping all keys
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'Hi {name.title()}.')
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'Hi {name.title()}.')
    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_languages[name].title()}!")

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for value in favorite_languages.values():
    print(value.title())

for value in set(favorite_languages.values()):
    print(f'\n{value.title()}')
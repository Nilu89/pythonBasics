print(f'6.1 Dictionaries, Person')
my_friend = {'name': 'nargiza', 'lastname': 'ikramova', 'age': 35, 'city': 'tashkent'}
print(my_friend)
print(f'\n6.2 Favorite number')
favorite_numbers = {'my': 5, 'husband': 7, 'ziyoda': 4, 'nazmina': 5, 'shahri': 16}
print(favorite_numbers)
print(f'\n6.3 Glossary')
glossary = {'sql': 'database', 'linux': 'server', 'python': 'automation'}
print(glossary)
print(f'\n6.4 Glossary 2')
glossary = {'sql': 'database', 'linux': 'server', 'python': 'automation'}
for k, v in glossary.items():
    print(f'key: {k.title()}')
    print(f'value: {v.title()}')
glossary = {
    'sql': 'database',
    'linux': 'server',
    'python': 'automation',
    'java': 'automation',
    'russian': 'russia',
    'english': 'USA',
    'spanish': 'mexico',
    'uzbek': 'uzbekistan'
}
for k, v in glossary.items():
    print(f'\tkey: {k.title()}')
    print(f'\tvalue: {v.title()}')
print(f"\n6.5 Rivers")
rivers = {'nile': 'egypt', 'amazon river': 'south america', 'mississippi': 'north america'}
for k, v  in rivers.items():
    print(f"The {k.title()} flows through {v.title()}.")
for name in rivers.keys():
    print(name.title())
for country in rivers.values():
    print(country.title())
print(f'\n6.6 Polling')
favorite_languages = {
    'nilufar': 'python',
    'shahri': 'german',
    'nazmina': 'spanish',
    'ziyoda': 'russian',
    'maruf': 'arabic',
    'mehri': 'arabic'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

people = ['nazmina', 'maruf', 'azimjon']

for name, language in favorite_languages.items():
    print(f"{name.title()}, you should take the {language.title()}.")

    if name in people:
        print(f"\t{name.title()}, thank you for your response. I invite you to take the {language.title()} as soon as possible.")
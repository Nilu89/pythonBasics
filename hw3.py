print(3.1)
name = ['John', 'Rose', 'Caitlin']
print(name)
print(name[1].upper())
print(3.2)
message = (f'Hi {name[1]}, how are you doing?')
message1 = (f'I am good {name[2]}, what about you?')
message2 = (f'My friend {name[-1].title()} is interested me to study in this class and to find a job.')
message3 = (f'I am fine also, I am studying hard and I cannot spend time to my family.')
print(message)
print(message1)
print(message2)
print(message3)
print(3.3)
cars = ['toyota corolla', 'sienna', 'jeep', 'honda', 'caravan']
print(cars)
message = (f'My dream was owning large capacity car, and last year, my dream became a reality. My husband bought me {cars[1].upper()}. Thanks, my darling.')
print(message)
cars.append('sedona')
cars.append('nexia')
print(cars)
cars.insert(0, 'corolla')
print(cars)
del cars[1]
print(cars)
# listdagi oxirgi valueni olish
popped_cars = cars.pop()
print(cars)
# olingan valueni uzini korsatish
print(popped_cars)
#Making sentence
print(f'The last car {popped_cars.title()} is my first car.')
# removing an item by value
cars.remove('jeep')
print(cars)
# Printing reason for removing
too_expensive = 'caravan'
#which value too remove from the list
cars.remove(too_expensive)
print(cars)
#but it still accessible to print with too_expensive or reason
print(f'\nA {too_expensive.title()} is too expensive for me.')
print(3.4)

guests = ['Nilufar_opa', 'Muxlisa', 'Feruza', 'Oydin']
print(guests)
message = f'\n\t{guests[0].title()} I invite you to come to my house tomorrow at 10 am. We will enjoy talking.'
print(message)
message1 = f'\n\t{guests[1]} I invite you to come to my house tomorrow at 10 am. We will enjoy talking.'
print(message1)
message2 = f'\n\t{guests[2]} I invite you to come to my house tomorrow at 10 am. We will enjoy talking.'
print(message2)
message3 = f'\n\t{guests[-1]}, could you come to us to help me today because I invited my friends to come tomorrow to have a breakfast.'
print(message3)
print(3.5)
guests.append('Etibor')
print(guests)
guests.remove('Oydin')
print(guests)
message = f'\n\t{guests[-1]} I would like to invite you tomorrow at 10 am to my house.'
print(message)
print(3.6)
print(guests)
guests.insert(0, 'Zaynura_opa')
guests.insert(3,'Farangiz')
guests.append('Rayhon_opa')
print(guests)
message = f'\n\tHi {guests[1]}, I found larger dinner table, so I would like to invite 3 more people. Could you come to my house the day after tommorrow at noon?'
print(message)
message1 = f'\n\tHi {guests[0]}, I invite you to my house the day after tommorrow at noon.'
print(message1)
message2 = f'\n\t{guests[2]}, could you come to us the day after tomorrow at noon? If you can please, come earlier.'
print(message2)
message3 = f'\n\t{guests[3]}, I invite you to my house the day after tomorrow. Bring your mom. I will also call her myself.'
print(message3)
message4 = f'\n\tHi {guests[4]}, do you have time on this Thursday? I invite you to my house not tomorrow, but on Thursday at noon because I found bigger table, so I would like to invite others also.'
print(message4)
message5 = f'\n\tHi {guests[5]}, I invite you to my house on Thursday at 12pm.'
print(message5)
message6 = f'\n\tHello {guests[-1]}, I invite you to my house on Thursday at 12pm, I told to Farangiz also. We will be waiting for you, come together.'
print(message6)

print(3.7)
print(guests)
popped_guest = guests.pop(0)
print(guests)
message = f'\n\tHi {popped_guest}, I am sorry, I cannot wait guests on Thursday.'
print(message)
popped_guest1 = guests.pop(2)
message1 = f'\n\tHi {popped_guest1[1]}, I am sorry, I cannot wait guests on Thursday. I will call again later.'
print(message1)
guests = ['Nilufar_opa', 'Muxlisa', 'Feruza', 'Etibor', 'Rayhon_opa']
print(guests)
popped_guest2 = guests.pop(-2)
message2 = f'Hi {popped_guest2[-2]}, I am sorry, I will invite later. I have some plans on that day.'
print(message2)
popped_guest3 = guests.pop(-1)
print(guests)
message3 = f'\n\t Hi {popped_guest3[-1]}, I am sorry, I will invite later.'
print(message3)
message4 = f'\n\tHi {guests[-1]}, I am sorry, I will invite you later.'
print(message4)
popped_guest4 = guests.pop(-1)
print(guests)
message5 = f'{guests[0]}, I will wait for you on Thursday at 12pm.'
print(message5)
message6 = f'{guests[1]}, Come to my house on Thursday at 12pm, we will hangout.'
print(message6)
del guests[0]
print(guests)
del guests[0]
print(guests)
print(3.8)
places = ['Hawai', 'Dubai', 'New_York', 'Makka', 'Japan']
print(places)
print(sorted(places))
print(f'\nHere is the original order:')
print(places)
print(f'\nHere is the sorted list:')
print(sorted(places))
print(f'\nHere is the reverse list:')
places.reverse()
print(places)
print(f'\nHere is the original order:')
places.reverse()
print(places)
print(f'\nHere is the sorted by alphabetical order:')
places.sort()
print(places)
print(f'\nHere is the sorted by reverse-alphabetical order:')
places.sort(reverse=True)
print(places)
print(f'\n3.9')
guests =  ['Nilufar_opa', 'Muxlisa', 'Feruza', 'Oydin']
print(guests)
print(len(guests))
print(f'\n3.10')
languages =['english', 'uzbek', 'russian', 'spanish', 'french']
print(languages)
languages.insert(1, 'german')
print(languages)
languages.append('arabic')
print(languages)
del languages [1]
print(languages)
languages.pop(1)
print(languages)
popped_language = 'uzbek'
print(popped_language)
print(f'My native language is {popped_language}.')
languages.sort()
print(languages)
languages.reverse()
print(languages)
print(len(languages))

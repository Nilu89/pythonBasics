cars = ['toyota', 'lexus', 'tesla', 'bmw']
print(cars)
for car in cars:
    print(f'In this iteration car = "{car}".')
    if car == 'tesla':
        print(f'My favorite car is {car.upper()}')
    elif car == 'bmw':
        print(F'Oh man, {car.upper()} is something right?!')
    else:
        print(f'Your current car is {car.title()}.')
print('-----------------------')
if True:
    print(f'\nhello')
nums = [4,2, 51, 10, 6,5]
if 5 in nums:
    print('5 is in the list')
elif 6 in nums:
    print('6 is in the list')
else:
    print('5 or 6 are not in the list')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print(True)
if 'pepperoni' in requested_toppings:
    print(False)
    'onions'

print(f'\n If Statement p 78')
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

age = 16
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote!')
    print('Please, register to vote as soon as you turn 18!')


age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote!')
    print('Please, register to vote as soon as you turn 18!')
print(f'\nIf-elif-else chain:')
age = 12
if age < 4:
    print('free')
elif age < 18:
    print('The cost is $25')
else:
    print('The cost is $40')

age = 12
if age < 4:
    price=0
elif age < 18:
    price=25
elif age < 65:
    price = 20
else:
    price=40
print(f'Your admission cost is ${price}.')
print(f'\nTesting multiple conditions')
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('add mushrooms')
if 'extra cheese' in requested_toppings:
    print('add extra cheese')
if 'cheese' in requested_toppings:
    print('add cheese')
print('Pizza is ready!')
goals = ['IT', 'job', 'russian', 'arabic', 'Koran' ]
if 'IT' in goals:
    print('learn')
if 'russian' in goals:
    print('great')
if 'Koran' in goals:
    print('good luck')
print('Great goals!')
print(f'\n Using if statement with lists')
toppings = ['mushroom', 'onion', 'pepper', 'beef']
for topping in toppings:
    print(f'Adding {topping}.')
kids = ['Shahri', 'Nazmina', 'Ziyoda', 'Azimjon']
for kid in kids:
    if kid == 'Azimjon':
        print('Azimjon is our only son. He is 3 years old.')
    else:
        print(f'{kid} is our child!')

supplies = ['pen', 'pencil', 'notebook', 'folder', 'paper']
for supply in supplies:
    if supply == 'paper':
        print('Sorry, we are out of paper.')
    else:
        print(f'{supply.title()} is enough for our class.')

print(f'\nChecking that a list is not empty')

ingredients = ['milk', 'sugar', 'flour', 'egg']
for ingredient in ingredients:
    if ingredient == 'sugar':
        print(f'Add {ingredient}.')
    else:
        print('Is it possible?')

ingredients = []
if ingredients:
    for ingredient in ingredients:
        print(f'add {ingredient}.')
    else:
        print('Is it possible?')

supplies = []
if supplies:
    for supply in supplies:
        print(f'Add {supply}.')
else:
    print('Are you sure?')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'extra cheese', 'french fries']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print('\nPizza is ready!')

my_kids_names = ['Shahri', 'Nazmina', 'Ziyoda', 'Azimjon']
friends_kids_names = ['Shahri', 'Pari', 'Umar', 'Ziyoda']
for friends_kids_name in friends_kids_names:
    if friends_kids_name in my_kids_names:
        print(f'{friends_kids_name} is our daughters name.')
    else:
        print(f'{friends_kids_name} is new name.')
nums = [8, 9, 56, 45, 3, 90]
if 3 in nums:
    print('3 in the list.')
if 90 in nums:
    print('90 in the list.')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car =='subaru')
print("\nIs car =='audi'? I predict False.")
print(car == 'audi')
print (f'\nHomework 5.1 Conditional tests.')
print(f'\n1')
car = 'toyota'
print("Is car == 'toyota'? I predict True.")
print(car =='toyota')
print("\nIs car =='audi'? I predict False.")
print(car == 'audi')
print(f'\n2')
age_0 = 22
print("If age_0 == 22? I predict True.")
print(age_0 == 22)
print("\nIf age_0 == 18? I predict False.")
print(age_0 == 18)
print(f'\n3')
color = 'black'
print("If color == black? I predict True.")
print(color == 'white')
print("\nIf color == white? I predict False.")
print(color == 'black')
print(f'\n4')
color = 'black'
print(color == 'white')
print(color == 'blue')
print(color == 'black')
print(f'\n5')
my_car = 'sienna'
print(my_car == 'corolla')
print(f'\n6')
my_cup_color = 'blue'
print(my_cup_color == 'blue')
print(f'\n7')
my_country = 'uzbekistan'
print(my_country == 'usa')
print(f'\n8')
state_i_live = 'michigan'
print(state_i_live == 'michigan')
print(f'\n9')
state_i_live = 'michigan'
print(state_i_live == 'ohio')
print(f'\n10')
my_daughter = 'ziyoda'
print(my_daughter == 'ziyoda')
print(f'\n5.2 More conditional tests.')
print(f'\n1 Equality and Inequality tests')
book = 'Python'
print(book == 'Python')
author = 'Eric Matthes'
print(author == 'Eric Matthes')
author = 'Eric Matthes'
if author != 'Rick Riordan':
    print("This is another author.")
TV = 70
if TV != 55:
    print('We need 55 inches TV.')
TV = 70
print(TV == 55)
print(f'\n2')
Learning_English = 'easy'
print(Learning_English =='easy')
IT_class = 'easy'
print(IT_class == 'hard')
my_car = 'Sienna'
print(my_car == 'sienna')
my_car = 'Sienna'
print(my_car.lower() == 'sienna')
I_am = 'QA analyst'
print(I_am.upper() == 'QA ANALYST')
print(f'\n3 Numerical Comparisons')
my_son = 1
print(my_son == 1)
my_sons_age = 3
print(my_sons_age >= 2)
my_sons_age = 3
print(my_sons_age != 2)
my_sons_age = 3
print(my_sons_age <= 2)
my_sons_age = 3
print(my_sons_age >= 3)
print(f'\n4  and & or')
my_son = 3
my_daughter = 8
print(my_son <= 5 and my_daughter >= 5)
print(my_son <= 8 or my_daughter < 8)
print(f'\n5 an item is in a list')
my_username = ['nilu', 'nilufar', 'nilush']
print('nilu89'in my_username)
print('nilu' in my_username)
print('nilush' in my_username)
print('nilufarxon' in my_username)
print(f'\n5 an item is not in a list')
my_usernames = ['nilu', 'nilufar', 'nilush']
username = 'malika'
print(f'{username.title()}, you can post a response if you wish.')
classes = ['linux', 'sql', 'automation']
lesson = 'chemistry'
if lesson not in classes:
    print("All of them challenged o_o_programming.")
classes = ['linux', 'sql', 'automation']
lesson = 'sql'
if lesson not in classes:
    print("All of them challenged o_o_programming.")
print(f'\n5.3 Alien colors #1')
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('Player get 5 points!')
if 'pink' in alien_color:
    print('Point 0')
print(f'\n5.4 #2')
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('Player get 5 points!')
else:
    print('Player get 10 points!')
print(f'\n5.5 #3')
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print('Player get 5 points!')
elif 'yellow' in alien_color:
    print('Player get 10 points!')
elif 'red' in alien_color:
    print('Player get 15 points!')

alien_color = ['green', 'yellow', 'red']
if 'yellow' in alien_color:
    print('Player get 10 points!')
elif 'green' in alien_color:
    print('Player get 5 points!')
elif 'red' in alien_color:
    print('Player get 15 points!')
print(f'\n5.6 Stages of life.')

age = 22
if age < 2:
    print('Baby')
elif age < 4 and age > 2:
    print('toddler')
elif age < 13 and age > 4:
    print('kid')
elif age < 20 and age > 13:
    print('teenager')
elif age < 65 and age > 20:
    print('adult')
else:
    print('elder')

print(f'\n5.7 Favorite fruit')
favorite_fruits = ['cherry', 'peach', 'pear', 'strawberry', 'orange']
if 'cherry' in favorite_fruits:
    print('I love cherry.')
if 'peach' in favorite_fruits:
    print('I enjoy to eat peach in summer.')
if 'pear' in favorite_fruits:
    print('Pear is delicious')
if 'strawberry' in favorite_fruits:
    print('Strawberries not sweet as before.')

print(f'\n5.8 Hello Admin')
users = ['Nilu', 'admin', 'John', 'Mark', 'Jenna']
for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f"Hello {user}, thank you for logging in again!")
print('We love our users!')
print(f'\n5.9 No users')
users = []
if user:
    for user in users:
        print(f'Hello {user}!')
    else:
        print('We need to find some users.')
print('We love users.')

print(f'\n5.10 Checking usernames')
current_users = ['Nilu', 'Lily', 'John', 'Mark', 'Jenna']
new_users = ['Tin', 'Max', 'Sara', 'Lily', 'John']
for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user}, you will need to enter new username.')
    else:
        print(f'{new_user}, this username is available!')

print(f'\n5.11 Ordinal numbers.')
ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print('1st')
    elif ordinal_number == 2:
        print('2nd')
    elif ordinal_number == 3:
        print('3rd')
    else:
        print(f'{ordinal_number}th')
print('Ordinal_numbers are ready!')

print(f'\n5.12 Styling if statements')
print("I styled my all if statemaents appropriately.")

print(f'\n5.13 Your ideas')
colleges = ['Nilufar', 'Zilola', 'Malika', 'Vosil_aka', 'Holida_opa']
friends = ['Nilufar', 'Muxlisa', 'Feruza']
for friend in friends:
    if friend in colleges:
        print(f'{friend}, is the popular name.')
    else:
        print(f"{friend}'s family are our nowadays family friend!")

educations = ['pre-k', 'school', 'college', 'university']
if 'school' in educations:
    print('All kids from age 5 to 16 must go to school.')
if 'pre-k' in educations:
    print('Age 0-5 children eligible to go to pre-k.')
if 'college' and 'university' in educations:
    print('All other children are able to go to colleges or universities.')

kids_party_plans = ['pizza', 'cake', 'chips', 'juice']
adults_party_plans = [ 'cake', 'osh','watermelon']
for adults_party_plan in adults_party_plans:
    if adults_party_plan in kids_party_plans:
        print(f"Both parties have same {adults_party_plan}.")
    else:
        print('We hope our guests would be happy!')

cakes = []
if cakes:
    for cake in cakes:
        print(f"Everyone wants to eat {cake}.")
    print('Part is over!')
else:
    print(f"No cakes todays birthday party!")




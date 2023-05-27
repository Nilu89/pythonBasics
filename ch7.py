print(f'7.1 Rental car')
name_car = input("What kind of car would you like to rent?")
print(f"Let me see if I can find you a {name_car}.")
print(f'7.2 Restaurant seating')
people = input('How many people would be in your dinner group?')
people = int(people)
if people >= 8:
    print(f"You'll have to wait for a table.")
else:
    print(f"Your table is ready!")
answer = input('Thank you!')
print(answer)
print(f'7.3 Multiples of ten')

number = ''
while number != -1:
    number = input('Give me the number I will tell you if it is multiple of 10.')
    if number == '':
        print(f'The number {number} is not multiple of 10.')
        print(f'The number {number} is a multiple of {int(number)/10}.')


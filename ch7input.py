message = input("Tell me something, and I will repeat it back to you:")
print(message)
name = input("Please, enter your name: ")
print(f"\nHello, {name}!")
prompt = 'If you share your name, we can personalize the messages you see.'
prompt += '\nWhat is your last name?'
name = input(prompt)
print(f'\nHello, {name}!')
age = input("How old are you?")
age = int(age)
age >= 18
height = input('How tall are you, in inches?')
height = int(height)
if height >= 48:
    print('You are tall enough to ride!')
else:
    print("You'll be able to ride when you are little older." )

number = (input('Enter a number and I will tell you if it is even or odd.'))
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

print(f'####################################################')





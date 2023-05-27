print(f'7.4 Pizza toppings')
prompt = "\nWhat toppings do you want to put your pizzas?"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f'You will add that topping to your pizza.')
print(f'#############################')
print(f'7.5 Movie tickets')
age = input("How old are you?")
age = int(age)
if age <= 3:
    print('Your ticket is free.')
elif age in range(3,13):
    print('Your ticket is $10.')
else:
    print('Your ticket is $15.')
print(f'7.6 Three Exits')
prompt = "\nWhat toppings do you want to put your pizzas?"
prompt += "\nEnter 'quit' to end the program."

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f'You will add that topping to your pizza.')
print(f"###################")
prompt = "\nWhat toppings do you want to put your pizzas?"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f'You will add that topping to your pizza.')
print(f"####################")
#This counting loop count from 1 to 21.
pen = 1
while pen <= 21:
    print(pen)
    pen +=3
# This loop will run forever to stop it Ctrl C
#pen = 1
#while pen <= 21:
 #   print(pen)
#This is to me to understand how continue works
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
print(f'7.8 Deli')
sandvich_orders = ['beef', 'chicken', 'veggie']
finished_sandviches = []
while sandvich_orders:
    sandvich = sandvich_orders.pop()
    print(f"Preparing sandviches: {sandvich} sandvich.")
finished_sandviches.append(sandvich)
print(f"\nThe following sandviches have been made:")
for finished_sandvich in finished_sandviches:
    print(finished_sandvich)

print(f"7.9 No Pastrami:")

sandvich_orders = ['pastrami', 'beef', 'pastrami', 'chicken', 'veggie', 'pastrami']
print(sandvich_orders)
finished_sandviches = []

while 'pastrami' in sandvich_orders:
    sandvich_orders.remove('pastrami')
    print(f"Deli has run out of pastrami.")

    finished_sandviches.append(sandvich_orders)
print(f"\nThe following sandviches have been made:")
for finished_sandvich in finished_sandviches:
    print(finished_sandvich)

print(f"7.10 Dream vacation")
responses = {}
polling_active = True
while polling_active:
    name = input(f"\nWhat is your name?")
    response = input("\nIf you could visit one place in the world, where would you go?")

    responses[name] = response
    repeat = input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False
print("\n----Results----")
for name, response in responses.items():
    print(f"{name.title()} would like to go {response} for vacation.")
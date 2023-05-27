# 4/23/2023 Chapter 7: While Loop
# while loop - looping with conditions
# Note: you need to increment/decrement or make sure there is ending condition for the while loop
# total < boundary value in a while loop

current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1
print(f'###########')
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 2
print(f'###########')
current_number = 10
while current_number >= 3:
    print(current_number)
    current_number -= 2
print(f'###########')
prompt = "Tell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program."

message = ""
#while message != 'quit':
#    message = input(prompt)
  #  if message != 'quit':
 #       print(message)
print(f'###########')
prompt = "Tell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program."

active = True
while active:
    #message = input(prompt)

    #if message == 'quit':
        active = False
   # else:
       # print(message)
print(f'########################')
prompt = "\nPlease enter the name of a city you have viaited:"
prompt += "\n(Enter 'quit' when you are finished.)"
#while True:
#    city = input(prompt)
  #  if city == 'quit':
#        print('quit')
 #else:
#        print(f"I have been in the city of {city.title()}.")
print(f'###########################')
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


#From videos youtube
name = input("What is your name?")
while name == '':
    print("You did not enter your name.")
    name = input("What is your name?")
print(f"Hello, {name}!")

age = int(input('How old are you?'))
while age < 0:
    print("Age can't be negative.")
    age = int(input('How old are you?'))
print(f"You are {age} years old.")

goal = input('What is your goal?')
while goal == '':
    print('You did not enter any information about your future goal.')
    goal = input('What is your goal?')
print(f"I wish you good luck to come true your goal.")

food = input("What is you favorite food(q to quit):")
while not food == "q":
    print(f"You like {food}.")
    food = input("What is you favorite food(q to quit):")
print("bye.")

num = int(input("Enter a # between 1-10:"))
while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a # between 1-10:"))
print(f"Your number is {num}.")


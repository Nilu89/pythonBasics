# Chapter 9
# self keyword used to show that functions and variables are belong to class
def sample():
    pass

class Dog:

    def __init__(self, name, breed,  age, color):
        # This is class constructor.
        self.breed = breed
        self.age = age
        self.name = name
        self.color = color

    #behavior

    def bark(self):
        print('Dog is barking')
        print(f"Statement inside the class, age: {self.age}")

    def run(self):
        abc = self.name
        print(f'{abc} is running fast......')
        self.bark()

dog1 = Dog('Roxi', 'husky', 3, 'black/white')
#dog1.name = 'Roxi'
#dog1.breed = 'husky'
#dog1.age = 3
#dog1.color = 'black/white'
print(f"name of the dog is {dog1.name}.")

dog2 = Dog('Flower', 'bulldog', 4, 'brown')
dog2.name = 'Flower'
dog3 = Dog('Meli', 'doberman', 1, 'black/brown')
dog3.name = 'Melis'

print("**********Behavior of the dog: dogs are running.")
dog1.run()
dog2.run()
dog3.run()


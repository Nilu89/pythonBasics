class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over.")

class Dog:

    my_dog = Dog('Willie', 6)
    print(f"My dog's name is {my_dog.name}.")
    print(f"My dog is {my_dog.age} years old.")

    my_pet = Dog('Reks', 10)
    print(f"The {my_pet.name} was lived with us in my homecountry.")
    print(f"{my_pet.name} was {my_pet.age} years old in 2018.")

    my_dog.sit()
    my_dog.roll_over()
    my_pet.sit()
    my_pet.roll_over()
    print('*********************************')
    class Dog:

        my_dog = Dog('Willie', 6)
        your_dog = Dog('Lucy', 3)
        print(f"My dog's name is {my_dog.name}.")
        print(f"He is {my_dog.age}.")
        print(f"Your dog's name is {your_dog.name}.")
        print(f"He is {your_dog.age}.")
        my_dog.sit()
        your_dog.roll_over()








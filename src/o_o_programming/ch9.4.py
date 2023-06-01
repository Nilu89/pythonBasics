print(f'9.4. Number served')


class Restaurant:
    pass

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_rest(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"This restaurant's cuisine_type is {self.type}.")

    def open_rest(self):
        print(f"{self.name} is open.")
        print(f"{self.number_served} number of customers the {self.name} has served.")

    def set_number_served(self):
        print(f"The {self.name} have been served {self.number_served} customers.")

    def increment_number_served(self):
        print(f"The {self.name} restaurant served {self.number_served} customers on May 31, 2023. It means customers number have been incremented.")


class Restaurant:
    new_restaurant = Restaurant('Galata', 'turkish')
    new_restaurant.describe_rest()
    new_restaurant.open_rest()
    new_restaurant.number_served = 12
    new_restaurant.set_number_served()
    new_restaurant.number_served = 30
    new_restaurant.increment_number_served()
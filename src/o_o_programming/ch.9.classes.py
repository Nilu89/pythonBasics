print(f'9.1 Restaurant')


class Restaurant:
    pass

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_rest(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"This restaurant's cuisine_type is {self.type}.")

    def open_rest(self):
        print(f"{self.name} is open.")


class Restaurant:
    new_restaurant = Restaurant('Galata', 'turkish')
    new_restaurant.describe_rest()
    new_restaurant.open_rest()


print(f'\n9.2 Three restaurants')


class Restaurant:
    pass

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_rest(self):
        print(f"The name of the restaurant is {self.name}.")
        print(f"This restaurant's cuisine_type is {self.type}.")

    def open_rest(self):
        print(f"{self.name} is open from 8am to 10pm.")


class Restaurant:
    uzbekistan = Restaurant("Tandir", "Uzbek")
    greece = Restaurant("Athens", "Greek")
    uzbekistan.describe_rest()
    uzbekistan.open_rest()
    greece.describe_rest()
    greece.open_rest()


print(f"\n9.3 Users")


class User:
    pass

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"My name is {self.first_name}. My last name is {self.last_name}.")

    def greet_user(self):
        print(f"Hello {self.first_name}!")
        print(f"Nice to meet you!")


class User:
    name = User('Lily', 'Shodieva')
    name.describe_user()
    name.greet_user()







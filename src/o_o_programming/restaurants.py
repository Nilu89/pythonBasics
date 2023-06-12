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



uzbekistan = Restaurant("Tandir", "Uzbek")
greece = Restaurant("Athens", "Greek")
uzbekistan.describe_rest()
uzbekistan.open_rest()
greece.describe_rest()
greece.open_rest()











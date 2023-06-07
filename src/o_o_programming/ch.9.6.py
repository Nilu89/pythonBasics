print(f"9.6-IceCreamStand (Inheritance)")
class Restaurant:
    pass

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_rest(self):
        print(f"\nThe name of the restaurant is {self.name}.")
        print(f"This restaurant's cuisine_type is {self.type}.")

    def open_rest(self):
        print(f"{self.name} is open.")

new_restaurant = Restaurant('Galata', 'turkish')
new_restaurant.describe_rest()
new_restaurant.open_rest()


class IceCreamStand(Restaurant):

    def __init__(self, name, type, flavors):
        super().__init__(name, type)
        self.flavors = flavors

    def icecream(self):
        print(f"The flavor is {self.flavors}.")
        print(f"We have only {self.flavors} flavor icecream left for today.")

ice_flavor = IceCreamStand('Tandoor', 'uzbek', 'chocolate')
print(ice_flavor.describe_rest())
ice_flavor.open_rest()
ice_flavor.icecream()

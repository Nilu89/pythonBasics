class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #setting default value to an attribute
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # setting default value to an attribute
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    #modifying attributes value through a method
    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # incrementing an attribute through method
    def increment_odometer(self, miles):
        self.odometer_reading += miles




class Battery:
    def __init__(self, battery_size=40):    # 1  Instances as attributes (we break large class into smaller - COMPOSITION
        self.battery_size = battery_size

    def describe_battery(self):             # 2 'describe_battery' method moved to this class so we don't need it on ElectricCar class. We need only init method in Electr class.
        print(f"This car has a {self.battery_size}-kwh battery.")

    def upgrade_battery(self, battery_size=65):
        self.battery_size = 65

    def get_range(self):            # Adding another method to Battery class
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

    print(f"This car can go about {range} miles on a full charge.")






# Inheritance. init method for child class
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year) #super is also function to call parent class
        self.battery_size = 40  # defining attribute and methods for child class 1
        self.battery = Battery()        # 3

    #defining attributes and methods for child class 2
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    # overriding methods from the parent class
    def fill_gas_tank(self):
        print("This car doesn't have gas tank!")

    def get_descriptive_name(self):
        print(f"new description: \n{self.battery_size} kWh")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()          # 4
my_leaf.battery.get_range()
my_leaf.get_descriptive_name()

my_leaf1 = ElectricCar('toyota', 'sienna', 2022)
print(my_leaf1.describe_battery())
my_leaf1.battery.upgrade_battery()
my_leaf1.battery.get_range()
my_leaf.battery.get_range()

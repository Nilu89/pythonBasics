# In this file We want to have a definition only (Classes)
class Car:
    """Blueprint to represent the general Car."""

    # Constructor
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0  # default value # hidden attribute from object, private
        # private this.odometer_reading = 0  in java

    # How to restrict object updating attributes directly, so we can only set odometer using the function
    # OOP concept - encapsulation, hide the attributes from the object (or child classes)
    # access modifier in java -> private

    def get_description(self):
        """summary of the car details, usually you have return statement"""
        print(f"Details of the car\n\tMake/model/year: {self.__make.title()}/{self.__model.upper()}/{self.__year}")

    # Polymorphism, method overloading is not allowed
    # def get_description(self, name):
    #     print(name)

    def get_odometer(self):
        return f'Current milage: {self.__odometer_reading}'

    def set_odometer(self, milage):
        """Updates the odometer reading to given milage."""
        print('updating the odometer reading ... ')
        if milage > self.__odometer_reading:
            self.__odometer_reading = milage
        else:
            print(f'invalid milage was entered for the odometer! value entered: {milage}')

    def increment_odometer(self, miles: int):
        """Adds trip miles to your overall milage of the car."""
        print(f'adding {miles} miles to your odometer reading...')
        # self.__odometer_reading = self.__odometer_reading + miles
        if miles > 0:
            self.__odometer_reading += miles
        else:
            print(f'miles should be positive number. value entered: {miles}')


# ElectricCar class is inheritting Car class (attributes and behaviour)
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    # when we dont have constructor (__init__ method) in the child class, parent class constructor is executed
    def __init__(self, make, model, year, battery_size=100):
        super().__init__(make, model, year)
        self.battery_size = battery_size  # in kWh (with default value)
        # battery_size is child class attribute only

    def describe_battery(self):
        print(f"Your current vehicle battery size: {self.battery_size}")

    def get_description(self):
        """New function for the Electric car, gives more details."""
        super().get_description()
        print(f"\tBattery size: {self.battery_size}")

car1 = Car('toyota', 'highlander', 2023)
car1.get_description()
# print(car1.model)  # you can do before hiding, after hiding you have use get_description() method
# print('car1.odometer_reading:', car1.__odometer_reading)
print('--------')
print(car1.get_odometer())
car1.set_odometer(10000)  # testing the set_odometer
print(car1.get_odometer())
# car1.odometer_reading = 5000  # does the same job as car1.set_odometer(), when function does not have a logic

print(car1.get_odometer())
car1.set_odometer(1000)  # testing the set_odometer
print(car1.get_odometer())
car1.set_odometer(20000)  # testing the set_odometer
print(car1.get_odometer())
car1.increment_odometer(50)  # testing the increment_odometer
print(car1.get_odometer())
# car1.increment_odometer('a')
car1.increment_odometer(-50)  # testing the increment_odometer
print(car1.get_odometer())

print('****** creating the electric car object...')
tesla1 = ElectricCar('tesla', 'X', 2023)
# after adding battery size to __init__ , we can still use 3 argument
# because battery_size was added as optional parameter

tesla1.get_description()
print(tesla1.get_odometer())
print('battery size:', tesla1.battery_size)
# print(car1.battery_size)  # parent does not have this attribute
# car1.describe_battery()  # parent does not have this method
tesla1.describe_battery()

print('-------- tesla 2 ---------------')
tesla2 = ElectricCar('tesla', 'Y', 2021, 90)
tesla2.describe_battery()

print("----- Method Overriding ------")
car1.get_description()
tesla2.get_description()
# h/w: 9-4 (done), 9-5
# h/w: 9-6 to 9-9

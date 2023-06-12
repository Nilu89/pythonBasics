
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


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
#setting default value to an attribute
my_new_car.read_odometer()
#modifying an attributes value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#modifying attributes value through a method
my_new_car.update_odometer(26)
my_new_car.read_odometer()
my_new_car.update_odometer(12)
my_new_car.read_odometer()

# incrementing an attribute through method
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(200)
my_used_car.read_odometer()

from src.o_o_programming.car import Car

from src.o_o_programming.car import Car
from src.o_o_programming.car_classes import ElectricCar

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

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.describe_battery()
my_leaf.get_description()
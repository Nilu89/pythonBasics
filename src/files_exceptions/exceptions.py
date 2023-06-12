# Chapter 10: Exception handling

from src.o_o_programming.car import Car

my_new_car = Car('audi', 'a4', 2024)
try:
    print('my_new_car.get_descriptive_name()',__my_new_car.get_descriptive_name())
    print('***********')
except NameError as error:
    print('NameError was caught')
    print('body of message: {error}.')
print('*****************')
#setting default value to an attribute
my_new_car.read_odometer()
#modifying an attributes value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# In this file We want to have a Execution only ( Objects)
from src.o_o_programming.car_classes import *

# create the object (instance of  Car class)
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

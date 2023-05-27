# Object - abstract data
# Data Structures: list, dictionary, tuple, set
# list - list of values (similar data types)

my_info = ['nilufar', 34, 'uzbekistan', 'four kids', True, '04/15/23']
cities = ['brooklyn', 'manhattan', 'los angelos']

print(my_info)
print(cities)
print(my_info[0])
print(f'First element of my_info list is: {my_info[0]}')
print(f'[First element of my_info list is: {my_info[0].title()}')
print(f'The last element on cities list is: { cities[2].title()}')
print(f'The last element on cities list is: { cities[-1].title()}')
#print(f'{ my_info[0].title() } will be { int(my_info[2] + 5 } years old in 5 years.')

cities.insert(1, 'houston')
print('updated list', cities)

cities[2] = 'new york'
print('updated manhattan:', cities)

print('# add new element to the end of the list (append) -------')
cities.append('seattle')
print(f'new city added to the list: {cities}')
print(f'new city added to the list: {cities[-1]}')
print('index of houston:', cities.index('houston'))
print('counting the elements of cities list:', len(cities))

print(cities)
del cities[0]
print(cities)

print (cities.pop())
print(cities)

cars = ['gentra', 'nexia', 'corolla', 'sienna']
print(cars)
message = (f'My first car is {cars[3].title()}.')
print(message)
#04/16/23
cars = ['lexus', 'bmw', 'tesla', 'toyota']
print (f'cars list: {cars}')
cars.sort(reverse=True)
print(f'sorted cars list with sort(reverse=True): {cars}')
cars.append('honda')
print(f'cars after append')

nums = [4, 23, 6, 0, -11, 4567, 1234]
nums.sort()
#smallest_num2

nums2 = [3, 5, 1, 0, -55, 100]
print(f'original list: {nums2}')
nums2.reverse()
print(f'reversed list: {nums2}')
# P43 .SORT() PERMANENTLY
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
# Alphabetical order
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
#Reverse alphabetical
cars.sort(reverse=True)
print(cars)
# sorted() TEMPORARILY
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)
# Reverse order not alphabetical, it is permanent
cars.reverse()
print(cars)
cars.reverse()
print(cars)
len(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
len(cars)
print(cars)
print(f'cars list: {cars}')
cars.sort()
print(cars)
print(f'cars list: {cars}')
cars.sort(reverse=True)
print(f'reverse sorted cars: {cars}')
print(sorted(cars))
print(f'sorted list with sorted(): {sorted(cars)}')
print(f'sorted reverse: {sorted(cars, reverse=True)}')
print(f'just sorted: {sorted(cars)}')
numbers = [4,9,0,-6,7679,45,356]
numbers.sort()
print(numbers)
print(min(numbers))
print(max(numbers))
print(sorted(numbers, reverse=True))
print(numbers)
numbers.reverse()
print(numbers)
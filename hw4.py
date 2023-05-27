print(4.1)
pizzas =['cheese', 'veggie', 'beef']
for pizza in pizzas:
    print(f'I like {pizza} pizza.')
    print(f'I can eat {pizza} pizza every day!')
    print(f'I really love pizza!')
print(f'\n 4.2')
animals = ['dog', 'cat', 'sheep']
for animal in animals:
    print(animal.title())
    print(f'A {animal} would make a great pet.')
print(f'Any of these animals would make a great pet!')
print(f'\n4.3')
for numbs in range(1,21):
    print(numbs)
print(f'\n4.4')
for numbs in range(1, 1000001):
    print(numbs)
print(f'\n4.5')
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(f'\n4.6')
for odd_numb in range(1,20,2):
    print(odd_numb)
print(f'\n4.7 Threes3-30')
multiples = []
for value in range(3,31):
    multiples.append(value * 3)
print(multiples)
print(f'\n4.8 Cubes 1-10')
cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
print(cubes)
print(f'\n4.9 Cube comprehension')
cubes = [value ** 3 for value in range (1,11)]
print(cubes)
print(f'\n4.10 Slices')
flowers = ['rose', 'tulip', 'phlox', 'begonia', 'lily', 'shrub']
print(flowers)
print(flowers[:3])
print(flowers[1:4])
print(flowers[3:])
print(f'\n4.11 My pizzas')
my_pizzas =['cheese', 'veggie', 'beef']
friend_pizzas = my_pizzas[:]
print('my_pizzas:')
print(my_pizzas)
print('friend_pizzas:')
print(friend_pizzas)
my_pizzas.append('chicken')
friend_pizzas.append('mushroom')
print(f'My favorite pizzas are: {my_pizzas}')
print(f"My friend's favorite pizzas are: {friend_pizzas}")
print(f'\n4.12')

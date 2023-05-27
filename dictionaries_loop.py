print("# Loop with Dictionaries")
student6 = {
    'name': 'raj',
    'age': 27,
    'location': 'dallas'
}
# for var in iterable:
#     code to execute in each loop
# in Dictionary default iteration returns only key, that is why variable you create is for key
for key in student6:
    print(f'element, by default key: {key}')
    print(f'value of the key: {student6[key]}')

print("Making the loop explicitly by keys with keys() function.")
for key in student6.keys():
    print(f'element, by default key: {key}')
    print(f'value of the key: {student6[key]}')

print("Looping through values only with values() function.")
for value in student6.values():
    print(f'value : {value}')

print("Looping through keys and values at the same time with items() function.")
for key, value in student6.items():
    print(f'key: {key}')
    print(f'value : {value}')

# H/W : 6-4, 6-5, 6-6

# H/W on Problem-solving:
# 1. given string input count how many vowels used in the string. (e, a, i, o, u)
    # hello -> 2 (count)
    # count = 0
# 2. given string input count how many times each letter is used. Ignore whitespace(spaces, tabs, enters)
    # helloe -> result={'h':1, 'e':1, 'l':2, 'o':1}
    # loop through input
    # result.setdefault('o', 1)
    # result['o'] = result['o'] + 1
for letter in 'hello':
    print(letter)

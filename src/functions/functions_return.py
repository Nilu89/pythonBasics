def get_full_name(firstname, lastname):
    return f"{firstname} {lastname}".title()

print(get_full_name('john', 'doe'))

def get_full_name(firstname, middlename, lastname):
    return f"{firstname} {middlename} {lastname}".title()
print(get_full_name('john', 'lee', 'doe'))


print(f'\tTo make an optional argument (middlename):')
def get_full_name(firstname,  lastname, middlename= ''):
    if middlename:
        return f"{firstname} {middlename} {lastname}".title()
    else:
        return f"{firstname} {lastname}".title()

print(get_full_name('john', 'doe'))
print(get_full_name('mark', 'twin'))
print(get_full_name('john', 'doe', 'lee'))
print(get_full_name('joshua', 'li', 'yang'))


print(f'\n\tReturning a dictionary')
def build_person(firstname, lastname):
    person = {'first': firstname.title(), 'last': lastname.title()}
    return person
print(build_person('nilufar', 'shodieva'))
print(f'\n\t Adding age')
def build_person(firstname, lastname, age=None):
    person = {'first': firstname.title(), 'last': lastname.title()}
    if age:
        person['age'] = age
    return person
print(build_person('nilufar', 'shodieva', age=23))

print(f"\n\tUsing function with a while loop")

def get_full_name(firstname, lastname):
    return f"{firstname} {lastname}".title()
while True:
    print('\nTell me your name')
    print("(enter 'q' at any time to quit)")
    f_name = input('Firstname: ')
    if f_name == 'q':
        break
    l_name = input('Lastname: ')
    if l_name  == 'q':
        break
formatted_name = get_full_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")

print(f'\nPassing a list')
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
users = ('lily', 'john', 'lee')
greet_users(users)

print(f"\n\tModifying a list in a function")
unp_des = ['phone case', 'robot', 'dodecahedron']
comp_mods= []
while unp_des:
    curr_des = unp_des.pop()
    print(f"Printing model: {curr_des}")
    comp_mods.append(curr_des)
print("\nThe following models have been printed:")
for comp_mod in comp_mods:
    print(comp_mod)

print(unp_des[:], comp_mods)
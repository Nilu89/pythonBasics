print("======= Variables =======")

print('function')
print(4567)
print(45+4588)
print(45*4588)

my_name = 'james bond'
my_age = 25
print('Hello, my name is', my_name)
print('thank you, this was', my_name, 'speaking with you tonight.')
print('if you have a comments, please address it to', my_name)
print('I will be', my_age+5, 'years old in 5 years.')

print('Hello, my name is', my_name.upper())
print('thank you, this was', my_name.title(), 'speaking with you tonight.')
print('if you have a comments, please address it to', my_name.lower)
print('I will be', my_age+5, 'years old in 5 years.')

# Number Variables
print('my_age is:', my_age)
print('division', my_age/5)
print('multiplication', my_age*5)
print('floor division', my_age//7) # 25/7=3.4=3
print('modulo:', my_age % 7) #25/7=3+4 =4 (remainder when you divide 25 to 7)

first_name = 'nilufar    '
last_name = 'shodieva        '
full_name = (first_name.strip() + ' ' + last_name.strip()).title()

print(full_name)

age = 16
age_str = '16' # string, text
print('you are eligible to apply for driving licence when you are ' + age_str)
print('Line 8: dealing with integer:', age + 5)
# print('Line 9: dealing with integer:', age_str + 5)

print(f'after 10 years you will be: {int(age_str)+10}!')
print('after 10 years you will be ' + str(int(age_str)+10) + '!')
print('after 10 years you will be', + int(age_str)+10,'!')

print(f'converting to integer to float: {float(age)}')
print(f"converting to integer to float: {float(age)}")

# Primitive Data types: string, boolean, integer.

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))
message = 'nilufar'
print(message)

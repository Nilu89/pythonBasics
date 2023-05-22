# H/W: FuzzBuzz ./fuzz_buzz.py
# create condition that prints 'Fuzz' if number is dividable by 3,
# returns 'Buzz' if number is dividable by 5, returns 'FuzzBuzz' if the number dividable by 15

# Sample inputs/outputs:
# num = 3  # output 'Fuzz' -> True/False -> Pass/Fail
# num = 27  # output 'Fuzz' -> Pass/Fail
# num = 10  # output 'Buzz' -> Pass/Fail
# num = 30  # output 'FuzzBuzz' -> Pass/Fail
# num = 45  # output 'FuzzBuzz' -> Pass/Fail
# num = 100  # output 'Buzz' -> Pass/Fail
# num = 0  # output 'Not Valid Entry', for any input less than 3 -> Pass/Fail
# num = 'a'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = ''  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = '\t'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail

print('Homework FuzzBuzz')

value = input('enter value:')
if (value >='a' and value <= 'z') or (value >= 'A' and value <= 'Z') or value.strip() == '' or int(value) < 3:
    print('not valid entry')
elif int(value) == 0:
    print('not valid entry')
elif int(value) % 15 == 0:
    print(f'FuzzBuzz')
elif int(value) % 5 == 0:
    print(f'Buzz')
elif int(value) % 3 == 0:
    print(f'Fuzz')
else:
    print(f'entered {value}')

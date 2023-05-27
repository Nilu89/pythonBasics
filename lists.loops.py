# Chapter 4 Looping: Iterative actions

magicians =['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print('hellooo')
    print('hellooo')
    print('hellooo')
magicians =['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see your next trick, {magician.title()}.")
print(f'Thank you, everyone. That was a great magic show!')


print(f'\nUsing Range() function.... p57')
print(f'range(): {list(range(5))}')
print(f'using range in a loop......')
for num in range(16,21):
    print(f'num: {num}')
nums = list(range(101,111))
print(nums)
value = list(range(1,11))
print(value)
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

square = []
for value in range(101,111):
    square.append(value ** 2)
    print(square)

squares = []
for value in range(101,111):
    square = value ** 2
    squares.append(square)
print(squares)

for num in range(101,111):
    print(f'square of {num} is: {num*num}')

squares = [value**2 for value in range (101,111)]

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

nums = [1,2,3,4,5,6,7,8,9]
print(min(nums))
print(max(nums))
print(sum(nums))

squares = [value **2 for value in range(1,11)]
print(squares)

sums = 0
for value in range(55,95):
    sums = sums + value
sums += value
print(sums)

nums = [4,23,5,6,-4,457,478]
print(nums[2:5])
nums_2_end = nums[2:]
print(nums[2:])
nums_start_5 = nums[:5]
print(nums[:5])
nums_copy = nums[:]
print(nums[:])
print(f'nums_copy: {nums[:]}')
print(f'nums_copy2: {nums}')
print(f'original_nums: {nums}')
nums_copy.append(567)
print(nums_copy)
nums.append(789)
print(f'nums_copy_after: {nums[:]}')
print(f'nums_copy2_after: {nums}')
print(f'original_nums_after: {nums}')

letters = ['a', 'b', 'c']
for letter in letters:
    print(letter)



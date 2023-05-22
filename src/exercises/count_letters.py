# H/W on Problem-solving:
# 1. given string input count how many vowels used in the string. (e, a, i, o, u)
    # hello -> 2 (count)
    # count = 0
# 2. given string input count how many times each letter is used. Ignore whitespace(spaces, tabs, enters)
    # helloe -> result={'h':1, 'e':1, 'l':2, 'o':1}
    # loop through input
    # result.setdefault('o', 1)
    # result['o'] = result['o'] + 1

input_text = input('enter any word:').lower()
vowel_count = 0
for letter in input_text:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowel_count = vowel_count + 1
print(f'number of vowels are: {vowel_count}')
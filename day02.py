letter = input('Input alphabet letter : ')
# vowels = {'a', 'e', 'i', 'o', 'u'}
vowels = 'aeiou'
if letter in vowels:
    print(f'{letter} is a vowel')
else:
    print(f'{letter} is a consonant')
# Day 37: Count the Vowels

def count_the_vowels(string):
    counts = 0
    vowels = 'aeiou'
    for letter in set(string.lower()):
        if letter in vowels:
            counts += 1
    if counts > 1:
        return f'{counts} vowels'
    return f'{counts} vowel'        

word = 'hello'
word2 = 'saas'
print(count_the_vowels(word))
print(count_the_vowels(word2))

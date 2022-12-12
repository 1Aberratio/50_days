# Day 19 : Words and Elements

def count_words(string):
    return f'{len(string.split())} words.'
    
def count_elements(elements):
    join_words = ''.join(elements.split())
    return f'{len(join_words)} elements.'

words_str = "I love learning"
print(count_words(words_str))
print(count_elements(words_str))

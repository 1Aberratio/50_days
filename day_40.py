# Day 40: Pig Latin

def translate(x):
    return ' '.join( [word[1:] + word[0] + 'ay' if word[0] not in 'aeiou' else word + 'yay' for word in x.split()] )

a = 'i love python'   
print(translate(a))

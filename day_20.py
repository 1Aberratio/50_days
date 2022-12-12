# Day 20 : Capitalize First Letter

def capitalize(words):
    return words.title()

string = "i like learning"
print(capitalize(string))

print('-'*35)

# Extra Challenge: Reversed List

strl = 'leArning is hard, bUt if You appLy youRself ' \
'you can achieVe success'

newList = [word[::-1] for word in strl.split() for letter in word if letter.isupper()]
print(newList)

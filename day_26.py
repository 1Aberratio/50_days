# Day 26 : Sort Words

def sort_words(string):
    l = []
    x = ','.join(sorted(set(string))).lstrip()
    l.append(x[1:])
    return l    

words = "love life"
print(sort_words(words))

print('-'*35)

# Extra Challenge: Length of Words

def string_length(str1):
    return {i:len(i) for i in str1.split()}

s = 'Hi my name is Richard'
print(string_length(s))

# Day 4: Only Floats

def only_floats(a, b):
    if a is float(a) and b is float(b): return 2
    elif a is float(a) or b is float(b): return 1
    else: return 0        

numb_1 = 12.1; numb_2 = 23
print(only_floats(numb_1, numb_2))

print('------------------------')

# Extra Challenge: Index of the Longest Word

def word_index(theWords):
    return theWords.index(max(theWords))

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]
print(word_index(words2))

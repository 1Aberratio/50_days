# Day 36: Count String

def count(word):
    return {i:word.count(i) for i in word}

string = 'hello'
print(count(string))

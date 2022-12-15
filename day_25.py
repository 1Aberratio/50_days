# Day 25 : All the Same

def all_the_same(eq):    
    tf = None
    
    for i in eq[1:]:
        if eq[0] == i: tf = True
        else: 
            tf = False 
            break
    return tf

nList = ['Mary', 'Mary', 'Mary']
nStr = "eeeeuee"

print(all_the_same(nList))
print(all_the_same(nStr))

print('-'*35)

# Extra Challenge: Reverse a String

def read_backwards(revStr):
    lstStr = revStr.split()[::-1]
    return ' '.join(lstStr)

str1 = "the love is real"

print(read_backwards(str1))

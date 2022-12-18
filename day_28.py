# Day 28: Return Indexes

def index_position(str1):
    return [index for index, letter in enumerate(str1) if letter.islower()]

word = 'LovE'
print(index_position(word))

print('-'*35)

# Extra Challenge: Largest Number

def largest_number(nList):
    numbers = ''.join(map(str,nList))
    x = ''.join(sorted(numbers, reverse=True))
    return f'{int(x):,}'   

list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))

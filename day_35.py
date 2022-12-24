# Day 35: Pangram

def check_pangram(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:    
        if letter not in string:
            return False
    return True     

sentence = "the quick brown fox jumps over a lazy dog"
print(check_pangram(sentence))

print('-'*35)

# Extra Challenge: Find my Position

def find_index(lst, num):
    if num in lst:
        return [index for index, i in enumerate(lst) if i == num]              
    return [num for j in lst]

list1 = [1, 2, 4, 6, 7, 7]

print(find_index(list1, 7))
print(find_index(list1, 8))

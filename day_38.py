# Day 38: Guess a Number

import random

def guess_a_number():    
    number = random.randint(1, 15)
    for i in range(3):
        user = int(input('Guess a number between 1 and 15: '))
        if user == number: return "\nYou win"
        elif user > number: print("The guess is too high")
        else: print("The guess is too low")
    return "\nYou lose"
    
print(guess_a_number())

print('-'*35)

# Extra Challenge: Find Missing Numbers

def missing_numbers(lst):  
    return [num for num in range(min(lst), max(lst)) if num not in lst]            

list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
print(missing_numbers(list))

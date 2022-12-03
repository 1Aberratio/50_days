# Day 11: Are They Equal?

def equal_strings(str1, str2):      
    return sorted(str1) == sorted(str2)
    
print(equal_strings('live', 'evil'))
print(equal_strings('rock', 'jazz'))

print('--------------------------')

# Extra Challenge: Swap Values

def swap_values(numbers):
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers

numbersList = [2, 4, 67, 7]
print(swap_values(numbersList))

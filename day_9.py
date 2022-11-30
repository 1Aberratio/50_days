# Day 9: Biggest Odd Number

def biggest_odd(numbers):
    return max(int(number) for number in numbers if int(number) % 2 != 0)
    
string = '23569'
print(biggest_odd(string))

print('-------------------------')

# Extra Challenge: Zeros to the End

def zeros_last(numbersList):
    if 0 in numbersList:
        for j in range(len(numbersList)):
            zero = numbersList.index(0)
            del numbersList[zero]   
            numbersList.append(0)                    
    else: numbersList.sort()
    return numbersList 

theList = [1, 4, 6, 0, 7, 0, 9] 
# theList = [2, 1, 4, 7, 6] 
print(zeros_last(theList))

# Day 21: List of Tuples

def make_tuples(lst_1, lst_2):
    return [(lst_1[i], lst_2[i]) for i in range(len(lst_1))]
    
f_list = [1,2,3,4]
s_list = [5,6,7,8]

print(make_tuples(f_list, s_list))

print('-'*35)

# Extra Challenge: Even Number or Average

def even_or_average():
    numList = []; even = []
    print("Please enter five numbers")
    
    for i in range(1,6):
        num = int(input(f'{i}) enter number: '))
        if num % 2 == 0: even.append(num)
        numList.append(num)
    
    if even == []: return f' Average: {sum(numList) / len(numList)}'
    else: return f' Largest even number: {max(even)}'
        
print(even_or_average())

# Day 18 : Any Number of Arguments

def any_number(*number):
    return sum(number)/len(number)    

print(any_number(12, 90, 12, 34))
print(any_number(12, 90))

print('-'*35)

# Extra Challenge: Add and Reverse
    
def add_reverse(lst_1, lst_2):
    a = len(lst_1); b = len(lst_2)
    if a == b:
        numbers_sum = [lst_1[i]+lst_2[i] for i in range(len(lst_1))]
        for num in range(0, a-1):
            numbers_sum[num],numbers_sum[-1] = numbers_sum[-1],numbers_sum[num]
        return numbers_sum
    return "the lists are not of equal lengths"

list_A = [10, 12, 34]; list_B = [12, 56, 78]
list_C = [34, 61, 10, 22]; list_D = [9, 10, 21, 13]
 
print(add_reverse(list_A, list_B))
print(add_reverse(list_A, list_C))
print(add_reverse(list_C, list_D))

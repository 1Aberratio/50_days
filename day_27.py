# Day 27: Unique Numbers

def unique_numbers(n_list):
    u_nums = sum(set(n_list))
    o_nums = sum(n_list)
    diff = o_nums - u_nums
    if diff % 2 == 0: return n_list
    else: return list(set(n_list))

l1 = [1, 2, 4, 5, 6, 7, 8, 8] # even (par)
l2 = [1, 2, 4, 5, 6, 7, 8, 5] # odd (impar)
print(unique_numbers(l1))
print(unique_numbers(l2))

print('-'*35)

# Extra Challenge: Difference of two Lists

def difference(lst1, lst2):
    a = [i for i in lst1 if i not in lst2]
    b = [j for j in lst2 if j not in lst1]
    return a + b

list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]
print(difference(list1, list2))

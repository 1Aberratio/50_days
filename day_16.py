# Day 16 : Sum the List

def sum_list(numbersList):
    newList = sum(numbersList, [])
    return sum(newList)

theList = [[2, 4, 5, 6], [2, 3, 5, 6]]
print(sum_list(theList))

print('-'*35)

# Extra Challenge: Unpack A Nest

nested_list = [[12, 34, 56, 67], [34, 68, 78]]
n1 = nested_list[0][1::2]
n2 = nested_list[1][0::2]
newList = list(set(n1+n2))

print(newList)

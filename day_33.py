# Day 33: List Intersection

def inter_section(lst1, lst2):
    a = [i for i in lst1 if i in lst2]
    b = [j for j in lst2 if j in lst1]
    return tuple(sorted(set(a + b)))

list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]

print(inter_section(list1, list2))

print('-'*35)

# Extra Challenge: Set or list

import time
start = time.time()

a = range(10000000)
x = set(a)
y = list(a)
n = 9999999

print(n in y[n:n+1]) # THIS OPTION (list) IS THE WINNER
# print(n in x)

end = time.time()
print(end-start)

'''
These are the run times in a round of five turns each (list and set)

list=> y              |set=> x
----------------------|----------------------
2.58                  |2.73
2.61                  |2.99
2.57                  |2.85
2.82                  |2.74
2.77                  |2.60
----                  -----
13.35 / 5 = 2.67      |13.91 / 5 = 2.78
'''

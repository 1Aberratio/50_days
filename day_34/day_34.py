# Day 34: Just Digits

import csv

def just_digits():
    f = open("python.csv")
    reader = csv.reader(f)
    one = sum(reader,[])
    x = ''.join(one)
    return [ch for ch in x.split() if ch.isnumeric()]
    
print(just_digits())

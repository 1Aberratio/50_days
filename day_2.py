# Day 2: Strings to Integers

def convert_add(stringList):
    return f"{list(map(int, stringList))} and the sum of the list is: {sum(map(int, stringList))}"

numberList = ['1', '3', '5']
print(convert_add(numberList))

print('--------------------------------')

# Extra Challenge: Duplicate Names

def check_duplicates(theFruits,theNames):
    duplicatesFruits = set(i for i in theFruits if theFruits.count(i)>1)
    duplicatesNames = set(j for j in theNames if theNames.count(j)>1)
    if len(duplicatesFruits)>0 and len(duplicatesNames)>0: 
      return f'first list: {duplicatesFruits} as a duplicate \nsecond list: {duplicatesNames} as a duplicate'
    elif len(duplicatesFruits)>0 and len(duplicatesNames)<1: 
      return f'first list: {duplicatesFruits} as a duplicate \nsecond list: no duplicates'
    elif len(duplicatesFruits)<1 and len(duplicatesNames)>0: 
      return f'first list: no duplicates \nsecond list: {duplicatesNames} as a duplicate'
    else: return f'no duplicates'
    
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
print(check_duplicates(fruits, names))

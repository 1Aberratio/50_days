# Day 3: Register Check

def register_check(students):
    return len([student for student in students.values() if student == 'yes'])

register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
print(register_check(register))

print('-----------------------------')

# Extra Challenge: Lowercase Names

names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
nameTuple = [name for name in names if name.islower()]
print(tuple(nameTuple))

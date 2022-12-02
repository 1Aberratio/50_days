# Day 7: A String Range

def string_range(number):
    numbers = [str(i) for i in range(number)]
    return '.'.join(numbers)

number_range = 6
print(string_range(number_range))

print('-------------------------')

# Extra Challenge: Dictionary of names

names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
s_names = dict()

for i in set(names):
    if i.startswith("S"):
        s_names[i] = names.count(i)
print(s_names)

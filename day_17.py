# Day 17: User Name Generator

def user_name(name):
    name = name.lower()
    import random
    number = random.randint(0, 9)
    return name[::-1] + str(number)

ur_name = input("Enter your first name: ")
print(user_name(ur_name))

print('-'*35)

# Extra Challenge: Sort by Length

def sort_length(names):
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if len(names[i]) > len(names[j]):
                names[i],names[j] = names[j],names[i]
    return names

names = ["Peter", "Jon", "Anastasia", "Jr", "Andrew"]
# names = ["Peter", "Jon", "Andrew"]
print(sort_length(names))

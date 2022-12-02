# Day 10: Hide my Password

def hide_password():
    password = input("Enter your password: ")
    stars = str.maketrans(password, '*' * len(password))
    return f'{password.translate(stars)} has {len(stars)} characters.'    

print(hide_password())

print('-----------------------')

# Extra Challenge: A Thousand Separator

def convert_numbers(theList):
    return [f'{number:,}' for number in theList]

numbersList = [1000000, 2356989, 2354672, 9878098]
print(convert_numbers(numbersList))

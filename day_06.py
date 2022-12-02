# Day 6 : User Name Generator

def user_name(user):
    name = user.find('@')
    return user[:name]
  
email = input("Enter your email: ")
print(user_name(email))

print('-----------------------')

# Extra Challenge: Zero Both ends

def zeroed(numbers):
    index_number = [0, -1]
    for i in index_number:
        numbers[i] = 0
    return numbers

numbersList = [2, 5, 7, 8, 9]
print(zeroed(numbersList))

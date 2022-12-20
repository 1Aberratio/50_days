# Day 31: Longest Word

def longest_word(wlist):
    word = max(wlist, key=len)
    return [len(word), word]

languages = ['Java', 'JavaScript', 'Python']
print(longest_word(languages))

print('-'*35)

# Extra Challenge: Create User

def create_user():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    password = input("Enter your password: ")
    
    userData = {}
    userData['name'] = name
    userData['age'] = age
    userData['password'] = password
    
    print("\nUser saved. Please login\n")
    
    while True:
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if name == userData['name'] and password == userData['password']:
          return "\nLogged in successfully\n"
        else:
          print("\nWrong password or user name. Please try again\n")
    
print(create_user())

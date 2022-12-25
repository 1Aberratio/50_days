# Day 39: Password Generator

import string
import random
    
def generate_password():    
    userP = int(input("How strong do you want your password?\n\
    1) weak => 5 characters\n\
    2) strong => 8 characters\n\
    3) very strong => 12 characters\n\
    Select your option (1, 2 or 3): "))
    
    if userP == 1:
        x = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(5)]
        return ''.join(x)
    elif userP == 2:
        x = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8)]
        return ''.join(x)     
    else:
        x = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12)]
        return ''.join(x)
print(generate_password())

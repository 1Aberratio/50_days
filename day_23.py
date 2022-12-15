# Day 23: Simple Calculator

while True:
    print("Choose the operation to perform:\n \
    1: Add | 2: Subtract | 3: Multiply | 4: Divide | Or press any letter to exit")    
    
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Finish")
        break 
        
    if choice < 1 or choice > 4: 
        print("Sorry, wrong choice.")
        break
    
    try:
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))
    except ValueError:
        print("Only numbers are accepted.")
        break
    
    if choice == 1:
        print(f'{num_1} + {num_2} = {num_1 + num_2}\n')
    elif choice == 2:
        print(f'{num_1} - {num_2} = {num_1 - num_2}\n')
    elif choice == 3:
        print(f'{num_1} * {num_2} = {num_1 * num_2}\n')
    elif choice == 4:
        try:
            print(f'{num_1} / {num_2} = {num_1 / num_2}\n')
        except ZeroDivisionError:
            print("Cannot be divided by 0")
            
print('-'*35)

# Extra Challenge: Multiply Words

def multiply_words(string):
    mult = 1; w_len = []
    for word in string.split():
        if word == word.capitalize(): continue
        else: 
            mult *= len(word)
            w_len.append(word)
            w_len.append(f'({len(word)})')
    return f"{mult} - {' '.join(w_len)}"

s = "love live and laugh"
t = "Hate war love Peace"

print(multiply_words(s))
print(multiply_words(t))

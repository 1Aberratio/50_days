# Day 15 : Same in Reverse

def same_in_reverse(word):
    theWord = word.lower()
    a,b = 'áéíóúü', 'aeiouu'
    change = str.maketrans(a,b)
    newWord = theWord.translate(change)
    new = ''.join(filter(str.isalnum, newWord))
    return new == new[::-1]
    
word_str = '¿Acaso hubo búhos acá?'
print(same_in_reverse(word_str))

print('-'*35)

# Extra Challenge: What’s My Age?

def your_age(student):
    name = student.lower()
    if name in names_age: 
        return f'Hi, {student.capitalize()}, you are {names_age[name]} years old.' 
    else:
        age = int(input("Your name is not in the database, please enter your age to be added: "))
        names_age[name] = age
        return f'Hi, {student.capitalize()}, you are {names_age[name]} years old.'

names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}

student_name = input("Enter your name: ")
print(your_age(student_name))

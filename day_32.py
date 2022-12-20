# Day 32: Password Validator

def password_validator():    
    while True:    
        password = input("Enter a password: ")
    
        ch_upper = [caracter.isupper() for caracter in password]
        ch_lower = [caracter.islower() for caracter in password]
        numbers = [caracter.isdigit() for caracter in password]
    
        if any(ch_upper) and any(ch_lower) and any(numbers) and len(password) > 7:
            return password
        elif not any(ch_upper):
            print("Password must contain at least one capital letter")
        elif not any(ch_lower):
            print("Password must have at least one lowercase letter")
        elif not any(numbers):
            print("Password must have at least one number")
        elif len(password) < 8:
            print("Password must be at least eight characters")

print(password_validator())

print('-'*35)

# Extra Challenge: Valid Email

def email_validator(mail_lst):
    valid_mail = []
    for mail in mail_lst:
        if '@' in mail and mail.count('@') == 1 and not mail.startswith('@') and mail.endswith('.com'): 
            valid_mail.append(mail)
        else: continue
    if valid_mail: return valid_mail
    return "all emails are invalid"       

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
print(email_validator(emails))

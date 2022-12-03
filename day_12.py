# Day 12 : Count the Dots

def count_dots(wrd): return f"{wrd.count('.')} points."

print(count_dots('h.e.l.p.'))
print(count_dots('he.lp.'))

print('----------------------------') 

# Extra Challenge: Your Age in Minutes

def age_in_minutes(year):
    import datetime

    date = datetime.date.today()
    current_year = date.strftime("%Y")

    while True:
        if len(year) != 4 or not year.isdigit():
            print("The year must contain only four numbers")
            year = input("Enter your year of birth: ")
        elif int(year) < 1900 or int(year) > int(current_year):
            print("The year must be in a range between 1900 to the current year")
            year = input("Enter your year of birth: ")
        else:
            minutes = (int(current_year) - int(year)) * 525600
            return f'You are {minutes:,} minutes old.'

user_year = input("Enter your year of birth: ")
print(age_in_minutes(user_year))

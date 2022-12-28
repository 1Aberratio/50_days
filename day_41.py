# Day 41: Only Words with Vowels

def words_with_vowels(words):
    wVowels = []    
    for word in words.split():   
        for letter in word:
            if letter in 'aeiou':
                wVowels.append(word)
                break
    return wVowels

str1 = "You have no rhythm"
print(words_with_vowels(str1))

print('-'*35)

# Extra Challenge: Class of Cars

class Car:
    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_cars(self):
        print(f"car_model = {self.model}")
        print(f"Color = {self.color}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}\n")

class Ford(Car):
    pass

class BMW(Car):
    pass

class Tesla(Car):
    pass

bmw1 = BMW("x6", "silver", 2018, "Auto", False)
tesla1 = Tesla("S", "beige", 2017, "Auto", True)
ford1 = Ford("focus", "white", 2020, "Auto", False)

ford1.print_cars()
bmw1.print_cars()
tesla1.print_cars()

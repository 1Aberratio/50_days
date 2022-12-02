# Day 1: Division and Square-root

def divide_or_square(number):
    if number % 5 == 0:
        return f" Raiz cuadrada de {number}:  {round(num**0.5, 2)}"
    else: return f"Residuo de {number}:  {number % 5}"

num = 10
print(divide_or_square(num))

print("-------------------------")

# Extra Challenge: Longest Value

def longest_value(dictionary):
    largest = ""
    for i in dictionary.values():
        if len(i) > len(largest):
            largest = i
    return largest

fruits = {'fruit': 'apple', 'color': 'green'}
print(longest_value(fruits))

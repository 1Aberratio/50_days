# Day 24: Average Calories

def average_calories(days):
    sumCal = 0
    for i in range(1, days+1):
        calories = float(input(f'Enter the number of calories consumed during the day {i}: '))
        sumCal += calories
    return f'\nAverage calories: {round(sumCal / i, 2)}'

nDays = int(input("Enter the number of days to calculate: "))
print(average_calories(nDays))

print('-'*35)

# Extra Challenge: Create a Nested List

def nested_lists(*lists):
    return list(lists)

l1 = [1, 2, 3, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 3, 4, 5]
print(nested_lists(l1,l2,l3))

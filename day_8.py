# Day 8 : Odd and Even

def odd_even(numbers):
    odd = min(i for i in numbers if i%2 != 0)
    even = max(j for j in numbers if j%2 == 0)
    return f'{even} - {odd} = {even-odd}'    

numbers_list = [1,2,4,6]
print(odd_even(numbers_list))

print('-----------------------') 

# Extra Challenge: List of Prime Numbers

def prime_numbers(number):     
    all_numbers = [i for i in range(2, number+1)]
    all_numbers.reverse(); count = 0
    prime_numbers = []
    for i in range(len(all_numbers)):
        for i in all_numbers:
            if number % i == 0: 
                count += 1
        if count == 1:
            prime_numbers.append(number)
            count = 0        
        else: count = 0
        number -= 1
    return prime_numbers[::-1]           

int_number = int(input("Enter an integer number: "))
print(prime_numbers(int_number))

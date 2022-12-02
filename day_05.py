# Day 5: My Discount

def my_discount():
    price = int(input("Enter the price of the product: "))
    discount = int(input("Enter the discount: "))
    discount_price = price * discount / 100
    return price - discount_price

print(my_discount())

print('---------------------')

# Extra Challenge: Tuple of Student Sex

students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
students_list = [student.lower() for student in students]
male = ('Male', students_list.count('male'))
female = ('female', students_list.count('female'))
count = [male, female]

print(count)

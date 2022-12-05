# Day 13: Pay Your Tax

def your_vat():
    while True:
        try:
            price = int(input("Please enter the price: "))  # 220
            vat = int(input("Please enter the VAT: "))  # 15
            break
        except ValueError:
            print("The price and the VAT must contain only integeres numbers. Please try again.")
            
    price_vat = price * vat / 100
    return int(price + price_vat)    # 253
 
print(your_vat())
print('-'*35)

# Extra Challenge: Pyramid of Snakes

def python_snakes(num):
    for i in range(2, num+1):
        print(" "*(num-i) + "• " + "•• "*(i-2) + "•")
    return ''
    
print(python_snakes(7))

# Name: Elisee Kaneza
# Date: [02/18/2025]
# Program: Coffee Shop Receipt 
# Description: This program calculates the total cost of coffee and muffins, including tax.

# Prices
coffee_price = 5.00
muffin_price = 4.00
tax_rate = 0.06

# User Input
coffees = int(input("Number of coffees bought? "))
muffins = int(input("Number of muffins bought? "))

# Calculations
subtotal = (coffees * coffee_price) + (muffins * muffin_price)
tax = subtotal * tax_rate
total = subtotal + tax

# Display Receipt
print("\n***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{coffees} Coffee at $5 each: $ {coffees * coffee_price:.2f}")
print(f"{muffins} Muffins at $4 each: $ {muffins * muffin_price:.2f}")
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")
print("***************************************")

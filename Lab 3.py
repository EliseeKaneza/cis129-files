"""
Program: Coffee Shop Receipt Generator
Author: [Elisee Kaneza]
Date: [02/24/2025]
Description:
    This program calculates a receipt for a coffee shop purchase. 
    It includes four menu items, applies a 6% tax, and displays a formatted receipt.
"""

# Prices of items
COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00
TEA_PRICE = 3.50
CROISSANT_PRICE = 3.75
TAX_RATE = 0.06  # 6% tax

# Getting user input
print("***************************************")
print("Welcome to Java Bliss Coffee Shop!")
num_coffee = int(input("Number of coffees bought? "))
num_muffin = int(input("Number of muffins bought? "))
num_tea = int(input("Number of teas bought? "))
num_croissant = int(input("Number of croissants bought? "))
print("***************************************\n")

# Calculating cost
subtotal_coffee = num_coffee * COFFEE_PRICE
subtotal_muffin = num_muffin * MUFFIN_PRICE
subtotal_tea = num_tea * TEA_PRICE
subtotal_croissant = num_croissant * CROISSANT_PRICE
subtotal = subtotal_coffee + subtotal_muffin + subtotal_tea + subtotal_croissant
tax = subtotal * TAX_RATE
total = subtotal + tax

# Displaying receipt
print("***************************************")
print("My Coffee Shop Receipt")
if num_coffee > 0:
    print(f"{num_coffee} Coffee at ${COFFEE_PRICE} each: ${subtotal_coffee:.2f}")
if num_muffin > 0:
    print(f"{num_muffin} Muffins at ${MUFFIN_PRICE} each: ${subtotal_muffin:.2f}")
if num_tea > 0:
    print(f"{num_tea} Tea at ${TEA_PRICE} each: ${subtotal_tea:.2f}")
if num_croissant > 0:
    print(f"{num_croissant} Croissants at ${CROISSANT_PRICE} each: ${subtotal_croissant:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
print("\nThank you for visiting Java Bliss Coffee Shop! We hope to see you again soon!")

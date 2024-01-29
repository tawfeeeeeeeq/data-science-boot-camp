"""
The purpose of this script is too calculate the total_stock worth in the cafe. 
"""

# Create a list called menu, which should contain at least four items sold in the cafe.
menu = ["breakfast", "lunch", "dinner", "special"]

# Create a dictionary called stock, which should contain the stock value for each item on your menu.
stock = { 
    "breakfast": 15,
    "lunch": 12,
    "dinner": 9,
    "special": 8
}

# Create another dictionary called price, which should contain the prices for each item on your menu.
price = { 
    "breakfast": 4.99,
    "lunch": 9.99,
    "dinner": 19.99,
    "special": 24.99
}

# Loop through the appropriate dictionaries above.
# Calculate the total_stock worth in the cafe and print it out.
total_stock = 0
for i in menu:
    total_stock += stock[i] * price[i]
print (f"Total stock value in cafe is £{total_stock}")
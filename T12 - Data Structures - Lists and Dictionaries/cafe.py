"""
The purpose of this script is too calculate the total_stock worth in the cafe. 
"""

# Create a list called menu, which should contain at least four items sold in the cafe.
menu = ["breakfast", "lunch", "dinner", "special"]

# Create a dictionary called stock, which should contain the stock value for each item on your menu.
stock = { 
    0: 15,
    1: 12,
    2: 9,
    3: 8
}

# Create another dictionary called price, which should contain the prices for each item on your menu.
price = { 
    0: 4.99,
    1: 9.99,
    2: 19.99,
    3: 24.99
}

# Loop through the appropriate dictionaries above.
# Calculate the total_stock worth in the cafe and print it out.
total_stock = 0
for i in range(len(menu)):
    total_stock += stock[i] * price[i]
print (f"Total stock value in cafe is £{total_stock}")
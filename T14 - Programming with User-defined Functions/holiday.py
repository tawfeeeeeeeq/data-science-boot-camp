"""
This program calculates a users total holiday cost, which includes the plane cost, hotel cost, and car-rental cost.
There is a function for calculating the plane_cost.
There is a function for calculating the hotel_cost.
There is a function for calculating the car_renal cost.
The function holiday_cost() is used to call the other 3 functions and return a total cost for the holiday.
"""

# This is a dicctionary which defines all the costs for each available destination
destinations = { 
    "london": {"flight": 200, "hotel": 49, "rental": 30},
    "paris":  {"flight": 300, "hotel": 96, "rental": 24},
    "madrid": {"flight": 250, "hotel": 73, "rental": 33},
    "berlin": {"flight": 150, "hotel": 54, "rental": 45}
}

# This function will return the flight cost associated with the chosen destination
def plane_cost(city):
    return destinations[city]["flight"]

# This function will retun the hotel cost assocaited with the chosen destination
def hotel_cost(nights, city):
    return destinations[city]["hotel"] * nights

# This function will return the car rental cost assocaiated with the chosen destination
def car_rental(days, city):
    return destinations[city]["rental"] * days

# This function will return the total cost of the holiday, by calling the previous 3 functions
def holiday_cost(nights,city,days):
    total = hotel_cost(nights,city) + plane_cost(city) + car_rental(days,city)
    return total

# This requests the city the user is flying to. It will ask on a loop until a valid destination is entered.
while True:
    city_flight = input("Where are you flying to? (London, Paris, Mardrid, Berlin): ").lower()
    if city_flight in destinations.keys():
        break
    else:
        print("Sorry, no flights to that destination, try again.")

# This requests the number of nights they will stay in the hotel. It will loop until a valid number is entered.
while True:
    try:
        num_nights = int(input("How many nights at the hotel?: "))
    except ValueError:
        print("Sorry, invalid input, try again.")
        continue
    else:
        break

# This requests the number of days they will rent a car. It will loop until a valid number is entered.
while True:
    try:
        rental_days = int(input("How many days are you hiring a car?: "))
    except ValueError:
        print("Sorry, invalid input, try again.")
        continue
    else:
        break

# This takes the 3 inputs from the user and calculates the total cost of the holiday
total_cost = holiday_cost(num_nights,city_flight,rental_days)

# Print out the details in a clear readable way
print()
print(f"Destination: {city_flight}")
print(f"Flight Cost: £{plane_cost(city_flight)}")
print(f"Hotel Cost: £{hotel_cost(num_nights, city_flight)} ({num_nights} nights)")
print(f"Car Rental: £{car_rental(rental_days, city_flight)} ({rental_days} days)")
print(f"TOTAL COST: £{total_cost}")

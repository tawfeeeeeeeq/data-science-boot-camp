# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")           # Syntax Error: Missing parentheses in call to 'print'.
print("\n")                                     # Syntax Error: unexpected indent and Missing parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"                                  # Logical Error: == used instead of =. Will not be able to Cast to int if the string contains letters.
age = int(age_Str) 
print("I'm " + str(age) + " years old.")        # Runtime Error: Must cast `age` to string

# Variables declaring additional years and printing the total years of age
years_from_now = "3"                            
total_years = age + int(years_from_now)         # Runtime Error: Adding and int to a string, need to cast 2nd value to int

print("The total number of years: " + str(total_years))     # Syntax Error: Missing parentheses in call to 'print'. Used wrong variable name, varibale shouldnt be in quotes, need to cast to str.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12                       # Runtime Error: `total` is not defined. should be total_years
print("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old") # Syntax Error: Missing parentheses in call to 'print'. cast total_months to str. Logical Error: need to add 6 months.

#HINT, 330 months is the correct answer

